#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.bigint;
import std.regex;
import std.path;
import std.file;

import TSF_Io;
import TSF_Forth;


void TSF_Urlpath_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Urlpath");
    string function()[string] TSF_Forth_cards=[
        "#TSF_fileext":&TSF_Urlpath_fileext, "#ファイルの拡張子":&TSF_Urlpath_fileext,
        "#TSF_abspath":&TSF_Urlpath_abspath, "#ファイルの絶対パス":&TSF_Urlpath_abspath,
        "#TSF_dirpath":&TSF_Urlpath_dirpath, "#ファイルのディレクトリ":&TSF_Urlpath_dirpath,
        "#TSF_chpath":&TSF_Urlpath_chpath, "#ディレクトリ移動":&TSF_Urlpath_chpath,
        "#TSF_basepath":&TSF_Urlpath_basepath, "#ファイルのディレクトリに移動":&TSF_Urlpath_basepath,
        "#TSF_existfile":&TSF_Urlpath_existfile, "#ファイル名の有無":&TSF_Urlpath_existfile,
        "#TSF_existdir":&TSF_Urlpath_existdir, "#ディレクトリ名の有無":&TSF_Urlpath_existdir,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Urlpath_fileext(){    //#TSFdoc:現在日時の取得。1枚[daytimeformat]ドローして1枚[daytime]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_fileext_api(TSF_Forth_drawthe()));
    return "";
}


string TSF_Urlpath_fileext_api(string TSF_filepath){    //#TSFdoc:ファイルの拡張子を取得。(TSFAPI)
//    writeln(format("TSF_Urlpath_fileext_api %s %s",TSF_filepath,extension(TSF_filepath)));
    return extension(TSF_filepath);
}

string TSF_Urlpath_abspath(){    //#TSFdoc:ファイルの絶対パスを取得する。1枚[path]ドローして1枚[abspath]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_abspath_api(TSF_Forth_drawthe()));
    return "";
}

string TSF_Urlpath_abspath_api(string TSF_filepath){    //#TSFdoc:ファイルの絶対パスを取得。(TSFAPI)
    return exists(TSF_filepath)?absolutePath(TSF_filepath):"";
}

string TSF_Urlpath_dirpath(){    //#TSFdoc:ディレクトリパスを取得する。1枚[path]ドローして1枚[dirpath]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_dirpath_api(TSF_Forth_drawthe()));
    return "";
}

string TSF_Urlpath_dirpath_api(string TSF_filepath){    //#TSFdoc:ディレクトリパスを取得。(TSFAPI)
    return exists(TSF_filepath)?dirName(TSF_filepath):"";
}

string TSF_Urlpath_chpath(){    //#TSFdoc:ディレクトリに移動する。1枚[path]ドロー。
    TSF_Urlpath_chpath_api(TSF_Forth_drawthe());
    return "";
}

void TSF_Urlpath_chpath_api(string TSF_dirpath){    //#TSFdoc:ディレクトリに移動。(TSFAPI)
    if( exists(TSF_dirpath) && isDir(TSF_dirpath) ){ chdir(TSF_dirpath); }
}

string TSF_Urlpath_basepath(){    //#TSFdoc:ファイルのあるディレクトリに移動する。1枚[path]ドロー。
    TSF_Urlpath_basepath_api(TSF_Forth_drawthe());
    return "";
}

void TSF_Urlpath_basepath_api(string TSF_filepath){    //#TSFdoc:ファイルのあるディレクトリパスを取得。(TSFAPI)
    if( exists(TSF_filepath) && isFile(TSF_filepath) ){ chdir(dirName(absolutePath(TSF_filepath))); }
}

string TSF_Urlpath_existfile(){    //#TSFdoc:ファイルの有無を確認する。1枚[path]ドローして1枚[0or1]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_existfile_api(TSF_Forth_drawthe()));
    return "";
}

string TSF_Urlpath_existfile_api(string TSF_filepath){    //#TSFdoc:ファイルの有無を確認。(TSFAPI)
    return ( exists(TSF_filepath) && isFile(TSF_filepath) )?"1":"0";
}

string TSF_Urlpath_existdir(){    //#TSFdoc:フォルダの有無を確認する。1枚[path]ドローして1枚[0or1]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Urlpath_existdir_api(TSF_Forth_drawthe()));
    return "";
}

string TSF_Urlpath_existdir_api(string TSF_dirpath){    //#TSFdoc:フォルダの有無を確認。(TSFAPI)
    return ( exists(TSF_dirpath) && isFile(TSF_dirpath) )?"1":"0";
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Urlpath_Initcards];
void TSF_Urlpath_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Urlpath」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Urlpath.log";
    TSF_debug_log=TSF_Io_printlog("--- %s ---".format(__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}

unittest {
//    TSF_Urlpath_debug(TSF_Io_argvs(["dmd","TSF_Urlpath.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE


