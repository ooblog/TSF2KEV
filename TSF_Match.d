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
void TSF_Match_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Match");
    string function()[string] TSF_Forth_cards=[
        "#!TSF_replacesQSN":&TSF_Match_replacesQSN, "#同択文字列群で順択置換":&TSF_Match_replacesQSN,
        "#!TSF_replacesQDN":&TSF_Match_replacesQDN, "#同択文字列で順択置換":&TSF_Match_replacesQDN,
        "#!TSF_replacesQON":&TSF_Match_replacesQON, "#同択で順択置換":&TSF_Match_replacesQON,
        "#!TSF_replacesRSN":&TSF_Match_replacesRSN, "#規択文字列群で順択置換":&TSF_Match_replacesRSN,
        "#!TSF_replacesaRDN":&TSF_Match_replacesRDN, "#規択文字列で順択置換":&TSF_Match_replacesRDN,
        "#!TSF_replacesRON":&TSF_Match_replacesRON, "#規択で順択置換":&TSF_Match_replacesRON,
        "#!TSF_aliasQSN":&TSF_Match_aliasQSN, "#同択文字列群で順択代入":&TSF_Match_aliasQSN,
        "#!TSF_aliasQDN":&TSF_Match_aliasQDN, "#同択文字列で順択代入":&TSF_Match_aliasQDN,
        "#!TSF_aliasQON":&TSF_Match_aliasQON, "#同択で順択代入":&TSF_Match_aliasQON,
        "#!TSF_casesQSN":&TSF_Match_casesQSN, "#例外あり同択文字列群で表択代入":&TSF_Match_casesQSN,
        "#!TSF_casesQDN":&TSF_Match_casesQDN, "#例外あり同択文字列で表択代入":&TSF_Match_casesQDN,
        "#!TSF_casesQON":&TSF_Match_casesQON, "#例外あり同択で表択代入":&TSF_Match_casesQON,
        "#!TSF_docsQ":&TSF_Match_docsQ, "#同択編集":&TSF_Match_docsQ,
        "#!TSF_Match":&TSF_Match_Match, "#置換代入系統一式":&TSF_Match_Match,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    }
    TSF_Match_Random=Random(unpredictableSeed);
}

void TSF_Match_replaceRAD(char TSF_QIRHL,char TSF_SDO,char TSF_FNCMVA,char TSF_RACD){    //#TSFdoc:replace,aliassの共通部品。(TSFAPI)
    string TSF_theN=TSF_Forth_drawthe();  string TSF_theO=TSF_Forth_drawthe();  string TSF_theT=TSF_Forth_drawthe();
    string TSF_Text="";  string[] TSF_cardsN=[],TSF_cardsO=[];   string[] TSF_cardsI=TSF_cardsN;  string TSF_cardsT="";
    long TSF_cardsN_len=0; long  TSF_cardsO_len=0;  char TSF_SDOpoke=' ';
    if( TSF_RACD== 'D' ){
        TSF_cardsN=[TSF_theN];  TSF_cardsN_len=1;
        TSF_cardsO=[TSF_theO];  TSF_cardsO_len=1;
        if( TSF_theT in TSF_Forth_stackD() ){
            TSF_Text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));  TSF_SDOpoke='S';
        }
    }
    else{
        switch( TSF_SDO ){
            case 'D':
                TSF_cardsN=[TSF_theN];  TSF_cardsN_len=1;
                TSF_cardsO=[TSF_theO];  TSF_cardsO_len=1;
                TSF_Text=TSF_theT;  TSF_SDOpoke='D';
                break;
            case 'O':
                TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[TSF_theN]);  TSF_cardsN_len=TSF_cardsN.length;
                TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[TSF_theO]);  TSF_cardsO_len=TSF_cardsO.length;
                if( TSF_theT in TSF_Forth_stackD() ){
                    TSF_Text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));  TSF_SDOpoke='S';
                }
                else{
                    TSF_Text=TSF_theT;  TSF_SDOpoke='D';
                }
                break;
            case 'S':
                TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=TSF_cardsN.length;
                TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);  TSF_cardsO_len=TSF_cardsO.length;
                if( TSF_theT in TSF_Forth_stackD() ){
                    TSF_Text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));  TSF_SDOpoke='S';
                }
                break;
            default: break;
        }
    }
    switch( TSF_FNCMVA ){
        case 'F': TSF_cardsI=null; 
            foreach(long TSF_peek;0..TSF_cardsO_len){ TSF_cardsI~=TSF_cardsN[$-1]; } break;
        case 'N': TSF_cardsI=null;
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_peek<TSF_cardsN_len?TSF_cardsN[TSF_peek]:""; } break;
        case 'C': TSF_cardsI=null;
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_cardsN[TSF_peek%TSF_cardsN_len]; } break;
        case 'M': TSF_cardsI=null;
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_cardsN[to!size_t(fmin(TSF_peek,TSF_cardsN_len-1))]; } break;
        case 'V': TSF_cardsI=null;
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_peek<TSF_cardsN_len?TSF_cardsN[$-1-TSF_peek]:""; } break;
        case 'A': TSF_cardsI=null;
            foreach(string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_cardsN[uniform(0,to!size_t(TSF_cardsN_len),TSF_Match_Random)]; } break;
        default: break;
    }
    switch( TSF_RACD ){
        case 'R':
            switch( TSF_QIRHL ){
                case 'Q':
                    foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_Text=TSF_Text.replace(TSF_card,TSF_cardsI[TSF_peek]); } break;
                case 'R':
                    foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_Text=TSF_Text.replaceAll(regex(TSF_card,"m"),TSF_cardsI[TSF_peek]); } break;
                default: break;
            }
        break;
        case 'C': TSF_cardsT=(TSF_cardsN.length==0)?"":TSF_cardsN[$-1]; goto case;
        case 'A':
            switch( TSF_QIRHL ){
                case 'Q':
                    foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){
                         if( TSF_Text==TSF_card ){ TSF_cardsT=TSF_cardsI[TSF_peek]; }
                    } break;
                case 'I':
                    foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){
                         if( count(TSF_Text,TSF_card) ){ TSF_cardsT=TSF_cardsI[TSF_peek]; }
                    } break;
                default: break;
            }
            TSF_Text=TSF_cardsT;
        break;
        case 'D':
            switch( TSF_QIRHL ){
                case 'Q':
                    TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[TSF_theN]);
                    TSF_Text=TSF_Text.replace(TSF_theO,TSF_Io_ESCdecode(join(TSF_cardsN,"\n")));
                break;
                default: break;
            }
        break;
        default: break;
    }
    switch( TSF_SDOpoke ){
        case 'S':
            TSF_Forth_setTSF(TSF_theT,TSF_Text,'@'); break;
        case 'D':
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_Text); break;
        default: break;
    }
}

string TSF_Match_replacesQSN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q','S','N','R');    return ""; }
string TSF_Match_replacesQDN(){    //#TSFdoc:stackTをカードとみなしてcardOの文字列をcardNの文字列に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q','D','N','R');    return ""; }
string TSF_Match_replacesQON(){    //#TSFdoc:stackTがカードかスタックか判断してON置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。
    TSF_Match_replaceRAD('Q','O','N','R');    return ""; }

string TSF_Match_replacesRSN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に正規表現で置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('R','S','N','R');    return ""; }
string TSF_Match_replacesRDN(){    //#TSFdoc:stackTをカードとみなしてcardOの文字列をcardNの文字列に正規表現で置換。不足分はゼロ文字列。3枚[cardT,cardO,cardN]ドロー。1枚[cardN]リターン。
    TSF_Match_replaceRAD('R','D','N','R');    return ""; }
string TSF_Match_replacesRON(){    //#TSFdoc:stackTがカードかスタックか判断してONを正規表現で置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。Tがカードなら1枚[cardN]リターン。
    TSF_Match_replaceRAD('R','O','N','R');    return ""; }

string TSF_Match_aliasQSN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列群で代入。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q','S','N','A');    return ""; }
string TSF_Match_aliasQDN(){    //#TSFdoc:stackTをカードとみなしてcardOの文字列と同択できたらstackNの文字列で代入。不足分はゼロ文字列。3枚[cardT,cardO,cardN]ドロー。
    TSF_Match_replaceRAD('Q','D','N','A');    return ""; }
string TSF_Match_aliasQON(){    //#TSFdoc:stackTがカードかスタックか判断してON置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。
    TSF_Match_replaceRAD('Q','O','N','A');    return ""; }

string TSF_Match_casesQSN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列群で代入。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q','S','N','C');    return ""; }
string TSF_Match_casesQDN(){    //#TSFdoc:stackTをカードとみなしてcardOの文字列と同択できたらstackNの文字列で代入。不足分はゼロ文字列。3枚[cardT,cardO,cardN]ドロー。1枚[cardN]リターン。
    TSF_Match_replaceRAD('Q','D','N','C');    return ""; }
string TSF_Match_casesQON(){    //#TSFdoc:stackTがカードかスタックか判断してON置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。Tがカードなら1枚[cardN]リターン。
    TSF_Match_replaceRAD('Q','O','N','C');    return ""; }

string TSF_Match_docsQ(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列またはスタックで編集。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q',' ',' ','D');    return ""; }


string TSF_Match_Match(){    //#TSFdoc:5*3*6*4=360もの関数を用意するのはしんどいので、replaceRADに渡すパラメータ用の関数を作成。4枚[stackT,stackO,stackN,macro]ドロー。
    string TSF_MP=TSF_Forth_drawthe();    TSF_MP~="    ";
    TSF_Match_replaceRAD(TSF_MP[0],TSF_MP[1],TSF_MP[2],TSF_MP[3]);
    return "";
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
void TSF_Match_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Match」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Match.log";
    TSF_debug_log=TSF_Io_printlog("--- %s ---".format(__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}

unittest {
//   TSF_Match_debug(TSF_Io_argvs(["dmd","TSF_Match.d"]));
}


//#! -- Copyright (c) 2017 ooblog --
//#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
