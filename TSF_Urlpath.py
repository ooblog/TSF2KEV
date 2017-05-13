#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *


def TSF_Urlpath_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Urlpath")
    TSF_Forth_cards={
        "#TSF_fileext":TSF_Urlpath_fileext, "#ファイルの拡張子":TSF_Urlpath_fileext,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

#TSF_doc:[filepath]ファイルの拡張子を取得する。1スタック積み下ろし、1スタック積み上げ。
def TSF_Urlpath_fileext():    #TSFdoc:ファイルの拡張子を取得する。1枚[path]ドローして1枚[.ext]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_fileext_api(TSF_Forth_drawthe()));
    return ""

def TSF_Urlpath_fileext_api(TSF_filepath):    #TSFdoc:ファイルの拡張子を取得。(TSFAPI)
    return os.path.splitext(TSF_filepath)[1]


TSF_Initcalldebug=[TSF_Urlpath_Initcards]
def TSF_Urlpath_debug(TSF_sysargvs):    #TSFdoc:「TSF_Urlpath」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Urlpath.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)

if __name__=="__main__":
    TSF_Urlpath_debug(TSF_Io_argvs(["python","TSF_Urlpath.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
