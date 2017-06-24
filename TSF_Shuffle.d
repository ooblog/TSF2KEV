#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.regex;
import std.random;

import TSF_Io;
import TSF_Forth;


Random TSF_Match_Random;
void TSF_Shuffle_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに基本的な命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Shuffle");
    string function()[string] TSF_Forth_cards=[
        "#TSF_swapBA":&TSF_Shuffle_swapBA, "#カードBA交換":&TSF_Shuffle_swapBA,
        "#TSF_swapCA":&TSF_Shuffle_swapCA, "#カードCA交換":&TSF_Shuffle_swapCA,
        "#TSF_swapCB":&TSF_Shuffle_swapCB, "#カードCB交換":&TSF_Shuffle_swapCB,
        "#TSF_swapAA":&TSF_Shuffle_swapAA, "#カードAA交換":&TSF_Shuffle_swapAA,
        "#TSF_swapCC":&TSF_Shuffle_swapCC, "#カードCC交換":&TSF_Shuffle_swapCC,
        "#TSF_peekCthe":&TSF_Shuffle_peekCthe, "#指定スタック周択読込":&TSF_Shuffle_peekCthe,
        "#TSF_peekCthis":&TSF_Shuffle_peekCthis, "#実行中スタック周択読込":&TSF_Shuffle_peekCthis,
        "#TSF_peekCthat":&TSF_Shuffle_peekCthat, "#積込先スタック周択読込":&TSF_Shuffle_peekCthat,
        "#TSF_peekCthey":&TSF_Shuffle_peekCthey, "#スタック一覧周択読込":&TSF_Shuffle_peekCthey,
        "#TSF_pokeCthe":&TSF_Shuffle_pokeCthe, "#指定スタック周択上書":&TSF_Shuffle_pokeCthe,
        "#TSF_peekMthe":&TSF_Shuffle_peekMthe, "#指定スタック囲択読込":&TSF_Shuffle_peekMthe,
        "#TSF_peekMthis":&TSF_Shuffle_peekMthis, "#実行中スタック囲択読込":&TSF_Shuffle_peekMthis,
        "#TSF_peekMthat":&TSF_Shuffle_peekMthat, "#積込先スタック囲択読込":&TSF_Shuffle_peekMthat,
        "#TSF_peekMthey":&TSF_Shuffle_peekMthey, "#スタック一覧囲択読込":&TSF_Shuffle_peekMthey,
        "#TSF_pokeMthe":&TSF_Shuffle_pokeMthe, "#指定スタック囲択上書":&TSF_Shuffle_pokeMthe,
        "#TSF_pokeMthis":&TSF_Shuffle_pokeMthis, "#実行中スタック囲択上書":&TSF_Shuffle_pokeMthis,
        "#TSF_pokeMthat":&TSF_Shuffle_pokeMthat, "#積込先スタック囲択上書":&TSF_Shuffle_pokeMthat,
        "#TSF_pokeMthey":&TSF_Shuffle_pokeMthey, "#スタック一覧囲択上書":&TSF_Shuffle_pokeMthey,
        "#TSF_pullMthe":&TSF_Shuffle_pullMthe, "#指定スタック囲択引抜":&TSF_Shuffle_pullMthe,
        "#TSF_pullMthis":&TSF_Shuffle_pullMthis, "#実行中スタック囲択引抜":&TSF_Shuffle_pullMthis,
        "#TSF_pullMthat":&TSF_Shuffle_pullMthat, "#積込先スタック囲択引抜":&TSF_Shuffle_pullMthat,
        "#TSF_pullMthey":&TSF_Shuffle_pullMthey, "#スタック一覧囲択引抜":&TSF_Shuffle_pullMthey,
        "#TSF_pushMthe":&TSF_Shuffle_pushMthe, "#指定スタック差込":&TSF_Shuffle_pushMthe,
        "#TSF_pushMthis":&TSF_Shuffle_pushMthis, "#実行中スタック差込":&TSF_Shuffle_pushMthis,
        "#TSF_pushMthat":&TSF_Shuffle_pushMthat, "#積込先スタック差込":&TSF_Shuffle_pushMthat,
        "#TSF_pushMthey":&TSF_Shuffle_pushMthey, "#スタック一覧差込":&TSF_Shuffle_pushMthey,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Shuffle_swapBA(){    //#TSFdoc:カードAとカードBを交換する。2枚[cardB,cardA]ドローして2枚[cardA,cardB]リターン。
    string TSF_swapA=TSF_Forth_drawthe();  string TSF_swapB=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);
    return "";
}

string TSF_Shuffle_swapCA(){    //#TSFdoc:カードAとカードCを交換する。3枚[cardC,cardB,cardA]ドローして3枚[cardA,cardB,cardC]リターン。
    string TSF_swapA=TSF_Forth_drawthe();  string TSF_swapB=TSF_Forth_drawthe();  string TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);
    return "";
}

string TSF_Shuffle_swapCB(){    //#TSFdoc:カードBとカードCを交換する。3枚[cardC,cardB,cardA]ドローして3枚[cardB,cardC,cardA]リターン
    string TSF_swapA=TSF_Forth_drawthe();  string TSF_swapB=TSF_Forth_drawthe();  string TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);
    return "";
}

string TSF_Shuffle_swapAA(){    //#TSFdoc:カードAをカードCの位置に沈下してカードBCを浮上。3枚[cardC,cardB,cardA]ドローして3枚[cardA,cardC,cardB]リターン。
    string TSF_swapA=TSF_Forth_drawthe();  string TSF_swapB=TSF_Forth_drawthe();  string TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);
    return "";
}

string TSF_Shuffle_swapCC(){    //#カードCをカードAの位置に浮上してカードBCを沈下。3枚[cardC,cardB,cardA]ドローして3枚[cardB,cardA,cardC]リターン。
    string TSF_swapA=TSF_Forth_drawthe();  string TSF_swapB=TSF_Forth_drawthe();  string TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);
    return "";
}


long[] TSF_Shuffle_cardsFNCMVA(string TSF_the,long TSF_peek,string TSF_seek,char TSF_FNCMVAQIRHL){    //#TSFdoc:peek,poke,pull,pushの共通部品。(TSFAPI)
    long[] TSF_Plist=[];
    long TSF_cardsL=0;
    if( TSF_the!="" ){
        if( TSF_the in TSF_Forth_stackD() ){
            TSF_cardsL=TSF_Forth_stackD()[TSF_the].length;
            if( 0<TSF_cardsL ){
                switch( TSF_FNCMVAQIRHL ){
                    case 'F':  TSF_Plist~=[TSF_cardsL-1];   break;
                    case 'N':  if( (0<=TSF_peek)&&(TSF_peek<TSF_cardsL) ){ TSF_Plist~=[TSF_peek]; }   break;
                    case 'C':  TSF_Plist~=[to!long(TSF_peek%TSF_cardsL)];   break;
                    case 'M':  TSF_Plist~=[to!long(fmin(fmax(TSF_peek,0),TSF_cardsL-1))];   break;
                    case 'V':  if( (0<=TSF_peek)&&(TSF_peek<TSF_cardsL) ){ TSF_Plist~=[TSF_cardsL-1-TSF_peek]; }   break;
                    case 'A':  TSF_Plist~=[uniform(0,TSF_cardsL,TSF_Match_Random)];   break;
                    case 'Q':
                        foreach(size_t TSF_peekreg,string TSF_card;TSF_Forth_stackD()[TSF_the]){
                            if( TSF_seek==TSF_card ){ TSF_Plist~=[TSF_peekreg]; }
                        }
                    break;
                    case 'I':
                        foreach(size_t TSF_peekreg,string TSF_card;TSF_Forth_stackD()[TSF_the]){
                            if( count(TSF_card,TSF_seek) ){ TSF_Plist~=[TSF_peekreg]; }
                        }
                    break;
                    case 'R':
                        foreach(size_t TSF_peekreg,string TSF_card;TSF_Forth_stackD()[TSF_the]){
                            if( match(TSF_card,regex(TSF_seek,"m")) ){ TSF_Plist~=[TSF_peekreg]; }
                        }
                    break;
                    case 'H':  break;
                    case 'L':  break;
                    default:  break;
                }
            }
        }
    }
    else{
        TSF_cardsL=TSF_Forth_stackO().length;
        if( 0<TSF_cardsL ){
            switch( TSF_FNCMVAQIRHL ){
                case 'F':  TSF_Plist~=[TSF_cardsL-1];   break;
                case 'N':  if( (0<=TSF_peek)&&(TSF_peek<TSF_cardsL) ){ TSF_Plist~=[TSF_peek]; }   break;
                case 'C':  TSF_Plist~=[to!long(TSF_peek%TSF_cardsL)];   break;
                case 'M':  TSF_Plist~=[to!long(fmin(fmax(TSF_peek,0),TSF_cardsL-1))];   break;
                case 'V':  if( (0<=TSF_peek)&&(TSF_peek<TSF_cardsL) ){ TSF_Plist~=[TSF_cardsL-1-TSF_peek]; }   break;
                case 'A':  TSF_Plist~=[uniform(0,TSF_cardsL,TSF_Match_Random)];   break;
                case 'Q':
                    foreach(size_t TSF_peekreg,string TSF_card;TSF_Forth_stackD()[TSF_the]){
                        if( TSF_seek==TSF_card ){ TSF_Plist~=[TSF_peekreg]; }
                    }
                break;
                case 'I':
                    foreach(size_t TSF_peekreg,string TSF_card;TSF_Forth_stackD()[TSF_the]){
                        if( count(TSF_card,TSF_seek) ){ TSF_Plist~=[TSF_peekreg]; }
                    }
                break;
                case 'R':  break;
                    foreach(size_t TSF_peekreg,string TSF_card;TSF_Forth_stackO()){
                        if( match(TSF_card,regex(TSF_seek,"m")) ){ TSF_Plist~=[TSF_peekreg]; }
                    }
                case 'H':  break;
                case 'L':  break;
                default:  break;
            }
        }
    }
    return TSF_Plist;
}

string[] TSF_Shuffle_peek(string TSF_the,long TSF_peek,string TSF_seek,char TSF_FNCMVAQIRHL){    //#TSFdoc:peekの共通部品。(TSFAPI)
    long[] TSF_Plist=TSF_Shuffle_cardsFNCMVA(TSF_the,TSF_peek,"",TSF_FNCMVAQIRHL);
    string[] TSF_pulllist=[];
    if( TSF_the!="" ){
        foreach(long TSF_P;TSF_Plist){
            TSF_pulllist~=[TSF_Forth_stackD()[TSF_the][to!size_t(TSF_P)]];
        }
    }
    else{
        foreach(long TSF_P;TSF_Plist){
            TSF_pulllist~=[TSF_Forth_stackO()[to!size_t(TSF_P)]];
        }
    }
    return TSF_pulllist;
}

void TSF_Shuffle_poke(string TSF_the,long TSF_peek,string TSF_seek,char TSF_FNCMVAQIRHL,string TSF_poke){    //#TSFdoc:pokeの共通部品。(TSFAPI)
    long[] TSF_Plist=TSF_Shuffle_cardsFNCMVA(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL);
    string[] TSF_pulllist=[];
    if( TSF_the!="" ){
        foreach(long TSF_P;TSF_Plist){
            TSF_Forth_stackD()[TSF_the][to!size_t(TSF_P)]=TSF_poke;
        }
    }
    else{
        foreach(long TSF_P;TSF_Plist){
            TSF_Forth_stackO()[to!size_t(TSF_P)]=TSF_poke;
        }
    }
}


void TSF_Shuffle_returnFNCMVA(string[] TSF_pulllist){    //#TSFdoc:peek,pullの共通部品。FNCMVAは単独のカードを返す。(TSFAPI)
    if( TSF_pulllist.length ){
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_pulllist[0]);
    }
    else{
        TSF_Forth_return(TSF_Forth_drawthat(),"");
    }
}

void TSF_Shuffle_returnQIRH(string[] TSF_pulllist){    //#TSFdoc:peek,pullの共通部品。QIRHは複数のカードを返す。(TSFAPI)
    foreach(string TSF_card;TSF_pulllist){
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card);
    }
    TSF_Forth_return(TSF_Forth_drawthat(),to!string(TSF_pulllist.length));
}

string TSF_Shuffle_peekCthe(){    //#TSFdoc:指定スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_peek(TSF_Forth_drawthe(),TSF_peek,"",'C'));
    return "";
}

string TSF_Shuffle_peekCthis(){    //#TSFdoc:実行中スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_peek(TSF_Forth_drawthis(),TSF_peek,"",'C'));
    return "";
}

string TSF_Shuffle_peekCthat(){    //#TSFdoc:積込先スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_peek(TSF_Forth_drawthat(),TSF_peek,"",'C'));
    return "";
}

string TSF_Shuffle_peekCthey(){    //#TSFdoc:スタック一覧から周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_peek("",TSF_peek,"",'C'));
    return "";
}

string TSF_Shuffle_pokeCthe(){    //#TSFdoc:指定スタックからカードを周択で上書。3枚[poke,the,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_the=TSF_Forth_drawthe();
    TSF_Shuffle_poke(TSF_the,TSF_peek,"",'C',TSF_Forth_drawthe());
    return "";
}


string TSF_Shuffle_peekM(string TSF_the,long TSF_peek){    //#TSFdoc:指定スタックからスタック名を囲択で読込。(TSFAPI)
    string TSF_pull="";
    if( TSF_the in TSF_Forth_stackD() ){
        size_t TSF_cardsN_len=TSF_stackD[TSF_the].length;
        if( 0<TSF_cardsN_len ){
            TSF_pull=TSF_Forth_stackD()[TSF_the][to!size_t(fmax(fmin(TSF_peek,TSF_cardsN_len-1),0))];
        }
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
    if( TSF_the in TSF_Forth_stackD() ){
        size_t TSF_cardsN_len=TSF_Forth_stackD()[TSF_the].length;
        if( 0<TSF_cardsN_len ){
            TSF_Forth_stackD()[TSF_the][to!size_t(fmax(fmin(TSF_peek,TSF_cardsN_len-1),0))]=TSF_poke;
        }
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

string TSF_Shuffle_pullM(string TSF_the,long TSF_peek){    //#TSFdoc:指定スタックからカードを囲択で引抜。(TSFAPI)
    string TSF_pull="";
    if( TSF_the in TSF_Forth_stackD() ){
        size_t TSF_cardsN_len=TSF_Forth_stackD()[TSF_the].length;
        if( 0<TSF_cardsN_len ){
            TSF_pull=TSF_Forth_stackD()[TSF_the][to!size_t(fmax(fmin(TSF_peek,TSF_cardsN_len-1),0))];
            TSF_Forth_stackD()[TSF_the]=TSF_Io_separatepullN(TSF_Forth_stackD()[TSF_the],TSF_peek);
        }
    }
    return TSF_pull;
}

string TSF_Shuffle_pullMthe(){    //#TSFdoc:指定スタックからカードを囲択で引抜。2枚[the,peek]ドローして1枚[card]リターン。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_pullM(TSF_Forth_drawthe(),TSF_peek));
    return "";
}

string TSF_Shuffle_pullMthis(){    //#TSFdoc:実行中スタックからカードを囲択で引抜。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_pullM(TSF_Forth_drawthis(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return "";
}

string TSF_Shuffle_pullMthat(){    //#TSFdoc:積込先スタックからカードを囲択で引抜。2枚[pull]←[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_pullM(TSF_Forth_drawthat(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return "";
}

string TSF_Shuffle_pullMthey(){    //#TSFdoc:スタック一覧からスタック名を囲択で引抜。1枚[peek]ドローして1枚[card]リターン。
    string TSF_pull="";  size_t TSF_cardsN_len=TSF_Forth_stackO().length;
    size_t TSF_peek=to!size_t(fmax(fmin(TSF_Io_RPNzero(TSF_Forth_drawthe()),TSF_cardsN_len-1),0));
    if( 0<TSF_cardsN_len ){
        TSF_pull=TSF_Forth_stackO()[to!size_t(TSF_peek)];
        TSF_Forth_stackO(TSF_Io_separatepullN(TSF_Forth_stackO(),TSF_peek));
        TSF_Forth_stackD().remove(TSF_pull);
    }
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_pull);
    return "";
}

void TSF_Shuffle_pushM(string TSF_the,long TSF_peek,string TSF_push){    //#TSFdoc:指定スタックにカードを囲択で差込。(TSFAPI)
    if( TSF_the in TSF_Forth_stackD() ){
        size_t TSF_cardsN_len=TSF_stackD[TSF_the].length;
        TSF_Forth_stackD()[TSF_the]=TSF_Io_separatepushN(TSF_Forth_stackD()[TSF_the],to!size_t(fmax(fmin(TSF_peek,TSF_cardsN_len-1),0)),TSF_push);
    }
}

string TSF_Shuffle_pushMthe(){    //#TSFdoc:指定スタックにカードを囲択で差込。3枚[push,the,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    string TSF_the=TSF_Forth_drawthe();
    TSF_Shuffle_pushM(TSF_the,TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Shuffle_pushMthis(){    //#TSFdoc:実行中スタックにカードを囲択で差込。2枚[push,peek]ドロー。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Shuffle_pushM(TSF_Forth_drawthis(),TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Shuffle_pushMthat(){    //#TSFdoc:積込先スタックにカードを囲択で差込。2枚[push,peek]ドロー。1枚リターンの可能性。
    long TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe());
    TSF_Shuffle_pushM(TSF_Forth_drawthat(),TSF_peek,TSF_Forth_drawthe());
    return "";
}

string TSF_Shuffle_pushMthey(){    //#TSFdoc:スタック一覧にスタック名として囲択で差込。2枚[push,peek]ドロー。
    size_t TSF_cardsN_len=TSF_Forth_stackO().length;
    size_t TSF_peek=to!size_t(fmax(fmin(TSF_Io_RPNzero(TSF_Forth_drawthe()),TSF_cardsN_len-1),0));
    string TSF_push=TSF_Forth_drawthe();
    if( TSF_push !in TSF_stackD ){
        TSF_Forth_stackO(TSF_Io_separatepushN(TSF_Forth_stackO(),TSF_peek,TSF_push));
        TSF_Forth_stackD()[TSF_push]=[];
    }
    return "";
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Shuffle_Initcards];
void TSF_Shuffle_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Shuffle」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Shuffle.log";
    TSF_debug_log=TSF_Io_printlog("--- %s ---".format(__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);

    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "shuffleclone:","#TSF_this","#TSF_fin."],"\t"),'T');
    TSF_Forth_setTSF("shuffleclone:",join([
        "adverbclone:","adverb:","#TSF_clonethe","shufflestacks:","#TSF_pullFthe","#TSF_this","adverbclone:","#TSF_argvsthe","#TSF_reverseN","adverbclone:","#TSF_lenthe"," ","#TSF_sandwichN","「#[2]」「[1]」「[0]」","#TSF_join[]","#TSF_echo","shufflejump:","shufflestacks:","#TSF_lenthe","0,1,[0]U","#TSF_join[]","#TSF_RPN","#TSF_peekNthe","#TSF_this"],"\t"),'T');
    TSF_Forth_setTSF("shufflejump:",join([
        "#!exit:","shuffleclone:"],"\t"),'T');
    TSF_Forth_setTSF("verb:",join(["peek","poke","push","pull"],"\t"),'O');
    TSF_Forth_setTSF("adverb:",join(["F","N","C","M","V","A","Q","I","R","H","L"],"\t"),'O');
    TSF_Forth_setTSF("pronoun:",join(["this","that","the","they"],"\t"),'O');
    TSF_Forth_setTSF("shufflestacks:",join([
        "pushM:","pullM:","pokeM:","peekM:","pokeC:","peekC:","pushN:","pullN:","pokeN:","peekN:","pushF:","pullF:","pokeF:","peekF:"],"\t"),'T');
    TSF_Forth_setTSF("peekF:",join(["TSF_peekFthe","adverbclone:","#TSF_peekFthe"],"\t"),'O');
    TSF_Forth_setTSF("pokeF:",join(["TSF_pokeFthe","$poke","adverbclone:","#TSF_pokeFthe","$poke"],"\t"),'O');
    TSF_Forth_setTSF("pullF:",join(["TSF_pullFthe","adverbclone:","#TSF_pullFthe"],"\t"),'O');
    TSF_Forth_setTSF("pushF:",join(["TSF_pushFthe","$push","adverbclone:","#TSF_pushFthe","$push"],"\t"),'O');
    TSF_Forth_setTSF("peekN:",join(["TSF_peekNthe","adverbclone:","1","#TSF_peekNthe"],"\t"),'O');
    TSF_Forth_setTSF("pokeN:",join(["TSF_pokeNthe","$poke","adverbclone:","1","#TSF_pokeNthe","$poke"],"\t"),'O');
    TSF_Forth_setTSF("pullN:",join(["TSF_pullNthe","adverbclone:","1","#TSF_pullNthe"],"\t"),'O');
    TSF_Forth_setTSF("pushN:",join(["TSF_pushNthe","$push","adverbclone:","1","#TSF_pushNthe","$push"],"\t"),'O');
    TSF_Forth_setTSF("peekC:",join(["TSF_peekCthe","adverbclone:","2","#TSF_peekCthe"],"\t"),'O');
    TSF_Forth_setTSF("pokeC:",join(["TSF_pokeCthe","$poke","adverbclone:","2","#TSF_pokeCthe","$poke"],"\t"),'O');
    TSF_Forth_setTSF("pullC:",join(["TSF_pullCthe","adverbclone:","2","#TSF_pullCthe"],"\t"),'O');
    TSF_Forth_setTSF("pushC:",join(["TSF_pushCthe","$push","adverbclone:","2","#TSF_pushCthe","$push"],"\t"),'O');
    TSF_Forth_setTSF("peekM:",join(["TSF_peekMthe","adverbclone:","3","#TSF_peekMthe"],"\t"),'O');
    TSF_Forth_setTSF("pokeM:",join(["TSF_pokeMthe","$poke","adverbclone:","3","#TSF_pokeMthe","$poke"],"\t"),'O');
    TSF_Forth_setTSF("pullM:",join(["TSF_pullMthe","adverbclone:","3","#TSF_pullMthe"],"\t"),'O');
    TSF_Forth_setTSF("pushM:",join(["TSF_pushMthe","$push","adverbclone:","3","#TSF_pushMthe","$push"],"\t"),'O');

//    TSF_debug_log=TSF_Forth_samplerun(__FILE__,true,TSF_debug_log);
    TSF_debug_log=TSF_Forth_samplerun(__FILE__,false,TSF_debug_log);
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);


}

unittest {
    TSF_Shuffle_debug(TSF_Io_argvs(["dmd","TSF_Shuffle.d"]));
}


//#! -- Copyright (c) 2017 ooblog --
//#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
