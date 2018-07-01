from models import SMSData
import datetime
from django.core.cache import cache


def sanityCheck(fromValue, toValue, textValue, call):
    #primary check
    if fromValue == toValue:
        return "",  "From and to can't be same"
    dictValues = {"from": fromValue, "to": toValue, "text": textValue}
    try:
        for key, val in dictValues.iteritems():
            if val == "":
                return "", key+" is missing"
            elif key == "text" and len(val) > 120:
                return "", key + " is invalid"
            elif key != "text" and (len(val) < 6 or len(val) > 16 or not val.isdigit()):
                return "", key + " is invalid"
            else:
                continue

        return call+" sms is ok", ""

    except:
        return "", " unknown failure "

def cacheFuncSet(fromValue, toValue, time=14400):
    try:
        fromTo = fromValue+"_"+toValue
        cache.set(fromTo, "", timeout=time)
    except :
        return False
    return True

def cacheFuncGet(fromValue,toValue):
    try:
        fromTo = fromValue+"_"+toValue
        exist = cache.get(fromTo)
        if exist is None:
            return False
    except :
        return False
    return True

def storeSMS(fromValue, toValue, textValue, user):
    print fromValue
    try:
        saveSms = SMSData(smsFrom=fromValue,smsTo=toValue,smsText=textValue,smsUser=user)
        saveSms.save()
    except :
        return False
    return True

def lastHourCheck(fromValue,blockCount=50):
    try:
        currTime = datetime.datetime.now()
        endTime = currTime - datetime.timedelta(minutes=60)
        fromCount = SMSData.objects.filter(smsTime__gt=endTime, smsTime__lte=currTime, smsFrom=fromValue).count()
        if fromCount < blockCount:
            return True
        else:
            return False
    except :
        return False
