#!/usr/bin/env python3
# -*- coding:utf-8 -*- 

"""
    Loki module for basic_information

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

from random import sample
import json
import os

DEBUG_basic_information = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_basic_information.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_basic_information:
        print("[basic_information] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    # birthday
    if utterance == "[你][今年]幾歲":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "年齡"

    if utterance == "[你]幾歲":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "年齡"

    if utterance == "[你]的年齡是多少":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "年齡"

    if utterance == "[你]的[生日]是什麼[時候]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "生日"

    if utterance == "[你]什麼[時候]出生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "出生日"

    if utterance == "[你]在哪[天]出生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "出生日"

    if utterance == "[你]幾[年]出生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "出生年"

    if utterance == "[你]的出生[年][份]是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "出生年" #

    if utterance == "[你]的出生月份是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "出生月" #

    if utterance == "[你][幾月]出生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["birthday"] = "出生月"
        
    # talent
    if utterance == "[你][會]什麼樂器": 
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "樂器"

    if utterance == "[你][會]什麼才藝":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "才藝"

    if utterance == "[你]有什麼才藝":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "才藝"

    if utterance == "[你][會]跳哪種舞風": 
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "跳舞"

    if utterance == "[你][會]跳舞嗎": 
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "跳舞"

    if utterance == "[你]是誰":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "易烊千璽"

    # debut 
    if utterance == "[你]屬於哪個團體":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "團體出道"

    if utterance == "[你]以什麼身份出道": 
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "團體出道"

    if utterance == "團體成員有誰": 
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "團體出道"

    if utterance == "[你]和誰[一起]出道":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "團體出道"

    if utterance == "[你]哪[一年]出道":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "團體出道"

    if utterance == "[你]哪[天]出道":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "團體出道"

    if utterance == "什麼顏色[能]代表[你]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "應援色"

    if utterance == "[你]的應援色是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "應援色"

    if utterance == "[你]的應援色是什麼顏色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "應援色"

    if utterance == "[你]的粉絲名是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "粉絲"

    if utterance == "[你]喜歡誰":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "粉絲" # 

    if utterance == "[你]喜歡[我]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["debut"] = "粉絲" #

    # family
    if utterance == "[你]在哪裡出生":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["family"] = "湖南" # 0

    if utterance == "[你]是哪國人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["family"] = "湖南" # 0

    if utterance == "[你]是哪裡人":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["family"] = "湖南" # 0

    if utterance == "[你]姓什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["family"] = "姓氏" # 1

    if utterance == "[你]的姓氏是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["family"] = "姓氏" # 1

    if utterance == "[你]有[兄弟][姐妹]嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["family"] = "弟弟" # 2

    if utterance == "[你]的英文名是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["family"] = "英文名" # 3

    # university
    if utterance == "[你]畢業於哪所大學":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["university"] = "大學" # 0
 
    if utterance == "[你]讀哪間大學":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["university"] = "大學" # 0

    return resultDICT