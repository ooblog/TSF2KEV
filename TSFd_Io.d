#! /usr/bin/env rdmd

import std.stdio;
import core.stdc.stdio;
import std.string;
import std.conv;
import std.windows.charset;
import std.array;
import std.file;
import core.vararg;

void main(){
//    writeln("Hello, world!");
    TSF_Io_printlog("Hello, world!はろーわーるど\n");
    TSF_Io_printlog("Hello, world!はろーわーるど");
    string TSF_log="test\n";
    TSF_log=TSF_Io_printlog("Hello, world!はろーわーるど",TSF_log);
    TSF_Io_printlog(TSF_log);
}

string TSF_Io_printlog(string TSF_text, ...){    //TSFdoc:SF_textをターミナル(stdout)に表示する。TSF_logに追記もできる。
 //   writefln("%d arguments",_arguments.length);
    string TSF_log="";
    if(_arguments.length>0){
        if (_arguments[0]==typeid(string)){
            TSF_log=va_arg!(string)(_argptr);
            TSF_log=TSF_log.back=='\n'?TSF_log:TSF_log~'\n';
        }
    }
    version(linux){
        puts(toStringz( TSF_text ));
    }
    version(Windows){
        puts(toStringz( to!(string)(toMBSz(TSF_text)) ));
    }
    TSF_log=TSF_text.back=='\n'?TSF_log~TSF_text:TSF_log~TSF_text~'\n';
    return TSF_log;
}

unittest{
}