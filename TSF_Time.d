#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.datetime;

import TSF_Io;
import TSF_Forth;


void TSF_Time_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Time");
    string function()[string] TSF_Forth_cards=[
        "#TSF_calender":&TSF_Time_calender, "#日時等に置換":&TSF_Time_calender,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
}

string TSF_Time_calender(){    //#TSFdoc:現在日時の取得。1枚[daytimeformat]ドローして1枚[daytime]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Time_getdaytime(TSF_Forth_drawthe()));
    return "";
}

string[] TSF_zodiacjp=["鼠","牛","虎","兎","龍","蛇","馬","羊","猿","鶏","犬","猪"];
string[] TSF_zodiacch=["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"];
long[] TSF_maxmonth=    [31,31,28,31,30,31,30,31,31,30,31,30,31,31];
long[] TSF_maxmonthleep=[31,31,29,31,30,31,30,31,31,30,31,30,31,31];
string[] TSF_monthjp=   [  "師走",  "睦月",   "如月",  "弥生",   "卯月",  "皐月","水無月",  "文月",  "葉月",  "長月",   "神無月",   "霜月",  "師走",  "睦月"];
string[] TSF_month_jp=  ["　師走","　睦月", "　如月","　弥生", "　卯月","　皐月","水無月","　文月","　葉月","　長月",   "神無月", "　霜月","　師走","　睦月"];
string[] TSF_monthjpiz= [  "師走",  "睦月",   "如月",  "弥生",   "卯月",  "皐月","水無月",  "文月",  "葉月",  "長月",   "神有月",   "霜月",  "師走",  "睦月"];
string[] TSF_month_jpiz=["　師走","　睦月", "　如月","　弥生", "　卯月","　皐月","水無月","　文月","　葉月","　長月",   "神有月", "　霜月","　師走","　睦月"];
string[] TSF_monthenl=  ["December","January","February","March","April", "May",   "June",  "July",  "August","September","October","November","December","January"];
string[] TSF_monthens=  ["Dec",     "Jan",    "Feb",     "Mar",  "Apr"  , "May",   "Jun",   "Jul",   "Aug",   "Sep",      "Oct",    "Nov",     "Dec",      "Jan"];
string[] TSF_monthenc=  ["D",       "J",      "F",          "C", "A",     "M",       "N",     "L",    "U",    "S",        "O",      "N"       ,"D",        "J"];
string[] TSF_monthenh=  ["December","January","February","marCh","April", "May",   "juNe",  "juLy",  "aUgust","September","October","November","December","January"];
string[] TSF_weekdayjp =["月",    "火",     "水",       "木",      "金",    "土",     "日"];
string[] TSF_weekdayens=["Mon",   "Tue",    "Wed"      ,"Thu",     "Fri",   "Sat",     "Sun"];
string[] TSF_weekdayenl=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
string[] TSF_weekdayenc=["M",     "T",      "W",           "R",    "F",     "S",        "U"];
string[] TSF_weekdayenh=["Monday","Tuesday","Wednesday","thuRsday","Friday","Saturday","sUnday"];
string[] TSF_ampmjp= ["午前","午後","徹夜"];
string[] TSF_ampmenl=["am",  "pm", "an"];
string[] TSF_ampmenu=["AM",  "PM", "AN"];

long TSF_earlier_diffminute=0,TSF_earlier_overhour=24;
SysTime TSF_earlier_now;
//auto TSF_meridian_now;
//auto TSF_allnight_now;
enum TSF_meridian {
    Year,Yearlower,YearZodiac,Yeardays,YearIso,WeekNumberYearIso,WeekDayIso,
    Month,Monthdays,
    EnumLen,};
long[TSF_meridian.EnumLen] TSF_meridian_Enum;
enum TSF_allnight {
    Year,Yearlower,YearZodiac,Yeardays,YearIso,WeekNumberYearIso,WeekDayIso,
    Month,Monthdays,carryMonth,
    EnumLen,};
long[TSF_allnight.EnumLen] TSF_allnight_Enum;

void TSF_time_setdaytime(...){
    TSF_earlier_now=Clock.currTime();
}

string TSF_Time_getdaytime(string TSF_daytimeformat){    //#TSFdoc:現在日時で上書き。(TSFAPI)
    return TSF_daytimeformat;
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Time_Initcards];
void TSF_Time_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Time」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Time.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
}

unittest {
//    TSF_Time_debug(TSF_Io_argvs(["dmd","TSF_Time.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE


