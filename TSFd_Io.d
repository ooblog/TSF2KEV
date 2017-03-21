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
    {    //OSversions
        version(linux){
            puts(toStringz( TSF_text ));
        }
        version(OSX){
            puts(toStringz( TSF_text ));
        }
        version(Windows){
            puts(toStringz( to!(string)(toMBSz(TSF_text)) ));
        }
    }
    TSF_log=TSF_text.back=='\n'?TSF_log~TSF_text:TSF_log~TSF_text~'\n';
    return TSF_log;
}

string[] TSF_Io_argvs(string[] TSF_argvobj){    //#TSFdoc:TSF起動コマンド引数の文字コード対策。
    string[] TSF_argvs; TSF_argvs.length=TSF_argvobj.length;
    {    //OSversions
        version(linux){
            foreach(int i,string TSF_argv;TSF_argvobj){
                TSF_argvs[i]=TSF_argv;
            }
        }
        version(OSX){
            foreach(int i,string TSF_argv;TSF_argvobj){
                TSF_argvs[i]=TSF_argv;
            }
        }
        version(Windows){
            foreach(int i,string TSF_argv;TSF_argvobj){
                TSF_argvs[i]=TSF_argv;
//                TSF_argvs[i]=fromMBSz(toStringz(cast(char[])TSF_argv));
            }
        }
    }
    return TSF_argvs;
}

string TSF_Io_loadtext(string TSF_path, ...){    //#TSFdoc:TSF_pathからTSF_textを読み込む。初期文字コードは「UTF-8」なのでいわゆるシフトJISを読み込む場合は「cp932」を指定する。
    string TSF_text="";
    string TSF_encoding="utf-8";
    if(_arguments.length>0){
        if (_arguments[0]==typeid(string)){
            TSF_encoding=va_arg!(string)(_argptr);
        }
    }
    return TSF_text;
}

void main(string[] TSF_argvobj){
//    writeln("Hello, world!");
    TSF_Io_printlog("Hello, world!はろーわーるど");
    string[] TSF_argvs=TSF_Io_argvs(TSF_argvobj);
    string TSF_log="test";
    foreach(string TSF_argv;TSF_argvobj){
        TSF_log=TSF_Io_printlog(TSF_argv,TSF_log);
    }
}
