#! /usr/bin/env rdmd

import std.stdio;
import core.stdc.stdio;
import std.string;
import std.conv;
import std.windows.charset;
import std.array;
import std.file;
import core.vararg;
import std.compiler;
import std.system;


string TSF_Io_printlog(string TSF_text, ...){    //#TSFdoc:テキストをstdoutに表示。ログに追記もできる。(TSFAPI)
//   writefln("%d arguments",_arguments.length);
    string TSF_log="";
    if( _arguments.length>0 ){
        if( _arguments[0]==typeid(string) ){
            TSF_log=va_arg!(string)(_argptr);
            if( TSF_log.length>0 ){
                TSF_log=TSF_log.back=='\n'?TSF_log:TSF_log~'\n';
            }
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
    if( TSF_text.length>0 ){
        TSF_log=TSF_text.back=='\n'?TSF_log~TSF_text:TSF_log~TSF_text~'\n';
    }
    return TSF_log;
}

string[] TSF_Io_argvs(string[] TSF_argvobj){    //#TSFdoc:TSF起動コマンド引数の文字コード対策。(TSFAPI)
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

string TSF_Io_loadtext(string TSF_path, ...){    //#TSFdoc:ファイルからテキストを読み込む。通常「UTF-8」を扱う。(TSFAPI)
    string TSF_text="";
    string TSF_encoding="utf-8";
    if( _arguments.length>0 ){
        if( _arguments[0]==typeid(string) ){
            TSF_encoding=va_arg!(string)(_argptr);
        }
    }
    TSF_encoding=toLower(TSF_encoding);
    foreach(string TSF_utf8;["utf-8","utf_8","u8","utf","utf8"]){
        if(TSF_encoding==TSF_utf8){ TSF_encoding="utf-8"; break; }
    }
    foreach(string TSF_sjis;["cp932","932","mskanji","ms-kanji","sjis","shiftjis","shift-jis","shift_jis"]){
        if(TSF_encoding==TSF_sjis){ TSF_encoding="cp932"; break; }
    }
    if( exists(TSF_path) ){
        TSF_text=readText(TSF_path);
        if( TSF_encoding=="cp932" ){
            version(Windows){
                TSF_text=fromMBSz(toStringz(cast(char[])TSF_text));
            }
        }
    }
    return TSF_text;
}

long TSF_Io_intstr0x(string TSF_Io_codestr){    //#TSFdoc:テキストを整数に変換する。10進と16進数も扱う。(TSFAPI)
    long TSF_Io_codeint=0;
    {
        try{
            TSF_Io_codeint=to!(int)(TSF_Io_codestr);
        }
        catch(ConvException e){
            TSF_Io_codeint=0;
        }
    }
    foreach(string TSF_Io_hexstr;["0x","U+","$"]){
        if( count(TSF_Io_codestr,TSF_Io_hexstr) ){
            try{
                TSF_Io_codeint=to!(int)(replace(TSF_Io_codestr,TSF_Io_hexstr,""),16);
            }
            catch(ConvException e){
                TSF_Io_codeint=0;
            }
        }
    }
    return TSF_Io_codeint;
}

real TSF_Io_floatstrND(string TSF_Io_codestr){        //#TSFdoc:テキストを小数に変換する。分数も扱う。(TSFAPI)
//real TSF_Io_floatstrND(string TSF_Io_codeobj){        //#TSFdoc:テキストを小数に変換する。分数も扱う。(TSFAPI)
    real TSF_Io_codefloatN=0.0, TSF_Io_codefloatD=0.0;
//    string TSF_Io_codestr=replace(TSF_Io_codeobj,"p",""); TSF_Io_codestr=replace(TSF_Io_codestr,"m","-"); TSF_Io_codestr=replace(TSF_Io_codestr,"|","/")
    {
        try{
            TSF_Io_codefloatN=to!(real)(TSF_Io_codestr);
        }
        catch(ConvException e){
            TSF_Io_codefloatN=0.0;
        }
    }
    foreach(string TSF_Io_fractionstr;["/"]){
        if( count(TSF_Io_codestr,TSF_Io_fractionstr) ){
        }
    }
    return TSF_Io_codefloatN;
}
//def TSF_Forth_popintthe(TSF_that):    #TSF_doc:スタックから数値として積み下ろす(TSFAPI)。
//    TSF_calcQ=TSF_Forth_popthat()
//    if '|' in TSF_calcQ:
//        TSF_calcN,TSF_calcD=TSF_calcQ.replace('m','-').replace('p','').split('|')
//        TSF_calcN,TSF_calcD=TSF_io_intstr0x(TSF_calcN),TSF_io_intstr0x(TSF_calcD)
 //       TSF_popdata=TSF_calcN//TSF_calcD if TSF_calcD != 0 else 0 
//    else:
//        TSF_calcN=TSF_calcQ.replace('m','-').replace('p','')
//        TSF_popdata=TSF_io_intstr0x(TSF_calcN)
//    return TSF_popdata

string TSF_Io_debug(string[] TSF_argvs){
    string TSF_debug_log="";
    TSF_debug_log=TSF_Io_printlog("TSF_Tab-Separated-Forth:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join(["UTF-8",":TSF_encoding","0",":TSF_fin."],"\t")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_argvs:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join(TSF_argvs,"\t")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_d:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join([format("D%s.%s",version_major,version_minor),text(os),"UTF-8"],"\t")),TSF_debug_log);
    return TSF_debug_log;
}

void main(string[] TSF_argvobj){
//    writeln("Hello, world!");
//    TSF_Io_printlog("Hello, world!はろーわーるど");
//    TSF_Io_printlog(text(TSF_Io_intstr0x("U+128")));
//    TSF_Io_printlog(text(256));
//    TSF_Io_printlog(text(TSF_Io_floatstrND("1.414|3")));
//    TSF_Io_printlog(text(3.14));
//    string[] TSF_argvs=TSF_Io_argvs(TSF_argvobj);
//    string TSF_log="test";
//    foreach(string TSF_argv;TSF_argvobj){
//        TSF_log=TSF_Io_printlog(TSF_argv,TSF_log);
//    }
//    if( TSF_argvs.length>1 ){
//        TSF_Io_printlog(TSF_Io_loadtext(TSF_argvs[1]));
//    }
    string[] TSF_argvs=TSF_Io_argvs(TSF_argvobj);
    writeln(format("--- %s ---",TSF_argvs[0]));
    string TSF_debug_savefilename="debug/debug_dIo.log";
    string TSF_debug_log=TSF_Io_debug(TSF_argvs);
//    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    writeln("--- fin. ---");
}


