#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import random
import re
from TSF_Io import *

def TSF_Forth_1ststack():    #TSFdoc:最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSFdoc:TSFバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945"

def TSF_Forth_Initcards(TSF_cardsD,TSF_cardsO):    #TSF_doc:ワードを初期化する(TSFAPI)。
    TSF_Forth_cards={
        "#TSF_fin.":TSF_Forth_fin,
        "#TSF_viewthe":TSF_Forth_viewthe,
        "#TSF_viewthis":TSF_Forth_viewthis,
        "#TSF_viewthat":TSF_Forth_viewthat,
        "#TSF_viewthey":TSF_Forth_viewthey,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Forth_fin():    #TSFdoc:TSF終了時のオプションを指定する。1枚[errmsg]ドロー。
    global TSF_callptrs
    TSF_callptrD={}
    return "#exit"

def TSF_Forth_viewthe():    #TSFdoc:指定したスタックを表示する。1枚[the]ドロー。
    TSF_Forth_view(TSF_Forth_drawthe())
    return ""

def TSF_Forth_viewthis():    #TSFdoc:実行中スタックを表示する。0枚ドロー。
    TSF_Forth_view(TSF_Forth_drawthis())
    return ""

def TSF_Forth_viewthat():    #TSFdoc:積込先スタックを表示する。0枚ドロー。
    TSF_Forth_view(TSF_Forth_drawthat())
    return ""

def TSF_Forth_viewthey():    #TSFdoc:スタック一覧を表示する。0枚ドロー。
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
def TSF_Forth_initTSF(TSF_argvs=[],TSF_addcards=[]):    #TSFdoc:スタックやカードなどをまとめて初期化する(TSFAPI)。
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_stackcount
    TSF_cardD={}
    TSF_stackD={}
    TSF_styleD={}
    TSF_callptrD={}
    TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO=[],[],[],[]
    TSF_stackthis,TSF_stackthat=TSF_Forth_1ststack(),TSF_Forth_1ststack()
    TSF_stackcount=0
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"0\t#TSF_fin.","T")
    TSF_Forth_setTSF("set(del)test","this:Peek\tthat:Poke\tthe:Pull\tthey:Push","T")
    TSF_Initcards=[TSF_Forth_Initcards]+TSF_addcards
    for TSF_Initcall in TSF_Initcards:
        TSF_cardD,TSF_cardO=TSF_Initcall(TSF_cardD,TSF_cardO)

def TSF_Forth_setTSF(TSF_the,TSF_text=None,TSF_style=None):    #TSFdoc:TSFの外からスタックにカードを積む。(TSFAPI)
    global TSF_stackD,TSF_styleD,TSF_stackO,TSF_styleO
    if TSF_style == None: TSF_style="T"
    if TSF_text != None:
        if not TSF_the in TSF_stackD:
            TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
        TSF_stackD[TSF_the]=TSF_text.rstrip('\n').replace('\t','\n').split('\n')
        TSF_styleD[TSF_the]=TSF_style
    else:
        if TSF_the in TSF_stackD:  del TSF_stackD[TSF_the]
        if TSF_the in TSF_styleD:  del TSF_styleD[TSF_the]
        if TSF_the in TSF_stackO: TSF_stackO.pop(TSF_stackO.index(TSF_the))
        if TSF_the in TSF_styleO: TSF_styleO.pop(TSF_styleO.index(TSF_the))


def TSF_Forth_run():    #TSFdoc:TSFデッキを走らせる。
    pass

#def TSF_Forth_run():    #TSF_doc:TSF_stacks,TSF_styles,TSF_callptrs,TSF_wordsなどをまとめて初期化する(TSFAPI)。
#    global TSF_stacks,TSF_styles,TSF_callptrs,TSF_words,TSF_Initcalls,TSF_stackthat,TSF_stackthis,TSF_stackcount
#    while True:
#        while TSF_stackcount < len(TSF_stacks[TSF_stackthis]):
#            TSF_stacknow,TSF_stacknext=TSF_stacks[TSF_stackthis][TSF_stackcount],None
#            if TSF_stacknow in TSF_words:
#                TSF_stacknext=TSF_words[TSF_stacknow]()
#            else:
#                TSF_Forth_pushthat(TSF_stacknow)
#            TSF_stackcount+=1
#            if TSF_stacknext != None:
#                if TSF_stacknext == "":
#                    if len(TSF_callptrs) > 0:
#                        TSF_stackthis,TSF_stackcount=TSF_callptrs.popitem(True)
#                    else:
#                        break
#                elif TSF_stacknext in TSF_stacks:
#                    if TSF_stacknext in TSF_callptrs:
#                        while TSF_stacknext in TSF_callptrs:
#                           TSF_callptrs.popitem(True)
#                    TSF_callptrs[TSF_stackthis]=TSF_stackcount
#                    TSF_stackthis=TSF_stacknext
#                    TSF_stackcount=0
#                else:
#                    break
#        if len(TSF_callptrs) > 0:
#            TSF_stackthis,TSF_stackcount=TSF_callptrs.popitem(True)
#        else:
#            break


def TSF_Forth_view(TSF_the,TSF_view_io=True,TSF_view_log=""):    #TSFdoc:スタックの内容をテキスト表示(TSFAPI)。
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

def TSF_Forth_draw(TSF_the):    #TSFdoc:スタックから1枚ドロー。(TSFAPI)
    global TSF_stacks
    TSF_draw=""
    if len(TSF_stackD[TSF_the]) and len(TSF_the) and TSF_the in TSF_stackD:
        TSF_draw=TSF_stackD[TSF_the].pop()
    return TSF_draw

def TSF_Forth_drawthe():    #TSFdoc:theスタックの取得(thatから1枚ドロー)。(TSFAPI)
    return TSF_Forth_draw(TSF_stackthat)

def TSF_Forth_drawthis():    #TSFdoc:theスタックの取得(thatから0枚ドロー)。(TSFAPI)
    return TSF_stackthis

def TSF_Forth_drawthat():    #TSFdoc:theスタックの取得(thatから0枚ドロー)。(TSFAPI)
    return TSF_stackthat

TSF_Initcalldebug=[TSF_Forth_Initcards]
def TSF_Io_debug(TSF_argvs):    #TSFdoc:「TSF_Forth」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_pyForth.log";
    print("--- {0} ---".format(__file__))
    TSF_Forth_initTSF(TSF_argvs,TSF_Initcalldebug)
    for TSF_the in TSF_stackO:
        TSF_debug_log=TSF_Forth_view(TSF_the,True,TSF_debug_log)
    print("TSF_Forth_drawthe:{0}",TSF_Forth_drawthe())
    print("TSF_Forth_drawthis:{0}",TSF_Forth_drawthis())
    print("TSF_Forth_drawthat:{0}",TSF_Forth_drawthat())
    TSF_Forth_setTSF("set(del)test")
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
