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
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsQQ(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")));
    return "";
}

string TSF_Calc_calcJA(){    //#TSFdoc:分数計算する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsJA(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")));
    return "";
}

string TSF_Calc_bracketsJA(string TSF_calcQ){    //#TSF_doc:分数電卓の日本語処理。(TSFAPI)
    string TSF_calcA=TSF_Calc_bracketsQQ(TSF_calcQ);
    return TSF_calcA;
}

//string TSF_Calc_operator=",f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><";
string TSF_Calc_bracketsQQ(string TSF_calcQ){    //#TSF_doc:分数電卓のmain。括弧の内側を検索。(TSFAPI)
    string TSF_calcA=TSF_calcQ;  long TSF_calcBLR=0,TSF_calcBCAP=0;
    auto TSF_calc_bracketreg=regex("[(](?<=[(])[^()]*(?=[)])[)]");
    while( count(TSF_calcA,"(") || count(TSF_calcA,")") ){
        TSF_calcBLR=0; TSF_calcBCAP=0;
        foreach(char TSF_calcB;TSF_calcQ){
//            TSF_calcA~=count(TSF_Calc_operator,TSF_calcB)?to!string(TSF_calcB):"";
            if( TSF_calcB=='(' ){ TSF_calcBLR+=1; }
            if( TSF_calcB==')' ){ TSF_calcBLR-=1;
                if( TSF_calcBLR<TSF_calcBCAP ){ TSF_calcBCAP=TSF_calcBLR; }
            }
        }
        if( TSF_calcBLR>0 ){
            foreach(long i;0..abs(TSF_calcBLR)){ TSF_calcA=TSF_calcA~")"; }
        }
        if( TSF_calcBLR<0 ){
            foreach(long i;0..abs(TSF_calcBLR)){ TSF_calcA="("~TSF_calcA; }
        }
        if( TSF_calcBCAP>0 ){
            foreach(long i;0..TSF_calcBCAP){ TSF_calcA="("~TSF_calcA~")"; }
        }
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
    if( count(TSF_calcQ,",") ){
         TSF_calcA=TSF_Io_RPN(TSF_calcQ);
    }
    else{
        TSF_calcA=TSF_Calc_addition(TSF_calcQ);
    }
    return TSF_calcA;
}

string TSF_Calc_addition(string TSF_calcQ){    //#TSF_doc:分数電卓の足し算引き算・消費税計算等。(TSFAPI)
    string TSF_calcA=TSF_calcQ;
    TSF_calcA=TSF_Calc_multiplication(TSF_calcQ);
    return TSF_calcA;
}

string TSF_Calc_multiplication(string TSF_calcQ){    //#TSF_doc:分数電卓の掛け算割り算等。公倍数公約数、最大値最小値も扱う。(TSFAPI)
    string TSF_calcA=TSF_calcQ;
    TSF_calcA=TSF_Calc_fractalize(TSF_calcQ);
    return TSF_calcA;
}

string TSF_Calc_fractalize(string TSF_calcQ){    //#TSF_doc:分数電卓なので小数を分数に。ついでに平方根や三角関数も。0で割る、もしくは桁が限界越えたときなどは「n|0」を返す。(TSFAPI)
    string TSF_calcA=TSF_calcQ;
    return TSF_calcA;
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Calc_Initcards];
void TSF_Calc_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Calc」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Calc.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "calccount:","#TSF_this","#TSF_fin."],"\t"),"T");
    TSF_Forth_setTSF("calccount:",join([
        "calcjump:","calcsample:","#TSF_lenthe","0,1,[0]U","#TSF_join[]","#TSF_RPN","#TSF_peekNthe","#TSF_this","calccount:","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("calcjump:",join([
        "#exit","calcpop:"],"\t"),"T");
    TSF_Forth_setTSF("calcpop:",join([
        "calcsample:","0","#TSF_pullNthe","#TSF_peekFthat","#TSF_calc","「[1]」→「[0]」","#TSF_join[]","#TSF_echo"],"\t"),"T");
    TSF_Forth_setTSF("calcpeekdata:",join([
        "009","108","207","306","405","504","603","702","801","900"],"\t"),"T");
    TSF_Forth_setTSF("calcsample:",join([
        "2,3+", "2,3-", "2,3*", "2,3/", "(2,3-),5+",
        "[calcpeekdata:8]",
        "4|6"],"\t"),"N");
    TSF_debug_log=TSF_Forth_samplerun(__FILE__,true,TSF_debug_log);
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);
}

unittest {
    TSF_Calc_debug(TSF_Io_argvs(["dmd","TSF_Calc.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE


