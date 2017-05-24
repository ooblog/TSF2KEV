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
        "#TSF_replacesQSN":&TSF_Match_replacesQSN, "#同択文字列群で順択置換":&TSF_Match_replacesQSN,
        "#TSF_replacesQDN":&TSF_Match_replacesQDN, "#同択文字列で順択置換":&TSF_Match_replacesQDN,
        "#TSF_replacesQON":&TSF_Match_replacesQON, "#同択で順択置換":&TSF_Match_replacesQON,
        "#TSF_aliasQSN":&TSF_Match_aliasQSN, "#同択文字列群で順択代入":&TSF_Match_aliasQSN,
        "#TSF_aliasQDN":&TSF_Match_aliasQDN, "#同択文字列で順択代入":&TSF_Match_aliasQDN,
        "#TSF_aliasQON":&TSF_Match_aliasQON, "#同択で順択代入":&TSF_Match_aliasQON,
        "#TSF_docsQ":&TSF_Match_docsQ, "#同択編集":&TSF_Match_docsQ,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    }
    TSF_Match_Random=Random(unpredictableSeed);
}

void TSF_Match_replaceRAD(char TSF_QIRHL,char TSF_SDO,char TSF_FNCMVA,char TSF_RAD){    //#TSFdoc:replace,aliassの共通部品。(TSFAPI)
    string TSF_theN=TSF_Forth_drawthe();  string TSF_theO=TSF_Forth_drawthe();  string TSF_theT=TSF_Forth_drawthe();
    string TSF_Text="";  string[] TSF_cardsN=[],TSF_cardsO=[];   string[] TSF_cardsI=TSF_cardsN;  string TSF_cardsT="";
    long TSF_cardsN_len=0; long  TSF_cardsO_len=0;  char TSF_SDOpoke=' ';
    if( TSF_RAD== 'D' ){
        TSF_cardsN=[TSF_theN];  TSF_cardsN_len=1;
        TSF_cardsO=[TSF_theO];  TSF_cardsO_len=1;
        if( TSF_theT in TSF_Forth_stackD() ){
            TSF_Text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));  TSF_SDOpoke='S';
        }
    }
    else{
        if( TSF_SDO=='D' || TSF_SDO=='O' ){
            TSF_cardsN=[TSF_theN];  TSF_cardsN_len=1;
            TSF_cardsO=[TSF_theO];  TSF_cardsO_len=1;
            TSF_Text=TSF_theT;  TSF_SDOpoke='D';
        }
        if( TSF_SDO=='S' || TSF_SDO=='O' ){
            TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=TSF_cardsN.length;
            TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);  TSF_cardsO_len=TSF_cardsO.length;
            if( TSF_theT in TSF_Forth_stackD() ){
                TSF_Text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));  TSF_SDOpoke='S';
            }
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
    switch( TSF_RAD ){
        case 'R':
            switch( TSF_QIRHL ){
                case 'Q':
                    foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_Text=TSF_Text.replace(TSF_card,TSF_cardsI[TSF_peek]); } break;
                case 'R':
                    foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_Text=TSF_Text.replaceAll(regex(TSF_card),TSF_cardsI[TSF_peek]); } break;
                default: break;
            }
        break;
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
            TSF_Forth_setTSF(TSF_theT,TSF_Text,'N'); break;
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

string TSF_Match_aliasQSN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列群で代入。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q','S','N','A');    return ""; }
string TSF_Match_aliasQDN(){    //#TSFdoc:stackTをカードとみなしてcardOの文字列と同択できたらstackNの文字列で代入。不足分はゼロ文字列。3枚[cardT,cardO,cardN]ドロー。
    TSF_Match_replaceRAD('Q','D','N','A');    return ""; }
string TSF_Match_aliasQON(){    //#TSFdoc:stackTがカードかスタックか判断してON置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。
    TSF_Match_replaceRAD('Q','O','N','A');    return ""; }

string TSF_Match_docsQ(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群と同択できたらstackNの文字列またはスタックで編集。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replaceRAD('Q',' ',' ','D');    return ""; }


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Forth_Initcards];
void TSF_Match_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Match」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Match.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}

unittest {
    TSF_Match_debug(TSF_Io_argvs(["dmd","TSF_Match.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
