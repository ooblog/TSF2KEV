#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;

import TSFd_Io;


string TSF_Forth_1ststack(){    //TSF_doc:TSF_初期化に使う最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:";
}

string TSF_Forth_version(){    //TSF_doc:TSF_初期化に使うバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945";
}

string function()[] TSF_Forth_Initcards(string function()[] TSF_cardsobj){
//    auto TSF_cards=TSF_cardsobj;
//    TSF_cards["TSF_Forth_version"]=TSF_Forth_version;
    return TSF_cardsobj;
}

string function()[] function(string function()[])[] TSF_Initcalls=[&TSF_Forth_Initcards];
void TSF_Forth_init(string[] TSF_argvs,string delegate()[] TSF_addcalls){
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
