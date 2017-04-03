#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.array;
import std.typecons;
import core.vararg;
import std.algorithm;

import TSF_Io;


string TSF_Forth_1ststack(){    //TSFdoc:最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:";
}

string TSF_Forth_version(){    //TSFdoc:TSFバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945";
}

void TSF_Forth_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){
    string function()[string] TSF_Forth_cards=[
        "#TSF_fin.":&TSF_Forth_fin, "#TSFを終了。":&TSF_Forth_fin,
        "#TSF_this":&TSF_Forth_this, "#スタックを実行":&TSF_Forth_this,
        "#TSF_that":&TSF_Forth_that, "#スタックに積込":&TSF_Forth_that,
        "#TSF_stylethe":&TSF_Forth_stylethe, "#指定スタックにスタイル指定":&TSF_Forth_stylethe,
        "#TSF_stylethis":&TSF_Forth_stylethis, "#実行中スタックにスタイル指定":&TSF_Forth_stylethis,
        "#TSF_stylethat":&TSF_Forth_stylethat, "#積込先スタックにスタイル指定":&TSF_Forth_stylethat,
        "#TSF_stylethey":&TSF_Forth_stylethey, "#全スタックにスタイル指定":&TSF_Forth_stylethey,
        "#TSF_viewthe":&TSF_Forth_viewthe, "#指定スタック表示":&TSF_Forth_viewthe,
        "#TSF_viewthis":&TSF_Forth_viewthis, "#実行中スタックを表示":&TSF_Forth_viewthis,
        "#TSF_viewthat":&TSF_Forth_viewthat, "#積込先スタックを表示":&TSF_Forth_viewthat,
        "#TSF_viewthey":&TSF_Forth_viewthey, "#スタック一覧を表示":&TSF_Forth_viewthey,
        "#TSF_RPN":&TSF_Forth_RPN, "#逆ポーランド電卓で計算":&TSF_Forth_RPN, "#小数計算":&TSF_Forth_RPN,
        "#TSF_echo":&TSF_Forth_echo, "#カードを表示":&TSF_Forth_echo,
        "#TSF_echoN":&TSF_Forth_echoN, "#N枚カードを表示":&TSF_Forth_echoN,
        "#TSF_argvs":&TSF_Forth_argvs, "#コマンド読込":&TSF_Forth_argvs,
        "#TSF_argvsthe":&TSF_Forth_argvsthe, "#指定スタック積込":&TSF_Forth_argvsthe,
        "#TSF_argvsthis":&TSF_Forth_argvsthis, "#実行中スタック積込":&TSF_Forth_argvsthis,
        "#TSF_argvsthat":&TSF_Forth_argvsthat, "#積込先スタック積込":&TSF_Forth_argvsthat,
        "#TSF_argvsthey":&TSF_Forth_argvsthey, "#スタック一覧積込":&TSF_Forth_argvsthey,
//#    TSF_words["#TSF_reverseN"]=TSF_shuffle_reverseN; TSF_words["#スタックN個逆順"]=TSF_shuffle_reverseN
        "#TSF_readtext":&TSF_Forth_readtext, "#テキストを読込":&TSF_Forth_readtext,
        "#TSF_mergethe":&TSF_Forth_mergethe, "#TSFに合成":&TSF_Forth_mergethe,
        "#TSF_publishthe":&TSF_Forth_publishthe, "#指定スタックをテキスト化":&TSF_Forth_publishthe,
        "#TSF_publishthis":&TSF_Forth_publishthis, "#実行中スタックをテキスト化":&TSF_Forth_publishthis,
        "#TSF_publishthat":&TSF_Forth_publishthat, "#積込先スタックをテキスト化":&TSF_Forth_publishthat,
        "#TSF_remove":&TSF_Forth_remove, "#ファイルを削除する":&TSF_Forth_remove,
        "#TSF_savetext":&TSF_Forth_savetext, "#テキストファイルに上書":&TSF_Forth_savetext,
        "#TSF_writetext":&TSF_Forth_writetext, "#テキストファイルに追記":&TSF_Forth_writetext,
        "#TSF_lenthe":&TSF_Forth_lenthe, "#指定スタック枚数":&TSF_Forth_lenthe,
        "#TSF_lenthis":&TSF_Forth_lenthis, "#実行中スタック枚数":&TSF_Forth_lenthis,
        "#TSF_lenthat":&TSF_Forth_lenthat, "#積込先スタック枚数":&TSF_Forth_lenthat,
        "#TSF_lenthey":&TSF_Forth_lenthey, "#スタック一覧枚数":&TSF_Forth_lenthey,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Forth_fin(){    //#TSFdoc:TSF終了時のオプションを指定する。1枚[errmsg]ドロー。
    TSF_callptrD=null; TSF_callptrO=[];
    return "#exit";
}

string TSF_Forth_this(){    //#TSF_doc:thisスタックの変更。1枚[this]ドロー。
    string TSF_card=TSF_Forth_drawthe();
    if( TSF_card.length==0 || ( TSF_card.length>0 && TSF_card.front=='#' ) ){ TSF_card="#exit"; }
    return TSF_card;
}

string TSF_Forth_that(){    //#TSF_doc:thatスタックの変更。1枚[that]ドロー。
    TSF_Forth_drawthat(TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_stylethe(){    //#TSFdoc:指定したスタックの表示方法を指定する。2枚[style,the]ドロー。
    string TSF_the=TSF_Forth_drawthe();
    TSF_Forth_style(TSF_the,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_stylethis(){    //#TSFdoc:実行中スタックの表示方法を指定する。1枚[style]ドロー。
    TSF_Forth_style(TSF_Forth_drawthis(),TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_stylethat(){    //#TSFdoc:積込先スタックの表示方法を指定する。1枚[style]ドロー。
    TSF_Forth_style(TSF_Forth_drawthat(),TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_stylethey(){    //#TSFdoc:全スタックの表示方法を一括指定。1枚[style]ドロー。
    string TSF_style=TSF_Forth_drawthe();
    foreach(string TSF_the;TSF_stackO){
        TSF_Forth_style(TSF_the,TSF_style);
    }
    return "";
}

string TSF_Forth_viewthe(){    //#TSFdoc:指定したスタックを表示する。1枚[the]ドロー。
    TSF_Forth_view(TSF_Forth_drawthe(),true);
    return "";
}

string TSF_Forth_viewthis(){    //#TSFdoc:実行中スタックを表示する。0枚ドロー。
    TSF_Forth_view(TSF_Forth_drawthis(),true);
    return "";
}

string TSF_Forth_viewthat(){    //#TSFdoc:積込先スタックを表示する。0枚ドロー。
    TSF_Forth_view(TSF_Forth_drawthat(),true);
    return "";
}

string TSF_Forth_viewthey(){    //#TSFdoc:スタック一覧を表示する。0枚ドロー。
    foreach(string TSF_the;TSF_stackO){
        TSF_Forth_view(TSF_the,true);
    }
    return "";
}

string TSF_Forth_RPN(){    //#TSF_doc:RPN電卓。1枚[rpn]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Io_RPN(TSF_Forth_drawthe()));
    return "";
}

string TSF_Forth_echo(){    //#TSF_doc:カードの表示。1枚[echo]ドロー。
    if( TSF_echo ){
        TSF_echo_log=TSF_Io_printlog(TSF_Forth_drawthe(),TSF_echo_log);
    }
    else{
        TSF_Io_printlog(TSF_Forth_drawthe());
    }
    return "";
}

string TSF_Forth_echoN(){    //#TSF_doc:カードの表示。RPN枚[echoN…echoA,N]ドロー。
//    long TSF_echoRPN=to!long(TSF_Io_RPN(TSF_Forth_drawthe()));
    long TSF_echoRPN=TSF_Io_RPNzero(TSF_Forth_drawthe());
    if( TSF_echoRPN>0 ){
        foreach(long TSF_count;0..TSF_echoRPN){
            TSF_Forth_echo();
        }
    }
    return "";
}

string TSF_Forth_argvs(){    //#TSF_doc:コマンドを積込む。0枚[]ドローしてコマンド枚数+1枚[argvN…argvA,N]リターン。
    long TSF_argvslen=TSF_mainandargvs.length?TSF_mainandargvs[1..$].length:0;
    if( TSF_argvslen>0 ){
        foreach(string TSF_card;TSF_mainandargvs[1..$]){
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
        }
    }
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_argvslen));
    return "";
}

string TSF_Forth_argvsthe(){    //#TSF_doc:指定スタックを積込む。1枚[the]ドローしてスタック枚数+1枚[cardN…cardA,N]リターン。
    string TSF_the=TSF_Forth_drawthe();
    if( TSF_the in TSF_stackD ){
        foreach(string TSF_card;TSF_stackD[TSF_the]){
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
        }
    }
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_stackD[TSF_the].length));
    return "";
}
string TSF_Forth_argvsthis(){    //#TSF_doc:実行中スタックを積込む。0枚[]ドローしてスタック枚数+1枚[cardN…cardA,N]リターン。
    string TSF_the=TSF_Forth_drawthis();
    if( TSF_the in TSF_stackD ){
        foreach(string TSF_card;TSF_stackD[TSF_the]){
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
        }
    }
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_stackD[TSF_the].length));
    return "";
}
string TSF_Forth_argvsthat(){    //#TSF_doc:積込先スタックを積込む。0枚[]ドローしてスタック枚数+1枚[cardN…cardA,N]リターン。
    string TSF_the=TSF_Forth_drawthat();
    if( TSF_the in TSF_stackD ){
        foreach(string TSF_card;TSF_stackD[TSF_the]){
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
        }
    }
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_stackD[TSF_the].length));
    return "";
}

string TSF_Forth_argvsthey(){    //#TSF_doc:スタック一覧を積込む。0枚[]ドローしてスタック枚数+1枚[cardN…cardA,N]リターン。
    foreach(string TSF_card;TSF_stackO){
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
    }
    return "";
}

string TSF_Forth_reversethe(){    //#TSF_doc:カードN枚を逆順に積込。スタック枚数+1枚[cardN…cardA,N]ドローしてスタック枚数[cardN…cardA]リターン。
    string[] TSF_stackR=null;
    long TSF_argvslen=TSF_Io_RPNzero(TSF_Forth_drawthe());
    return "";
}


string TSF_Forth_lenthe(){    //TSF_doc:指定スタックの枚数を取得。1枚[the]ドローして1枚[N]リターン。
    string TSF_the=TSF_Forth_drawthe();
    if( TSF_the in TSF_stackD ){
        TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_stackD[TSF_the].length));
    }
    return "";
}

string TSF_Forth_lenthis(){    //TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_stackD[TSF_Forth_drawthis()].length));
    return "";
}

string TSF_Forth_lenthat(){    //TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_stackD[TSF_Forth_drawthat()].length));
    return "";
}

string TSF_Forth_lenthey(){    //TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_stackD.length));
    return "";
}

string TSF_Forth_readtext(){    //#TSF_doc:ファイル名のスタックにテキストを読み込む。1枚[path]ドロー。
    string TSF_path=TSF_Forth_drawthe();
    TSF_Forth_loadtext(TSF_path,TSF_path);
    return "";
}

string TSF_Forth_mergethe(){    //#TSF_doc:テキストをTSFとして読み込む。1枚[merge]ドロー。
    TSF_Forth_merge(TSF_Forth_drawthe(),[TSF_Forth_1ststack()]);
    return "";
}

string TSF_Forth_publishthe(){    //#TSF_doc:指定スタックをテキスト化。2枚[path,the]ドロー。
    string TSF_the=TSF_Forth_drawthe();
    string TSF_publish_log=TSF_Forth_view(TSF_the,false,"");
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_the]);
    return "";
}

string TSF_Forth_publishthis(){    //#TSF_doc:実行中スタックをテキスト化。1枚[path]ドロー。
    string TSF_publish_log=TSF_Forth_view(TSF_Forth_drawthis(),false,"");
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_Forth_drawthis()]);
    return "";
}

string TSF_Forth_publishthat(){    //#TSF_doc:実行中スタックをテキスト化。1枚[path]ドロー。
    string TSF_publish_log=TSF_Forth_view(TSF_Forth_drawthat(),false,"");
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_Forth_drawthat()]);
    return "";
}

string TSF_Forth_remove(){    //#TSF_doc:ファイルを削除する。1枚[path]ドロー。
    TSF_Io_savetext(TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_savetext(){    //#TSF_doc:テキスト化スタックをファイルに保存する。2枚[path,the]ドロー。
    string TSF_the=TSF_Forth_drawthe();
    string TSF_text=(TSF_the in TSF_stackD)?TSF_Io_ESCdecode(join(TSF_stackD[TSF_the],"\n")):"";
    TSF_Io_savetext(TSF_Forth_drawthe(),TSF_text);
    return "";
}

string TSF_Forth_writetext(){    //#TSF_doc:テキスト化スタックをファイルに追記する。2枚[path,the]ドロー。
    string TSF_the=TSF_Forth_drawthe();
    string TSF_text=(TSF_the in TSF_stackD)?TSF_Io_ESCdecode(join(TSF_stackD[TSF_the],"\n")):"";
    TSF_Io_writetext(TSF_Forth_drawthe(),TSF_text);
    return "";
}


string[] TSF_mainandargvs=null;
string function()[string] TSF_cardD=null;
string[] [string] TSF_stackD=null;
string [string] TSF_styleD=null;
long[string] TSF_callptrD=null;
string[] TSF_cardO=[],TSF_stackO=[],TSF_styleO=[],TSF_callptrO=[];
string TSF_stackthis=TSF_Forth_1ststack(),TSF_stackthat=TSF_Forth_1ststack();
long TSF_cardscount=0;
void TSF_Forth_initTSF(string[] TSF_sysargvs,void function(ref string function()[string],ref string[])[] TSF_addcalls){    //#TSFdoc:スタックやカードなどをまとめて初期化する(TSFAPI)。
    TSF_cardD=null;
    TSF_stackD=null;
    TSF_styleD=null;
    TSF_callptrD=null;
    TSF_cardO,TSF_stackO=[],TSF_styleO=[],TSF_callptrO=[];
    TSF_stackthis=TSF_Forth_1ststack(),TSF_stackthat=TSF_Forth_1ststack();
    TSF_cardscount=0;
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"#TSF_fin.","T");
    TSF_mainandargvs=TSF_sysargvs;
    void function(ref string function()[string],ref string[])[]  TSF_Initcards=[&TSF_Forth_Initcards]~TSF_addcalls;
    foreach(void function(ref string function()[string],ref string[]) TSF_Initcard;TSF_Initcards){
        TSF_Initcard(TSF_cardD,TSF_cardO);
    }
}

string TSF_Forth_style(string TSF_the, ...){    //#TSF_doc:スタックの表示スタイルを指定する(TSFAPI)。
    string TSF_style="";
    if( TSF_the !in TSF_stackD ){
        if( _arguments.length>0 && _arguments[0]==typeid(string) ){
            TSF_styleD[TSF_the]=TSF_style;
        }
        TSF_style=TSF_styleD[TSF_the];
    }
    return TSF_style;
}

void TSF_Forth_setTSF(string TSF_the, ...){    //#TSFdoc:スタックやカードなどをまとめて初期化する(TSFAPI)。
    string TSF_text="",TSF_style="T";
    if( _arguments.length>0 ){
        if( _arguments[0]==typeid(string) ){
            TSF_text=va_arg!(string)(_argptr);
        }
        if( _arguments.length>1 && _arguments[1]==typeid(string) ){
            TSF_style=va_arg!(string)(_argptr);
        }
        if( TSF_the !in TSF_stackD ){
            TSF_stackO~=[TSF_the];  TSF_styleO~=[TSF_the];
        }
        TSF_stackD[TSF_the]=replace(stripRight(TSF_text),"\t","\n").split("\n");
        TSF_styleD[TSF_the]=TSF_style;
    }
    else{
        if( TSF_the !in TSF_stackD ){ TSF_stackD.remove(TSF_the); }
        if( TSF_the !in TSF_styleD ){ TSF_styleD.remove(TSF_the); }
        if( count(TSF_stackO,TSF_the) ){ TSF_stackO=remove!((TSF_stackO){return TSF_stackO==TSF_the;})(TSF_stackO); }
        if( count(TSF_styleO,TSF_the) ){ TSF_styleO=remove!((TSF_styleO){return TSF_styleO==TSF_the;})(TSF_styleO); }
    }
}

string TSF_Forth_loadtext(string TSF_the,string TSF_path){    //#TSF_doc:スタックにテキストファイルを読み込む。(TSFAPI)
    string TSF_text=TSF_Io_loadtext(TSF_path);
    TSF_text=TSF_Io_ESCencode(TSF_text);
    TSF_Forth_setTSF(TSF_the,TSF_text,"N");
    return TSF_text;
}

void TSF_Forth_merge(string TSF_path,string[] TSF_ESCstack=[], ...){    //#TSF_doc:スタック内のテキストをTSFとして読み込む。(TSFAPI)
    bool TSF_mergedel=false;
    if( _arguments.length>0 && _arguments[0]==typeid(bool) ){
        TSF_mergedel=va_arg!(bool)(_argptr);
    }
    if( TSF_path in TSF_stackD ){
        string TSF_the=TSF_Forth_1ststack(); string TSF_line="";  string[] TSF_lineL=null;
        foreach(string TSF_card;TSF_stackD[TSF_path]){
            if( TSF_card.length==0 || TSF_card.front=='#' ){ continue; }
            TSF_line=TSF_Io_ESCdecode(TSF_card);
            if( TSF_line.front!='\t' ){
                TSF_lineL=TSF_line.split("\t");
                if( count(TSF_ESCstack,TSF_lineL[0])==0 ){
                    if( TSF_the !in TSF_stackD ){
                        TSF_stackO~=[TSF_the]; TSF_styleO~=[TSF_the];
                    }
                    TSF_stackD[TSF_the]=null;
                    TSF_styleD[TSF_the]=TSF_lineL.length>=2?"O":"";
                }
            }
            if( count(TSF_ESCstack,TSF_the)==0 ){
                TSF_lineL=TSF_line.split("\t")[1..$];
                if( TSF_the !in TSF_stackD ){
                    TSF_stackO~=[TSF_the]; TSF_styleO~=[TSF_the];
                }
                TSF_stackD[TSF_the]~=TSF_lineL;
                if( TSF_styleD[TSF_the]!="O" ){
                    TSF_styleD[TSF_the]=TSF_lineL.length>=2?"T":"N";
                }
            }
        }
        if( TSF_mergedel ){
            TSF_Forth_setTSF(TSF_path);
        }
    }
}

long TSF_stackmax=20;
bool TSF_echo=false;  string TSF_echo_log="";
string TSF_Forth_run(...){    //#TSFdoc:TSFデッキを走らせる。
    string TSF_cardnow=""; string TSF_stacknext="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_echo=true; TSF_echo_log~=va_arg!(string)(_argptr);
    }
    else{
        TSF_echo=false; TSF_echo_log="";
    }
    if( count(TSF_stackD[TSF_Forth_1ststack()],"#TSF_fin." )==0 ){
        TSF_Forth_return(TSF_Forth_1ststack(),"#TSF_fin.");
    }
    while(true){
        while( TSF_cardscount<TSF_stackD[TSF_stackthis].length && TSF_cardscount<TSF_stackmax ){
            TSF_cardnow=TSF_stackD[TSF_stackthis][to!size_t(TSF_cardscount)];  TSF_cardscount++;
            if( TSF_cardnow !in TSF_cardD ){
                TSF_Forth_return(TSF_stackthat,TSF_cardnow);
            }
            else{
                TSF_stacknext=TSF_cardD[TSF_cardnow]();
                if( TSF_stacknext=="" ){
                    continue;
                }
                else if( TSF_stacknext !in TSF_stackD ){
                    break;
                }
                else{
                    while( count(TSF_callptrO,TSF_stacknext) ){
                        TSF_callptrD.remove(TSF_callptrO[$-1]); TSF_callptrO.popBack();
                    }
                    TSF_callptrD[TSF_stackthis]=TSF_cardscount;  TSF_callptrO~=[TSF_stackthis];
                    TSF_stackthis=TSF_stacknext;
                    TSF_cardscount=0;
                }
            }
        }
        if( TSF_callptrO.length>0 ){
            TSF_stackthis=TSF_callptrO[$-1]; TSF_cardscount=TSF_callptrD[TSF_callptrO[$-1]];
            TSF_callptrD.remove(TSF_callptrO[$-1]); TSF_callptrO.popBack();
        }
        else{
            break;
        }
    }
    return TSF_echo_log;
}

string TSF_Forth_view(string TSF_the,bool TSF_view_io, ...){    //#TSFdoc:スタックの内容をテキスト表示(TSFAPI)。
    string TSF_view_log="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_view_log=va_arg!(string)(_argptr);
    }
    if( TSF_the in TSF_stackD ){
        string TSF_style=TSF_styleD.get(TSF_the,"T");
        string TSF_view_logline="";
        switch( TSF_style ){
            case "O":  TSF_view_logline=format("%s\t%s\n",TSF_the,join(TSF_stackD[TSF_the],"\t"));  break;
            case "T":  TSF_view_logline=format("%s\n\t%s\n",TSF_the,join(TSF_stackD[TSF_the],"\t"));  break;
            case "N": default:  TSF_view_logline=format("%s\n\t%s\n",TSF_the,join(TSF_stackD[TSF_the],"\n\t"));  break;
        }
        TSF_view_log=(TSF_view_io)?TSF_Io_printlog(TSF_view_logline,TSF_view_log):TSF_view_log~TSF_view_logline;
    }
    return TSF_view_log;
}

string TSF_Forth_draw(string TSF_the){    //#TSFdoc:スタックから1枚ドロー。(TSFAPI)
    string TSF_draw="";
    if( TSF_stackD[TSF_the].length>0 && TSF_the.length>0 && TSF_the in TSF_stackD ){
        TSF_draw=TSF_stackD[TSF_the][$-1];  TSF_stackD[TSF_the].popBack();
    }
    return TSF_draw;
}

string TSF_Forth_drawthe(){    //#TSFdoc:theスタックの取得(thatから1枚ドロー)。(TSFAPI)
    return TSF_Forth_draw(TSF_stackthat);
}

string TSF_Forth_drawthis(...){    //#TSFdoc:thisスタックの取得(thatから0枚ドロー)。(TSFAPI)
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_stackthis=va_arg!(string)(_argptr);
    }
    return TSF_stackthis;
}

string TSF_Forth_drawthat(...){    //#TSFdoc:thatスタックの取得(thatから0枚ドロー)。(TSFAPI)
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_stackthat=va_arg!(string)(_argptr);
    }
    return TSF_stackthat;
}

void TSF_Forth_return(string TSF_the,string TSF_card){    //#TSFdoc:theスタックに1枚リターン。(TSFAPI)
    if( TSF_the !in TSF_stackD ){
        TSF_stackO~=[TSF_the];
        TSF_stackD[TSF_the]=null;
    }
    TSF_stackD[TSF_the]~=[TSF_card];
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
string TSF_Forth_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Forth」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_dForth.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"PPPP:\t#TSF_this\tTSF_argvs:\t#TSF_that\t#TSF_argvs\t#TSF_fin.","T");
    TSF_Forth_setTSF("PPPP:","this:Peek\tthat:Poke\tthe:Pull\tthey:Push\t2\t#TSF_echoN\tlen:\t#TSF_this","T");
    TSF_Forth_setTSF("len:","len:\t#TSF_that\tlen:\t#TSF_lenthe\t#TSF_lenthis\t#TSF_lenthat\t#TSF_lenthey\t#exit\t#TSF_this","T");
    foreach(string TSF_the;TSF_stackO){
        TSF_debug_log=TSF_Forth_view(TSF_the,true,TSF_debug_log);
    }
    TSF_debug_log=TSF_Io_printlog("--- run ---",TSF_debug_log);
    TSF_debug_log=TSF_Forth_run(TSF_debug_log);
    TSF_debug_log=TSF_Io_printlog("--- fin. ---",TSF_debug_log);
    foreach(string TSF_the;TSF_stackO){
        TSF_debug_log=TSF_Forth_view(TSF_the,true,TSF_debug_log);
    }
    TSF_debug_log=TSF_Io_printlog(format("--- %s > %s ---",__FILE__,TSF_debug_savefilename),TSF_debug_log);
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);
    return TSF_debug_log;
}


unittest {
    TSF_Forth_debug(TSF_Io_argvs(["dmd","TSF_Forth.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
