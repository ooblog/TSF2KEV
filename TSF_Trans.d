#! /usr/bin/env rdmd

import std.stdio;
import std.file;
import std.path;
import std.array;
import std.algorithm;
import core.vararg;
import std.typecons;
import std.string;

import TSF_Io;
import TSF_Forth;


void TSF_Forth_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSF_doc:関数カードに基本的な命令を追加する。(TSFAPI)
    string function()[string] TSF_Forth_cards=[
        "#TSF_Python":&TSF_Trans_python, "#デッキのpython化":&TSF_Trans_python,
        "#TSF_D-lang":&TSF_Trans_dlang, "#デッキのD言語化":&TSF_Trans_dlang,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Trans_python(){    //#TSFdoc:TSFデッキのPython化。1枚[path]ドロー。
    return "";
}

string TSF_Trans_dlang(){    //#TSFdoc:TSFデッキのD言語化。1枚[path]ドロー。
    return "";
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
string TSF_Trans_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Trans」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Trans.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
    return TSF_debug_log;
}

unittest {
    TSF_Trans_debug(TSF_Io_argvs(["dmd","TSF_Trans.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
