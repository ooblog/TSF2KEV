#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
#import random
#import re
from TSF_Io import *

def TSF_Forth_1ststack():    #TSFdoc:最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSFdoc:TSFバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945"

def TSF_Forth_Initcards(TSF_cardsD,TSF_cardsO):    #TSF_doc:ワードを初期化する(TSFAPI)。
    TSF_Forth_cards={
        "#TSF_fin.":TSF_Forth_fin, "#TSFを終了。":TSF_Forth_fin,
        "#TSF_this":TSF_Forth_this, "#スタックを実行":TSF_Forth_this,
        "#TSF_that":TSF_Forth_that, "#スタックに積込":TSF_Forth_that,
        "#TSF_stylethe":TSF_Forth_stylethe, "#指定スタックにスタイル指定":TSF_Forth_stylethe,
        "#TSF_stylethis":TSF_Forth_stylethis, "#実行中スタックにスタイル指定":TSF_Forth_stylethis,
        "#TSF_stylethat":TSF_Forth_stylethat, "#積込先スタックにスタイル指定":TSF_Forth_stylethat,
        "#TSF_stylethey":TSF_Forth_stylethey, "#全スタックにスタイル指定":TSF_Forth_stylethey,
        "#TSF_viewthe":TSF_Forth_viewthe, "#指定スタック表示":TSF_Forth_viewthe,
        "#TSF_viewthis":TSF_Forth_viewthis, "#実行中スタックを表示":TSF_Forth_viewthis,
        "#TSF_viewthat":TSF_Forth_viewthat, "#積込先スタックを表示":TSF_Forth_viewthat,
        "#TSF_viewthey":TSF_Forth_viewthey, "#スタック一覧を表示":TSF_Forth_viewthey,
        "#TSF_RPN":TSF_Forth_RPN, "#逆ポーランド電卓で計算":TSF_Forth_RPN, "#小数計算":TSF_Forth_RPN,
        "#TSF_echo":TSF_Forth_echo, "#カードを表示":TSF_Forth_echo,
        "#TSF_echoN":TSF_Forth_echoN, "#N枚カードを表示":TSF_Forth_echoN,
        "#TSF_argvs":TSF_Forth_argvs, "#コマンド読込":TSF_Forth_argvs,
        "#TSF_readtext":TSF_Forth_readtext, "#テキストを読込":TSF_Forth_readtext,
        "#TSF_mergethe":TSF_Forth_mergethe, "#TSFに合成":TSF_Forth_mergethe,
        "#TSF_publishthe":TSF_Forth_publishthe, "#指定スタックをテキスト化":TSF_Forth_publishthe,
        "#TSF_publishthis":TSF_Forth_publishthis, "#実行中スタックをテキスト化":TSF_Forth_publishthis,
        "#TSF_publishthat":TSF_Forth_publishthat, "#積込先スタックをテキスト化":TSF_Forth_publishthat,
        "#TSF_remove":TSF_Forth_remove, "#ファイルを削除する":TSF_Forth_remove,
        "#TSF_savetext":TSF_Forth_savetext, "#テキストファイルに上書":TSF_Forth_savetext,
        "#TSF_writetext":TSF_Forth_writetext, "#テキストファイルに追記":TSF_Forth_writetext,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Forth_fin():    #TSFdoc:TSF終了時のオプションを指定する。1枚[errmsg]ドロー。
    global TSF_fincode
    global TSF_callptrD,TSF_callptrO
    TSF_callptrD={};  TSF_callptrO=[];
    return "#exit"

def TSF_Forth_this():    #TSF_doc:thisスタックの変更。1枚[this]ドロー。
    TSF_card=TSF_Forth_drawthe();
    if len(TSF_card) == 0 or TSF_card.startswith('#'):  TSF_cardnow="#exit"
    return TSF_card

def TSF_Forth_that():    #TSF_doc:thatスタックの変更。1枚[that]ドロー。
    TSF_Forth_drawthat(TSF_Forth_drawthe())
    return ""

def TSF_Forth_stylethe():    #TSFdoc:指定したスタックの表示方法を指定する。2枚[style,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_style(TSF_the,TSF_Forth_drawthe())
    return ""

def TSF_Forth_stylethis():    #TSFdoc:実行中スタックの表示方法を指定する。1枚[style]ドロー。
    TSF_Forth_style(TSF_Forth_drawthis(),TSF_Forth_drawthe())
    return ""

def TSF_Forth_stylethat():    #TSFdoc:積込先スタックの表示方法を指定する。1枚[style]ドロー。
    TSF_Forth_style(TSF_Forth_drawthat(),TSF_Forth_drawthe())
    return ""

def TSF_Forth_stylethey():    #TSFdoc:全スタックの表示方法を一括指定。1枚[style]ドロー。
    TSF_style=TSF_Forth_drawthe()
    for TSF_the in TSF_stackO:
        TSF_Forth_style(TSF_the,TSF_style)
    return ""

def TSF_Forth_viewthe():    #TSFdoc:指定スタックを表示する。1枚[the]ドロー。
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
        TSF_Forth_view(TSF_the)
    return ""

def TSF_Forth_RPN():    #TSF_doc:RPN電卓。1枚[rpn]ドロー。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Io_RPN(TSF_Forth_drawthe()))
    return ""

def TSF_Forth_echo():    #TSF_doc:カードの表示。1枚[echo]ドロー。
    global TSF_echo_log
    if TSF_echo:
        TSF_echo_log=TSF_Io_printlog(TSF_Forth_drawthe(),TSF_echo_log)
    else:
        TSF_Io_printlog(TSF_Forth_drawthe())
    return ""

def TSF_Forth_echoN():    #TSF_doc:カードの複数枚表示。RPN枚[echoN…echoA,N]ドロー。
    TSF_echoRPN=max(int(TSF_Io_RPN(TSF_Forth_drawthe())),0)
    if TSF_echoRPN > 0:
        for TSF_count in range(TSF_echoRPN):
            TSF_Forth_echo()
    return ""

def TSF_Forth_argvs():    #TSF_doc:コマンドをカード召喚。RPN枚[argvN…argvA,N]リターン。
    TSF_argvslen=len(TSF_mainandargvs[1:]) if len(TSF_mainandargvs) > 0 else 0
    if TSF_argvslen > 0:
        for TSF_card in TSF_mainandargvs[1:]:
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_argvslen))

def TSF_Forth_readtext():   #TSF_doc:ファイル名のスタックにテキストを読み込む。1枚[path]ドロー。
    TSF_path=TSF_Forth_drawthe()
    TSF_Forth_loadtext(TSF_path,TSF_path)
    return ""

def TSF_Forth_mergethe():   #TSF_doc:テキストをTSFとして読み込む。1枚[merge]ドロー。
    TSF_Forth_merge(TSF_Forth_drawthe(),[TSF_Forth_1ststack()])
    return ""

def TSF_Forth_publishthe():   #TSF_doc:指定スタックをテキスト化。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_publish_log=TSF_Forth_view(TSF_the,False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_the])
    return None

def TSF_Forth_publishthis():   #TSF_doc:実行中スタックをテキスト化。1枚[path]ドロー。
    TSF_publish_log=TSF_Forth_view(TSF_Forth_drawthis(),False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_Forth_drawthis()])
    return None

def TSF_Forth_publishthat():   #TSF_doc:積込先スタックをテキスト化。1枚[path]ドロー。
    TSF_publish_log=TSF_Forth_view(TSF_Forth_drawthat(),False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_Forth_drawthat()])
    return None

def TSF_Forth_remove():   #TSF_doc:ファイルを削除する。1枚[path]ドロー。
    TSF_Io_savetext(TSF_Forth_drawthe())
    return None

def TSF_Forth_savetext():   #TSF_doc:テキスト化スタックをファイルに保存する。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_text=TSF_Io_ESCdecode("\n".join(TSF_stackD[TSF_the])) if TSF_the in TSF_stackD else ""
    TSF_Io_savetext(TSF_Forth_drawthe(),TSF_text)
    return None

def TSF_Forth_writetext():   #TSF_doc:テキスト化スタックをファイルに追記する。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_text=TSF_Io_ESCdecode("\n".join(TSF_stackD[TSF_the])) if TSF_the in TSF_stackD else ""
    TSF_Io_writetext(TSF_Forth_drawthe(),TSF_text)
    return None


TSF_mainandargvs=[]
TSF_cardD={}
TSF_stackD={}
TSF_styleD={}
TSF_callptrD={}
TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO=[],[],[],[]
TSF_stackthis,TSF_stackthat=TSF_Forth_1ststack(),TSF_Forth_1ststack()
TSF_cardscount=0
def TSF_Forth_initTSF(TSF_sysargvs=[],TSF_addcards=[]):    #TSFdoc:スタックやカードなどをまとめて初期化する(TSFAPI)。
    global TSF_mainandargvs
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    TSF_cardD={}
    TSF_stackD={}
    TSF_styleD={}
    TSF_callptrD={}
    TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO=[],[],[],[]
    TSF_stackthis,TSF_stackthat=TSF_Forth_1ststack(),TSF_Forth_1ststack()
    TSF_cardscount=0
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"#TSF_fin.","T")
    TSF_mainandargvs=TSF_sysargvs
    TSF_Initcards=[TSF_Forth_Initcards]+TSF_addcards
    for TSF_Initcall in TSF_Initcards:
        TSF_cardD,TSF_cardO=TSF_Initcall(TSF_cardD,TSF_cardO)

def TSF_Forth_style(TSF_the,TSF_style=None):    #TSF_doc:スタックの表示スタイルを指定する(TSFAPI)。
    global TSF_styles
    if TSF_the in TSF_stackD:
        if TSF_style != None:
            TSF_styleD[TSF_the]=TSF_style
        TSF_style=TSF_styleD[TSF_the]
    else:
        TSF_style=""
    return TSF_style

def TSF_Forth_setTSF(TSF_the,TSF_text=None,TSF_style=None):    #TSFdoc:TSFの外からスタックにカードを積む/無を積むと削除。(TSFAPI)
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

def TSF_Forth_loadtext(TSF_the,TSF_path):    #TSF_doc:スタックにテキストファイルを読み込む。(TSFAPI)
    TSF_text=TSF_Io_loadtext(TSF_path)
    TSF_text=TSF_Io_ESCencode(TSF_text)
    TSF_Forth_setTSF(TSF_the,TSF_text,"N")
    return TSF_text

def TSF_Forth_merge(TSF_path,TSF_ESCstack=[],TSF_mergedel=False):    #TSF_doc:スタック内のテキストをTSFとして読み込む。(TSFAPI)
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    if TSF_path in TSF_stackD:
        TSF_the=TSF_Forth_1ststack()
        for TSF_card in TSF_stackD[TSF_path]:
            if len(TSF_card) == 0 or TSF_card.startswith("#"): continue;
            TSF_line=TSF_Io_ESCdecode(TSF_card)
            if not TSF_line.startswith('\t'):
                TSF_lineL=TSF_line.split('\t')
                if not TSF_lineL[0] in TSF_ESCstack:
                    TSF_the=TSF_lineL[0]
                    if not TSF_the in TSF_stackD:
                        TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
                    TSF_stackD[TSF_the]=[]
                    TSF_styleD[TSF_the]="O" if len(TSF_lineL) >= 2 else ""
            if not TSF_the in TSF_ESCstack:
                TSF_lineL=TSF_line.split('\t')[1:]
                if not TSF_the in TSF_stackD:
                    TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
                TSF_stackD[TSF_the].extend(TSF_lineL)
                if TSF_styleD[TSF_the] != "O":
                    TSF_styleD[TSF_the]="T" if len(TSF_lineL) >= 2 else "N"
        if TSF_mergedel:
             TSF_Forth_setTSF(TSF_path)


TSF_echo,TSF_echo_log=False,""
def TSF_Forth_run(TSF_run_log=None):    #TSFdoc:TSFデッキを走らせる。
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    global TSF_echo,TSF_echo_log
    if TSF_run_log != None:
        TSF_echo,TSF_echo_log=True,TSF_run_log
    else:
        TSF_echo,TSF_echo_log=False,""
    if not "#TSF_fin." in TSF_stackD[TSF_Forth_1ststack()]:
        TSF_Forth_return(TSF_Forth_1ststack(),"#TSF_fin.")
    while True:
        while TSF_cardscount < len(TSF_stackD[TSF_stackthis]) < 16:
            TSF_cardnow=TSF_stackD[TSF_stackthis][TSF_cardscount];  TSF_cardscount+=1;
            if not TSF_cardnow in TSF_cardD:
                TSF_Forth_return(TSF_stackthat,TSF_cardnow)
            else:
                TSF_stacknext=TSF_cardD[TSF_cardnow]()
                if TSF_stacknext == "":
                    continue
                elif not TSF_stacknext in TSF_stackD:
                    break
                else:
                    while TSF_stacknext in TSF_callptrO:
                        TSF_callptrD.pop(TSF_callptrO.pop())
                    TSF_callptrD[TSF_stackthis]=TSF_cardscount;  TSF_callptrO.append(TSF_stackthis);
                    TSF_stackthis=TSF_stacknext
                    TSF_cardscount=0
        if len(TSF_callptrO) > 0:
            TSF_stackthis=TSF_callptrO[-1]; TSF_cardscount=TSF_callptrD[TSF_callptrO[-1]];
            TSF_callptrD.pop(TSF_callptrO.pop())
        else:
            break
    return TSF_echo_log

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
    global TSF_stackD,TSF_stackO
    TSF_draw=""
    if len(TSF_stackD[TSF_the]) and len(TSF_the) and TSF_the in TSF_stackD:
        TSF_draw=TSF_stackD[TSF_the].pop()
    return TSF_draw

def TSF_Forth_drawthe():    #TSFdoc:theスタックの取得(thatから1枚ドロー)。(TSFAPI)
    return TSF_Forth_draw(TSF_stackthat)

def TSF_Forth_drawthis(TSF_the=None):    #TSFdoc:thisスタックの取得(thatから0枚ドロー)。(TSFAPI)
    global TSF_stackthis
    if TSF_the != None:
        TSF_stackthis=TSF_the
    return TSF_stackthis

def TSF_Forth_drawthat(TSF_the=None):    #TSFdoc:thatスタックの取得(thatから0枚ドロー)。(TSFAPI)
    global TSF_stackthat
    if TSF_the != None:
        TSF_stackthat=TSF_the
    return TSF_stackthat

def TSF_Forth_return(TSF_the,TSF_card):    #TSFdoc:theスタックに1枚リターン。(TSFAPI)
    if not TSF_the in TSF_stackD:
        TSF_stackO.append(TSF_the)
        TSF_stackD[TSF_the]=[]
    TSF_stackD[TSF_the].append(TSF_card)


TSF_Initcalldebug=[TSF_Forth_Initcards]
def TSF_Io_debug(TSF_sysargvs):    #TSFdoc:「TSF_Forth」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_pyForth.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"PPPP\t#TSF_this\tTSF_argvs:\t#TSF_that\t#TSF_argvs\t#TSF_fin.","T")
    TSF_Forth_setTSF("PPPP","this:Peek\tthat:Poke\tthe:Pull\tthey:Push\t2\t#TSF_echoN","T")
    for TSF_the in TSF_stackO:
        TSF_debug_log=TSF_Forth_view(TSF_the,True,TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("--- run ---",TSF_debug_log)
    TSF_debug_log=TSF_Forth_run(TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("--- fin. ---",TSF_debug_log)
    for TSF_the in TSF_stackO:
        TSF_debug_log=TSF_Forth_view(TSF_the,True,TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("--- {0} > {1} ---".format(__file__,TSF_debug_savefilename),TSF_debug_log)
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    return TSF_debug_log


if __name__=="__main__":
    TSF_Io_debug(TSF_Io_argvs(["python","TSF_Forth.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
