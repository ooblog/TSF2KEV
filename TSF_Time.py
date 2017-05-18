#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import datetime
import random

from TSF_Io import *
from TSF_Forth import *


def TSF_Time_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Time")
    TSF_Forth_cards={
        "#TSF_calender":TSF_Time_calender, "#日時置換":TSF_Time_calender,
#    TSF_words["#TSF_diffminute"]=TSF_time_diffminute; TSF_words["#時差設定"]=TSF_time_diffminute
#    TSF_words["#TSF_overhour"]=TSF_time_overhour; TSF_words["#徹夜時間設定"]=TSF_time_overhour
#    TSF_words["#TSF_nowset"]=TSF_time_nowset; TSF_words["#現在時刻更新"]=TSF_time_nowset
#        "#TSF_timer":TSF_Time_timer, "#タイマー置換":TSF_Time_timer,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Time_calender():    #TSFdoc:現在日時の取得。1枚[daytimeformat]ドローして1枚[daytime]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Time_getdaytime(TSF_Forth_drawthe()));
    return ""

TSF_zodiacjp=("鼠","牛","虎","兎","龍","蛇","馬","羊","猿","鶏","犬","猪")
TSF_zodiacch=("子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥")
TSF_maxmonth=    (31,31,28,31,30,31,30,31,31,30,31,30,31,31)
TSF_maxmonthleep=(31,31,29,31,30,31,30,31,31,30,31,30,31,31)
TSF_monthjp=   (  "師走",  "睦月",   "如月",  "弥生",   "卯月",  "皐月","水無月",  "文月",  "葉月",  "長月",   "神無月",   "霜月",  "師走",  "睦月")
TSF_month_jp=  ("　師走","　睦月", "　如月","　弥生", "　卯月","　皐月","水無月","　文月","　葉月","　長月",   "神無月", "　霜月","　師走","　睦月")
TSF_monthjpiz= (  "師走",  "睦月",   "如月",  "弥生",   "卯月",  "皐月","水無月",  "文月",  "葉月",  "長月",   "神有月",   "霜月",  "師走",  "睦月")
TSF_month_jpiz=("　師走","　睦月", "　如月","　弥生", "　卯月","　皐月","水無月","　文月","　葉月","　長月",   "神有月", "　霜月","　師走","　睦月")
TSF_monthenl=  ("December","January","February","March","April", "May",   "June",  "July",  "August","September","October","November","December","January")
TSF_monthens=  ("Dec",     "Jan",    "Feb",     "Mar",  "Apr"  , "May",   "Jun",   "Jul",   "Aug",   "Sep",      "Oct",    "Nov",     "Dec",      "Jan")
TSF_monthenc=  ("D",       "J",      "F",          "C", "A",     "M",       "N",     "L",    "U",    "S",        "O",      "N"       ,"D",        "J")
TSF_monthenh=  ("December","January","February","marCh","April", "May",   "juNe",  "juLy",  "aUgust","September","October","November","December","January")
TSF_weekdayjp =("月",    "火",     "水",       "木",      "金",    "土",     "日")
TSF_weekdayens=("Mon",   "Tue",    "Wed"      ,"Thu",     "Fri",   "Sat",     "Sun")
TSF_weekdayenl=("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
TSF_weekdayenc=("M",     "T",      "W",           "R",    "F",     "S",        "U")
TSF_weekdayenh=("Monday","Tuesday","Wednesday","thuRsday","Friday","Saturday","sUnday")
TSF_ampmjp= ("午前","午後","徹夜")
TSF_ampmenl=("am",  "pm", "an")
TSF_ampmenu=("AM",  "PM", "AN")


TSF_earlier_diffminute,TSF_earlier_overhour=0,24
TSF_earlier_now,TSF_meridian_now,TSF_allnight_now=datetime.datetime.now(),datetime.datetime.now(),datetime.datetime.now()
TSF_meridian_EnumLen=7+2;  (
    TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiac,TSF_meridian_Yeardays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso,
    TSF_meridian_Month,TSF_meridian_Monthdays,
)=range(0,TSF_meridian_EnumLen)
TSF_meridian_Enum=[0]*TSF_meridian_EnumLen;
TSF_allnight_EnumLen=7+3;  (
    TSF_allnight_Year,TSF_allnight_Yearlower,TSF_allnight_YearZodiac,TSF_allnight_Yeardays,TSF_allnight_YearIso,TSF_allnight_WeekNumberYearIso,TSF_allnight_WeekDayIso,
    TSF_allnight_Month,TSF_allnight_Monthdays,TSF_allnight_carryMonth,
)=range(0,TSF_allnight_EnumLen)
TSF_allnight_Enum=[0]*TSF_allnight_EnumLen;

TSF_TimeEnum=0
#TSF_earlier_diffminute,TSF_earlier_overhour=0,24
#TSF_earlier_now,TSF_meridian_now,TSF_allnight_now=None,None,None
#TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiac,TSF_meridian_Yeardays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso=None,None,None,None,None,None,None
#TSF_allnight_Year,TSF_allnight_Yearlower,TSF_allnight_YearZodiac,TSF_allnight_Yeardays,TSF_allnight_YearIso,TSF_allnight_WeekNumberYearIso,TSF_allnight_WeekDayIso,TSF_allnight_carryYear=None,None,None,None,None,None,None,None
#TSF_meridian_Month,TSF_meridian_Monthdays=None,None
#TSF_allnight_Month,TSF_allnight_Monthdays,TSF_allnight_carryMonth=None,None,None
#TSF_meridian_Daymonth,TSF_meridian_Dayyear,TSF_meridian_Weekday,TSF_meridian_Weeknumber,TSF_meridian_yearWeeksiso=None,None,None,None,None
#TSF_allnight_Daymonth,TSF_allnight_Dayyear,TSF_allnight_Weekday,TSF_allnight_Weeknumber,TSF_allnight_yearWeeksiso,TSF_allnight_carryDay=None,None,None,None,None,None
#TSF_meridian_Hour,TSF_meridian_HourAP=None,None
#TSF_allnight_Hour,TSF_allnight_HourAPO,TSF_allnight_carryHour=None,None,None
#TSF_meridian_miNute,TSF_meridian_Second,TSF_meridian_miLlisecond,TSF_meridian_micRosecond=None,None,None,None
#TSF_meridian_Beat=None
#TSF_time_Counter,TSF_time_randOm=0,random.random()

def TSF_time_setdaytime(TSF_diffminute=0,TSF_overhour=30):    #TSF_doc:時刻の初期化。実際の年月日等の取得は遅延処理で行う。
    TSF_earlier_now=datetime.datetime.now()

def TSF_Time_getdaytime(TSF_daytimeformat):    #TSFdoc:現在日時で上書き。(TSFAPI)
    global TSF_time_Counter
    if TSF_earlier_now == None or TSF_diffminute != None or TSF_overhour != None:
        TSF_time_setdaytime(TSF_diffminute if TSF_diffminute != None else TSF_earlier_diffminute,TSF_overhour if TSF_overhour != None else TSF_earlier_overhour)
    return TSF_daytimeformat


TSF_Initcalldebug=[TSF_Time_Initcards]
def TSF_Time_debug(TSF_sysargvs):    #TSFdoc:「TSF_Time」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Time.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)

if __name__=="__main__":
    TSF_Time_debug(TSF_Io_argvs(["python","TSF_Time.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
