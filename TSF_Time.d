#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.datetime;
import core.time;
import std.typecons;
import core.vararg;

import TSF_Io;
import TSF_Forth;


void TSF_Time_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Time");
    string function()[string] TSF_Forth_cards=[
        "#TSF_calender":&TSF_Time_calender, "#日時等に置換":&TSF_Time_calender,
        "#TSF_overhour":&TSF_Time_overhour, "#徹夜設定":&TSF_Time_overhour,
        "#TSF_nowdaytime":&TSF_Time_nowdaytime, "#日時取得":&TSF_Time_nowdaytime,
        "#TSF_calender":&TSF_Time_calender, "#日時置換":&TSF_Time_calender,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    }
    TSF_Time_setdaytime(0,30);
}

string TSF_Time_diffminute(){    //#TSFdoc:時差を設定する。現在時刻も更新。1枚[diffminute]ドロー。
    TSF_Time_setdaytime(TSF_Io_RPNzero(TSF_Forth_drawthat()));
    return "";
}

string TSF_Time_overhour(){    //#TSFdoc:徹夜時間を設定する。現在時刻も更新。1枚[overhour]ドロー。
    TSF_Time_setdaytime(TSF_Io_RPNzero(TSF_Forth_drawthat()));
    return "";
}

string TSF_Time_nowdaytime(){    //#TSFdoc:徹現在時刻の更新のみ。0枚[]ドロー。
    TSF_Time_setdaytime();
    return "";
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

long TSF_earlier_diffminute=0,TSF_earlier_overhour=30;
SysTime TSF_earlier_now,TSF_diff_now;
enum TSF_meridian {
    Year,Yearlower,YearZodiac,Yeardays,YearIso,WeekNumberYearIso,WeekDayIso,
    Month,Monthdays,
    Daymonth,Dayyear,Weekday,Weeknumber,yearWeeksiso,
    Hour,HourAP,
    EnumLen,};
long[TSF_meridian.EnumLen] TSF_meridian_Enum;
enum TSF_allnight {
    Year,Yearlower,YearZodiac,Yeardays,YearIso,WeekNumberYearIso,WeekDayIso,
    Month,Monthdays,carryMonth,
    Daymonth,Dayyear,Weekday,Weeknumber,yearWeeksiso,carryDay,
    Hour,HourAPO,carryHour,
    miNute,Second,miLlisecond,micRosecond,
    Beat,
    EnumLen,};
long[TSF_allnight.EnumLen] TSF_allnight_Enum;
long TSF_Time_EnumNULL=-10000;

void TSF_Time_setdaytime(...){
    if( _arguments.length>0 && _arguments[0]==typeid(long) ){
        TSF_earlier_diffminute=va_arg!(long)(_argptr);
    }
    if( _arguments.length>1 && _arguments[1]==typeid(long) ){
        long TSF_overhour=va_arg!(long)(_argptr);
        TSF_earlier_overhour=to!long(fmin(fmax(TSF_overhour,24),48));
    }
    TSF_earlier_now=Clock.currTime();
    TSF_diff_now=TSF_earlier_now+dur!"minutes"(TSF_earlier_diffminute);
    foreach(long Enum;0..TSF_meridian.EnumLen){ TSF_meridian_Enum[to!size_t(Enum)]=TSF_Time_EnumNULL; }
    foreach(long Enum;0..TSF_allnight.EnumLen){ TSF_allnight_Enum[to!size_t(Enum)]=TSF_Time_EnumNULL; }
}

long TSF_Time_meridian_Year(){    //#TSF_doc:現在時刻年4桁の遅延処理。(TSFAPI)
    TSF_meridian_Enum[TSF_meridian.Year]=TSF_meridian_Enum[TSF_meridian.Year]!=TSF_Time_EnumNULL?TSF_meridian_Enum[TSF_meridian.Year]:TSF_earlier_now.year;
    return TSF_meridian_Enum[TSF_meridian.Year];
}

long TSF_Time_meridian_Yearlower(){    //#TSF_doc:現在時刻年下2桁の遅延処理。(TSFAPI)
    TSF_meridian_Enum[TSF_meridian.Yearlower]=TSF_meridian_Enum[TSF_meridian.Yearlower]!=TSF_Time_EnumNULL?TSF_meridian_Enum[TSF_meridian.Yearlower]:TSF_earlier_now.year%100;
    return TSF_meridian_Enum[TSF_meridian.Yearlower];
}

long TSF_Time_meridian_Month(){    //#TSF_doc:現在時刻月2桁の遅延処理。(TSFAPI)
    TSF_meridian_Enum[TSF_meridian.Month]=TSF_meridian_Enum[TSF_meridian.Month]!=TSF_Time_EnumNULL?TSF_meridian_Enum[TSF_meridian.Month]:TSF_earlier_now.month;
    return TSF_meridian_Enum[TSF_meridian.Month];
}

string TSF_Time_getdaytime(string daytimeformat){    //#TSFdoc:現在日時で上書き。(TSFAPI)
    string TSF_daytimeformat=daytimeformat;
    string[] TSF_tfList=TSF_daytimeformat.split("@@");
    foreach(size_t TSF_tfcount,string TSF_tf;TSF_tfList){
        TSF_tf=!count(TSF_tf,"@000y")?TSF_tf:TSF_tf.replace("@000y","%04d".format(TSF_Time_meridian_Year()));
        TSF_tf=!count(TSF_tf,"@___y")?TSF_tf:TSF_tf.replace("@___y","%4d".format(TSF_Time_meridian_Year()));
        TSF_tf=!count(TSF_tf,"@4y")?TSF_tf:TSF_tf.replace("@4y","%d".format(TSF_Time_meridian_Year()));
        TSF_tf=!count(TSF_tf,"@0y")?TSF_tf:TSF_tf.replace("@0y","%02d".format(TSF_Time_meridian_Yearlower()));
        TSF_tf=!count(TSF_tf,"@_y")?TSF_tf:TSF_tf.replace("@_y","%2d".format(TSF_Time_meridian_Yearlower()));
        TSF_tf=!count(TSF_tf,"@2y")?TSF_tf:TSF_tf.replace("@2y","%d".format(TSF_Time_meridian_Yearlower()));

        TSF_tf=!count(TSF_tf,"@0m")?TSF_tf:TSF_tf.replace("@0m","%02d".format(TSF_Time_meridian_Month()));
        TSF_tf=!count(TSF_tf,"@_m")?TSF_tf:TSF_tf.replace("@_m","%2d".format(TSF_Time_meridian_Month()));
        TSF_tf=!count(TSF_tf,"@m")?TSF_tf:TSF_tf.replace("@m","%d".format(TSF_Time_meridian_Month()));

        TSF_tf=!count(TSF_tf,"@T")?TSF_tf:TSF_tf.replace("@T","\t");
        TSF_tf=!count(TSF_tf,"@E")?TSF_tf:TSF_tf.replace("@E","\n");
        TSF_tf=!count(TSF_tf,"@Z")?TSF_tf:TSF_tf.replace("@Z","");
        TSF_tfList[TSF_tfcount]=TSF_tf;
    }
    TSF_daytimeformat=join(TSF_tfList,"@");
    return TSF_daytimeformat;
}


void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Time_Initcards];
void TSF_Time_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Time」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Time.log";
    TSF_debug_log=TSF_Io_printlog("--- %s ---".format(__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "#TSF_nowdaytime","timecount:","#TSF_this","#TSF_fin."],"\t"),'T');
    TSF_Forth_setTSF("timecount:",join([
        "timejump:","timesample:","#TSF_lenthe","0,1,[0]U","#TSF_join[]","#TSF_RPN","#TSF_peekNthe","#TSF_this","timecount:","#TSF_this"],"\t"),'T');
    TSF_Forth_setTSF("timejump:",join([
        "#exit","timepop:"],"\t"),'T');
    TSF_Forth_setTSF("timepop:",join([
        "timesample:","0","#TSF_pullNthe","#TSF_peekFthat","#TSF_calender","「[1]」→「[0]」","#TSF_join[]","#TSF_echo"],"\t"),'T');
    TSF_Forth_setTSF("timesample:",join([
        "@000y","@___y","@4y","@0y","@_y","@2y",
        "@0m","@_m","@m",
        ],"\t"),'N');
    TSF_debug_log=TSF_Forth_samplerun(__FILE__,true,TSF_debug_log);
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);
}

unittest {
    TSF_Time_debug(TSF_Io_argvs(["dmd","TSF_Time.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE


