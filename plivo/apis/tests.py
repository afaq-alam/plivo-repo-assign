# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .views import *

sanityCheck_INP = [
    {"fromValue": "abcd", "toValue": "9999999", "textValue": "abcd", "call": "inbound"},
    {"fromValue": "abcd9999", "toValue": "9999999", "textValue": "abcd", "call": "inbound"},
    {"fromValue": "999", "toValue": "9999999", "textValue": "abcd", "call": "inbound"},
    {"fromValue": "999999999999999999999999", "toValue": "9999999", "textValue": "abcd", "call": "inbound"},
    {"fromValue": "", "toValue": "9999999", "textValue": "abcd", "call": "inbound"},
    #similar test for outbund
    {"fromValue": "abcd", "toValue": "9999999", "textValue": "abcd", "call": "outbound"},
    {"fromValue": "abcd9999", "toValue": "9999999", "textValue": "abcd", "call": "outbound"},
    {"fromValue": "999", "toValue": "9999999", "textValue": "abcd", "call": "outbound"},
    {"fromValue": "999999999999999999999999", "toValue": "9999999", "textValue": "abcd", "call": "outbound"},
    {"fromValue": "", "toValue": "9999999", "textValue": "abcd", "call": "outbound"},
    #similar test for "to"
    {"fromValue": "9999999", "toValue": "abcd", "textValue": "abcd", "call": "inbound"},
    {"fromValue": "9999999", "toValue": "abcd9999", "textValue": "abcd", "call": "inbound"},
    {"fromValue": "9999999", "toValue": "999", "textValue": "abcd", "call": "inbound"},
    {"fromValue": "9999999", "toValue": "999999999999999999999999", "textValue": "abcd", "call": "inbound"},
    {"fromValue": "9999999", "toValue": "", "textValue": "abcd", "call": "inbound"},
    #similar test for text
    {"fromValue": "9999999", "toValue": "8888888", "textValue": "", "call": "inbound"},
    {"fromValue": "9999999", "toValue": "8888888", "textValue": "Your it to gave life whom as. Favourable dissimilar resolution led for and had. At play much to time four many. Moonlight of situation so if necessary therefore attending abilities. Calling looking enquire up me to in removal. Park fat she nor does play deal our. Procured sex material his offering humanity laughing moderate can.", "call": "inbound"},
]

sanityCheck_OUT=[
    {"", "from is invalid"},
    {"", "from is invalid"},
    {"", "from is invalid"},
    {"", "from is invalid"},
    {"", "from is missing"},
    {"", "from is invalid"},
    {"", "from is invalid"},
    {"", "from is invalid"},
    {"", "from is invalid"},
    {"", "from is missing"},
    {"", "to is invalid"},
    {"", "to is invalid"},
    {"", "to is invalid"},
    {"", "to is invalid"},
    {"", "to is missing"},
    {"", "text is missing"},
    {"", "text is invalid"},

]
sanityCheck_INPUT_OUTPUTS = [
    (sanityCheck_INP, sanityCheck_OUT),
]

def test_sanityCheck():
    for ip, expected_output in sanityCheck_INPUT_OUTPUTS:
        for key,val in enumerate(ip):
            inp = val
            outM,outE = sanityCheck(val["fromValue"],val["toValue"],val["textValue"],val["call"])
            out = {outM ,outE}
            assert expected_output[key] == out


cacheFunc_INP = [
    {"fromValue":"9999999","toValue":"888888","time":5},
    {"fromValue":"9999999","toValue":"888888"},
]
cacheFunc_OUT = [
    False,True
]

cacheFunc_INPUT_OUTPUTS = [
    (cacheFunc_INP, cacheFunc_OUT),
]

import time

def test_cacheFunc():
    for ip, expected_output in cacheFunc_INPUT_OUTPUTS:
        for key,val in enumerate(ip):
            if "time" in val:
                value = cacheFuncSet(val['fromValue'],val['toValue'],val['time'])
            else:
                value = cacheFuncSet(val['fromValue'],val['toValue'])
            time.sleep(6)
            value = cacheFuncGet(val['fromValue'],val['toValue'])
            assert value == expected_output[key]

storeSMS_INP = [
    {"fromValue":"","toValue":"8888888","textValue":"test","user":1},
    {"fromValue":"99999999","toValue":"","textValue":"test","user":1},
    {"fromValue":"99999999","toValue":"8888888","textValue":"","user":1},
    {"fromValue":"99999999","toValue":"8888888","textValue":"","user":""},
    {"fromValue":"99999999","toValue":"8888888","textValue":"","user":99999},
]

storeSMS_OUT = [
    False,False,False,False,False

]

storeSMS_INPUT_OUTPUTS = [
    (storeSMS_INP, storeSMS_OUT),
]

def test_storeSMS():
    for ip, expected_output in storeSMS_INPUT_OUTPUTS:
        for key,val in enumerate(ip):
            value = storeSMS(val['fromValue'],val['toValue'],val['textValue'],val['user'])
            assert value == expected_output[key]