#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import re

from TSF_Io import *
from TSF_Forth import *


def TSF_Match_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Match")
    TSF_Forth_cards={
        "#TSF_replace":TSF_Match_replace, "#文字列を置換":TSF_Match_replace,
        "#TSF_resub":TSF_Match_resub, "#文字列を正規表現で置換":TSF_Match_resub,
#        "#TSF_regex":TSF_Match_regex "#文字列を正規表現で置換":TSF_Match_regex,
#        "#TSF_count":TSF_Match_count, "#文字列を計数":TSF_Match_count,
#        "#TSF_regcount":TSF_Match_regcount, "#文字列を正規表現で計数":TSF_Match_regcount,
#        "#TSF_replacesF":TSF_Match_replacesF, "#文字列群で表択置換":TSF_Match_replacesF,
#        "#TSF_replaceF":TSF_Match_replaceF, "#文字列で表択風置換":TSF_Match_replaceF,
        "#TSF_replacesN":TSF_Match_replacesN, "#文字列群で順択置換":TSF_Match_replacesN,
        "#TSF_replacesC":TSF_Match_replacesC, "#文字列群で周択置換":TSF_Match_replacesC,
        "#TSF_replacesM":TSF_Match_replacesM, "#文字列群で囲択置換":TSF_Match_replacesM,
#        "#TSF_replacesV":TSF_Match_replacesV, "#文字列群で逆択置換":TSF_Match_replacesV,
#        "#TSF_replacesA":TSF_Match_replacesA, "#文字列群で乱択置換":TSF_Match_replacesA,
#        "#TSF_replacesQ":TSF_Match_replacesQ, "#文字列群で同択置換":TSF_Match_replacesQ,
#        "#TSF_replacesI":TSF_Match_replacesI, "#文字列群で含択置換":TSF_Match_replacesI,
#        "#TSF_replacesR":TSF_Match_replacesR, "#文字列群で規択置換":TSF_Match_replacesR,
#        "#TSF_replacesH":TSF_Match_replacesH, "#文字列群で似択置換":TSF_Match_replacesH,
#        "#TSF_replacesL":TSF_Match_replacesL, "#文字列群で札択置換":TSF_Match_replacesL,
#        "#TSF_regexesF":TSF_Match_regexesF, "#正規表現の文字列群で表択置換":TSF_Match_regexesF,
#        "#TSF_regexF":TSF_Match_regexF, "#正規表現の文字列で表択風置換":TSF_Match_regexF,
#        "#TSF_regexesN":TSF_Match_regexesN, "#正規表現の文字列群で順択置換":TSF_Match_regexesN,
#        "#TSF_regexesC":TSF_Match_regexesC, "#正規表現の文字列群で周択置換":TSF_Match_regexesC,
#        "#TSF_regexesM":TSF_Match_regexesM, "#正規表現の文字列群で囲択置換":TSF_Match_regexesM,
#        "#TSF_regexesV":TSF_Match_regexesV, "#正規表現の文字列群で逆択置換":TSF_Match_regexesV,
#        "#TSF_regexesA":TSF_Match_regexesA, "#正規表現の文字列群で乱択置換":TSF_Match_regexesA,
#        "#TSF_regexesQ":TSF_Match_regexesQ, "#正規表現の文字列群で同択置換":TSF_Match_regexesQ,
#        "#TSF_regexesI":TSF_Match_regexesI, "#正規表現の文字列群で含択置換":TSF_Match_regexesI,
#        "#TSF_regexesR":TSF_Match_regexesR, "#正規表現の文字列群で規択置換":TSF_Match_regexesR,
#        "#TSF_regexesH":TSF_Match_regexesH, "#正規表現の文字列群で似択置換":TSF_Match_regexesH,
#        "#TSF_regexesL":TSF_Match_regexesL, "#正規表現の文字列群で札択置換":TSF_Match_regexesL,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Match_replace():    #TSFdoc:文字列を置換。3枚[cardT,cardO,cardN]ドローして1枚[cardT]リターン。
    TSF_theN=TSF_Forth_drawthe()
    TSF_theO=TSF_Forth_drawthe()
    TSF_theT=TSF_Forth_drawthe()
    TSF_theT=TSF_theT.replace(TSF_theO,TSF_theN)
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_theT)
    return ""

def TSF_Match_resub():    #TSFdoc:文字列を正規表現で置換。3枚[cardT,cardO,cardN]ドローして1枚[cardT]リターン。
    TSF_theN=TSF_Forth_drawthe()
    TSF_theO=TSF_Forth_drawthe()
    TSF_theT=TSF_Forth_drawthe()
    TSF_theT=re.sub(re.compile(TSF_theO,re.MULTILINE),TSF_theN,TSF_theT)
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_theT)
    return ""

def TSF_Match_replacesN():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_theN=TSF_Forth_drawthe();  TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=len(TSF_cardsN);
    TSF_theO=TSF_Forth_drawthe();  TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    TSF_theT=TSF_Forth_drawthe()
    if TSF_theT in TSF_Forth_stackD():
        TSF_text=TSF_Io_ESCdecode("\n".join(TSF_Forth_stackD()[TSF_theT]))
        for TSF_peek,TSF_card in enumerate(TSF_cardsO):
            if TSF_peek < TSF_cardsN_len:
                TSF_text=TSF_text.replace(TSF_card,TSF_cardsN[TSF_peek])
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N")
    return ""

def TSF_Match_replacesC():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分は周択。3枚[stackT,stackO,stackN]ドロー。
    TSF_theN=TSF_Forth_drawthe();  TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=len(TSF_cardsN);
    TSF_theO=TSF_Forth_drawthe();  TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    TSF_theT=TSF_Forth_drawthe()
    if TSF_theT in TSF_Forth_stackD():
        TSF_text=TSF_Io_ESCdecode("\n".join(TSF_Forth_stackD()[TSF_theT]))
        for TSF_peek,TSF_card in enumerate(TSF_cardsO):
            TSF_text=TSF_text.replace(TSF_card,TSF_cardsN[TSF_peek%TSF_cardsN_len])
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N")
    return ""

def TSF_Match_replacesM():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分は囲択。3枚[stackT,stackO,stackN]ドロー。
    TSF_theN=TSF_Forth_drawthe();  TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=len(TSF_cardsN);
    TSF_theO=TSF_Forth_drawthe();  TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    TSF_theT=TSF_Forth_drawthe()
    if TSF_theT in TSF_Forth_stackD():
        TSF_text=TSF_Io_ESCdecode("\n".join(TSF_Forth_stackD()[TSF_theT]))
        for TSF_peek,TSF_card in enumerate(TSF_cardsO):
            TSF_text=TSF_text.replace(TSF_card,TSF_cardsN[min(TSF_peek,TSF_cardsN_len-1)])
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N")
    return ""


TSF_Initcalldebug=[TSF_Match_Initcards]
def TSF_Match_debug(TSF_sysargvs):    #TSFdoc:「TSF_Match」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Match.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)

if __name__=="__main__":
    TSF_Match_debug(TSF_Io_argvs(["python","TSF_Match.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
