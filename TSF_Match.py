#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import re

from TSF_Io import *
from TSF_Forth import *


def TSF_Match_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Match")
    TSF_Forth_cards={
        "#TSF_replacesQN":TSF_Match_replacesQN, "#同択文字列群で順択置換":TSF_Match_replacesQN,
        "#TSF_replacesQC":TSF_Match_replacesQC, "#同択文字列群で周択置換":TSF_Match_replacesQC,
        "#TSF_replacesQM":TSF_Match_replacesQM, "#同択文字列群で囲択置換":TSF_Match_replacesQM,
#        "#TSF_replacesQV":TSF_Match_replacesQV, "#同択文字列群で逆択置換":TSF_Match_replacesQV,
#        "#TSF_replacesQA":TSF_Match_replacesQA, "#同択文字列群で乱択置換":TSF_Match_replacesQA,
        "#TSF_replacesQT":TSF_Match_replacesQT, "#同択文字列群で額択置換":TSF_Match_replacesQT,
#        "#TSF_replacesIN":TSF_Match_replacesIN, "#含択文字列群で順択置換":TSF_Match_replacesIN,
#        "#TSF_replacesIC":TSF_Match_replacesIC, "#含択文字列群で周択置換":TSF_Match_replacesIC,
#        "#TSF_replacesIM":TSF_Match_replacesIM, "#含択文字列群で囲択置換":TSF_Match_replacesIM,
#        "#TSF_replacesIV":TSF_Match_replacesIV, "#含択文字列群で逆択置換":TSF_Match_replacesIV,
#        "#TSF_replacesIA":TSF_Match_replacesIA, "#含択文字列群で乱択置換":TSF_Match_replacesIA,
#        "#TSF_replacesIT":TSF_Match_replacesIT, "#含択文字列群で額択置換":TSF_Match_replacesIT,
#        "#TSF_replacesRN":TSF_Match_replacesRN, "#規択文字列群で順択置換":TSF_Match_replacesRN,
#        "#TSF_replacesRC":TSF_Match_replacesRC, "#規択文字列群で周択置換":TSF_Match_replacesRC,
#        "#TSF_replacesRM":TSF_Match_replacesRM, "#規択文字列群で囲択置換":TSF_Match_replacesRM,
#        "#TSF_replacesRV":TSF_Match_replacesRV, "#規択文字列群で逆択置換":TSF_Match_replacesRV,
#        "#TSF_replacesRA":TSF_Match_replacesRA, "#規択文字列群で乱択置換":TSF_Match_replacesRA,
        "#TSF_replacesRT":TSF_Match_replacesRT, "#含択文字列群で額択置換":TSF_Match_replacesRT,
#        "#TSF_replacesHN":TSF_Match_replacesHN, "#似択文字列群で順択置換":TSF_Match_replacesHN,
#        "#TSF_replacesHC":TSF_Match_replacesHC, "#似択文字列群で周択置換":TSF_Match_replacesHC,
#        "#TSF_replacesHM":TSF_Match_replacesHM, "#似択文字列群で囲択置換":TSF_Match_replacesHM,
#        "#TSF_replacesHV":TSF_Match_replacesHV, "#似択文字列群で逆択置換":TSF_Match_replacesHV,
#        "#TSF_replacesHA":TSF_Match_replacesHA, "#似択文字列群で乱択置換":TSF_Match_replacesHA,
#        "#TSF_replacesHT":TSF_Match_replacesHT, "#似択文字列群で額択置換":TSF_Match_replacesHT,
        "#TSF_aliasQN":TSF_Match_aliasQN, "#同択カードを順択置換":TSF_Match_aliasQN,
#        "#TSF_aliasesQC":TSF_Match_aliasesQC, "#文字列群で順択置換":TSF_Match_aliasesQC,
#        "#TSF_aliasesQM":TSF_Match_aliasesQM, "#文字列群で順択置換":TSF_Match_aliasesQM,
#        "#TSF_aliasesQV":TSF_Match_aliasesQV, "#文字列群で順択置換":TSF_Match_aliasesQV,
#        "#TSF_aliasesQA":TSF_Match_aliasesQA, "#文字列群で順択置換":TSF_Match_aliasesQA,
#        "#TSF_countsQ":TSF_Match_countsQ, "#文字列群で同択計数":TSF_Match_countsQ,
#        "#TSF_countsI":TSF_Match_countsI, "#文字列群で含択計数":TSF_Match_countsI,
#        "#TSF_countsL":TSF_Match_countsL, "#文字列群で規択計数":TSF_Match_countsL,
#        "#TSF_countsH":TSF_Match_countsH, "#文字列群で似択計数":TSF_Match_countsH,
#        "#TSF_countsL":TSF_Match_countsL, "#文字列群で札択計数":TSF_Match_countsL,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Match_replacesQN():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
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

def TSF_Match_replacesQC():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分は周択。3枚[stackT,stackO,stackN]ドロー。
    TSF_theN=TSF_Forth_drawthe();  TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=len(TSF_cardsN);
    TSF_theO=TSF_Forth_drawthe();  TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    TSF_theT=TSF_Forth_drawthe()
    if TSF_theT in TSF_Forth_stackD():
        TSF_text=TSF_Io_ESCdecode("\n".join(TSF_Forth_stackD()[TSF_theT]))
        for TSF_peek,TSF_card in enumerate(TSF_cardsO):
            TSF_text=TSF_text.replace(TSF_card,TSF_cardsN[TSF_peek%TSF_cardsN_len])
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N")
    return ""

def TSF_Match_replacesQM():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分は囲択。3枚[stackT,stackO,stackN]ドロー。
    TSF_theN=TSF_Forth_drawthe();  TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=len(TSF_cardsN);
    TSF_theO=TSF_Forth_drawthe();  TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    TSF_theT=TSF_Forth_drawthe()
    if TSF_theT in TSF_Forth_stackD():
        TSF_text=TSF_Io_ESCdecode("\n".join(TSF_Forth_stackD()[TSF_theT]))
        for TSF_peek,TSF_card in enumerate(TSF_cardsO):
            TSF_text=TSF_text.replace(TSF_card,TSF_cardsN[min(TSF_peek,TSF_cardsN_len-1)])
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N")
    return ""

def TSF_Match_replacesQT():    #TSFdoc:stackTをテキストとみなしてcardOの文字列をcardNの文字列に置換。3枚[stackT,cardO,cardN]ドロー。1枚リターン[cardN]。
    TSF_theN=TSF_Forth_drawthe()
    TSF_theO=TSF_Forth_drawthe()
    TSF_theT=TSF_Forth_drawthe()
    TSF_theT=TSF_theT.replace(TSF_theO,TSF_theN)
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_theT)
    return ""

def TSF_Match_replacesRT():    #TSFdoc:stackTをテキストとみなしてcardOの文字列をcardNの文字列に置換。3枚[stackT,cardO,cardN]ドロー。1枚リターン[cardN]。
    TSF_theN=TSF_Forth_drawthe()
    TSF_theO=TSF_Forth_drawthe()
    TSF_theT=TSF_Forth_drawthe()
    TSF_theT=re.sub(re.compile(TSF_theO,re.MULTILINE),TSF_theN,TSF_theT)
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_theT)
    return ""

def TSF_Match_aliasQN():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分は囲択。3枚[cardT,stackO,stackN]ドロー。1枚リターン[cardN]。
    TSF_theN=TSF_Forth_drawthe();  TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=len(TSF_cardsN);
    TSF_theO=TSF_Forth_drawthe();  TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    TSF_cardT=TSF_Forth_drawthe();
    for TSF_peek,TSF_card in enumerate(TSF_cardsO):
        if TSF_cardT == TSF_card:
            TSF_cardT=TSF_cardsN[min(TSF_peek,TSF_cardsN_len-1)]
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_cardT)
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
