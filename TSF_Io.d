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
import std.math;


string TSF_Io_printlog(string TSF_text, ...){    //#TSFdoc:テキストをstdoutに表示。ログに追記もできる。(TSFAPI)
    string TSF_log="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_log=va_arg!(string)(_argptr);
        if( TSF_log.length>0 ){
            TSF_log=TSF_log.back=='\n'?TSF_log:TSF_log~'\n';
        }
    }
    auto TSF_Io_printf=toStringz(TSF_text);
    version(Windows){
        TSF_Io_printf=toStringz(to!string(toMBSz(TSF_text)));
    }
    if( TSF_text.length>0 && TSF_text.back=='\n' ){
        printf("%s",TSF_Io_printf);
        TSF_log=join([TSF_log,TSF_text]);
    }
    else{
        printf("%s\n",TSF_Io_printf);
        TSF_log=join([TSF_log,TSF_text,"\n"]);
    }
    return TSF_log;
}

string[] TSF_Io_argvs(string[] TSF_argvdup){    //#TSFdoc:TSF起動コマンド引数の文字コード対策。(TSFAPI)
    string[] TSF_argvs; TSF_argvs.length=TSF_argvdup.length;
    {    //OSversions
        version(linux){
            foreach(int i,string TSF_argv;TSF_argvdup){ TSF_argvs[i]=TSF_argv; }
        }
        version(OSX){
            foreach(int i,string TSF_argv;TSF_argvdup){ TSF_argvs[i]=TSF_argv; }
        }
        version(Windows){
            foreach(int i,string TSF_argv;TSF_argvdup){
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
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_encoding=va_arg!(string)(_argptr);
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
//        if( TSF_encoding=="cp932" ){
//            version(Windows){
//                TSF_text=fromMBSz(toStringz(to!char[](TSF_text)));
//            }
//        }
    }
    return TSF_text;
}

string TSF_Io_ESCencode(string TSF_textdup){    //#TSFdoc:「\t」を「&tab;」に置換。(TSFAPI)
    string TSF_text=TSF_textdup.replace("&","&amp;").replace("\t","&tab;");
    return TSF_text;
}

string TSF_Io_ESCdecode(string TSF_textdup){   //#TSFdoc:「&tab;」を「\t」に戻す。(TSFAPI)
    string TSF_text=TSF_textdup.replace("&tab;","\t").replace("&amp;","&");
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
        TSF_pull=TSF_separate[to!size_t(TSF_peek)];
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

string TSF_Io_splitpokeN(string TSF_tsv,string TSF_split,long TSF_peek,string TSF_poke){    //#TSFdoc:TSVなどから数値指定で上書。(TSFAPI)
    string[] TSF_splitpoked=TSF_Io_separatepokeN(TSF_tsv.split(TSF_split),TSF_peek,TSF_poke);
    return join(TSF_splitpoked,TSF_split);
}
string[] TSF_Io_separatepokeN(string[] TSF_separate,long TSF_peek,string TSF_poke){    //#TSFdoc:リストから数値指定で上書。(TSFAPI)
    string[] TSF_separatepoke=TSF_separate;
    if( 0<=TSF_peek && TSF_peek<TSF_separate.length ){
        TSF_separatepoke[to!size_t(TSF_peek)]=TSF_poke;
    }
    return TSF_separatepoke;
}
string TSF_Io_splitpokeL(string TSF_ltsv,string TSF_split,string TSF_label,string TSF_poke){    //#TSFdoc:LTSVからラベル指定で上書。(TSFAPI)
    string[] TSF_splitpoked=TSF_Io_separatepokeL(TSF_ltsv.split(TSF_split),TSF_label,TSF_poke);
    return join(TSF_splitpoked,TSF_split);
}
string[] TSF_Io_separatepokeL(string[] TSF_separate,string TSF_label,string TSF_poke){    //#TSFdoc:リストからラベル指定で上書。(TSFAPI)
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
        TSF_joined=TSF_separate[0..to!size_t(TSF_peek)]~TSF_separate[to!size_t(TSF_peek)+1..$];
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
        TSF_joined=TSF_separate[0..to!size_t(TSF_peek)]~[TSF_push]~TSF_separate[to!size_t(TSF_peek)..$];
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

string TSF_Io_RPN(string TSF_RPN){    //#TSFdoc:逆ポーランド電卓。分数は簡易的に小数で処理するので不正確。ゼロ除算も「n|0」とテキストで返す。(TSFAPI)
    string TSF_RPNanswer="";
    string TSF_RPNnum="";  int TSF_RPNminus=0;
    real[] TSF_RPNstack=[];
    string TSF_RPNseq=TSF_RPN~="  ";
    if( count(["U+","0x"],TSF_RPN[0..2]) ){ TSF_RPNseq="$"~TSF_RPN[2..$]; }
    real TSF_RPNstackL,TSF_RPNstackR,TSF_RPNstackF;
    string[] TSF_RPNcalcND;
    opeexit_rpn: foreach(char TSF_RPNope;TSF_RPNseq){
        if( count("0123456789abcdef.pm$|",TSF_RPNope) ){
            TSF_RPNnum~=TSF_RPNope;
        }
        else{
            if( TSF_RPNnum.length>0 ){
                TSF_RPNminus=TSF_RPNnum.count('m');  TSF_RPNnum=TSF_RPNnum.replace("p","").replace("m","");
                real TSF_RPNcalcN,TSF_RPNcalcD;
                if( count(TSF_RPNnum,'|') ){
                    try{
                        TSF_RPNcalcND=TSF_RPNnum.split("|");
                        TSF_RPNcalcN=count(TSF_RPNcalcND[0],'$')?to!real(to!long(TSF_RPNcalcND[0].replace("$",""),16)):to!real(TSF_RPNcalcND[0]);
                        TSF_RPNcalcD=count(TSF_RPNcalcND[$-1],'$')?to!real(to!long(TSF_RPNcalcND[$-1].replace("$",""),16)):to!real(TSF_RPNcalcND[$-1]);
                    }
                    catch(ConvException e){
                        TSF_RPNanswer="n|0";
                        break;
                    }
                }
                else{
                    try{
                        TSF_RPNcalcN=count(TSF_RPNnum,'$')?to!real(to!long(TSF_RPNnum.replace("$",""),16)):to!real(TSF_RPNnum);  TSF_RPNcalcD=1.0;
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
            if( count("!",TSF_RPNope) ){
                if( TSF_RPNstack.length ){
                    TSF_RPNstackL=TSF_RPNstack.back; TSF_RPNstack.popBack();
                }
                else{
                    TSF_RPNstackL=0.0;
                }
                switch( TSF_RPNope ){
                    case '!':  default: TSF_RPNstack~=abs(TSF_RPNstackL);  break;
                }
            }
            else if( count("+-*/\\#%<>",TSF_RPNope) ){
                if( TSF_RPNstack.length ){
                    TSF_RPNstackR=TSF_RPNstack.back; TSF_RPNstack.popBack();
                }
                else{
                    TSF_RPNstackR=0.0;
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
                            TSF_RPNanswer="n|0";  break opeexit_rpn;
                        }
                    break;
                    case '\\':
                        if( TSF_RPNstackR!=0.0 ){
                            TSF_RPNstack~=to!real(to!long(TSF_RPNstackL/TSF_RPNstackR));
                        }
                        else{
                            TSF_RPNanswer="n|0";  break opeexit_rpn;
                        }
                    break;
                    case '#':
                        if( TSF_RPNstackR!=0.0 ){
                            if( TSF_RPNstackR>0 ){
                                TSF_RPNstack~=TSF_RPNstackL%TSF_RPNstackR;
                            }
                            else{
                                if( TSF_RPNstackL%abs(TSF_RPNstackR)!=0 ){
                                    TSF_RPNstack~=abs(TSF_RPNstackR)-TSF_RPNstackL%abs(TSF_RPNstackR);
                                }
                                else{
                                    TSF_RPNstack~=0.0;
                                }
                            }
                        }
                        else{
                            TSF_RPNanswer="n|0";  break opeexit_rpn;
                        }
                    break;
                    case '%':  TSF_RPNstack~=TSF_RPNstackL+TSF_RPNstackL*TSF_RPNstackR/100.0;  break;
                    case '>':  TSF_RPNstack~=fmin(TSF_RPNstackL,TSF_RPNstackR);  break;
                    case '<':  TSF_RPNstack~=fmax(TSF_RPNstackL,TSF_RPNstackR);  break;
                    default:  break;
                }
            }
            else if( count("ZzOoUu",TSF_RPNope) ){
                if( TSF_RPNstack.length ){
                    TSF_RPNstackF=TSF_RPNstack.back; TSF_RPNstack.popBack();
                }
                else{
                    TSF_RPNstackF=0.0;
                }
                if( TSF_RPNstack.length ){
                    TSF_RPNstackR=TSF_RPNstack.back; TSF_RPNstack.popBack();
                }
                else{
                    TSF_RPNstackR=0.0;
                }
                if( TSF_RPNstack.length ){
                    TSF_RPNstackL=TSF_RPNstack.back; TSF_RPNstack.popBack();
                }
                else{
                    TSF_RPNstackL=0.0;
                }
                switch( TSF_RPNope ){
                    case 'Z':  TSF_RPNstack~=TSF_RPNstackF==0?TSF_RPNstackL:TSF_RPNstackR;  break;
                    case 'z':  TSF_RPNstack~=TSF_RPNstackF!=0?TSF_RPNstackL:TSF_RPNstackR;  break;
                    case 'O':  TSF_RPNstack~=TSF_RPNstackF>=0?TSF_RPNstackL:TSF_RPNstackR;  break;
                    case 'o':  TSF_RPNstack~=TSF_RPNstackF>0?TSF_RPNstackL:TSF_RPNstackR;  break;
                    case 'U':  TSF_RPNstack~=TSF_RPNstackF<=0?TSF_RPNstackL:TSF_RPNstackR;  break;
                    case 'u':  TSF_RPNstack~=TSF_RPNstackF<0?TSF_RPNstackL:TSF_RPNstackR;  break;
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
        if( TSF_RPNanswer!="0" ){
            TSF_RPNanswer=TSF_RPNanswer.front=='-'?TSF_RPNanswer.replace("-","m"):"p"~TSF_RPNanswer;
        }
    }
    return TSF_RPNanswer;
}

long TSF_Io_RPNzero(string TSF_RPN){    //#TSFdoc:逆ポーランド電卓。分数は簡易的に小数で処理するので不正確。ゼロ除算を「0」と数値で返す。(TSFAPI)
    string TSF_RPNtext=TSF_Io_RPN(TSF_RPN);
    TSF_RPNtext=TSF_RPNtext.replace("p","").replace("m","-");
    long TSF_RPNanswer=0;
    try{
        TSF_RPNanswer=to!long(TSF_RPNtext);
    }
    catch(ConvException e){
        TSF_RPNanswer=0;
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
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_text=va_arg!(string)(_argptr); TSF_remove=false;
    }
    TSF_Io_savedir(TSF_path);
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

void TSF_Io_writetext(string TSF_path,string TSF_addtext){    //#TSFdoc:TSF_pathにTSF_textを追記する。(TSFAPI)
    string TSF_text="";
    if( TSF_addtext.length>0 ){
        TSF_text=TSF_addtext.back=='\n'?TSF_text:TSF_addtext~'\n';
    }
    TSF_Io_savedir(TSF_path);
    if( exists(TSF_path) ){
        std.file.append(TSF_path,TSF_text);
    }
    else{
        std.file.write(TSF_path,TSF_text);
    }
}


void TSF_Io_debug(string[] TSF_argvs){
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Io.log";
    std.stdio.writeln(format("--- %s ---",__FILE__));
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
    foreach(string debug_rpn;[
        "0","0.0","U+p128","$ffff","1.414|3","2,3+","2,m3+","2,3-","2,m3-","2,3*","2,3/","0|0","0,0/","5,3\\","5,3#","5,3<","5,3>",
        "5,7,p1Z","5,7,0Z","5,7,m1Z","5,7,p1z","5,7,0z","5,7,m1z","5,7,p1O","5,7,0O","5,7,m1O","5,7,p1o","5,7,0o","5,7,m1o","5,7,p1U","5,7,0U","5,7,m1U","5,7,p1u","5,7,0u","5,7,m1u"
    ]){
        TSF_debug_log=TSF_Io_printlog(format("\t%s\t%s",debug_rpn,TSF_Io_RPN(debug_rpn)),TSF_debug_log);
    }
    std.stdio.writeln(format("--- fin. > %s ---",TSF_debug_savefilename));
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);
}


unittest {
//    TSF_Io_debug(TSF_Io_argvs(["TSFd_Io.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE

