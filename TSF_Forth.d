#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.typecons;
import core.vararg;

import TSF_Io;


string TSF_Forth_1ststack(){    //TSF_doc:TSF_初期化に使う最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:";
}

string TSF_Forth_version(){    //TSF_doc:TSF_初期化に使うバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945";
}

void TSF_Forth_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){
    string function()[string] TSF_Forth_cards=[
        "#TSF_viewthe":&TSF_Forth_viewthe,
        "#TSF_viewthis":&TSF_Forth_viewthis,
        "#TSF_viewthat":&TSF_Forth_viewthat,
        "#TSF_viewthey":&TSF_Forth_viewthey,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Forth_viewthe(){    //#TSF_doc:[]積込先スタックを表示する。0スタック積み下ろし。
//    string TSF_debug_log=TSF_Forth_view(TSF_stackthe(),true);
    return "";
}

string TSF_Forth_viewthis(){    //#TSF_doc:[]積込先スタックを表示する。0スタック積み下ろし。
    string TSF_debug_log=TSF_Forth_view(TSF_stackthis,true);
    return "";
}

string TSF_Forth_viewthat(){    //#TSF_doc:[]積込先スタックを表示する。0スタック積み下ろし。
    string TSF_debug_log=TSF_Forth_view(TSF_stackthat,true);
    return "";
}

string TSF_Forth_viewthey(){    //#TSF_doc:[]スタック一覧を表示する。0スタック積み下ろし。
    string TSF_debug_log="";
    foreach(string TSF_the;TSF_stackO){
        TSF_debug_log=TSF_Forth_view(TSF_the,true,TSF_debug_log);
    }
    return "";
}


void function(ref string function()[string],ref string[])[] TSF_Initcards=[&TSF_Forth_Initcards];
string function()[string] TSF_cardD=null;
string[] [string] TSF_stackD=null;
string [string] TSF_styleD=null;
long[string] TSF_callptrD=null;
string[] TSF_cardO=[],TSF_stackO=[],TSF_styleO=[],TSF_callptrO=[];
string TSF_stackthis=TSF_Forth_1ststack(),TSF_stackthat=TSF_Forth_1ststack();
long TSF_stackcount=0;
void TSF_Forth_init(string[] TSF_argvs,void function(ref string function()[string],ref string[])[] TSF_addcalls){
//    TSF_stackD=null,TSF_styleD=null,TSF_callptrD=null,TSF_cardD=null;
    TSF_cardD=null;
    TSF_stackD=null;
    TSF_styleD=null;
    TSF_callptrD=null;
    TSF_cardO,TSF_stackO=[],TSF_styleO=[],TSF_callptrO=[];
    TSF_stackthis=TSF_Forth_1ststack(),TSF_stackthat=TSF_Forth_1ststack();
    TSF_stackD[TSF_stackthis]=["0","#TSF_fin."]; TSF_stackO~=[TSF_stackthis];
    void function(ref string function()[string],ref string[])[]  TSF_Initcards=[&TSF_Forth_Initcards];
    TSF_stackthis=TSF_Forth_1ststack(),TSF_stackthat=TSF_Forth_1ststack();
    TSF_stackcount=0;
    foreach(void function(ref string function()[string],ref string[]) TSF_Initcard;TSF_Initcards){
        TSF_Initcard(TSF_cardD,TSF_cardO);
    }
//    writef("TSF_callptrD:");  foreach(string function() cardD;TSF_callptrD){  writef("%p ",cardD);  }  writeln("");
//    writef("TSF_cardO:");  foreach(string cardO;TSF_cardO){  writef("%s ",cardO);  }  writeln("");
//    writef("TSF_cardD:%s\n",TSF_cardD["#(debug)TSF_version"]());
}

string TSF_Forth_view(string TSF_the,bool TSF_view_io, ...){
    string TSF_view_log="";
    if( _arguments.length>0 ){
        if( _arguments[0]==typeid(string) ){
            TSF_view_log=va_arg!(string)(_argptr);
        }
    }
    std.stdio.writeln(format("TSF_Forth_view:%s",TSF_the));
    if( TSF_the in TSF_stackD ){
        string TSF_style=(TSF_the in TSF_styleD)?TSF_styleD[TSF_the]:"T";
        string TSF_view_logline="";
        switch( TSF_style ){
            case "O":  TSF_view_logline=format("%s\t%s\n",TSF_the,join(TSF_stackD[TSF_the],"\t"));  break;
            case "T":  TSF_view_logline=format("%s\n\t%s\n",TSF_the,join(TSF_stackD[TSF_the],"\t"));  break;
            case "N": default:  TSF_view_logline=format("%s\n\t%s\n",TSF_the,join(TSF_stackD[TSF_the],"\n\t"));  break;
        }
        TSF_view_log=(TSF_view_io)?TSF_Io_printlog(TSF_view_logline,TSF_view_log):TSF_view_log~TSF_view_logline;
    }
    return TSF_view_log;
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
string TSF_Forth_debug(string[] TSF_argvs){
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_dForth.log";
    std.stdio.writeln(format("--- %s ---",__MODULE__));
    TSF_Forth_init(TSF_argvs,TSF_Initcalldebug);
    foreach(string TSF_the;TSF_stackO){
        TSF_debug_log=TSF_Forth_view(TSF_the,true,TSF_debug_log);
    }
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
