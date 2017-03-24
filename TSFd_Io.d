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

long TSF_Io_intstr0x(string TSF_Io_codestrobj){    //#TSFdoc:テキストを整数に変換する。10進と16進数も扱う。(TSFAPI)
    string TSF_Io_codestr=replace(replace(TSF_Io_codestrobj,"p",""),"m","-");
    long TSF_Io_codeint=to!int(TSF_Io_floatstrND(TSF_Io_codestr));
    foreach(string TSF_Io_hexstr;["0x","U+","$"]){
        if( count(TSF_Io_codestr,TSF_Io_hexstr) ){
            try{
                TSF_Io_codeint=to!int(replace(TSF_Io_codestr,TSF_Io_hexstr,""),16);
            }
            catch(ConvException e){
                TSF_Io_codeint=0;
            }
        }
    }
    return TSF_Io_codeint;
}

real TSF_Io_floatstrND(string TSF_Io_codestrobj){    //#TSFdoc:テキストを小数に変換する。分数も扱う。(TSFAPI)
    string TSF_Io_codestr=replace(replace(replace(TSF_Io_codestrobj,"p",""),"m","-"),"|","/");
    real TSF_Io_codefloat=0.0;
    string TSF_Io_calcN,TSF_Io_calcD;
    if( count(TSF_Io_codestr,"/") ){
        string[] TSF_Io_codesplit=split(TSF_Io_codestr,"/");
        TSF_Io_calcN=TSF_Io_codesplit[0]; TSF_Io_calcD=TSF_Io_codesplit[$-1];
    }
    else{
        TSF_Io_calcN=TSF_Io_codestr; TSF_Io_calcD="1";
    }
    try{
        TSF_Io_codefloat=to!real(TSF_Io_calcN)/to!real(TSF_Io_calcD);
    }
    catch(ConvException e){
        TSF_Io_codefloat=0.0;
    }
    return TSF_Io_codefloat;
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
    string[] TSF_separate=TSF_text.split(TSF_split);
    long TSF_splitlen=TSF_Io_separatelen(TSF_separate);
    return TSF_splitlen;
}
long TSF_Io_separatelen(string[] TSF_separate){    //#TSFdoc:リストの数を取得。(TSFAPI)
    long TSF_separatelen=TSF_separate.length;
    return TSF_separatelen;
}

//#def TSF_Io_splitpeekN(TSF_text,TSF_split,TSF_peek):
//#    pass
//#def TSF_Io_splitpokeN(TSF_text,TSF_split):
//#    pass
//#def TSF_Io_splitpullN(TSF_text,TSF_split):
//#    pass
//#def TSF_Io_splitpushN(TSF_text,TSF_split):
//#    pass
//#def TSF_Io_splitpeekL(TSF_text,TSF_split):
//#    pass
//#def TSF_Io_splitpokeL(TSF_text,TSF_split):
//#    pass
//#def TSF_Io_splitpullL(TSF_text,TSF_split):
//#    pass
//#def TSF_Io_splitpushL(TSF_text,TSF_split):
//#    pass

void TSF_Io_savedir(string TSF_path){    //#TSFdoc:リストの数を取得。(TSFAPI)
    string TSF_Io_workdir=dirName(absolutePath(TSF_path));
    writeln(format("TSF_Io_workdir=%s",TSF_Io_workdir));
}
//auto dirName(R)(R path)
//Char[] dirname(Char)(Char[] fullname);
//string rel2abs(string path); 
//pure @safe string absolutePath(string path, lazy string base = getcwd()); 


//def TSF_Io_savedir(TSF_path):    #TSFdoc:「TSF_Io_savetext()」でファイル保存する時、1階層分のフォルダ1個を作成する。
//    TSF_Io_workdir=os.path.dirname(os.path.normpath(TSF_path))
//    if not os.path.exists(TSF_Io_workdir) and not os.path.isdir(TSF_Io_workdir) and len(TSF_Io_workdir): os.mkdir(TSF_Io_workdir)
//
//def TSF_Io_savedirs(TSF_path):    #TSFdoc:「TSF_Io_savetext()」でファイル保存する時、一気に深い階層のフォルダを複数作れてしまうので取扱い注意(扱わない)。
//    TSF_Io_workdir=os.path.dirname(os.path.normpath(TSF_path))
//    if not os.path.exists(TSF_Io_workdir) and not os.path.isdir(TSF_Io_workdir) and len(TSF_Io_workdir): os.makedirs(TSF_Io_workdir)
//
//def TSF_Io_savetext(TSF_path,TSF_text=None):    #TSFdoc:TSF_pathにTSF_textを保存する。TSF_textを省略した場合ファイルを削除する。空のファイルを作る場合はTSF_textに文字列長さ0の文字列変数を用意する。
//    if TSF_text != None:
//        TSF_Io_savedir(TSF_path)
//        if not TSF_text.endswith('\n'):
//            TSF_text+='\n'
//        if sys.version_info.major == 2:
//            with open(TSF_path,'wb') as TSF_Io_fileobj:
//                TSF_Io_fileobj.write(TSF_text.encode("UTF-8"))
//        if sys.version_info.major == 3:
//            with open(TSF_path,mode="w",encoding="UTF-8",errors="xmlcharrefreplace",newline='\n') as TSF_Io_fileobj:
//                TSF_Io_fileobj.write(TSF_text)
//    else:
//        os.remove(TSF_text)
//
//def TSF_Io_writetext(TSF_path,TSF_text):    #TSFdoc:TSF_pathにTSF_textを追記する。
//    if TSF_text != None:
//        TSF_Io_savedir(TSF_path)
//        if not TSF_text.endswith('\n'):
//            TSF_text+='\n'
//        if sys.version_info.major == 2:
//            with open(TSF_path,'ab') as TSF_Io_fileobj:
//                TSF_Io_fileobj.write(TSF_text.encode("UTF-8"))
//        if sys.version_info.major == 3:
//            with open(TSF_path,mode="a",encoding="UTF-8",errors="xmlcharrefreplace",newline='\n') as TSF_Io_fileobj:
//                TSF_Io_fileobj.write(TSF_text)




string TSF_Io_debug(string[] TSF_argvs){
    string TSF_debug_log="";
    TSF_debug_log=TSF_Io_printlog("TSF_Tab-Separated-Forth:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join(["UTF-8",":TSF_encoding","0",":TSF_fin."],"\t")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_argvs:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join(TSF_argvs,"\t")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_d:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",join([format("D%s.%s",version_major,version_minor),text(os),"UTF-8"],"\t")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("TSF_debug:",TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s","helloワールド\u5496\u55B1"),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_intstr0x("U+p128")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_floatstrND("1.414|3")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_floatstrND("3.14")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_ESCencode("tsv\tL:Tsv")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_ESCdecode("tsv&tab;L:Tsv")),TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog(format("\t%s",TSF_Io_splitlen(TSF_debug_log,"\n")),TSF_debug_log);
    return TSF_debug_log;
}

void main(string[] TSF_argvobj){
    string[] TSF_argvs=TSF_Io_argvs(TSF_argvobj);
    writeln(format("--- %s ---",TSF_argvs[0]));
    string TSF_debug_savefilename="debug/debug_dIo.log";
    string TSF_debug_log=TSF_Io_debug(TSF_argvs);
    TSF_Io_savedir(TSF_debug_savefilename);
//    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    writeln("--- fin. ---");
}


