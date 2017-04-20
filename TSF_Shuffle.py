#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *


def TSF_Shuffle_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードにDやPythonに翻訳する命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Shuffle")
    TSF_Forth_cards={
#        "#TSF_peekCthe":TSF_Forth_peekCthe, "#指定スタック表面読込":TSF_Forth_peekCthe,
#        "#TSF_peekCthis":TSF_Forth_peekCthis, "#実行中スタック表面読込":TSF_Forth_peekCthis,
#        "#TSF_peekCthat":TSF_Forth_peekCthat, "#積込先スタック表面読込":TSF_Forth_peekCthat,
#        "#TSF_peekCthey":TSF_Forth_peekCthey, "#スタック一覧表面読込":TSF_Forth_peekCthey,
#        "#TSF_pokeCthe":TSF_Forth_pokeCthe, "#指定スタック表面上書":TSF_Forth_pokeCthe,
#        "#TSF_pokeCthis":TSF_Forth_pokeCthis, "#実行中スタック表面上書":TSF_Forth_pokeCthis,
#        "#TSF_pokeCthat":TSF_Forth_pokeCthat, "#積込先スタック表面上書":TSF_Forth_pokeCthat,
#        "#TSF_pokeCthey":TSF_Forth_pokeCthey, "#スタック一覧表面上書":TSF_Forth_pokeCthey,
#        "#TSF_pullCthe":TSF_Forth_pullCthe, "#指定スタック表面引抜":TSF_Forth_pullCthe,
#        "#TSF_pullCthis":TSF_Forth_pullCthis, "#実行中スタック表面引抜":TSF_Forth_pullCthis,
#        "#TSF_pullCthat":TSF_Forth_pullCthat, "#積込先スタック表面引抜":TSF_Forth_pullCthat,
#        "#TSF_pullCthey":TSF_Forth_pullCthey, "#スタック一覧表面引抜":TSF_Forth_pullCthey,
#        "#TSF_pushCthe":TSF_Forth_pushCthe, "#指定スタック差込":TSF_Forth_pushCthe,
#        "#TSF_pushCthis":TSF_Forth_pushCthis, "#実行中スタック差込":TSF_Forth_pushCthis,
#        "#TSF_pushCthat":TSF_Forth_pushCthat, "#積込先スタック差込":TSF_Forth_pushCthat,
#        "#TSF_pushCthey":TSF_Forth_pushCthey, "#スタック一覧差込":TSF_Forth_pushCthey,
        "#TSF_peekMthe":TSF_Shuffle_peekMthe, "#指定スタック囲択読込":TSF_Shuffle_peekMthe,
        "#TSF_peekMthis":TSF_Shuffle_peekMthis, "#実行中スタック囲択読込":TSF_Shuffle_peekMthis,
        "#TSF_peekMthat":TSF_Shuffle_peekMthat, "#積込先スタック囲択読込":TSF_Shuffle_peekMthat,
        "#TSF_peekMthey":TSF_Shuffle_peekMthey, "#スタック一覧囲択読込":TSF_Shuffle_peekMthey,
#        "#TSF_pokeMthe":TSF_Forth_pokeMthe, "#指定スタック表面上書":TSF_Forth_pokeMthe,
#        "#TSF_pokeMthis":TSF_Forth_pokeMthis, "#実行中スタック表面上書":TSF_Forth_pokeMthis,
#        "#TSF_pokeMthat":TSF_Forth_pokeMthat, "#積込先スタック表面上書":TSF_Forth_pokeMthat,
#        "#TSF_pokeMthey":TSF_Forth_pokeMthey, "#スタック一覧表面上書":TSF_Forth_pokeMthey,
#        "#TSF_pullMthe":TSF_Forth_pullMthe, "#指定スタック表面引抜":TSF_Forth_pullMthe,
#        "#TSF_pullMthis":TSF_Forth_pullMthis, "#実行中スタック表面引抜":TSF_Forth_pullMthis,
#        "#TSF_pullMthat":TSF_Forth_pullMthat, "#積込先スタック表面引抜":TSF_Forth_pullMthat,
#        "#TSF_pullMthey":TSF_Forth_pullMthey, "#スタック一覧表面引抜":TSF_Forth_pullMthey,
#        "#TSF_pushMthe":TSF_Forth_pushMthe, "#指定スタック差込":TSF_Forth_pushMthe,
#        "#TSF_pushMthis":TSF_Forth_pushMthis, "#実行中スタック差込":TSF_Forth_pushMthis,
#        "#TSF_pushMthat":TSF_Forth_pushMthat, "#積込先スタック差込":TSF_Forth_pushMthat,
#        "#TSF_pushMthey":TSF_Forth_pushMthey, "#スタック一覧差込":TSF_Forth_pushMthey,
#        "#TSF_peekLthe":TSF_Forth_peekLthe, "#指定スタックラベルで読込":TSF_Forth_peekLthe,
#        "#TSF_peekLthis":TSF_Forth_peekLthis, "#実行中スタックラベルで読込":TSF_Forth_peekLthis,
#        "#TSF_peekLthat":TSF_Forth_peekLthat, "#積込先スタックラベルで読込":TSF_Forth_peekLthat,
#        "#TSF_peekLthey":TSF_Forth_peekLthey, "#スタック一覧ラベルで読込":TSF_Forth_peekLthey,
#        "#TSF_pokeLthe":TSF_Forth_pokeLthe, "#指定スタックラベルで上書":TSF_Forth_pokeLthe,
#        "#TSF_pokeLthis":TSF_Forth_pokeLthis, "#実行中スタックラベルで上書":TSF_Forth_pokeLthis,
#        "#TSF_pokeLthat":TSF_Forth_pokeLthat, "#積込先スタックラベルで上書":TSF_Forth_pokeLthat,
#        "#TSF_pokeLthey":TSF_Forth_pokeLthey, "#スタック一覧ラベルで上書":TSF_Forth_pokeLthey,
#        "#TSF_pullLthe":TSF_Forth_pullLthe, "#指定スタックラベルで引抜":TSF_Forth_pullLthe,
#        "#TSF_pullLthis":TSF_Forth_pullLthis, "#実行中スタックラベルで引抜":TSF_Forth_pullLthis,
#        "#TSF_pullLthat":TSF_Forth_pullLthat, "#積込先スタックラベルで引抜":TSF_Forth_pullLthat,
#        "#TSF_pullLthey":TSF_Forth_pullLthey, "#スタック一覧ラベルで引抜":TSF_Forth_pullLthey,
#        "#TSF_pushLthe":TSF_Forth_pushLthe, "#指定スタックラベルで差込":TSF_Forth_pushLthe,
#        "#TSF_pushLthis":TSF_Forth_pushLthis, "#実行中スタックラベルで差込":TSF_Forth_pushLthis,
#        "#TSF_pushLthat":TSF_Forth_pushLthat, "#積込先スタックラベルで差込":TSF_Forth_pushLthat,
#        "#TSF_pushLthey":TSF_Forth_pushLthey, "#スタック一覧ラベルで差込":TSF_Forth_pushLthey,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO


def TSF_Shuffle_peekMthe():    #TSFdoc:指定スタックから囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    return ""

def TSF_Shuffle_peekMthis():    #TSFdoc:実行中スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    return ""

def TSF_Shuffle_peekMthat():    #TSFdoc:積込先スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    return ""

def TSF_Shuffle_peekMthey():    #TSFdoc:スタック一覧から最後尾スタック名を囲択で読込。1枚[peek]ドローして1枚[card]リターン。
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

