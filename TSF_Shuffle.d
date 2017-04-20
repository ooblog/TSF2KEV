#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;

import TSF_Io;
import TSF_Forth;


void TSF_Shuffle_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに基本的な命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Shuffle");
    string function()[string] TSF_Forth_cards=[
        "#TSF_peekMthe":&TSF_Shuffle_peekMthe, "#指定スタック囲択読込":&TSF_Shuffle_peekMthe,
        "#TSF_peekMthis":&TSF_Shuffle_peekMthis, "#実行中スタック囲択読込":&TSF_Shuffle_peekMthis,
        "#TSF_peekMthat":&TSF_Shuffle_peekMthat, "#積込先スタック囲択読込":&TSF_Shuffle_peekMthat,
        "#TSF_peekMthey":&TSF_Shuffle_peekMthey, "#スタック一覧囲択読込":&TSF_Shuffle_peekMthey,
        "#TSF_pokeMthe":&TSF_Shuffle_pokeMthe, "#指定スタック囲択上書":&TSF_Shuffle_pokeMthe,
        "#TSF_pokeMthis":&TSF_Shuffle_pokeMthis, "#実行中スタック囲択上書":&TSF_Shuffle_pokeMthis,
        "#TSF_pokeMthat":&TSF_Shuffle_pokeMthat, "#積込先スタック囲択上書":&TSF_Shuffle_pokeMthat,
        "#TSF_pokeMthey":&TSF_Shuffle_pokeMthey, "#スタック一覧囲択上書":&TSF_Shuffle_pokeMthey,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Shuffle_peekM(string TSF_the,long TSF_peek){    //#TSFdoc:指定スタックからスタック名を囲択で読込。(TSFAPI)。
    string TSF_pull="";  size_t TSF_cardsN_len=TSF_stackD[TSF_the].length;
    if( (TSF_the in TSF_Forth_stackD())&&(0<TSF_cardsN_len) ){
        TSF_pull=TSF_Forth_stackD()[TSF_the][to!size_t(fmax(fmin(TSF_peek,TSF_cardsN_len-1),0))];
    }
    return TSF_pull;
}

string TSF_Shuffle_peekMthe(){    //#TSFdoc:指定スタックから囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthe(),TSF_peek));
    return "";
}

string TSF_Shuffle_peekMthis(){    //#TSFdoc:実行中スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthis(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return "";
}

string TSF_Shuffle_peekMthat(){    //#TSFdoc:積込先スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthat(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return "";
}

string TSF_Shuffle_peekMthey(){    //#TSFdoc:スタック一覧から最後尾スタック名を囲択で読込。1枚[peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_pull="";  size_t TSF_cardsN_len=TSF_Forth_stackO.length;
    if( 0<TSF_cardsN_len ){
        TSF_pull=TSF_Forth_stackO()[to!size_t(fmax(fmin(TSF_peek,TSF_cardsN_len-1),0))];
    }
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_pull);
    return "";
}

void TSF_Shuffle_pokeM(string TSF_the,long TSF_peek,string TSF_poke){    //#TSFdoc:指定スタックからカードを囲択で読込。(TSFAPI)
    string TSF_pull="";  size_t TSF_cardsN_len=TSF_Forth_stackD()[TSF_the].length;
    if( (TSF_the in TSF_Forth_stackD())&&(0<TSF_cardsN_len) ){
        TSF_Forth_stackD()[TSF_the][to!size_t(fmax(fmin(TSF_peek,TSF_cardsN_len-1),0))]=TSF_poke;
    }
}

string TSF_Shuffle_pokeMthe(){    //#TSFdoc:指定スタックからカードを囲択で上書。3枚[poke,the,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_the=TSF_Forth_drawthe();
    TSF_Shuffle_pokeM(TSF_the,TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Shuffle_pokeMthis(){    //#TSFdoc:実行中スタックからカードを囲択で上書。2枚[poke,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Shuffle_pokeM(TSF_Forth_drawthis(),TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Shuffle_pokeMthat(){    //TSF_doc:積込先スタックからカードを囲択で上書。2枚[poke,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Shuffle_pokeM(TSF_Forth_drawthat(),TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Shuffle_pokeMthey(){    //#TSFdoc:スタック一覧からスタック名を囲択で上書。2枚[poke,peek]ドロー。
    size_t TSF_cardsN_len=TSF_Forth_stackO().length;
    size_t TSF_peek=to!size_t(fmax(fmin(TSF_Io_RPNzero(TSF_Forth_drawthe()),TSF_cardsN_len-1),0));
    string TSF_poke=TSF_Forth_drawthe();
    if( 0<TSF_cardsN_len ){
        string TSF_pull=TSF_Forth_stackO()[TSF_peek];
        if( TSF_pull!=TSF_poke ){
            TSF_Forth_stackO()[TSF_peek]=TSF_poke;
            string[] TSF_stackR=TSF_Forth_stackD()[TSF_pull]; TSF_Forth_stackD().remove(TSF_pull);
            TSF_Forth_stackD()[TSF_poke]=TSF_stackR;
        }
    }
    return "";
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Shuffle_Initcards];
void TSF_Shuffle_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Shuffle」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Shuffle.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}


unittest {
//    TSF_Shuffle_debug(TSF_Io_argvs(["dmd","TSF_Shuffle.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE

