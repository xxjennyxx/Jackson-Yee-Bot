#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for songs_and_films

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

DEBUG_songs_and_films = True
CHATBOT_MODE = False

userDefinedDICT = {}
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except Exception as e:
    print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_songs_and_films.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_songs_and_films:
        print("[songs_and_films] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)

    # talent
    if utterance == "[你]是歌手嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "才藝"
            pass

    if utterance == "[你]是演員嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "才藝"
            pass

    if utterance == "[你]是舞者嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["talent"] = "才藝"
            pass

    # songs
    if utterance == "[你]最新的[一首]歌是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["songs"] = "新歌" # 0

    if utterance == "[你]的音樂風格是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["songs"] = "風格" # 1

    if utterance == "[我]想聽[你]的歌":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["songs"] = "聽歌"
    elif utterance == "[粉霧海]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["links"] = args[0] 
    
    if utterance == "[我]想聽歌":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["songs"] = "聽歌"
    elif utterance == "[粉霧海]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["links"] = args[0] 

    # links
    if utterance == "[可以]給[我][粉霧海]的連結嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["links"] = args[2] 

    if utterance == "[我]想聽[粉霧海]":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["links"] = args[1] 

    # album
    if utterance == "[你]出過哪些專輯":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["album"] = "專輯" # 0

    if utterance == "[你]有什麼專輯":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["album"] = "專輯" # 0

    if utterance == "[後座劇場]有什麼歌":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["album"] = args[0] # 1-4

    # films
    if utterance == "[你]拍過哪些電影":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["films"] = "電影" # 0

    if utterance == "[你]最新的電影是哪部":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["films"] = "滿江紅" # 1
        
    if utterance == "[你]在[少年的你][中]扮演什麼角色":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["films"] = args[1] # 1-8

    if utterance == "[你]在[少年的你][中]演什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
        else:
            resultDICT["films"] = args[1] # 1-8

    return resultDICT