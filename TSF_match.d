#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;


import TSF_Io;
import TSF_Forth;


void TSF_Match_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSF_doc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Match");
    string function()[string] TSF_Forth_cards=[
        "#TSF_replaceN":&TSF_match_replacesN, "#文字列群で置換":&TSF_match_replacesN,
//        "#TSF_replaceC":&TSF_match_replacesN, "#文字列群で周択置換":&TSF_match_replacesN,
//        "#TSF_replaceM":&TSF_match_replacesN, "#文字列群で囲択置換":&TSF_match_replacesN,
//        "#TSF_replaceV":&TSF_match_replacesN, "#文字列群で逆択置換":&TSF_match_replacesN,
//        "#TSF_replaceA":&TSF_match_replacesN, "#文字列群で乱択置換":&TSF_match_replacesN,
//        "#TSF_replacestacks":&TSF_match_resubN, "#正規表現群で置換":&TSF_match_resubN,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_match_replacesN(){    //#TSF_doc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。3枚[stackT,stackO,stackN]ドロー。
    string TSF_theN=TSF_Forth_drawthe();  string[] TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  size_t TSF_cardsN_len=TSF_cardsN.length;
    string TSF_theO=TSF_Forth_drawthe();  string[] TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    string TSF_theS=TSF_Forth_drawthe();
    string TSF_text="";
    if( TSF_theS in TSF_Forth_stackD() ){
        TSF_text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theS],"\n"));
        foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){
            if( TSF_peek<TSF_cardsN_len ){
                TSF_text=replace(TSF_text,TSF_card,TSF_cardsN[TSF_peek]);
            }
        }
        TSF_Forth_setTSF(TSF_theS,TSF_text,"N");
    }
    return "";
}



void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
void TSF_Match_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Match」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Match.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}

unittest {
    TSF_Match_debug(TSF_Io_argvs(["dmd","TSF_Match.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
