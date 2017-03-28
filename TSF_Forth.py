#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import random
import re
from TSF_Io import *

def TSF_Forth_1ststack():    #TSF_doc:TSF_初期化に使う最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSF_doc:TSF_初期化に使うバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945"

def TSF_Forth_Initcards(TSF_cardsD,TSF_cardsO):    #TSF_doc:ワードを初期化する(TSFAPI)。
    TSF_Forth_cards={
        "#TSF_viewthe":TSF_Forth_viewthe,
        "#TSF_viewthis":TSF_Forth_viewthis,
        "#TSF_viewthat":TSF_Forth_viewthat,
        "#TSF_viewthey":TSF_Forth_viewthey,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Forth_viewthe():    #TSF_doc:[stack]指定したスタックを表示する。1スタック積み下ろし。
#    TSF_Forth_view(TSF_Forth_popthat())
    return ""

def TSF_Forth_viewthis():    #TSF_doc:[]実行中スタックを表示する。0スタック積み下ろし。
    TSF_Forth_view(TSF_stackthis)
    return ""

def TSF_Forth_viewthat():    #TSF_doc:[]積込先スタックを表示する。0スタック積み下ろし。
    TSF_Forth_view(TSF_stackthat)
    return ""

def TSF_Forth_viewthey():    #TSF_doc:[]スタック一覧を表示する。0スタック積み下ろし。
    for TSF_the in TSF_stackO:
        TSF_Forth_view(TSF_the,True)
    return ""


TSF_Initcards=[]
TSF_cardD={}
TSF_stackD={}
TSF_styleD={}
TSF_callptrD={}
TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO=[],[],[],[]
TSF_stackthis,TSF_stackthat=TSF_Forth_1ststack(),TSF_Forth_1ststack()
TSF_stackcount=0
def TSF_Forth_init(TSF_argvs=[],TSF_addcards=[]):    #TSF_doc:TSF_stacks,TSF_styles,TSF_callptrs,TSF_wordsなどをまとめて初期化する(TSFAPI)。
    global TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardD,TSF_stackO,TSF_styleO,TSF_callptrO,TSF_cardO
    global TSF_stackthis,TSF_stackthat,TSF_stackcount
    TSF_cardD={}
    TSF_stackD={}
    TSF_styleD={}
    TSF_callptrD={}
    TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO=[],[],[],[]
    TSF_stackthis,TSF_stackthat=TSF_Forth_1ststack(),TSF_Forth_1ststack()
    TSF_stackcount=0
    TSF_stackD[TSF_stackthis]=["0","#TSF_fin."]; TSF_stackO.append(TSF_stackthis)
#    TSF_stackD["#TSF_argvs"]=TSF_argvs[1:]; TSF_stackO.append("#TSF_argvs")
    TSF_Initcards=[TSF_Forth_Initcards]+TSF_addcards
    for TSF_Initcall in TSF_Initcards:
        TSF_cardD,TSF_cardO=TSF_Initcall(TSF_cardD,TSF_cardO)
#    print("TSF_cardO",TSF_cardO)
#    print("TSF_cardD",TSF_cardD)
#    print("TSF_cardD",TSF_cardD["#(debug)TSF_version"]())

def TSF_Forth_view(TSF_the,TSF_view_io=True,TSF_view_log=""):    #TSF_doc:スタックの内容をテキスト表示(TSFAPI)。
    if TSF_view_log == None: TSF_view_log="";
    if TSF_the in TSF_stackD:
        TSF_style=TSF_styleD.get(TSF_the,"T")
        if TSF_style == "O":
            TSF_view_logline="{0}\t{1}\n".format(TSF_the,"\t".join(TSF_stackD[TSF_the]))
        elif TSF_style == "T":
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_the,"\t".join(TSF_stackD[TSF_the]))
        else:  # TSF_style == "N":
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_the,"\n\t".join(TSF_stackD[TSF_the]))
        TSF_view_log=TSF_Io_printlog(TSF_view_logline,TSF_log=TSF_view_log) if TSF_view_io == True else TSF_view_log+TSF_view_logline
    return TSF_view_log


TSF_Initcalldebug=[TSF_Forth_Initcards]
def TSF_Io_debug(TSF_argvs):    #TSFdoc:「TSF/TSF_io.py」単体テスト風デバッグ関数。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_pyForth.log";
    print("--- {0} ---".format(__file__))
    TSF_Forth_init(TSF_argvs,TSF_Initcalldebug)
    for TSF_the in TSF_stackO:
        TSF_debug_log=TSF_Forth_view(TSF_the,True,TSF_debug_log)
    print("--- fin. > {0} ---".format(TSF_debug_savefilename))
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    return TSF_debug_log


if __name__=="__main__":
    TSF_Io_debug(TSF_Io_argvs(sys.argv))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
