#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.array;
import std.typecons;
import core.vararg;
import std.algorithm;

import TSF_Io;


string TSF_Forth_1ststack(){    //#TSFdoc:最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:";
}

string TSF_Forth_version(){    //#TSFdoc:TSFバージョン(ブランチ)名(TSFAPI)。
    return "20170413R040745";
}

void TSF_Forth_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSF_doc:関数カードに基本的な命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Forth");
    string function()[string] TSF_Forth_cards=[
        "#TSF_fin.":&TSF_Forth_fin, "#TSFを終了。":&TSF_Forth_fin,
        "#TSF_countmax":&TSF_Forth_countmax, "#カード数え上げ上限":&TSF_Forth_countmax,
        "#TSF_this":&TSF_Forth_this, "#スタック実行":&TSF_Forth_this,
        "#TSF_that":&TSF_Forth_that, "#スタック積込":&TSF_Forth_that,
        "#TSF_stylethe":&TSF_Forth_stylethe, "#指定スタックにスタイル指定":&TSF_Forth_stylethe,
        "#TSF_stylethis":&TSF_Forth_stylethis, "#実行中スタックにスタイル指定":&TSF_Forth_stylethis,
        "#TSF_stylethat":&TSF_Forth_stylethat, "#積込先スタックにスタイル指定":&TSF_Forth_stylethat,
        "#TSF_stylethey":&TSF_Forth_stylethey, "#全スタックにスタイル指定":&TSF_Forth_stylethey,
        "#TSF_viewthe":&TSF_Forth_viewthe, "#指定スタック表示":&TSF_Forth_viewthe,
        "#TSF_viewthis":&TSF_Forth_viewthis, "#実行中スタック表示":&TSF_Forth_viewthis,
        "#TSF_viewthat":&TSF_Forth_viewthat, "#積込先スタック表示":&TSF_Forth_viewthat,
        "#TSF_viewthey":&TSF_Forth_viewthey, "#スタック一覧表示":&TSF_Forth_viewthey,
        "#TSF_RPN":&TSF_Forth_RPN, "#逆ポーランド電卓で計算":&TSF_Forth_RPN, "#小数計算":&TSF_Forth_RPN,
        "#TSF_echo":&TSF_Forth_echo, "#カードを表示":&TSF_Forth_echo,
        "#TSF_echoN":&TSF_Forth_echoN, "#N枚カードを表示":&TSF_Forth_echoN,
        "#TSF_argvs":&TSF_Forth_argvs, "#コマンド読込":&TSF_Forth_argvs,
        "#TSF_argvsthe":&TSF_Forth_argvsthe, "#指定スタック積込":&TSF_Forth_argvsthe,
        "#TSF_argvsthis":&TSF_Forth_argvsthis, "#実行中スタック積込":&TSF_Forth_argvsthis,
        "#TSF_argvsthat":&TSF_Forth_argvsthat, "#積込先スタック積込":&TSF_Forth_argvsthat,
        "#TSF_argvsthey":&TSF_Forth_argvsthey, "#スタック一覧積込":&TSF_Forth_argvsthey,
        "#TSF_reverseN":&TSF_Forth_reverseN, "#N枚逆順積込":&TSF_Forth_reverseN,
        "#TSF_joinN":&TSF_Forth_joinN, "#N枚1枚化":&TSF_Forth_joinN,
        "#TSF_join[]":&TSF_Forth_joinsquarebrackets, "#括弧で連結":&TSF_Forth_joinsquarebrackets,
        "#TSF_sandwichN":&TSF_Forth_sandwichN, "#N枚挟んで1枚化":&TSF_Forth_sandwichN,
        "#TSF_split":&TSF_Forth_split, "#文字で分割":&TSF_Forth_split,
        "#TSF_chars":&TSF_Forth_chars, "#一文字ずつに分割":&TSF_Forth_chars,
        "#TSF_charslen":&TSF_Forth_charslen, "#文字数を数える":&TSF_Forth_charslen,
        "#TSF_lenthe":&TSF_Forth_lenthe, "#指定スタック枚数":&TSF_Forth_lenthe,
        "#TSF_lenthis":&TSF_Forth_lenthis, "#実行中スタック枚数":&TSF_Forth_lenthis,
        "#TSF_lenthat":&TSF_Forth_lenthat, "#積込先スタック枚数":&TSF_Forth_lenthat,
        "#TSF_lenthey":&TSF_Forth_lenthey, "#スタック一覧枚数":&TSF_Forth_lenthey,
        "#TSF_peekFthe":&TSF_Forth_peekFthe, "#指定スタック表面読込":&TSF_Forth_peekFthe,
        "#TSF_peekFthis":&TSF_Forth_peekFthis, "#実行中スタック表面読込":&TSF_Forth_peekFthis,
        "#TSF_peekFthat":&TSF_Forth_peekFthat, "#積込先スタック表面読込":&TSF_Forth_peekFthat,
        "#TSF_peekFthey":&TSF_Forth_peekFthey, "#スタック一覧表面読込":&TSF_Forth_peekFthey,
        "#TSF_peekNthe":&TSF_Forth_peekNthe, "#指定スタック読込":&TSF_Forth_peekNthe,
        "#TSF_peekNthis":&TSF_Forth_peekNthis, "#実行中スタック読込":&TSF_Forth_peekNthis,
        "#TSF_peekNthat":&TSF_Forth_peekNthat, "#積込先スタック読込":&TSF_Forth_peekNthat,
        "#TSF_peekNthey":&TSF_Forth_peekNthey, "#スタック一覧読込":&TSF_Forth_peekNthey,
        "#TSF_pullFthe":&TSF_Forth_pullFthe, "#指定スタック表面引抜":&TSF_Forth_pullFthe,
        "#TSF_pulltFhis":&TSF_Forth_pullFthis, "#実行中スタック表面引抜":&TSF_Forth_pullFthis,
        "#TSF_pullFthat":&TSF_Forth_pullFthat, "#積込先スタック表面引抜":&TSF_Forth_pullFthat,
        "#TSF_pullFthey":&TSF_Forth_pullFthey, "#スタック一覧表面引抜":&TSF_Forth_pullFthey,
        "#TSF_pullNthe":&TSF_Forth_pullNthe, "#指定スタック引抜":&TSF_Forth_pullNthe,
        "#TSF_pulltNhis":&TSF_Forth_pullNthis, "#実行中スタック引抜":&TSF_Forth_pullNthis,
        "#TSF_pullNthat":&TSF_Forth_pullNthat, "#積込先スタック引抜":&TSF_Forth_pullNthat,
        "#TSF_pullNthey":&TSF_Forth_pullNthey, "#スタック一覧引抜":&TSF_Forth_pullNthey,
        "#TSF_pushFthe":&TSF_Forth_pushFthe, "#指定スタック差込":&TSF_Forth_pushFthe,
        "#TSF_pushFthis":&TSF_Forth_pushFthis, "#実行中スタック差込":&TSF_Forth_pushFthis,
        "#TSF_pushFthat":&TSF_Forth_pushFthat, "#積込先スタック差込":&TSF_Forth_pushFthat,
        "#TSF_pushFthey":&TSF_Forth_pushFthey, "#スタック一覧差込":&TSF_Forth_pushFthey,
        "#TSF_pushNthe":&TSF_Forth_pushNthe, "#指定スタック差込":&TSF_Forth_pushNthe,
        "#TSF_pushNthis":&TSF_Forth_pushNthis, "#実行中スタック差込":&TSF_Forth_pushNthis,
        "#TSF_pushNthat":&TSF_Forth_pushNthat, "#積込先スタック差込":&TSF_Forth_pushNthat,
        "#TSF_pushNthey":&TSF_Forth_pushNthey, "#スタック一覧差込":&TSF_Forth_pushNthey,
        "#TSF_readtext":&TSF_Forth_readtext, "#テキストを読込":&TSF_Forth_readtext,
        "#TSF_mergethe":&TSF_Forth_mergethe, "#TSFに合成":&TSF_Forth_mergethe,
        "#TSF_publishthe":&TSF_Forth_publishthe, "#指定スタックをテキスト化":&TSF_Forth_publishthe,
        "#TSF_publishthis":&TSF_Forth_publishthis, "#実行中スタックをテキスト化":&TSF_Forth_publishthis,
        "#TSF_publishthat":&TSF_Forth_publishthat, "#積込先スタックをテキスト化":&TSF_Forth_publishthat,
        "#TSF_remove":&TSF_Forth_remove, "#ファイルを削除する":&TSF_Forth_remove,
        "#TSF_savetext":&TSF_Forth_savetext, "#テキストファイルに上書":&TSF_Forth_savetext,
        "#TSF_writetext":&TSF_Forth_writetext, "#テキストファイルに追記":&TSF_Forth_writetext,
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

string TSF_Forth_countmax(){    //#TSFdoc:TSFスタックのカード数え上げ枚数の上限を指定。1枚[errmsg]ドロー。
    TSF_stackmax=TSF_Io_RPNzero(TSF_Forth_drawthe());
    return "";
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
    long TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe());
    if( TSF_len>0 ){
        foreach(long TSF_count;0..TSF_len){
            TSF_Forth_echo();
        }
    }
    return "";
}

string TSF_Forth_argvs(){    //#TSF_doc:コマンドを積込む。0枚[]ドローしてコマンド枚数+1枚[argvN…argvA,N]リターン。
    long TSF_len=TSF_mainandargvs.length?TSF_mainandargvs[1..$].length:0;
    if( TSF_len>0 ){
        foreach(string TSF_card;TSF_mainandargvs[1..$]){
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
        }
    }
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_len));
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

string TSF_Forth_argvsthey(){    //#TSF_doc:カードN枚を逆順に積込。カード枚数+総数1枚[cardN…cardA,N]ドローしてカード枚数[cardN…cardA]リターン。
    foreach(string TSF_card;TSF_stackO){
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
    }
    return "";
}

string TSF_Forth_reverseN(){    //#TSF_doc:カードN枚を逆順に積込。カード枚数+総数1枚[cardN…cardA,N]ドローしてカード枚数[cardN…cardA]リターン。
    string[] TSF_stackR=null;
    long TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe());
    if( TSF_len>0 ){
        foreach(long TSF_count;0..TSF_len){
            TSF_stackR~=[TSF_Forth_drawthe()];
        }
        foreach(string TSF_card;TSF_stackR){
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
        }
    }
    return "";
}

string TSF_Forth_joinN(){    //#TSF_doc:カードN枚を連結する。カード枚数+総数1枚[cardN…cardA,N]ドローして1枚[joined]リターン。
    string[] TSF_stackR=null;
    long TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe());
    if( TSF_len>0 ){
        foreach(long TSF_count;0..TSF_len){
            TSF_stackR~=[TSF_Forth_drawthe()];
        }
        TSF_stackR.reverse();
        TSF_Forth_return(TSF_Forth_drawthat(),join(TSF_stackR));
    }
    return "";
}

string TSF_Forth_joinsquarebrackets(){    //#TSF_doc:カードN枚を角括弧で連結する。数式の元を1枚[calc]ドローして1枚[joined]リターン。
    string TSF_calc=TSF_Forth_drawthe();
    string TSF_bracket;
    foreach(long TSF_count;0..TSF_Forth_len(TSF_Forth_drawthat())){
        TSF_bracket="["~to!string(TSF_count)~"]";
        if( count(TSF_calc,TSF_bracket) ){
            TSF_calc=replace(TSF_calc,TSF_bracket,TSF_Forth_drawthe());
        }
        else{
            break;
        }
    }
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_calc);
    return "";
}

string TSF_Forth_sandwichN(){    //#TSF_doc:カードN枚を連結する。カード枚数+総数1枚+接続詞1枚[cardN…cardA,N,joint]ドローして1枚[joined]リターン。
    string[] TSF_stackR=null;
    string TSF_joint=TSF_Forth_drawthe();
    long TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe());
    if( TSF_len>0 ){
        foreach(long TSF_count;0..TSF_len){
            TSF_stackR~=[TSF_Forth_drawthe()];
        }
        TSF_stackR.reverse();
        TSF_Forth_return(TSF_Forth_drawthat(),join(TSF_stackR,TSF_joint));
    }
    return "";
}

string TSF_Forth_split(){    //#TSF_doc:文字列を分割する。続詞1枚[joint]ドローしてカード枚数+総数1枚[cardN…cardA,N]リターン。
    string TSF_joint=TSF_Forth_drawthe();
    string TSF_joined=TSF_Forth_drawthe();
    string[] TSF_stackR=TSF_joined.split(TSF_joint);
    TSF_stackR.reverse();
    foreach(string TSF_card;TSF_stackR){
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
    }
    return "";
}

string TSF_Forth_chars(){    //#TSF_doc:文字列を一文字ずつに分割する。1枚[chars]ドローしてカード枚数+総数1枚[cardN…cardA,N]リターン。
    string TSF_joined=TSF_Forth_drawthe();
    char[] TSF_stackR=cast(char[])TSF_joined;
    TSF_stackR.reverse();
    foreach(char TSF_card;TSF_stackR){
        TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_card));
    }
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_joined.length));
    return "";
}

string TSF_Forth_charslen(){    //#TSF_doc:文字数を数える。1枚[chars]ドローして1枚[N]リターン。
    string TSF_joined=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_joined.length));
    return "";
}

long TSF_Forth_len(string TSF_the){    //#TSF_doc:指定スタックの枚数を取得。(TSFAPI)。
    long TSF_len=0;
    if( TSF_the in TSF_stackD ){
        TSF_len=TSF_stackD[TSF_the].length;
    }
    return TSF_len;
}

string TSF_Forth_lenthe(){    //#TSF_doc:指定スタックの枚数を取得。1枚[the]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_Forth_len(TSF_Forth_drawthe())));
    return "";
}

string TSF_Forth_lenthis(){    //#TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_Forth_len(TSF_Forth_drawthis())));
    return "";
}

string TSF_Forth_lenthat(){    //#TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_Forth_len(TSF_Forth_drawthat())));
    return "";
}

string TSF_Forth_lenthey(){    //#TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_stackD.length));
    return "";
}

string TSF_Forth_peekF(string TSF_the){    //#指定スタックから表面カードを読込(TSFAPI)。
    string TSF_pull="";
    if( (TSF_the in TSF_stackD)&&(0<TSF_stackD[TSF_the].length) ){
        TSF_pull=TSF_stackD[TSF_the][$-1];
    }
    return TSF_pull;
}

string TSF_Forth_peekFthe(){    //#TSF_doc:指定スタックから表面カードを読込。1枚[the]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekF(TSF_Forth_drawthe()));
    return "";
}

string TSF_Forth_peekFthis(){    //#TSF_doc:実行中スタックから表面カードを読込。0枚[]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekF(TSF_Forth_drawthis()));
    return "";
}

string TSF_Forth_peekFthat(){    //#TSF_doc:積込先スタックから表面カードを読込(旧「#TSF_carbonthat」に該当)。0枚[]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekF(TSF_Forth_drawthat()));
    return "";
}

string TSF_Forth_peekFthey(){    //#TSF_doc:スタック一覧から最後尾スタック名を読込。0枚[]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_stackO.length?TSF_stackO[$-1]:"");
    return "";
}

string TSF_Forth_peekN(string TSF_the,long TSF_peek){    //#TSF_doc:指定スタックからカードを数値で読込。(TSFAPI)。
    string TSF_pull="";
    if( (TSF_the in TSF_stackD)&&(0<=TSF_peek)&&(TSF_peek<TSF_stackD[TSF_the].length) ){
        TSF_pull=TSF_stackD[TSF_the][to!size_t(TSF_peek)];
    }
    return TSF_pull;
}

string TSF_Forth_peekNthe(){    //#TSF_doc:指定スタックからカードを数値で読込。2枚[the,peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekN(TSF_Forth_drawthe(),TSF_peek));
    return "";
}

string TSF_Forth_peekNthis(){    //#TSF_doc:実行中スタックからカードを数値で読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekN(TSF_Forth_drawthis(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return "";
}

string TSF_Forth_peekNthat(){    //#TSF_doc:積込先スタックからカードを数値で読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekN(TSF_Forth_drawthat(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return "";
}

string TSF_Forth_peekNthey(){    //#TSF_doc:スタック一覧からスタック名を数値で読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Io_separatepeekN(TSF_stackO,TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return "";
}

string TSF_Forth_pokeF(string TSF_the,string TSF_poke){    //#TSF_doc:指定スタックの表面カードに上書。(TSFAPI)
    if( (TSF_the in TSF_stackD)&&(0<TSF_stackD[TSF_the].length) ){
        TSF_stackD[TSF_the][$-1]=TSF_poke;
    }
    return "";
}

string TSF_Forth_pokeFthe(){    //#TSF_doc:指定スタックから表面カードを上書。2枚[poke,the]ドロー。
    string TSF_the=TSF_Forth_drawthe();
    TSF_Forth_pokeF(TSF_the,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pokeFthis(){    //#TSF_doc:実行中スタックから表面カードを上書。1枚[poke]ドロー。
    TSF_Forth_pokeF(TSF_Forth_drawthis(),TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pokeFthat(){    //#TSF_doc:積込先スタックの表面カードを上書。1枚[poke]ドロー。
    TSF_Forth_pokeF(TSF_Forth_drawthat(),TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pokeFthey(){    //#TSF_doc:スタック一覧の最後尾スタック名を上書。1枚[poke]ドロー。
    if( (0<TSF_stackD.length) ){
        string TSF_poke=TSF_Forth_drawthe();
        string TSF_pull=TSF_stackO[$-1];
        if( TSF_pull!=TSF_poke ){
            TSF_stackO[$-1]=TSF_poke;
            string[] TSF_stackR=TSF_stackD[TSF_pull]; TSF_stackD.remove(TSF_pull);
            TSF_stackD[TSF_poke]=TSF_stackR;
        }
    }
    return "";
}

void TSF_Forth_pokeN(string TSF_the,long TSF_peek,string TSF_poke){    //#TSF_doc:指定スタックからカードを数値で読込。(TSFAPI)。
    if( (TSF_the in TSF_stackD)&&(0<=TSF_peek)&&(TSF_peek<TSF_stackD[TSF_the].length) ){
        TSF_stackD[TSF_the][to!size_t(TSF_peek)]=TSF_poke;
    }
}

string TSF_Forth_pokeNthe(){    //#TSF_doc:指定スタックからカードを数値で上書。3枚[poke,the,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_the=TSF_Forth_drawthe();
    TSF_Forth_pokeN(TSF_the,TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pokeNthis(){    //#TSF_doc:実行中スタックからカードを数値で上書。2枚[poke,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_pokeN(TSF_Forth_drawthis(),TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pokeNthat(){    //TSF_doc:積込先スタックからカードを数値で上書。2枚[poke,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_pokeN(TSF_Forth_drawthat(),TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pokeNthey(){    //#TSF_doc:スタック一覧からスタック名を数値で上書。2枚[poke,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_poke=TSF_Forth_drawthe();
    if( (0<=TSF_peek)&&(TSF_peek<TSF_stackD.length) ){
        string TSF_pull=TSF_stackO[to!size_t(TSF_peek)];
        if( TSF_pull!=TSF_poke ){
            TSF_stackO[to!size_t(TSF_peek)]=TSF_poke;
            string[] TSF_stackR=TSF_stackD[TSF_pull]; TSF_stackD.remove(TSF_pull);
            TSF_stackD[TSF_poke]=TSF_stackR;
        }
    }
    return "";
}

string TSF_Forth_pullF(string TSF_the){    //#TSF_doc:指定スタックから表面カードを引抜。(TSFAPI)
    string TSF_pull="";
    if( TSF_the in TSF_stackD ){
        TSF_pull=TSF_stackD[TSF_the][$-1]; TSF_stackD[TSF_the].popBack();
    }
    return TSF_pull;
}

string TSF_Forth_pullFthe(){    //#TSF_doc:指定スタックから表面カードを引抜。1枚[the]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_pullF(TSF_Forth_drawthe()));
    return "";
}

string TSF_Forth_pullFthis(){    //#TSF_doc:実行中スタックから表面カードを引抜。0枚[]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_pullF(TSF_Forth_drawthis()));
    return "";
}

string TSF_Forth_pullFthat(){    //#TSF_doc:積込先スタックから表面カードを引抜のみ(リターンしない)。1枚[card]ドロー。
    TSF_Forth_pullF(TSF_Forth_drawthat());
    return "";
}

string TSF_Forth_pullFthey(){    //#TSF_doc:スタック一覧から最後尾スタック名を引抜。0枚[]ドローして1枚[card]リターン。
    string TSF_pull="";
    if( TSF_stackO.length ){
        TSF_pull=TSF_stackO[$-1]; TSF_stackO.popBack();
        TSF_stackD.remove(TSF_pull);
    }
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_pull);
    return "";
}

string TSF_Forth_pullN(string TSF_the,long TSF_peek){    //#TSF_doc:指定スタックからカードを数値で引抜。(TSFAPI)
    string TSF_pull="";
    if( (TSF_the in TSF_stackD)&&(0<=TSF_peek)&&(TSF_peek<TSF_stackD[TSF_the].length) ){
        TSF_pull=TSF_stackD[TSF_the][to!size_t(TSF_peek)];
        TSF_stackD[TSF_the]=TSF_Io_separatepullN(TSF_stackD[TSF_the],TSF_peek);
    }
    return TSF_pull;
}

string TSF_Forth_pullNthe(){    //#TSF_doc:指定スタックからカードを数値で引抜。2枚[the,peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_pullN(TSF_Forth_drawthe(),TSF_peek));
    return "";
}

string TSF_Forth_pullNthis(){    //#TSF_doc:実行中スタックからカードを数値で引抜。1枚[peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_pullN(TSF_Forth_drawthis(),TSF_peek));
    return "";
}

string TSF_Forth_pullNthat(){    //#TSF_doc:積込先スタックからカードを数値で引抜。1枚[peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_pullN(TSF_Forth_drawthat(),TSF_peek));
    return "";
}

string TSF_Forth_pullNthey(){    //#TSF_doc:スタック一覧からスタック名を数値で引抜。1枚[peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_pull="";
    if( (0<=TSF_peek)&&(TSF_peek<TSF_stackD.length) ){
        TSF_pull=TSF_stackO[to!size_t(TSF_peek)];
        TSF_stackO=TSF_Io_separatepullN(TSF_stackO,TSF_peek);
        TSF_stackD.remove(TSF_pull);
    }
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_pull);
    return "";
}

void TSF_Forth_pushF(string TSF_the,string TSF_push){    //TSF_doc:指定スタックに表面カードとして差込。(TSFAPI)
    if( TSF_the in TSF_stackD ){
        TSF_stackD[TSF_the]~=[TSF_push];
    }
}

string TSF_Forth_pushFthe(){    //#TSF_doc:実行中スタックに表面カードとして差込。2枚[push,the]ドロー。
    string TSF_the=TSF_Forth_drawthe();
    TSF_Forth_pushF(TSF_the,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pushFthis(){    //#TSF_doc:実行中スタックに表面カードとして差込。1枚[push]ドロー。
    TSF_Forth_pushF(TSF_Forth_drawthat(),TSF_Forth_drawthis());
    return "";
}

string TSF_Forth_pushFthat(){    //#TSF_doc:積込先スタックに表面カードとして差込(同じカードを1枚ドロー1枚リターンなので変化無し)。
//    TSF_Forth_pushF(TSF_Forth_drawthat(),TSF_Forth_drawthat());
    return "";
}

string TSF_Forth_pushFthey(){    //#TSF_doc:スタック一覧に最後尾スタック名として差込。1枚[push]ドロー。
    string TSF_push=TSF_Forth_drawthe();
    if( TSF_push !in TSF_stackD ){
        TSF_stackO~=[TSF_push];
        TSF_stackD[TSF_push]=null;
    }
    return "";
}

void TSF_Forth_pushN(string TSF_the,long TSF_peek,string TSF_push){    //#TSF_doc:指定スタックにカードを数値で差込。(TSFAPI)
    if( TSF_push in TSF_stackD ){
        TSF_stackD[TSF_the]=TSF_Io_separatepushN(TSF_stackD[TSF_the],TSF_peek,TSF_push);
    }
}

string TSF_Forth_pushNthe(){    //#TSF_doc:指定スタックにカードを数値で差込。3枚[push,the,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_the=TSF_Forth_drawthe();
    TSF_Forth_pushN(TSF_the,TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pushNthis(){    //#TSF_doc:実行中スタックにカードを数値で差込。2枚[push,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_pushN(TSF_Forth_drawthis(),TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pushNthat(){    //#TSF_doc:積込先スタックにカードを数値で差込。2枚[push,peek]ドロー。1枚リターンの可能性。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_pushN(TSF_Forth_drawthis(),TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Forth_pushNthey(){    //#TSF_doc:スタック一覧にスタック名として差込。2枚[push,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_push=TSF_Forth_drawthe();
    if( TSF_push !in TSF_stackD ){
        TSF_stackO=TSF_Io_separatepushN(TSF_stackO,TSF_peek,TSF_push);
        TSF_stackD[TSF_push]=null;
    }
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

string[] TSF_importlist=null;
string[] TSF_Forth_importlist(...){    //#TSF_doc:モジュール一覧を管理する(TSFAPI)。
    string TSF_import="";
    if( _arguments.length>0 && _arguments[0]==typeid(string) ){
        TSF_import=va_arg!(string)(_argptr);
        if( count(TSF_importlist,TSF_import)==0 ){
            TSF_importlist~=[TSF_import];
        }
    }
    return TSF_importlist;
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
        TSF_stackD[TSF_the]=replace(stripRight(TSF_text,'\n'),"\t","\n").split("\n");
        TSF_styleD[TSF_the]=TSF_style;
    }
    else{
        if( TSF_the in TSF_stackD ){ TSF_stackD.remove(TSF_the); }
        if( TSF_the in TSF_styleD ){ TSF_styleD.remove(TSF_the); }
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
                    TSF_the=TSF_lineL[0];
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

long TSF_stackmax=256;
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
    if( TSF_stackD[TSF_the].length && TSF_the.length>0 && TSF_the in TSF_stackD ){
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

string[] TSF_Forth_mainandargvs(){    //#TSFdoc:argvsの取得。(TSFAPI)
    return TSF_mainandargvs;
}

string[] [string] TSF_Forth_stackD(){    //#TSFdoc:TSF_stackDの取得。(TSFAPI)
    return TSF_stackD;
}

string[] TSF_Forth_stackO(){    //#TSFdoc:TSF_stackOの取得。(TSFAPI)
    return TSF_stackO;
}

string [string] TSF_Forth_style(){    //#TSFdoc:TSF_styleDの取得。(TSFAPI)
    return TSF_styleD;
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
string TSF_Forth_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Forth」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Forth.log";
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
//    TSF_Forth_debug(TSF_Io_argvs(["dmd","TSF_Forth.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
