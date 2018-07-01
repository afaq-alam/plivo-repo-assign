# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from decorator import authenticate
from utility import *

@require_http_methods('GET')
@authenticate
def inbound(request,user):
    fromValue = request.GET.get("from","").lstrip("0") #excluding any leading zeroes
    toValue = request.GET.get("to","").lstrip("0")
    textValue = request.GET.get("text","")
    retValue = {}
    message, error = sanityCheck(fromValue, toValue, textValue, "inbound")
    if error == "":
        storeSMSResp = storeSMS(fromValue, toValue, textValue, user)
        if not storeSMSResp:
            retValue ={"message": "", "error": " unknown failure "}
            response = JsonResponse(retValue, status=502)
            return response
        textValueCheck=textValue.replace('\\n', "").replace('\\r', "").replace('\\r\\n', "")
        if textValueCheck.lower() == "stop":
            if not cacheFuncSet(fromValue,toValue):
                message = ""
                error = "unknown failure"
    retValue = {"message": message, "error": error}
    return JsonResponse(retValue)

@require_http_methods('GET')
@authenticate
def outbound(request,user):
    fromValue = request.GET.get("from", "").lstrip("0")
    toValue = request.GET.get("to", "").lstrip("0")
    textValue = request.GET.get("text", "")
    retValue = {}
    message, error = sanityCheck(fromValue, toValue, textValue,"outbound")
    if error == "":
        if cacheFuncGet(fromValue,toValue):
            message = ""
            error = "sms from " + fromValue + " and to " + toValue + " blocked by STOP request"
            retValue = {"message": message, "error": error}
            response = JsonResponse(retValue, status=403)
            return response
        if not lastHourCheck(fromValue):
            message = ""
            error = "limit reached for from "+fromValue
            retValue = {"message": message, "error": error}
            response = JsonResponse(retValue,status=429)
            return response
    retValue = {"message": message, "error": error}
    return JsonResponse(retValue)
