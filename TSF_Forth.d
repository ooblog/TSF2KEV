#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.array;
import std.typecons;
import core.vararg;
import std.algorithm;

import TSF_Io;


string TSF_Forth_1ststack(){    //TSFdoc:最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:";
}

string TSF_Forth_version(){    //TSFdoc:TSFバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945";
}

void TSF_Forth_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){
    string function()[string] TSF_Forth_cards=[
        "#TSF_fin.":&TSF_Forth_fin,
        "#TSF_this":&TSF_Forth_this,
        "#TSF_that":&TSF_Forth_that,
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

string TSF_fincode="0";
string TSF_Forth_fin(){    //#TSFdoc:TSF終了時のオプションを指定する。1枚[errmsg]ドロー。
    TSF_callptrD=null; TSF_callptrO=[];
    TSF_fincode=TSF_Forth_drawthe();
    return "#exit";
}

string TSF_Forth_this(){    //#TSF_doc:thisスタックの変更。1枚[this]ドロー。
    string TSF_card=TSF_Forth_drawthe();
    if( TSF_card.length==0 || ( TSF_card.length>0 && TSF_card.front=='#' ) ){ TSF_card="#exit"; }
    return TSF_card;
}

string TSF_Forth_that(){    //#TSF_doc:thatスタックの変更。1枚[that]ドロー。
    TSF_Forth_drawthat(TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_viewthe(){    //#TSFdoc:指定したスタックを表示する。1枚[the]ドロー。
    string TSF_debug_log=TSF_Forth_view(TSF_Forth_drawthe(),true);
    return "";
}

string TSF_Forth_viewthis(){    //#TSFdoc:実行中スタックを表示する。0枚ドロー。
    string TSF_debug_log=TSF_Forth_view(TSF_Forth_drawthis(),true);
    return "";
}

string TSF_Forth_viewthat(){    //#TSFdoc:積込先スタックを表示する。0枚ドロー。
    string TSF_debug_log=TSF_Forth_view(TSF_Forth_drawthat(),true);
    return "";
}

string TSF_Forth_viewthey(){    //#TSFdoc:スタック一覧を表示する。0枚ドロー。
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
long TSF_cardscount=0;
void TSF_Forth_initTSF(string[] TSF_argvs,void function(ref string function()[string],ref string[])[] TSF_addcalls){    //#TSFdoc:スタックやカードなどをまとめて初期化する(TSFAPI)。
//    TSF_stackD=null,TSF_styleD=null,TSF_callptrD=null,TSF_cardD=null;
    TSF_cardD=null;
    TSF_stackD=null;
    TSF_styleD=null;
    TSF_callptrD=null;
    TSF_cardO,TSF_stackO=[],TSF_styleO=[],TSF_callptrO=[];
    TSF_stackthis=TSF_Forth_1ststack(),TSF_stackthat=TSF_Forth_1ststack();
    TSF_cardscount=0;
//    TSF_Forth_setTSF(TSF_Forth_1ststack(),"0\t#TSF_fin.","T");
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"set(del)test\t#TSF_this\t0\t#TSF_fin.","T");
    TSF_Forth_setTSF("set(del)test","this:Peek\tthat:Poke\tthe:Pull\tthey:Push","T");
    void function(ref string function()[string],ref string[])[]  TSF_Initcards=[&TSF_Forth_Initcards];
    foreach(void function(ref string function()[string],ref string[]) TSF_Initcard;TSF_Initcards){
        TSF_Initcard(TSF_cardD,TSF_cardO);
    }
}

void TSF_Forth_setTSF(string TSF_the, ...){    //#TSFdoc:スタックやカードなどをまとめて初期化する(TSFAPI)。
    string TSF_text="",TSF_style="T";
    if( _arguments.length>0 ){
        if( _arguments[0]==typeid(string) ){
            TSF_text=va_arg!(string)(_argptr);
        }
        if( _arguments.length>1 && _arguments[1]==typeid(string) ){
            TSF_style=va_arg!(string)(_argptr);
        }
        if( TSF_the !in TSF_stackD ){
            TSF_stackO~=[TSF_the];  TSF_styleO~=[TSF_the];
        }
        TSF_stackD[TSF_the]=replace(stripRight(TSF_text),"\t","\n").split("\n");
        TSF_styleD[TSF_the]=TSF_style;
    }
    else{
        if( TSF_the !in TSF_stackD ){ TSF_stackD.remove(TSF_the); }
        if( TSF_the !in TSF_styleD ){ TSF_styleD.remove(TSF_the); }
        if( count(TSF_stackO,TSF_the) ){ TSF_stackO=remove!((TSF_stackO){return TSF_stackO==TSF_the;})(TSF_stackO); }
        if( count(TSF_styleO,TSF_the) ){ TSF_styleO=remove!((TSF_styleO){return TSF_styleO==TSF_the;})(TSF_styleO); }
    }
}

string TSF_Forth_run(){
    string TSF_cardnow=""; string TSF_stacknext="";
    while(true){
        while( TSF_cardscount<TSF_stackD[TSF_stackthis].length && TSF_cardscount<16 ){
            TSF_cardnow=TSF_stackD[TSF_stackthis][to!int(TSF_cardscount)];  TSF_cardscount++;
            if( TSF_cardnow !in TSF_cardD ){
                TSF_Forth_return(TSF_stackthat,TSF_cardnow);
            }
            else{
                TSF_stacknext=TSF_cardD[TSF_cardnow]();
                if( TSF_stacknext=="" ){
                    continue;
                }
                else if( TSF_stacknext !in TSF_stackD ){
                    break;
                }
                else{
                    while( count(TSF_callptrO,TSF_stacknext) ){
                        TSF_callptrD.remove(TSF_callptrO[$-1]); TSF_callptrO.length--;
                    }
                    TSF_callptrD[TSF_stackthis]=TSF_cardscount;  TSF_callptrO~=[TSF_stackthis];
                    TSF_stackthis=TSF_stacknext;
                    TSF_cardscount=0;
                }
            }
        }
        if( TSF_callptrO.length>0 ){
            TSF_stackthis=TSF_callptrO[$-1]; TSF_cardscount=TSF_callptrD[TSF_callptrO[$-1]];
            TSF_callptrD.remove(TSF_callptrO[$-1]); TSF_callptrO.length--;
        }
        else{
            break;
        }
    }
    return TSF_fincode;
}

string TSF_Forth_view(string TSF_the,bool TSF_view_io, ...){    //#TSFdoc:スタックの内容をテキスト表示(TSFAPI)。
    string TSF_view_log="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_view_log=va_arg!(string)(_argptr);
    }
    if( TSF_the in TSF_stackD ){
        string TSF_style=TSF_styleD.get(TSF_the,"T");
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

string TSF_Forth_draw(string TSF_the){    //#TSFdoc:スタックから1枚ドロー。(TSFAPI)
    string TSF_draw="";
    if( TSF_stackD[TSF_the].length>0 && TSF_the.length>0 && TSF_the in TSF_stackD ){
        TSF_draw=TSF_stackD[TSF_the][$-1];  TSF_stackD[TSF_the].length--;
    }
    return TSF_draw;
}

string TSF_Forth_drawthe(){    //#TSFdoc:theスタックの取得(thatから1枚ドロー)。(TSFAPI)
    return TSF_Forth_draw(TSF_stackthat);
}

string TSF_Forth_drawthis(...){    //#TSFdoc:thisスタックの取得(thatから0枚ドロー)。(TSFAPI)
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_stackthis=va_arg!(string)(_argptr);
    }
    return TSF_stackthis;
}

string TSF_Forth_drawthat(...){    //#TSFdoc:thatスタックの取得(thatから0枚ドロー)。(TSFAPI)
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_stackthat=va_arg!(string)(_argptr);
    }
    return TSF_stackthat;
}

void TSF_Forth_return(string TSF_the,string TSF_card){    //#TSFdoc:theスタックに1枚リターン。(TSFAPI)
    if( TSF_card.length>0 && TSF_card.front!='#' ){
        if( TSF_the !in TSF_stackD ){
            TSF_stackO~=[TSF_the];
        }
        TSF_stackD[TSF_the]~=[TSF_card];
    }
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
string TSF_Forth_debug(string[] TSF_argvs){    //#TSFdoc:「TSF_Forth」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_dForth.log";
    std.stdio.writeln(format("--- %s ---",__FILE__));
    TSF_Forth_initTSF(TSF_argvs,TSF_Initcalldebug);
    foreach(string TSF_the;TSF_stackO){
        TSF_debug_log=TSF_Forth_view(TSF_the,true,TSF_debug_log);
    }
//    std.stdio.writeln(format("TSF_Forth_drawthe:%s",TSF_Forth_drawthe()));
//    std.stdio.writeln(format("TSF_Forth_drawthis:%s",TSF_Forth_drawthis()));
//    std.stdio.writeln(format("TSF_Forth_drawthat:%s",TSF_Forth_drawthat()));
//    TSF_Forth_setTSF("set(del)test");
    std.stdio.writeln("--- run ---");
    TSF_Forth_run();
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
