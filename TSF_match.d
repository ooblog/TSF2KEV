#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.regex;


import TSF_Io;
import TSF_Forth;


void TSF_Match_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Match");
    string function()[string] TSF_Forth_cards=[
        "#TSF_replace":&TSF_match_replace, "#文字列を置換":&TSF_match_replace,
        "#TSF_resub":&TSF_match_resub, "#文字列を正規表現で置換":&TSF_match_resub,
        "#TSF_replacesN":&TSF_match_replacesN, "#文字列群で置換":&TSF_match_replacesN,
//        "#TSF_replacesC":&TSF_match_replacesN, "#文字列群で周択置換":&TSF_match_replacesN,
//        "#TSF_replacesM":&TSF_match_replacesN, "#文字列群で囲択置換":&TSF_match_replacesN,
//        "#TSF_replacesV":&TSF_match_replacesN, "#文字列群で逆択置換":&TSF_match_replacesN,
//        "#TSF_replacesA":&TSF_match_replacesN, "#文字列群で乱択置換":&TSF_match_replacesN,
//        "#TSF_replacesstacks":&TSF_match_resubN, "#正規表現群で置換":&TSF_match_resubN,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_match_replace(){    //#TSFdoc:文字列を置換。3枚[cardT,cardO,cardN]ドローして1枚[cardT]リターン。
    string TSF_theN=TSF_Forth_drawthe();
    string TSF_theO=TSF_Forth_drawthe();
    string TSF_theT=TSF_Forth_drawthe();
    TSF_theT=TSF_theT.replace(TSF_theO,TSF_theN);
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_theT);
    return "";
}

string TSF_match_resub(){    //#TSFdoc:文字列を正規表現で置換。3枚[cardT,cardO,cardN]ドローして1枚[cardT]リターン。
    string TSF_theN=TSF_Forth_drawthe();
    string TSF_theO=TSF_Forth_drawthe();
    string TSF_theT=TSF_Forth_drawthe();
    TSF_theT=TSF_theT.replace(TSF_theO,TSF_theN);
    TSF_theT=replaceAll(TSF_theT,regex(TSF_theO),TSF_theN);
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_theT);
    return "";
}

string TSF_match_replacesN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    string TSF_theN=TSF_Forth_drawthe();  string[] TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  size_t TSF_cardsN_len=TSF_cardsN.length;
    string TSF_theO=TSF_Forth_drawthe();  string[] TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    string TSF_theT=TSF_Forth_drawthe();
    string TSF_text="";
    if( TSF_theT in TSF_Forth_stackD() ){
        TSF_text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));
        foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){
            if( TSF_peek<TSF_cardsN_len ){
                TSF_text=replace(TSF_text,TSF_card,TSF_cardsN[TSF_peek]);
            }
        }
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N");
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
