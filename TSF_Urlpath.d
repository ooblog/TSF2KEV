#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.bigint;
import std.regex;
import std.path;

import TSF_Io;
import TSF_Forth;


void TSF_Urlpath_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Urlpath");
    string function()[string] TSF_Forth_cards=[
        "#TSF_fileext":&TSF_Urlpath_fileext, "#ファイルの拡張子":&TSF_Urlpath_fileext,
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


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Urlpath_Initcards];
void TSF_Urlpath_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Urlpath」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Urlpath.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}

unittest {
//    TSF_Urlpath_debug(TSF_Io_argvs(["dmd","TSF_Urlpath.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE


