#! /usr/bin/env rdmd

import std.stdio;
import core.stdc.stdio;
import std.string;
import std.conv;
import std.windows.charset;
import std.array;
import std.file;
import core.vararg;

string TSF_Io_printlog(string TSF_text, ...){    //#TSFdoc:SF_textをターミナル(stdout)に表示する。TSF_logに追記もできる。
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

string[] TSF_Io_argvs(string[] TSF_argvobj){    //#TSFdoc:TSF起動コマンド引数の文字コード対策。
    string[] TSF_argvs; TSF_argvs.length=TSF_argvobj.length;
    version(linux){
        for(int i=0;i<TSF_argvobj.length;i++){
            TSF_argvs[i]=TSF_argvobj[i];
        }
    }
    version(Windows){
        for(int i=0;i<TSF_argvobj.length;i++){
            TSF_argvs[i]=TSF_argvobj[i];
//            TSF_argvs[i]=fromMBSz(toStringz(cast(char[])TSF_argvobj[i]));
        }
    }
    return TSF_argvs;
}


void main(string[] TSF_argvobj){
//    writeln("Hello, world!");
    TSF_Io_printlog("Hello, world!はろーわーるど");
    string[] TSF_argvs=TSF_Io_argvs(TSF_argvobj);
    string TSF_log="test";
    for(int i=0;i<TSF_argvs.length;i++){
        TSF_log=TSF_Io_printlog(TSF_argvs[i],TSF_log);
    }
}
