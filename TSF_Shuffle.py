#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *


def TSF_Shuffle_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードにDやPythonに翻訳する命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Shuffle")
    TSF_Forth_cards={
#        "#TSF_peekCthe":TSF_Shuffle_peekCthe, "#指定スタック表面読込":TSF_Shuffle_peekCthe,
#        "#TSF_peekCthis":TSF_Shuffle_peekCthis, "#実行中スタック表面読込":TSF_Shuffle_peekCthis,
#        "#TSF_peekCthat":TSF_Shuffle_peekCthat, "#積込先スタック表面読込":TSF_Shuffle_peekCthat,
#        "#TSF_peekCthey":TSF_Shuffle_peekCthey, "#スタック一覧表面読込":TSF_Shuffle_peekCthey,
#        "#TSF_pokeCthe":TSF_Shuffle_pokeCthe, "#指定スタック表面上書":TSF_Shuffle_pokeCthe,
#        "#TSF_pokeCthis":TSF_Shuffle_pokeCthis, "#実行中スタック表面上書":TSF_Shuffle_pokeCthis,
#        "#TSF_pokeCthat":TSF_Shuffle_pokeCthat, "#積込先スタック表面上書":TSF_Shuffle_pokeCthat,
#        "#TSF_pokeCthey":TSF_Shuffle_pokeCthey, "#スタック一覧表面上書":TSF_Shuffle_pokeCthey,
#        "#TSF_pullCthe":TSF_Shuffle_pullCthe, "#指定スタック表面引抜":TSF_Shuffle_pullCthe,
#        "#TSF_pullCthis":TSF_Shuffle_pullCthis, "#実行中スタック表面引抜":TSF_Shuffle_pullCthis,
#        "#TSF_pullCthat":TSF_Shuffle_pullCthat, "#積込先スタック表面引抜":TSF_Shuffle_pullCthat,
#        "#TSF_pullCthey":TSF_Shuffle_pullCthey, "#スタック一覧表面引抜":TSF_Shuffle_pullCthey,
#        "#TSF_pushCthe":TSF_Shuffle_pushCthe, "#指定スタック差込":TSF_Shuffle_pushCthe,
#        "#TSF_pushCthis":TSF_Shuffle_pushCthis, "#実行中スタック差込":TSF_Shuffle_pushCthis,
#        "#TSF_pushCthat":TSF_Shuffle_pushCthat, "#積込先スタック差込":TSF_Shuffle_pushCthat,
#        "#TSF_pushCthey":TSF_Shuffle_pushCthey, "#スタック一覧差込":TSF_Shuffle_pushCthey,
        "#TSF_peekMthe":TSF_Shuffle_peekMthe, "#指定スタック囲択読込":TSF_Shuffle_peekMthe,
        "#TSF_peekMthis":TSF_Shuffle_peekMthis, "#実行中スタック囲択読込":TSF_Shuffle_peekMthis,
        "#TSF_peekMthat":TSF_Shuffle_peekMthat, "#積込先スタック囲択読込":TSF_Shuffle_peekMthat,
        "#TSF_peekMthey":TSF_Shuffle_peekMthey, "#スタック一覧囲択読込":TSF_Shuffle_peekMthey,
        "#TSF_pokeMthe":TSF_Shuffle_pokeMthe, "#指定スタック囲択上書":TSF_Shuffle_pokeMthe,
        "#TSF_pokeMthis":TSF_Shuffle_pokeMthis, "#実行中スタック囲択上書":TSF_Shuffle_pokeMthis,
        "#TSF_pokeMthat":TSF_Shuffle_pokeMthat, "#積込先スタック囲択上書":TSF_Shuffle_pokeMthat,
        "#TSF_pokeMthey":TSF_Shuffle_pokeMthey, "#スタック一覧囲択上書":TSF_Shuffle_pokeMthey,
#        "#TSF_pullMthe":TSF_Shuffle_pullMthe, "#指定スタック囲択引抜":TSF_Shuffle_pullMthe,
#        "#TSF_pullMthis":TSF_Shuffle_pullMthis, "#実行中スタック囲択引抜":TSF_Shuffle_pullMthis,
#        "#TSF_pullMthat":TSF_Shuffle_pullMthat, "#積込先スタック囲択引抜":TSF_Shuffle_pullMthat,
#        "#TSF_pullMthey":TSF_Shuffle_pullMthey, "#スタック一覧囲択引抜":TSF_Shuffle_pullMthey,
#        "#TSF_pushMthe":TSF_Shuffle_pushMthe, "#指定スタック差込":TSF_Shuffle_pushMthe,
#        "#TSF_pushMthis":TSF_Shuffle_pushMthis, "#実行中スタック差込":TSF_Shuffle_pushMthis,
#        "#TSF_pushMthat":TSF_Shuffle_pushMthat, "#積込先スタック差込":TSF_Shuffle_pushMthat,
#        "#TSF_pushMthey":TSF_Shuffle_pushMthey, "#スタック一覧差込":TSF_Shuffle_pushMthey,
#        "#TSF_peekLthe":TSF_Shuffle_peekLthe, "#指定スタックラベルで読込":TSF_Shuffle_peekLthe,
#        "#TSF_peekLthis":TSF_Shuffle_peekLthis, "#実行中スタックラベルで読込":TSF_Shuffle_peekLthis,
#        "#TSF_peekLthat":TSF_Shuffle_peekLthat, "#積込先スタックラベルで読込":TSF_Shuffle_peekLthat,
#        "#TSF_peekLthey":TSF_Shuffle_peekLthey, "#スタック一覧ラベルで読込":TSF_Shuffle_peekLthey,
#        "#TSF_pokeLthe":TSF_Shuffle_pokeLthe, "#指定スタックラベルで上書":TSF_Shuffle_pokeLthe,
#        "#TSF_pokeLthis":TSF_Shuffle_pokeLthis, "#実行中スタックラベルで上書":TSF_Shuffle_pokeLthis,
#        "#TSF_pokeLthat":TSF_Shuffle_pokeLthat, "#積込先スタックラベルで上書":TSF_Shuffle_pokeLthat,
#        "#TSF_pokeLthey":TSF_Shuffle_pokeLthey, "#スタック一覧ラベルで上書":TSF_Shuffle_pokeLthey,
#        "#TSF_pullLthe":TSF_Shuffle_pullLthe, "#指定スタックラベルで引抜":TSF_Shuffle_pullLthe,
#        "#TSF_pullLthis":TSF_Shuffle_pullLthis, "#実行中スタックラベルで引抜":TSF_Shuffle_pullLthis,
#        "#TSF_pullLthat":TSF_Shuffle_pullLthat, "#積込先スタックラベルで引抜":TSF_Shuffle_pullLthat,
#        "#TSF_pullLthey":TSF_Shuffle_pullLthey, "#スタック一覧ラベルで引抜":TSF_Shuffle_pullLthey,
#        "#TSF_pushLthe":TSF_Shuffle_pushLthe, "#指定スタックラベルで差込":TSF_Shuffle_pushLthe,
#        "#TSF_pushLthis":TSF_Shuffle_pushLthis, "#実行中スタックラベルで差込":TSF_Shuffle_pushLthis,
#        "#TSF_pushLthat":TSF_Shuffle_pushLthat, "#積込先スタックラベルで差込":TSF_Shuffle_pushLthat,
#        "#TSF_pushLthey":TSF_Shuffle_pushLthey, "#スタック一覧ラベルで差込":TSF_Shuffle_pushLthey,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Shuffle_peekM(TSF_the,TSF_peek):    #TSFdoc:指定スタックからスタック名を囲択で読込。(TSFAPI)。
    TSF_pull="";  TSF_cardsN_len=len(TSF_Forth_stackD()[TSF_the])
    if TSF_the in TSF_Forth_stackD() and 0 < TSF_cardsN_len:
        TSF_pull=TSF_Forth_stackD()[TSF_the][max(min(TSF_peek,TSF_cardsN_len-1),0)]
    return TSF_pull

def TSF_Shuffle_peekMthe():    #TSFdoc:指定スタックから囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthe(),TSF_peek))
    return ""

def TSF_Shuffle_peekMthis():    #TSFdoc:実行中スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthis(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return ""

def TSF_Shuffle_peekMthat():    #TSFdoc:積込先スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthat(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return ""

def TSF_Shuffle_peekMthey():    #TSFdoc:スタック一覧から最後尾スタック名を囲択で読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_pull="";  TSF_cardsN_len=len(TSF_Forth_stackO())
    if TSF_the in TSF_Forth_stackO() and 0 < TSF_cardsN_len:
        TSF_pull=TSF_Forth_stackO()[max(min(TSF_peek,TSF_cardsN_len-1),0)]
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_pull)
    return ""

def TSF_Shuffle_pokeM(TSF_the,TSF_peek,TSF_poke):    #TSFdoc:指定スタックからカードを囲択で読込。(TSFAPI)
    TSF_cardsN_len=len(TSF_Forth_stackD()[TSF_the])
    if TSF_the in TSF_Forth_stackD() and 0 < TSF_cardsN_len:
        TSF_Forth_stackD()[TSF_the][max(min(TSF_peek,TSF_cardsN_len-1),0)]=TSF_poke

def TSF_Shuffle_pokeMthe():    #TSFdoc:指定スタックからカードを囲択で上書。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Shuffle_pokeM(TSF_the,TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeMthis():    #TSFdoc:実行中スタックからカードを囲択で上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_pokeM(TSF_Forth_drawthis(),TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeMthat():    #TSFdoc:積込先スタックからカードを囲択で上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_pokeM(TSF_Forth_drawthat(),TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeMthey():    #TSFdoc:スタック一覧からスタック名を囲択で上書。2枚[poke,peek]ドロー。
    TSF_cardsN_len=len(TSF_Forth_stackO())
    TSF_peek=max(min(TSF_Io_RPNzero(TSF_Forth_drawthe()),TSF_cardsN_len-1),0)
    TSF_poke=TSF_Forth_drawthe()
    if 0 < TSF_cardsN_len:
        TSF_pull=TSF_Forth_stackO()[TSF_peek]
        if TSF_pull!=TSF_poke:
            TSF_Forth_stackO()[TSF_peek]=TSF_poke
            TSF_stackR=TSF_Forth_stackD().pop(TSF_pull)
            TSF_Forth_stackD()[TSF_poke]=TSF_stackR
    return ""


TSF_Initcalldebug=[TSF_Shuffle_Initcards]
def TSF_Shuffle_debug(TSF_sysargvs):    #TSFdoc:「TSF_Shuffle」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Shuffle.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)

if __name__=="__main__":
    TSF_Shuffle_debug(TSF_Io_argvs(["python","TSF_Shuffle.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE

