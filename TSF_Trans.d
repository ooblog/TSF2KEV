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


void TSF_Trans_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSF_doc:関数カードに基本的な命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Trans");
    string function()[string] TSF_Forth_cards=[
        "#TSF_Python":&TSF_Trans_python, "#デッキのpython化":&TSF_Trans_python,
        "#TSF_D-lang":&TSF_Trans_dlang, "#デッキのD言語化":&TSF_Trans_dlang,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Trans_python(){    //#TSFdoc:TSFデッキのPython化。1枚[path]ドロー。
    TSF_Trans_generator_python(TSF_Forth_drawthe());
    return "";
}

string TSF_Trans_dlang(){    //#TSFdoc:TSFデッキのD言語化。1枚[path]ドロー。
//    TSF_Trans_generator_dlang(TSF_Forth_drawthe())
    return "";
}

void TSF_Trans_generator_python(string TSF_tsfpath,...){    //#TSFdoc:TSFデッキのPython化。(TSFAPI)
    string TSF_pyhonpath="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_pyhonpath=va_arg!(string)(_argptr);
    }
    writeln(format("TSF_Forth_importlist %s",TSF_Forth_importlist()));
    string TSF_text="",TSF_card="";
    if( exists(TSF_tsfpath) ){
        if( TSF_Forth_loadtext(TSF_tsfpath,TSF_tsfpath).length ){
            TSF_Forth_merge(TSF_tsfpath,null,true);
        }
        TSF_text~="#! /usr/bin/env rdmd\n";
        TSF_text~="\n";
        TSF_text~="import TSF_Io;\n";
        foreach(string TSF_import;TSF_Forth_importlist()){
            TSF_text~=format("import %s;\n",TSF_import);
            TSF_card~=format("&%s_Initcards,",TSF_import);
        }
        TSF_text~="\nvoid main(string[] sys_argvs){\n";
        TSF_text~="    string[] TSF_sysargvs=TSF_Io_argvs(sys_argvs);\n";
        TSF_text~="    void function(ref string function()[string],ref string[])[] TSF_Initcallrun=["~stripRight(TSF_card,',')~"];\n";
        if( TSF_pyhonpath.length ){
//            TSF_io_savetext(TSF_pyhonpath,TSF_text)
        }
        else{
            foreach(string TSF_textline;TSF_text.split('\n')){
                TSF_Io_printlog(TSF_textline);
            }
        }
    }
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
string TSF_Trans_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Trans」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Trans.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
    return TSF_debug_log;
}

unittest {
    TSF_Trans_debug(TSF_Io_argvs(["dmd","TSF_Trans.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
