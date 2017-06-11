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
        "#TSF_casesQSN":TSF_Match_casesQSN, "#例外あり同択文字列群で表択代入":TSF_Match_casesQSN,
        "#TSF_casesQDN":TSF_Match_casesQDN, "#例外あり同択文字列で表択代入":TSF_Match_casesQDN,
        "#TSF_casesQON":TSF_Match_casesQON, "#例外あり同択で表択代入":TSF_Match_casesQON,
        "#TSF_docsQ":TSF_Match_docsQ, "#同択編集":TSF_Match_docsQ,
        "#TSF_Match":TSF_Match_Match, "#置換代入系統一式":TSF_Match_Match,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

# TSF --calc 5*3*6*2 = 180
def TSF_Match_replaceRAD(TSF_QIRHL,TSF_SDO,TSF_FNCMVA,TSF_RACD):    #TSFdoc:replace,aliassの共通部品。(TSFAPI)
    TSF_theN=TSF_Forth_drawthe();  TSF_theO=TSF_Forth_drawthe();  TSF_theT=TSF_Forth_drawthe();
    TSF_Text="";  TSF_cardsN,TSF_cardsO=[],[];  TSF_cardsI=TSF_cardsN;  TSF_cardsT="";
    TSF_cardsN_len=0;  TSF_cardsO_len=0;  TSF_SDOpoke="";
    if TSF_RACD == 'D':
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
    if TSF_RACD == 'R':
        if TSF_QIRHL == 'Q':
            for TSF_peek,TSF_card in enumerate(TSF_cardsO):
                TSF_Text=TSF_Text.replace(TSF_card,TSF_cardsI[TSF_peek])
#        elif TSF_QIRHL == 'I':
        elif TSF_QIRHL == 'R':
            for TSF_peek,TSF_card in enumerate(TSF_cardsO):
                TSF_Text=re.sub(re.compile(TSF_card,re.MULTILINE),TSF_cardsI[TSF_peek],TSF_Text)
#        elif TSF_QIRHL == 'H':
#        elif TSF_QIRHL == 'L':
    elif TSF_RACD == 'C' or TSF_RACD == 'A':
        if TSF_RACD == 'C':
            TSF_cardsT=TSF_cardsN[-1]
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
    elif TSF_RACD == 'D':
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

def TSF_Match_casesQSN():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列群で代入。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q','S','N','C');    return ""
def TSF_Match_casesQDN():    #TSFdoc:stackTをカードとみなしてcardOの文字列と同択できたらstackNの文字列で代入。不足分はゼロ文字列。3枚[cardT,cardO,cardN]ドロー。1枚[cardN]リターン。
    TSF_Match_replaceRAD('Q','D','N','C');    return ""
def TSF_Match_casesQON():    #TSFdoc:stackTがカードかスタックか判断してON置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。Tがカードなら1枚[cardN]リターン。
    TSF_Match_replaceRAD('Q','O','N','C');    return ""

def TSF_Match_docsQ():    #TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列またはスタックで編集。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q',' ',' ','D');    return ""


def TSF_Match_Match():    #TSFdoc:5*3*6*4=360もの関数を用意するのはしんどいので、replaceRADに渡すパラメータ用の関数を作成。4枚[stackT,stackO,stackN,macro]ドロー。
    TSF_MP=TSF_Forth_drawthe();    TSF_MP="".join([TSF_MP,"    "])
    TSF_Match_replaceRAD(TSF_MP[0],TSF_MP[1],TSF_MP[2],TSF_MP[3])
    return ""


TSF_Initcalldebug=[TSF_Match_Initcards]
def TSF_Match_debug(TSF_sysargvs):    #TSFdoc:「TSF_Match」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Match.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)

if __name__=="__main__":
    TSF_Match_debug(TSF_Io_argvs(["python","TSF_Match.py"]))


#! -- Copyright (c) 2017 ooblog --
#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
