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


void TSF_Shuffle_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに基本的な命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Shuffle");
    string function()[string] TSF_Forth_cards=[
        "#TSF_peekMthe":&TSF_Shuffle_peekMthe, "#指定スタック囲択読込":&TSF_Shuffle_peekMthe,
        "#TSF_peekMthis":&TSF_Shuffle_peekMthis, "#実行中スタック囲択読込":&TSF_Shuffle_peekMthis,
        "#TSF_peekMthat":&TSF_Shuffle_peekMthat, "#積込先スタック囲択読込":&TSF_Shuffle_peekMthat,
        "#TSF_peekMthey":&TSF_Shuffle_peekMthey, "#スタック一覧囲択読込":&TSF_Shuffle_peekMthey,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Shuffle_peekMthe(){    //#TSFdoc:指定スタックから囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    return "";
}

string TSF_Shuffle_peekMthis(){    //#TSFdoc:実行中スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    return "";
}

string TSF_Shuffle_peekMthat(){    //#TSFdoc:積込先スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    return "";
}

string TSF_Shuffle_peekMthey(){    //#TSFdoc:スタック一覧から最後尾スタック名を囲択で読込。1枚[peek]ドローして1枚[card]リターン。
    return "";
}



void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Shuffle_Initcards];
void TSF_Shuffle_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Shuffle」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Shuffle.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}


unittest {
//    TSF_Shuffle_debug(TSF_Io_argvs(["dmd","TSF_Shuffle.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE

