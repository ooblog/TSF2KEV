#! /usr/bin/env rdmd
//import TSFd_Io;
import std.stdio;
import std.string;

string TSF_Forth_1ststack(){    //TSF_doc:TSF_初期化に使う最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:";
}

string TSF_Forth_version(){    //TSF_doc:TSF_初期化に使うバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945";
}


string TSF_Io_debug(string[] TSF_argvs){
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_dForth.log";
    std.stdio.writeln(format("--- %s ---",__MODULE__));
    std.stdio.writeln(format("--- fin. > %s ---",TSF_debug_savefilename));
//    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);
    return TSF_debug_log;
}

//void main(string[] TSF_argvobj){
//    TSF_Io_debug(TSF_Io_argvs(TSF_argvobj));
//mixin(`writeln("Hello, World!");`);
//}
static if(1){
    mixin(`void main(){writeln("Hello, World!");}`);
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
