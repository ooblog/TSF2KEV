#! /usr/bin/env rdmd

import std.stdio;
import core.stdc.stdio;
import std.string;
import std.conv;
import std.windows.charset;
import std.array;
import std.file;
import std.path;
import core.vararg;
import std.compiler;
import std.system;
import std.typecons;


string TSF_Io_printlog(string TSF_text, ...){    //#TSFdoc:テキストをstdoutに表示。ログに追記もできる。(TSFAPI)
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
            puts(toStringz( to!string(toMBSz(TSF_text)) ));
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
//                TSF_argvs[i]=fromMBSz(toStringz(to!char[](TSF_argv)));
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
                TSF_text=fromMBSz(toStringz(to!char[](TSF_text)));
            }
        }
    }
    return TSF_text;
}

string TSF_Io_ESCencode(string TSF_textobj){    //#TSFdoc:「\t」を「&tab;」に置換。(TSFAPI)
    string TSF_text=replace(replace(TSF_textobj,"&","&amp;"),"\t","&tab;");
    return TSF_text;
}

string TSF_Io_ESCdecode(string TSF_textobj){   //#TSFdoc:「&tab;」を「\t」に戻す。(TSFAPI)
    string TSF_text=replace(replace(TSF_textobj,"&tab;","\t"),"&amp;","&");
    return TSF_text;
}

long TSF_Io_splitlen(string TSF_text,string TSF_split){    //#TSFdoc:テキストの行数などを取得。(TSFAPI)
    long TSF_splitlen=TSF_Io_separatelen(TSF_text.split(TSF_split));
    return TSF_splitlen;
}
long TSF_Io_separatelen(string[] TSF_separate){    //#TSFdoc:リストの数を取得。(TSFAPI)
    long TSF_separatelen=TSF_separate.length;
    return TSF_separatelen;
}

string TSF_Io_splitpeekN(string TSF_tsv,string TSF_split,long TSF_peek){    //#TSFdoc:TSVなどから数値指定で読込。(TSFAPI)
    string TSF_pull=TSF_Io_separatepeekN(TSF_tsv.split(TSF_split),TSF_peek);
    return TSF_pull;
}
string TSF_Io_separatepeekN(string[] TSF_separate,long TSF_peek){    //#TSFdoc:リストから数値指定で読込。(TSFAPI)
    string TSF_pull="";
    if( 0<=TSF_peek && TSF_peek<TSF_separate.length ){
        TSF_pull=TSF_separate[to!int(TSF_peek)];
    }
    return TSF_pull;
}
string TSF_Io_splitpeekL(string TSF_ltsv,string TSF_split,string TSF_label){    //#TSFdoc:LTSVからラベル指定で読込。(TSFAPI)
    string TSF_pull=TSF_Io_separatepeekL(TSF_ltsv.split(TSF_split),TSF_label);
    return TSF_pull;
}
string TSF_Io_separatepeekL(string[] TSF_separate,string TSF_label){    //#TSFdoc:リストからラベル指定で読込。(TSFAPI)
    string TSF_pull="";
    if( TSF_label.length>0 ){
        foreach(string TSF_separated;TSF_separate){
            if( indexOf(TSF_separated,TSF_label)==0 ){
                TSF_pull=TSF_separated[TSF_label.length..$];
            }
        }
    }
    return TSF_pull;
}

string TSF_Io_splitpokeN(string TSF_tsv,string TSF_split,long TSF_peek,string TSF_poke){    //#TSFdoc:TSVなどから数値指定で書込。(TSFAPI)
    string[] TSF_splitpoked=TSF_Io_separatepokeN(TSF_tsv.split(TSF_split),TSF_peek,TSF_poke);
    return join(TSF_splitpoked,TSF_split);
}
string[] TSF_Io_separatepokeN(string[] TSF_separate,long TSF_peek,string TSF_poke){    //#TSFdoc:リストから数値指定で書込。(TSFAPI)
    string[] TSF_separatepoke=TSF_separate;
    if( 0<=TSF_peek && TSF_peek<TSF_separate.length ){
        TSF_separatepoke[to!int(TSF_peek)]=TSF_poke;
    }
    return TSF_separatepoke;
}
string TSF_Io_splitpokeL(string TSF_ltsv,string TSF_split,string TSF_label,string TSF_poke){    //#TSFdoc:LTSVからラベル指定で書込。(TSFAPI)
    string[] TSF_splitpoked=TSF_Io_separatepokeL(TSF_ltsv.split(TSF_split),TSF_label,TSF_poke);
    return join(TSF_splitpoked,TSF_split);
}
string[] TSF_Io_separatepokeL(string[] TSF_separate,string TSF_label,string TSF_poke){    //#TSFdoc:リストからラベル指定で書込。(TSFAPI)
    string[] TSF_separatepoke=TSF_separate;
    if( TSF_label.length>0 ){
        foreach(int TSF_peek,string TSF_separated;TSF_separate){
            if( indexOf(TSF_separated,TSF_label)==0 ){
                TSF_separatepoke[TSF_peek]=TSF_label~TSF_poke;
            }
        }
    }
    return TSF_separatepoke;
}

string TSF_Io_splitpullN(string TSF_tsv,string TSF_split,long TSF_peek){    //#TSFdoc:TSVなどから数値指定で引抜。(TSFAPI)
    string[] TSF_separated=TSF_Io_separatepullN(TSF_tsv.split(TSF_split),TSF_peek);
    return join(TSF_separated,TSF_split);
}
string[] TSF_Io_separatepullN(string[] TSF_separate,long TSF_peek){    //TSFdoc:リストから数値指定で引抜。(TSFAPI)
    string[] TSF_joined=TSF_separate;
    if( 0<=TSF_peek && TSF_peek<TSF_separate.length ){
        TSF_joined=TSF_separate[0..to!int(TSF_peek)]~TSF_separate[to!int(TSF_peek)+1..$];
    }
    return TSF_joined;
}
string TSF_Io_splitpullL(string TSF_ltsv,string TSF_split,string TSF_label){    //#TSFdoc:LTSVからラベル指定で引抜。(TSFAPI)
    string[] TSF_separated=TSF_Io_separatepullL(TSF_ltsv.split(TSF_split),TSF_label);
    return join(TSF_separated,TSF_split);
}
string[] TSF_Io_separatepullL(string[] TSF_separate,string TSF_label){    //#TSFdoc:リストからラベル指定で引抜。(TSFAPI)
    string[] TSF_joined=TSF_separate;
    if( TSF_label.length>0 ){
        foreach(int TSF_peek,string TSF_separated;TSF_separate){
            if( indexOf(TSF_separated,TSF_label)==0 ){
                TSF_joined=TSF_separate[0..TSF_peek]~TSF_separate[TSF_peek+1..$];
            }
        }
    }
    return TSF_joined;
}

string TSF_Io_splitpushN(string TSF_tsv,string TSF_split,long TSF_peek,string TSF_push){    //#TSFdoc:TSVなどから数値指定で差込。(TSFAPI)
    string[] TSF_separated=TSF_Io_separatepushN(TSF_tsv.split(TSF_split),TSF_peek,TSF_push);
    return join(TSF_separated,TSF_split);
}
string[] TSF_Io_separatepushN(string[] TSF_separate,long TSF_peek,string TSF_push){    //#TSFdoc:リストから数値指定で差込。(TSFAPI)
    string[] TSF_joined=TSF_separate;
    if( 0<=TSF_peek && TSF_peek<TSF_separate.length ){
        TSF_joined=TSF_separate[0..to!int(TSF_peek)]~[TSF_push]~TSF_separate[to!int(TSF_peek)..$];
    }
    else if( TSF_peek<0 ){
        TSF_joined=[TSF_push]~TSF_separate;
    }
    else if( TSF_separate.length<=TSF_peek ){
        TSF_joined=TSF_separate~[TSF_push];
    }
    return TSF_joined;
}
string TSF_Io_splitpushL(string TSF_tsv,string TSF_split,string TSF_label,string TSF_push){    //#TSFdoc:TSVなどから数値指定で差込。(TSFAPI)
    string[] TSF_separated=TSF_Io_separatepushL(TSF_tsv.split(TSF_split),TSF_label,TSF_push);
    return join(TSF_separated,TSF_split);
}
string[] TSF_Io_separatepushL(string[] TSF_separate,string TSF_label,string TSF_push){    //#TSFdoc:リストから数値指定で差込。(TSFAPI)
    string[] TSF_joined=[];
    if( TSF_label.length>0 ){
        foreach(int TSF_peek,string TSF_separated;TSF_separate){
            if( indexOf(TSF_separated,TSF_label)==0 ){
                TSF_joined=TSF_separate; TSF_joined[TSF_peek]=TSF_label~TSF_push; 
            }
        }
        if( TSF_joined.length==0 ){
            TSF_joined=TSF_separate~[TSF_label~TSF_push];
        }
    }
    else{
        TSF_joined=TSF_separate;
    }
    return TSF_joined;
}

string TSF_Io_RPN(string TSF_RPN){    //#TSFdoc:逆ポーランド電卓(TSFAPI)
    string TSF_RPNanswer="";
    string TSF_RPNnum="";  int TSF_RPNminus=0;
    real[] TSF_RPNstack=[];
    string TSF_RPNseq=replace(replace(TSF_RPN,"U+","$"),"0x","$")~" ";
    real TSF_RPNstackL,TSF_RPNstackR;
    string[] TSF_RPNcalcND;
    opeexit: foreach(char TSF_RPNope;TSF_RPNseq){
        if( count("0123456789.pm$|",TSF_RPNope) ){
            TSF_RPNnum~=TSF_RPNope;
        }
        else{
            if( TSF_RPNnum.length>0 ){
                TSF_RPNminus=count(TSF_RPNnum,'m');  TSF_RPNnum=replace(replace(TSF_RPNnum,"p",""),"m","");
                real TSF_RPNcalcN,TSF_RPNcalcD;
                if( count(TSF_RPNnum,'$') ){
                    try{
                        TSF_RPNcalcN=to!int(replace(TSF_RPNnum,"$",""),16);  TSF_RPNcalcD=1.0;
                    }
                    catch(ConvException e){
                        TSF_RPNanswer="n|0";
                        break;
                    }
                }
                else if( count(TSF_RPNnum,'|') ){
                    try{
                        TSF_RPNcalcND=TSF_RPNnum.split("|");
                        TSF_RPNcalcN=to!real(TSF_RPNcalcND[0]);  TSF_RPNcalcD=to!real(TSF_RPNcalcND[1]);
                    }
                    catch(ConvException e){
                        TSF_RPNanswer="n|0";
                        break;
                    }
                }
                else{
                    try{
                        TSF_RPNcalcN=to!real(TSF_RPNnum);  TSF_RPNcalcD=1.0;
                    }
                    catch(ConvException e){
                        TSF_RPNanswer="n|0";
                        break;
                    }
                }
                if( TSF_RPNminus%2 ){
                    TSF_RPNcalcN=-TSF_RPNcalcN;
                }
                if( TSF_RPNcalcD!=0.0 ){
                    TSF_RPNstack~=TSF_RPNcalcN/TSF_RPNcalcD;
                }
                else{
                    TSF_RPNanswer="n|0";
                    break;
                }
                TSF_RPNnum="";
            }
            if( count("+-*/",TSF_RPNope) ){
                if( TSF_RPNstack.length ){
                    TSF_RPNstackR=TSF_RPNstack.back; TSF_RPNstack.popBack();
                }
                else{
                    TSF_RPNstackL=0.0;
                }
                if( TSF_RPNstack.length ){
                    TSF_RPNstackL=TSF_RPNstack.back; TSF_RPNstack.popBack();
                }
                else{
                    TSF_RPNstackL=0.0;
                }
                switch( TSF_RPNope ){
                    case '+':  TSF_RPNstack~=TSF_RPNstackL+TSF_RPNstackR;  break;
                    case '-':  TSF_RPNstack~=TSF_RPNstackL-TSF_RPNstackR;  break;
                    case '*':  TSF_RPNstack~=TSF_RPNstackL*TSF_RPNstackR;  break;
                    case '/':
                        if( TSF_RPNstackR!=0.0 ){
                            TSF_RPNstack~=TSF_RPNstackL/TSF_RPNstackR;
                        }
                        else{
                            TSF_RPNanswer="n|0";
                            break opeexit;
                        }
                    break;
                    default:  break;
                }
            }
        }
    }
    if( TSF_RPNstack.length ){
        TSF_RPNstackL=TSF_RPNstack.back; TSF_RPNstack.popBack();
    }
    else{
        TSF_RPNstackL=0.0;
    }
    if( TSF_RPNanswer != "n|0" ){
        TSF_RPNanswer=( TSF_RPNstackL!=to!long(TSF_RPNstackL) )?to!string(TSF_RPNstackL):to!string(to!long(TSF_RPNstackL));
    }
    return TSF_RPNanswer;
}

void TSF_Io_savedir(string TSF_path){    //「TSF_Io_savetext()」でファイル保存する時、1階層分のフォルダを作成する。(TSFAPI)
    string TSF_Io_workdir=dirName(absolutePath(TSF_path));
    if( exists(TSF_Io_workdir)==false && TSF_Io_workdir.length>0 ){
        mkdir(TSF_Io_workdir);
    }
}

void TSF_Io_savedirs(string TSF_path){    //一気に深い階層のフォルダを複数作れてしまうので取扱い注意(扱わない)。(TSFAPI)
    string TSF_Io_workdir=dirName(absolutePath(TSF_path));
    if( exists(TSF_Io_workdir)==false && TSF_Io_workdir.length>0 ){
        mkdirRecurse(TSF_Io_workdir);
    }
}

void TSF_Io_savetext(string TSF_path, ...){    //#TSFdoc:TSF_pathにTSF_textを保存する。TSF_textを省略した場合ファイルを削除する。(TSFAPI)
    string TSF_text="";  bool TSF_remove=true;
    if( _arguments.length>0 ){
        if( _arguments[0]==typeid(string) ){
            TSF_text=va_arg!(string)(_argptr); TSF_remove=false;
            TSF_Io_savedir(TSF_path);
        }
    }
    if( TSF_text.length>0 ){
        TSF_text=TSF_text.back=='\n'?TSF_text:TSF_text~'\n';
    }
    if( TSF_remove ){
        if( exists(TSF_path) ){
            remove(TSF_path);
        }
    }
    else{
        std.file.write(TSF_path,TSF_text);
    }
}

void TSF_Io_writetext(string TSF_path,string TSF_text){    //#TSFdoc:TSF_pathにTSF_textを追記する。(TSFAPI)
    if( TSF_text.length>0 ){
        TSF_text=TSF_text.back=='\n'?TSF_text:TSF_text~'\n';
    }
    TSF_Io_savedir(TSF_path);
    if( exists(TSF_path) ){
        std.file.append(TSF_path,TSF_text);
    }
    else{
        std.file.write(TSF_path,TSF_text);
    }
}


string TSF_Io_debug(string[] TSF_argvs){
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_dIo.log";
    std.stdio.writeln(format("--- %s ---",__MODULE__));
    TSF_debug_log=TSF_Io_printlog("TSF_Tab-Separated-Forth:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join(["UTF-8",":TSF_encoding","0",":TSF_fin."],"\t")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_argvs:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join(TSF_argvs,"\t")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_d:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join([format("D(%s)%s.%s",vendor,version_major,version_minor),text(os),"UTF-8"],"\t")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_debug_tsv:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s","helloワールド\u5496\u55B1"),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_ESCencode("csv\ttsv\tLTSV\tL:Tsv\tTSF")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_ESCdecode("csv&tab;tsv&tab;LTSV&tab;L:Tsv&tab;TSF")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitlen(TSF_debug_log,"\n")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitlen("csv\ttsv\tLTSV\tL:Tsv\tTSF","\t")),TSF_debug_log);
    string TSF_debug_PPPP="this:Peek\tthat:Poke\tthe:Pull\tthey:Push";
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpeekN(TSF_debug_PPPP,"\t",0)),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpeekL(TSF_debug_PPPP,"\t","this:")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpokeN(TSF_debug_PPPP,"\t",1,"poked")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpokeL(TSF_debug_PPPP,"\t","that:","poked")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpokeL(TSF_debug_PPPP,"\t","cards:","poked")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpullN(TSF_debug_PPPP,"\t",2)),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpullL(TSF_debug_PPPP,"\t","the:")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpushN(TSF_debug_PPPP,"\t",-1,"pushed")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpushN(TSF_debug_PPPP,"\t",3,"pushed")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpushN(TSF_debug_PPPP,"\t",10,"pushed")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpushL(TSF_debug_PPPP,"\t","they:","pushed")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitpushL(TSF_debug_PPPP,"\t","cards:","pushed")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_debug_rpn:",TSF_debug_log);
    foreach(string debug_rpn;["U+p128","1.414|3","2,3+","2,m3+","2,3-","2,m3-","2,3*","2,3/","0|0","0,0/"]){
        TSF_debug_log=TSF_Io_printlog(format("\t%s\t%s",debug_rpn,TSF_Io_RPN(debug_rpn)),TSF_debug_log);
    }
    std.stdio.writeln(format("--- fin. > %s ---",TSF_debug_savefilename));
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);
    return TSF_debug_log;
}


unittest {
//    TSF_Io_debug(TSF_Io_argvs(["TSFd_Io.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE

