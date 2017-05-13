#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.bigint;
import std.regex;

import TSF_Io;
import TSF_Forth;


void TSF_Time_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Time");
    string function()[string] TSF_Forth_cards=[
        "#TSF_calender":&TSF_Time_calender, "#日時等に置換":&TSF_Time_calender,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Time_calender(){    //#TSFdoc:現在日時の取得。1枚[daytimeformat]ドローして1枚[daytime]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Time_getdaytime(TSF_Forth_drawthe()));
    return "";
}


string TSF_Time_getdaytime(string TSF_daytimeformat){    //#TSFdoc:現在日時で上書き。(TSFAPI)
    return TSF_daytimeformat;
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Time_Initcards];
void TSF_Time_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Time」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Time.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}

unittest {
//    TSF_Time_debug(TSF_Io_argvs(["dmd","TSF_Time.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE


