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
        "#TSF_replacesQN":&TSF_Match_replacesQN, "#文字列群で順択置換":&TSF_Match_replacesQN,
        "#TSF_replacesQC":&TSF_Match_replacesQC, "#文字列群で周択置換":&TSF_Match_replacesQC,
        "#TSF_replacesQM":&TSF_Match_replacesQM, "#文字列群で囲択置換":&TSF_Match_replacesQM,
        "#TSF_replacesQT":&TSF_Match_replacesQT, "#同択文字列群で額択置換":&TSF_Match_replacesQT,
        "#TSF_replacesRT":&TSF_Match_replacesRT, "#含択文字列群で額択置換":&TSF_Match_replacesRT,
        "#TSF_aliasQN":&TSF_Match_aliasQN, "#同択カードを順択置換":&TSF_Match_aliasQN,
        "#TSF_replacesQSN":&TSF_Match_replacesQSN, "#同択文字列群で順択置換":&TSF_Match_replacesQSN,
        "#TSF_replacesQDN":&TSF_Match_replacesQDN, "#同択文字列で順択置換":&TSF_Match_replacesQDN,
        "#TSF_replacesQON":&TSF_Match_replacesQON, "#同択で順択置換":&TSF_Match_replacesQON,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    }
    TSF_Match_Random=Random(unpredictableSeed);
}

void TSF_Match_replace(string TSF_QIRHL,string TSF_SDO,string TSF_FNCMVA){    //#TSFdoc:replace関連の共通部品。(TSFAPI)
    string TSF_theN=TSF_Forth_drawthe();  string TSF_theO=TSF_Forth_drawthe();  string TSF_theT=TSF_Forth_drawthe();
    string TSF_Text="";  string[] TSF_cardsN=[],TSF_cardsO=[];   string[] TSF_cardsI=TSF_cardsN;
    long TSF_cardsN_len=0; long  TSF_cardsO_len=0;  string TSF_SDOpoke="";
    if( TSF_SDO=="D" || TSF_SDO=="O" ){
        TSF_cardsN=[TSF_theN];  TSF_cardsN_len=1;
        TSF_cardsO=[TSF_theO];  TSF_cardsO_len=1;
        TSF_Text=TSF_theT;  TSF_SDOpoke="D";
    }
    if( TSF_SDO=="S" || TSF_SDO=="O" ){
        TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  TSF_cardsN_len=TSF_cardsN.length;
        TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);  TSF_cardsO_len=TSF_cardsO.length;
        if( TSF_theT in TSF_Forth_stackD() ){
            TSF_Text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));  TSF_SDOpoke="S";
        }
    }
    switch( TSF_FNCMVA ){
        case "F": TSF_cardsI=null; 
            foreach(long TSF_peek;0..TSF_cardsO_len){ TSF_cardsI~=TSF_cardsN[$-1]; } break;
        case "N": TSF_cardsI=null;
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_peek<TSF_cardsN_len?TSF_cardsN[TSF_peek]:""; } break;
        case "C": TSF_cardsI=null;
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_cardsN[TSF_peek%TSF_cardsN_len]; } break;
        case "M": TSF_cardsI=null;
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_cardsN[to!size_t(fmin(TSF_peek,TSF_cardsN_len-1))]; } break;
        case "V": TSF_cardsI=null;
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_peek<TSF_cardsN_len?TSF_cardsN[$-1-TSF_peek]:""; } break;
        case "A": TSF_cardsI=null;
            foreach(string TSF_card;TSF_cardsO){ TSF_cardsI~=TSF_cardsN[uniform(0,to!size_t(TSF_cardsN_len),TSF_Match_Random)]; } break;
        default: break;
    }
    switch( TSF_QIRHL ){
        case "Q":
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_Text=TSF_Text.replace(TSF_card,TSF_cardsI[TSF_peek]); } break;
        case "R":
            foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){ TSF_Text=TSF_Text.replaceAll(regex(TSF_card),TSF_cardsI[TSF_peek]); } break;
        default: break;
    }
    switch( TSF_SDOpoke ){
        case "S":
            TSF_Forth_setTSF(TSF_theT,TSF_Text,"N"); break;
        case "D":
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_Text); break;
        default: break;
    }
}

string TSF_Match_replacesQSN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replace("Q","S","N");    return ""; }
string TSF_Match_replacesQDN(){    //#TSFdoc:stackTをカードとみなしてcardOの文字列をcardNの文字列に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    TSF_Match_replace("Q","D","N");    return ""; }
string TSF_Match_replacesQON(){    //#TSFdoc:stackTがカードかスタックか判断してON置換。不足分はゼロ文字列。3枚[T,O,N]ドロー。
    TSF_Match_replace("Q","O","N");    return ""; }


string TSF_Match_replacesQN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分はゼロ文字列。3枚[stackT,stackO,stackN]ドロー。
    string TSF_theN=TSF_Forth_drawthe();  string[] TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  size_t TSF_cardsN_len=TSF_cardsN.length;
    string TSF_theO=TSF_Forth_drawthe();  string[] TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    string TSF_theT=TSF_Forth_drawthe();
    string TSF_text="";
    if( TSF_theT in TSF_Forth_stackD() ){
        TSF_text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));
        foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){
            if( TSF_peek<TSF_cardsN_len ){
                TSF_text=TSF_text.replace(TSF_card,TSF_cardsN[TSF_peek]);
            }
        }
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N");
    }
    return "";
}

string TSF_Match_replacesQC(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分は周択。3枚[stackT,stackO,stackN]ドロー。
    string TSF_theN=TSF_Forth_drawthe();  string[] TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  size_t TSF_cardsN_len=TSF_cardsN.length;
    string TSF_theO=TSF_Forth_drawthe();  string[] TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    string TSF_theT=TSF_Forth_drawthe();
    string TSF_text="";
    if( TSF_theT in TSF_Forth_stackD() ){
        TSF_text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));
        foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){
            TSF_text=TSF_text.replace(TSF_card,TSF_cardsN[TSF_peek%TSF_cardsN_len]);
        }
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N");
    }
    return "";
}

string TSF_Match_replacesQM(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分は囲択。3枚[stackT,stackO,stackN]ドロー。
    string TSF_theN=TSF_Forth_drawthe();  string[] TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  size_t TSF_cardsN_len=TSF_cardsN.length;
    string TSF_theO=TSF_Forth_drawthe();  string[] TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    string TSF_theT=TSF_Forth_drawthe();
    string TSF_text="";
    if( TSF_theT in TSF_Forth_stackD() ){
        TSF_text=TSF_Io_ESCdecode(join(TSF_Forth_stackD()[TSF_theT],"\n"));
        foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){
            TSF_text=TSF_text.replace(TSF_card,TSF_cardsN[to!size_t(fmin(TSF_peek,TSF_cardsN_len))]);
        }
        TSF_Forth_setTSF(TSF_theT,TSF_text,"N");
    }
    return "";
}

string TSF_Match_replacesQT(){    //#TSFdoc:stackTをテキストとみなしてcardOの文字列をcardNの文字列に置換。3枚[stackT,cardO,cardN]ドロー。1枚リターン[cardN]。
    string TSF_theN=TSF_Forth_drawthe();
    string TSF_theO=TSF_Forth_drawthe();
    string TSF_theT=TSF_Forth_drawthe();
    TSF_theT=TSF_theT.replace(TSF_theO,TSF_theN);
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_theT);
    return "";
}

string TSF_Match_replacesRT(){    //#TSFdoc:stackTをテキストとみなしてcardOの文字列をcardNの文字列に置換。3枚[stackT,cardO,cardN]ドロー。1枚リターン[cardN]。
    string TSF_theN=TSF_Forth_drawthe();
    string TSF_theO=TSF_Forth_drawthe();
    string TSF_theT=TSF_Forth_drawthe();
    TSF_theT=TSF_theT.replace(TSF_theO,TSF_theN);
    TSF_theT=replaceAll(TSF_theT,regex(TSF_theO),TSF_theN);
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_theT);
    return "";
}

string TSF_Match_aliasQN(){    //#TSFdoc:stackTをテキストとみなしてstackOの文字列群をstackNの文字列群に置換。不足分は囲択。3枚[cardT,stackO,stackN]ドロー。1枚リターン[cardN]。
    string TSF_theN=TSF_Forth_drawthe();  string[] TSF_cardsN=TSF_Forth_stackD().get(TSF_theN,[]);  size_t TSF_cardsN_len=TSF_cardsN.length;
    string TSF_theO=TSF_Forth_drawthe();  string[] TSF_cardsO=TSF_Forth_stackD().get(TSF_theO,[]);
    string TSF_cardT=TSF_Forth_drawthe();
    foreach(size_t TSF_peek,string TSF_card;TSF_cardsO){
        if( TSF_cardT==TSF_card ){
            TSF_cardT=TSF_cardsN[to!size_t(fmin(TSF_peek,TSF_cardsN_len))];
        }
    }
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_cardT);
    return "";
}


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
