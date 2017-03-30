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


void TSF_sample_Helloworld(){
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",
        join(["Hello world","#TSF_echo"],"\t"),"T");
    TSF_sample_run("TSF_sample_Helloworld");
}

void TSF_sample_run(...){
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        string TSF_sample_sepalete=va_arg!(string)(_argptr);
        TSF_Io_printlog(format("-- %s source --",TSF_sample_sepalete));
        TSF_Forth_viewthey();
        TSF_Io_printlog(format("-- %s run --",TSF_sample_sepalete));
    }
    TSF_Forth_run();
}


void main(string[] sys_argvs){
    string[] TSF_argvs=TSF_Io_argvs(sys_argvs);
    string TSF_bootcommand=TSF_argvs.length<2?"":TSF_argvs[1];
    TSF_Forth_initTSF(TSF_argvs,null);
    if( exists(TSF_bootcommand) ){
    }
    else if( count(["--hello","--helloworld","--Helloworld"],TSF_bootcommand) ){
        TSF_sample_Helloworld();
    }
    else{  // if( count(["--help" )
        TSF_sample_Helloworld();
    }
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
