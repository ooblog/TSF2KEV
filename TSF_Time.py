#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import re

from TSF_Io import *
from TSF_Forth import *


def TSF_Time_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Time")
    TSF_Forth_cards={
        "#TSF_calender":TSF_time_calender, "#日時等に置換":TSF_time_calender,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_time_calender():    #TSFdoc:現在日時の取得。1枚[timeformat]ドローして1枚[time]リターン。
    TSF_TimeQ=TSF_Forth_drawthe()
    TSF_TimeA=TSF_Time_brackets(TSF_TimeQ)
    TSF_Forth_return(TSF_TimeA);
    return ""

TSF_Initcalldebug=[TSF_Time_Initcards]
def TSF_Time_debug(TSF_sysargvs):    #TSFdoc:「TSF_Time」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Time.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)

if __name__=="__main__":
    TSF_Time_debug(TSF_Io_argvs(["python","TSF_Time.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
