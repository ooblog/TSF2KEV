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
    TSF_Trans_generator_dlang(TSF_Forth_drawthe());
    return "";
}

void TSF_Trans_generator_python(string TSF_tsfpath,...){    //#TSFdoc:TSFデッキのPython化。(TSFAPI)
    string TSF_pyhonpath="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_pyhonpath=va_arg!(string)(_argptr);
    }
    string TSF_text="",TSF_card="";
    if( exists(TSF_tsfpath) ){
        if( TSF_Forth_loadtext(TSF_tsfpath,TSF_tsfpath).length ){
            TSF_Forth_merge(TSF_tsfpath,null,true);
        }
        TSF_text~="#! /usr/bin/env python\n";
        TSF_text~="# -*- coding: UTF-8 -*-\n";
        TSF_text~="from __future__ import division,print_function,absolute_import,unicode_literals\n\n";
        TSF_text~="from TSF_Io import *\n";
        foreach(string TSF_import;TSF_Forth_importlist()){
            TSF_text~=format("from %s import *\n",TSF_import);
            TSF_card~=format("%s_Initcards,",TSF_import);
        }
        TSF_text~="\nTSF_sysargvs=TSF_Io_argvs(sys.argv)\n";
        TSF_text~="TSF_Initcallrun=["~stripRight(TSF_card,',')~"]\n";
        TSF_text~="TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcallrun)\n\n";
        foreach(string TSF_the;TSF_Forth_stack().keys()){
            TSF_text=TSF_Trans_view_python(TSF_the,false,TSF_text);
        }
        TSF_text~="\nTSF_Forth_run()\n";
        if( TSF_pyhonpath.length ){
            TSF_Io_savetext(TSF_pyhonpath,TSF_text);
        }
        else{
            foreach(string TSF_textline;TSF_text.split('\n')){
                TSF_Io_printlog(TSF_textline);
            }
        }
    }
}

string TSF_Trans_view_python(string TSF_the,bool TSF_view_io, ...){    //#TSFdoc:スタックの内容をPython風テキスト表示。(TSFAPI)
    string TSF_view_log="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_view_log=va_arg!(string)(_argptr);
    }
    string[] TSF_cards;
    string TSF_style;
    if( TSF_the in TSF_Forth_stack() ){
        TSF_cards=TSF_Forth_stack()[TSF_the];
        foreach(size_t TSF_count,string TSF_card;TSF_cards){
            TSF_cards[TSF_count]=replace(replace(replace(replace(TSF_Io_ESCdecode(TSF_card),"\\","\\\\"),"\"","\\\""),"\t","\\t"),"\n","\\n");
        }
        TSF_style=TSF_Forth_style().get(TSF_the,"T");
        string TSF_view_logline="";
        switch( TSF_style ){
            case "O":  TSF_view_logline=format("TSF_Forth_setTSF(\"%s\",\"\\t\".join([\"%s\"]),\"O\")\n",TSF_the,join(TSF_cards,"\",\""));  break;
            case "T":  TSF_view_logline=format("TSF_Forth_setTSF(\"%s\",\"\\t\".join([\n    \"%s\"]),\"T\")\n",TSF_the,join(TSF_cards,"\",\""));  break;
            case "N":  default:  TSF_view_logline=format("TSF_Forth_setTSF(\"%s\",\"\\t\".join([\n    \"%s\"]),\"N\")\n",TSF_the,join(TSF_cards,"\",\n    \""));  break;
        }
        TSF_view_log=(TSF_view_io)?TSF_Io_printlog(TSF_view_logline,TSF_view_log):TSF_view_log~TSF_view_logline;
    }
    return TSF_view_log;
}

void TSF_Trans_generator_dlang(string TSF_tsfpath,...){    //#TSFdoc:TSFデッキのD言語化。(TSFAPI)
    string TSF_dlangpath="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_dlangpath=va_arg!(string)(_argptr);
    }
    string TSF_text="",TSF_card="";
    if( exists(TSF_tsfpath) ){
        if( TSF_Forth_loadtext(TSF_tsfpath,TSF_tsfpath).length ){
            TSF_Forth_merge(TSF_tsfpath,null,true);
        }
        TSF_text~="#! /usr/bin/env rdmd\n\n";
        TSF_text~="import std.string;\n\n";
        TSF_text~="import TSF_Io;\n";
        foreach(string TSF_import;TSF_Forth_importlist()){
            TSF_text~=format("import %s;\n",TSF_import);
            TSF_card~=format("&%s_Initcards,",TSF_import);
        }
        TSF_text~="\nvoid main(string[] sys_argvs){\n";
        TSF_text~="    string[] TSF_sysargvs=TSF_Io_argvs(sys_argvs);\n";
        TSF_text~="    void function(ref string function()[string],ref string[])[] TSF_Initcallrun=["~stripRight(TSF_card,',')~"];\n";
        TSF_text~="TSF_Forth_initTSF(TSF_sysargvs[1..$],TSF_Initcallrun);\n\n";
        foreach(string TSF_the;TSF_Forth_stack().keys()){
            TSF_text=TSF_Trans_view_dlang(TSF_the,false,TSF_text);
        }
        TSF_text~="\n    TSF_Forth_run();\n}\n";
        if( TSF_dlangpath.length ){
            TSF_Io_savetext(TSF_dlangpath,TSF_text);
        }
        else{
            foreach(string TSF_textline;TSF_text.split('\n')){
                TSF_Io_printlog(TSF_textline);
            }
        }
    }
}

string TSF_Trans_view_dlang(string TSF_the,bool TSF_view_io, ...){    //#TSFdoc:スタックの内容をD言語風テキスト表示。(TSFAPI)
    string TSF_view_log="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_view_log=va_arg!(string)(_argptr);
    }
    string[] TSF_cards;
    string TSF_style;
    if( TSF_the in TSF_stackD ){
        TSF_cards=TSF_Forth_stack()[TSF_the];
        foreach(size_t TSF_count,string TSF_card;TSF_cards){
            TSF_cards[TSF_count]=replace(replace(replace(replace(TSF_Io_ESCdecode(TSF_card),"\\","\\\\"),"\"","\\\""),"\t","\\t"),"\n","\\n");
        }
        TSF_style=TSF_Forth_style().get(TSF_the,"T");
//        writeln(format("TSF_the,TSF_style:%s %s",TSF_the,TSF_style));
        string TSF_view_logline="";
        switch( TSF_style ){
            case "O":  TSF_view_logline=format("    TSF_Forth_setTSF(\"%s\",join([\"%s\"],\"\\t\"),\"O\");\n",TSF_the,join(TSF_stackD[TSF_the],"\",\""));  break;
            case "T":  TSF_view_logline=format("    TSF_Forth_setTSF(\"%s\",join([\n        \"%s\"],\"\\t\"),\"T\");\n",TSF_the,join(TSF_stackD[TSF_the],"\",\""));  break;
            case "N":  default:  TSF_view_logline=format("    TSF_Forth_setTSF(\"%s\",join([\n        \"%s\"],\"\\t\"),\"N\");\n",TSF_the,join(TSF_stackD[TSF_the],"\",\n        \""));  break;
        }
        TSF_view_log=(TSF_view_io)?TSF_Io_printlog(TSF_view_logline,TSF_view_log):TSF_view_log~TSF_view_logline;
    }
    return TSF_view_log;
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
