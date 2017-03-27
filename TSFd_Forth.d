#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.typecons;

import TSFd_Io;


string TSF_Forth_1ststack(){    //TSF_doc:TSF_初期化に使う最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:";
}

string TSF_Forth_version(){    //TSF_doc:TSF_初期化に使うバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945";
}

void TSF_Forth_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){
    string function()[string] TSF_Forth_cards=["#(debug)TSF_version":&TSF_Forth_version ];
    TSF_cardsD["#(debug)TSF_version"]=TSF_Forth_cards["#(debug)TSF_version"];
//    TSF_cardsO[0]="#test";
//    TSF_cardsD["#test"]=&TSF_Forth_version;
}

void function(ref string function()[string],ref string[])[]  TSF_Initcalls=[&TSF_Forth_Initcards];
string[] TSF_stackD=[],TSF_styleD=[],TSF_callptrD=[],TSF_cardD=[];
string[] TSF_stackO=[],TSF_styleO=[],TSF_callptrO=[],TSF_cardO=[];
string TSF_stackthis=TSF_Forth_1ststack(),TSF_stackthat=TSF_Forth_1ststack();
long TSF_stackcount=0;
void TSF_Forth_init(string[] TSF_argvs,void function(ref string function()[string],ref string[])[] TSF_addcalls){
    TSF_stackD=[],TSF_styleD=[],TSF_callptrD=[],TSF_cardD=[];
    TSF_stackO=[],TSF_styleO=[],TSF_callptrO=[],TSF_cardO=[];
    TSF_stackthis=TSF_Forth_1ststack(),TSF_stackthat=TSF_Forth_1ststack();
    TSF_stackcount=0;
    TSF_Initcalls=[&TSF_Forth_Initcards]~TSF_addcalls;
}


string function()[] TSF_Initcalldebug=[&TSF_Forth_version,&TSF_Forth_1ststack];
string TSF_Forth_debug(string[] TSF_argvs){
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_dForth.log";
    writeln(TSF_Initcalldebug[0]());
    std.stdio.writeln(format("--- %s ---",__MODULE__));
    std.stdio.writeln(format("--- fin. > %s ---",TSF_debug_savefilename));
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);
    return TSF_debug_log;
}


unittest {
    TSF_Forth_debug(TSF_Io_argvs(["TSFd_Forth.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
