#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *


def TSF_Urlpath_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Urlpath")
    TSF_Forth_cards={
        "#TSF_fileext":TSF_Urlpath_fileext, "#ファイルの拡張子":TSF_Urlpath_fileext,
        "#TSF_abspath":TSF_Urlpath_abspath, "#ファイルの絶対パス":TSF_Urlpath_abspath,
        "#TSF_dirpath":TSF_Urlpath_dirpath, "#ファイルのディレクトリ":TSF_Urlpath_dirpath,
        "#TSF_chpath":TSF_Urlpath_chpath, "#ディレクトリ移動":TSF_Urlpath_chpath,
        "#TSF_basepath":TSF_Urlpath_basepath, "#ファイルのディレクトリに移動":TSF_Urlpath_basepath,
        "#TSF_existfile":TSF_Urlpath_existfile, "#ファイル名の有無":TSF_Urlpath_existfile,
        "#TSF_existdir":TSF_Urlpath_existdir, "#ディレクトリ名の有無":TSF_Urlpath_existdir,
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

def TSF_Urlpath_abspath():    #TSFdoc:ファイルの絶対パスを取得する。1枚[path]ドローして1枚[abspath]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_abspath_api(TSF_Forth_drawthe()));
    return ""

def TSF_Urlpath_abspath_api(TSF_filepath):    #TSFdoc:ファイルの絶対パスを取得。(TSFAPI)
    return os.path.abspath(TSF_filepath) if( os.path.isfile(TSF_filepath) ) else ""

def TSF_Urlpath_dirpath():    #TSFdoc:ディレクトリパスを取得する。1枚[path]ドローして1枚[dirpath]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_dirpath_api(TSF_Forth_drawthe()));
    return ""

def TSF_Urlpath_dirpath_api(TSF_filepath):    #TSFdoc:ディレクトリパスを取得。(TSFAPI)
    return os.path.dirname(TSF_filepath) if( os.path.isfile(TSF_filepath) ) else ""

def TSF_Urlpath_chpath():    #TSFdoc:ディレクトリに移動する。1枚[path]ドロー。
    TSF_Urlpath_chpath_api(TSF_Forth_drawthe());
    return ""

def TSF_Urlpath_chpath_api(TSF_dirpath):    #TSFdoc:ディレクトリパスに移動。(TSFAPI)
    if( os.path.isdir(TSF_dirpath) ): os.chdir(TSF_dirpath);

def TSF_Urlpath_basepath():    #TSFdoc:ファイルのあるディレクトリに移動する。1枚[path]ドロー。
    TSF_Urlpath_basepath_api(TSF_Forth_drawthe());
    return ""

def TSF_Urlpath_basepath_api(TSF_filepath):    #TSFdoc:ファイルのあるディレクトリパスを取得。(TSFAPI)
    if( os.path.isfile(TSF_filepath) ): os.chdir(os.path.dirname(os.path.abspath(TSF_filepath)));

def TSF_Urlpath_existfile():    #TSFdoc:ファイルの有無を確認する。1枚[path]ドローして1枚[0or1]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_existfile_api(TSF_Forth_drawthe()));
    return ""

def TSF_Urlpath_existfile_api(TSF_filepath):    #TSFdoc:ファイルの有無を確認。(TSFAPI)
    return "1" if( os.path.isfile(TSF_filepath) ) else "0"

def TSF_Urlpath_existdir():    #TSFdoc:フォルダの有無を確認する。1枚[path]ドローして1枚[0or1]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_existdir_api(TSF_Forth_drawthe()));
    return ""

def TSF_Urlpath_existdir_api(TSF_dirpath):    #TSFdoc:フォルダの有無を確認。(TSFAPI)
    return "1" if( os.path.isdir(TSF_dirpath) ) else "0"


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
