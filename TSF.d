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


void TSF_sample_help(){
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        join(["help:","#TSF_argvsthe","#TSF_reverseN","help:","#TSF_lenthe","#TSF_echoN","#TSF_fin."],"\t"),"T");
    TSF_Forth_setTSF("help:",
        join([
        "usage: ./TSF.py [command|file.tsf] [argv] ...",
        "commands:",
        "  --help        this commands view",
        "  --helloworld  \"Hello world  #TSF_echo\" sample",
//        "  --RPN         decimal calculator \"1/3-m1|2\"-> 0.8333... sample",
        ],"\t"),"N");
    TSF_sample_run("TSF_sample_help");
}

void TSF_sample_run(...){
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        string TSF_sample_sepalete=va_arg!(string)(_argptr);
        TSF_Io_printlog(format("-- %s source --",TSF_sample_sepalete));
//        TSF_Forth_viewthey();
        TSF_Io_printlog(format("-- %s run --",TSF_sample_sepalete));
    }
    TSF_Forth_run();
}

void TSF_sample_Helloworld(){
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        join(["Hello world","#TSF_echo"],"\t"),"T");
    TSF_sample_run("TSF_sample_Helloworld");
}


void main(string[] sys_argvs){
    string[] TSF_sysargvs=TSF_Io_argvs(sys_argvs);
    string TSF_bootcommand=TSF_sysargvs.length<2?"":TSF_sysargvs[1];
    TSF_Forth_initTSF(TSF_sysargvs[1..$],null);
    if( exists(TSF_bootcommand) && TSF_Forth_loadtext(TSF_bootcommand,TSF_bootcommand).length>0 ){
        TSF_Forth_merge(TSF_bootcommand,null,true);
//        TSF_Forth_viewthey();
        TSF_sample_run();
    }
    else if( count(["--help","--commands"],TSF_bootcommand) ){
        TSF_sample_help();
    }
    else if( count(["--hello","--helloworld","--Helloworld"],TSF_bootcommand) ){
        TSF_sample_Helloworld();
    }
    else if( count(["--RPN","--rpn"],TSF_bootcommand) ){
        TSF_sample_help();
    }
    else{
        TSF_sample_help();
    }
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
