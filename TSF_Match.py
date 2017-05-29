#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import re
import random

from TSF_Io import *
from TSF_Forth import *


def TSF_Match_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Match")
    TSF_Forth_cards={
#        "#TSF_replacesQN":TSF_Match_replacesQN, "#同択文字列群で順択置換":TSF_Match_replacesQN,
#        "#TSF_replacesQC":TSF_Match_replacesQC, "#同択文字列群で周択置換":TSF_Match_replacesQC,
#        "#TSF_replacesQM":TSF_Match_replacesQM, "#同択文字列群で囲択置換":TSF_Match_replacesQM,
#        "#TSF_replacesQV":TSF_Match_replacesQV, "#同択文字列群で逆択置換":TSF_Match_replacesQV,
#        "#TSF_replacesQA":TSF_Match_replacesQA, "#同択文字列群で乱択置換":TSF_Match_replacesQA,
#        "#TSF_replacesQT":TSF_Match_replacesQT, "#同択文字列群で額択置換":TSF_Match_replacesQT,
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
#        "#TSF_replacesRT":TSF_Match_replacesRT, "#含択文字列群で額択置換":TSF_Match_replacesRT,
#        "#TSF_replacesHN":TSF_Match_replacesHN, "#似択文字列群で順択置換":TSF_Match_replacesHN,
#        "#TSF_replacesHC":TSF_Match_replacesHC, "#似択文字列群で周択置換":TSF_Match_replacesHC,
#        "#TSF_replacesHM":TSF_Match_replacesHM, "#似択文字列群で囲択置換":TSF_Match_replacesHM,
#        "#TSF_replacesHV":TSF_Match_replacesHV, "#似択文字列群で逆択置換":TSF_Match_replacesHV,
#        "#TSF_replacesHA":TSF_Match_replacesHA, "#似択文字列群で乱択置換":TSF_Match_replacesHA,
#        "#TSF_replacesHT":TSF_Match_replacesHT, "#似択文字列群で額択置換":TSF_Match_replacesHT,
#        "#TSF_aliasQN":TSF_Match_aliasQN, "#同択カードを順択置換":TSF_Match_aliasQN,
#        "#TSF_aliasesQC":TSF_Match_aliasesQC, "#文字列群で順択置換":TSF_Match_aliasesQC,
#        "#TSF_aliasesQM":TSF_Match_aliasesQM, "#文字列群で順択置換":TSF_Match_aliasesQM,
#        "#TSF_aliasesQV":TSF_Match_aliasesQV, "#文字列群で順択置換":TSF_Match_aliasesQV,
#        "#TSF_aliasesQA":TSF_Match_aliasesQA, "#文字列群で順択置換":TSF_Match_aliasesQA,
#        "#TSF_countsQ":TSF_Match_countsQ, "#文字列群で同択計数":TSF_Match_countsQ,
#        "#TSF_countsI":TSF_Match_countsI, "#文字列群で含択計数":TSF_Match_countsI,
#        "#TSF_countsL":TSF_Match_countsL, "#文字列群で規択計数":TSF_Match_countsL,
#        "#TSF_countsH":TSF_Match_countsH, "#文字列群で似択計数":TSF_Match_countsH,
#        "#TSF_countsL":TSF_Match_countsL, "#文字列群で札択計数":TSF_Match_countsL,
        "#TSF_replacesQSN":TSF_Match_replacesQSN, "#同択文字列群で順択置換":TSF_Match_replacesQSN,
        "#TSF_replacesQDN":TSF_Match_replacesQDN, "#同択文字列で順択置換":TSF_Match_replacesQDN,
        "#TSF_replacesQON":TSF_Match_replacesQON, "#同択で順択置換":TSF_Match_replacesQON,
        "#TSF_aliasQSN":TSF_Match_aliasQSN, "#同択文字列群で順択代入":TSF_Match_aliasQSN,
        "#TSF_aliasQDN":TSF_Match_aliasQDN, "#同択文字列で順択代入":TSF_Match_aliasQDN,
        "#TSF_aliasQON":TSF_Match_aliasQON, "#同択で順択代入":TSF_Match_aliasQON,
        "#TSF_docsQ":TSF_Match_docsQ, "#同択編集":TSF_Match_docsQ,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

# TSF --calc 5*3*6*2 = 180
def TSF_Match_replaceRAD(TSF_QIRHL,TSF_SDO,TSF_FNCMVA,TSF_RAD):    #TSFdoc:replace,aliassの共通部品。(TSFAPI)
    TSF_theN=TSF_Forth_drawthe();  TSF_theO=TSF_Forth_drawthe();  TSF_theT=TSF_Forth_drawthe();
    TSF_Text="";  TSF_cardsN,TSF_cardsO=[],[];  TSF_cardsI=TSF_cardsN;  TSF_cardsT="";
    TSF_cardsN_len=0;  TSF_cardsO_len=0;  TSF_SDOpoke="";
    if TSF_RAD == 'D':
        TSF_cardsN=[TSF_theN];  TSF_cardsN_len=1;
        TSF_cardsO=[TSF_theO];  TSF_cardsO_len=1;
        if TSF_theT in TSF_Forth_stackD():
            TSF_Text=TSF_Io_ESCdecode("\n".join(TSF_Forth_stackD()[TSF_theT]));  TSF_SDOpoke='S';
    else:
        if TSF_SDO == 'D':
            TSF_cardsN=[TSF_theN];  TSF_cardsN_len=1;
            TSF_cardsO=[TSF_theO];  TSF_cardsO_len=1;
            TSF_Text=TSF_theT;  TSF_SDOpoke='D';
        elif TSF_SDO == 'O':
            TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[TSF_theN]);  TSF_cardsN_len=len(TSF_cardsN);
            TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[TSF_theO]);  TSF_cardsO_len=len(TSF_cardsO);
            if TSF_theT in TSF_Forth_stackD():
                TSF_Text=TSF_Io_ESCdecode("\n".join(TSF_Forth_stackD()[TSF_theT]));  TSF_SDOpoke='S';
            else:
                TSF_Text=TSF_theT;  TSF_SDOpoke='D';
        elif TSF_SDO == 'S':
            TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=len(TSF_cardsN);
            TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);  TSF_cardsO_len=len(TSF_cardsO);
            if TSF_theT in TSF_Forth_stackD():
                TSF_Text=TSF_Io_ESCdecode("\n".join(TSF_Forth_stackD()[TSF_theT]));  TSF_SDOpoke='S';
    if TSF_FNCMVA == 'F':
        TSF_cardsI=[TSF_cardsN[-1] for TSF_peek in range(TSF_cardsO_len)]
    elif TSF_FNCMVA == 'N':
        TSF_cardsI=[(TSF_cardsN[TSF_peek] if TSF_peek < TSF_cardsN_len else "") for TSF_peek in range(TSF_cardsO_len)]
    elif TSF_FNCMVA == 'C':
        TSF_cardsI=[TSF_cardsN[TSF_peek%TSF_cardsN_len] for TSF_peek in range(TSF_cardsO_len)]
    elif TSF_FNCMVA == 'M':
        TSF_cardsI=[TSF_cardsN[min(TSF_peek,TSF_cardsN_len-1)] for TSF_peek in range(TSF_cardsO_len)]
    elif TSF_FNCMVA == 'V':
        TSF_cardsI=[(TSF_cardsN[-1-TSF_peek] if TSF_peek < TSF_cardsN_len else "") for TSF_peek in range(TSF_cardsO_len)]
    elif TSF_FNCMVA == 'A':
        TSF_cardsI=[TSF_cardsN[random.randint(0,TSF_cardsN_len-1)] for TSF_peek in range(TSF_cardsO_len)]
    if TSF_RAD == 'R':
        if TSF_QIRHL == 'Q':
            for TSF_peek,TSF_card in enumerate(TSF_cardsO):
                TSF_Text=TSF_Text.replace(TSF_card,TSF_cardsI[TSF_peek])
#        elif TSF_QIRHL == 'I':
        elif TSF_QIRHL == 'R':
            for TSF_peek,TSF_card in enumerate(TSF_cardsO):
                TSF_Text=re.sub(re.compile(TSF_card,re.MULTILINE),TSF_cardsI[TSF_peek],TSF_Text)
#        elif TSF_QIRHL == 'H':
#        elif TSF_QIRHL == 'L':
    elif TSF_RAD == 'A':
        if TSF_QIRHL == 'Q':
            for TSF_peek,TSF_card in enumerate(TSF_cardsO):
                if TSF_Text == TSF_card:
                    TSF_cardsT=TSF_cardsI[TSF_peek];  break;
        if TSF_QIRHL == 'I':
            for TSF_peek,TSF_card in enumerate(TSF_cardsO):
                if TSF_card in TSF_Text:
                    TSF_cardsT=TSF_cardsI[TSF_peek];  break;
#        elif TSF_QIRHL == 'R':
#        elif TSF_QIRHL == 'H':
#        elif TSF_QIRHL == 'L':
        TSF_Text=TSF_cardsT
    if TSF_RAD == 'D':
        if TSF_QIRHL == 'Q':
            TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[TSF_theN]);
            TSF_Text=TSF_Text.replace(TSF_theO,TSF_Io_ESCdecode("\n".join(TSF_cardsN)))
#        elif TSF_QIRHL == 'I':
#        elif TSF_QIRHL == 'R':
#        elif TSF_QIRHL == 'H':
#        elif TSF_QIRHL == 'L':
    if TSF_SDOpoke == 'S':
        TSF_Forth_setTSF(TSF_theT,TSF_Text,'@')
    elif TSF_SDOpoke == 'D':
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_Text)

def TSF_Match_replacesQSN():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q','S','N','R');    return ""
def TSF_Match_replacesQDN():    #TSFdoc:stackTをカードとみなしてcardOの文字列をcardNの文字列に置換。不足分はゼロ文字列。3枚[cardT,cardO,cardN]ドロー。1枚[cardN]リターン。
    TSF_Match_replaceRAD('Q','D','N','R');    return ""
def TSF_Match_replacesQON():    #TSFdoc:stackTがカードかスタックか判断してON置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。Tがカードなら1枚[cardN]リターン。
    TSF_Match_replaceRAD('Q','O','N','R');    return ""

def TSF_Match_aliasQSN():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列群で代入。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q','S','N','A');    return ""
def TSF_Match_aliasQDN():    #TSFdoc:stackTをカードとみなしてcardOの文字列と同択できたらstackNの文字列で代入。不足分はゼロ文字列。3枚[cardT,cardO,cardN]ドロー。1枚[cardN]リターン。
    TSF_Match_replaceRAD('Q','D','N','A');    return ""
def TSF_Match_aliasQON():    #TSFdoc:stackTがカードかスタックか判断してON置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。Tがカードなら1枚[cardN]リターン。
    TSF_Match_replaceRAD('Q','O','N','A');    return ""

def TSF_Match_docsQ():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列またはスタックで編集。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q',' ',' ','D');    return ""


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
