#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.bigint;
import std.regex;

import TSF_Io;
import TSF_Forth;


void TSF_Calc_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Calc");
    string function()[string] TSF_Forth_cards=[
        "#TSF_calc":&TSF_Calc_calc, "#分数計算":&TSF_Calc_calc,
        "#TSF_calcJA":&TSF_Calc_calcJA, "#分数計算(日本語)":&TSF_Calc_calcJA,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Calc_calcsquarebrackets(string TSF_calcQ,string TSF_calcBL,string TSF_calcBR){    //#TSFdoc:スタックからpeek(読込)ショートカット角括弧で連結する。(TSFAPI)
    string TSF_calcA=TSF_calcQ,TSF_calcK="";
    foreach(string TSF_stacksK,string[] TSF_stacksV;TSF_Forth_stackD()){
        TSF_calcK=TSF_calcBL~TSF_stacksK;
        if( count(TSF_calcA,TSF_calcK) ){
            foreach(size_t TSF_stackC,string TSF_stackQ;TSF_stacksV){
                TSF_calcK=TSF_calcBL~TSF_stacksK~to!string(TSF_stackC)~TSF_calcBR;
                if( count(TSF_calcA,TSF_calcK) ){
                    TSF_calcA=replace(TSF_calcA,TSF_calcK,TSF_stackQ);
                }
            }
        }
    }
    return TSF_calcA;
}

string TSF_Calc_calc(){    //#TSFdoc:分数計算する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
//    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsQQ(TSF_Forth_drawthe()));
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsQQ(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")));
    return "";
}

string TSF_Calc_calcJA(){    //#TSFdoc:分数計算する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
//    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsJA(TSF_Forth_drawthe()));
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsJA(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")));
    return "";
}

string TSF_Calc_bracketsJA(string TSF_calcQ){    //#TSF_doc:分数電卓の日本語処理。(TSFAPI)
    string TSF_calcA=TSF_Calc_bracketsQQ(TSF_calcQ);
    return TSF_calcA;
}

string TSF_Calc_operator=",f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><";
string TSF_Calc_bracketsQQ(string TSF_calcQ){    //#TSF_doc:分数電卓のmain。括弧の内側を検索。(TSFAPI)
    string TSF_calcA="";  long TSF_calcbracketLR=0,TSF_calcbracketCAP=0;
    foreach(char TSF_calcbracketQ;TSF_calcQ){
        TSF_calcA~=count(TSF_Calc_operator,TSF_calcbracketQ)?to!string(TSF_calcbracketQ):"";
        if( TSF_calcbracketQ=='(' ){ TSF_calcbracketLR+=1; }
        if( TSF_calcbracketQ==')' ){ TSF_calcbracketLR-=1;
            if( TSF_calcbracketLR<TSF_calcbracketCAP ){ TSF_calcbracketCAP=TSF_calcbracketLR; }
        }
    }
    if( TSF_calcbracketLR>0 ){
        foreach(long i;0..abs(TSF_calcbracketLR)){ TSF_calcA=TSF_calcA~")"; }
    }
    if( TSF_calcbracketLR<0 ){
        foreach(long i;0..abs(TSF_calcbracketLR)){ TSF_calcA="("~TSF_calcA; }
    }
    if( TSF_calcbracketCAP>0 ){
        foreach(long i;0..TSF_calcbracketCAP){ TSF_calcA="("~TSF_calcA~")"; }
    }
    auto TSF_calc_bracketreg=regex("[(](?<=[(])[^()]*(?=[)])[)]");
    while( count(TSF_calcA,"(") ){
        foreach(TSF_calcK;match(TSF_calcA,TSF_calc_bracketreg)){
            TSF_calcA=replace(TSF_calcA,TSF_calcK.hit,TSF_Calc_function(TSF_calcK.hit));
        }
        TSF_calcA=replace(TSF_calcA,TSF_calcA,TSF_Calc_function(TSF_calcA));
    }
    TSF_calcA=replace(TSF_calcA,TSF_calcA,TSF_Calc_function(TSF_calcA));
    return TSF_calcA;
}

string TSF_Calc_function(string TSF_calcQ){    //#TSFdoc:分数電卓の和集合積集合およびゼロ比較演算子系。(TSFAPI)
    string TSF_calcA=TSF_calcQ;
//    TSF_calcA=TSF_Calc_addition(TSF_calcQ)
    if( count(TSF_calcQ,",") ){
         TSF_calcA=TSF_Io_RPN(TSF_calcQ);
    }
    else{
//        TSF_calcA=TSF_Calc_addition(TSF_calcQ)
    }
    return TSF_calcA;
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
void TSF_Calc_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Calc」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Calc.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}

unittest {
    TSF_Calc_debug(TSF_Io_argvs(["dmd","TSF_Calc.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE


