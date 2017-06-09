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
        "#TSF_diffminute":TSF_Time_diffminute, "#時差設定":TSF_Time_diffminute,
        "#TSF_overhour":TSF_Time_overhour, "#徹夜設定":TSF_Time_overhour,
        "#TSF_nowdaytime":TSF_Time_nowdaytime, "#日時取得":TSF_Time_nowdaytime,
        "#TSF_calender":TSF_Time_calender, "#日時置換":TSF_Time_calender,
#        "#TSF_timer":TSF_Time_timer, "#タイマー置換":TSF_Time_timer,
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    TSF_Time_setdaytime(0,30)
    return TSF_cardsD,TSF_cardsO

def TSF_Time_diffminute():    #TSFdoc:時差を設定する。現在時刻も更新。1枚[diffminute]ドロー。
    TSF_Time_setdaytime(TSF_diffminute=TSF_Io_RPNzero(TSF_Forth_drawthat()))
    return ""

def TSF_Time_overhour():    #TSFdoc:徹夜時間を設定する。現在時刻も更新。1枚[overhour]ドロー。
    TSF_Time_setdaytime(TSF_overhour=TSF_Io_RPNzero(TSF_Forth_drawthat()))
    return ""

def TSF_Time_nowdaytime():    #TSFdoc:徹現在時刻の更新のみ。0枚[]ドロー。
    TSF_Time_setdaytime()
    return ""

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

TSF_earlier_diffminute,TSF_earlier_overhour=0,30
TSF_earlier_now=datetime.datetime.now()
TSF_diff_now=TSF_earlier_now+datetime.timedelta(minutes=0)
TSF_meridian_EnumLen=7+2+5+2+4+1;  (
    TSF_meridian_Year,TSF_meridian_Yearlower,TSF_meridian_YearZodiac,TSF_meridian_Yeardays,TSF_meridian_YearIso,TSF_meridian_WeekNumberYearIso,TSF_meridian_WeekDayIso,
    TSF_meridian_Month,TSF_meridian_Monthdays,
    TSF_meridian_Daymonth,TSF_meridian_Dayyear,TSF_meridian_Weekday,TSF_meridian_Weeknumber,TSF_meridian_yearWeeksiso,
    TSF_meridian_Hour,TSF_meridian_HourAP,
    TSF_meridian_miNute,TSF_meridian_Second,TSF_meridian_miLlisecond,TSF_meridian_micRosecond,
    TSF_meridian_Beat,
)=range(0,TSF_meridian_EnumLen)
TSF_meridian_Enum=[0]*TSF_meridian_EnumLen;
TSF_allnight_EnumLen=7+3+6+3;  (
    TSF_allnight_Year,TSF_allnight_Yearlower,TSF_allnight_YearZodiac,TSF_allnight_Yeardays,TSF_allnight_YearIso,TSF_allnight_WeekNumberYearIso,TSF_allnight_WeekDayIso,
    TSF_allnight_Month,TSF_allnight_Monthdays,TSF_allnight_carryMonth,
    TSF_allnight_Daymonth,TSF_allnight_Dayyear,TSF_allnight_Weekday,TSF_allnight_Weeknumber,TSF_allnight_yearWeeksiso,TSF_allnight_carryDay,
    TSF_allnight_Hour,TSF_allnight_HourAPO,TSF_allnight_carryHour,
)=range(0,TSF_allnight_EnumLen)
TSF_allnight_Enum=[0]*TSF_allnight_EnumLen;
TSF_counter_Counter=0
TSF_Time_EnumNULL=None

#TSF_time_Counter,TSF_time_randOm=0,random.random()

def TSF_Time_setdaytime(TSF_diffminute=None,TSF_overhour=None):    #TSF_doc:時刻の初期化。実際の年月日等の取得は遅延処理で行う。
    global TSF_earlier_diffminute,TSF_earlier_overhour
    TSF_earlier_diffminute=TSF_diffminute if TSF_diffminute != None else TSF_earlier_diffminute
    TSF_earlier_overhour=min(max(TSF_overhour,24),48) if TSF_overhour != None else TSF_earlier_overhour
    global TSF_earlier_now,TSF_diff_now,TSF_meridian_Enum,TSF_allnight_Enum
    TSF_earlier_now=datetime.datetime.now()
    TSF_diff_now=TSF_earlier_now+datetime.timedelta(minutes=TSF_earlier_diffminute)
    TSF_meridian_Enum=[TSF_Time_EnumNULL for Enum in range(TSF_meridian_EnumLen)]
    TSF_allnight_Enum=[TSF_Time_EnumNULL for Enum in range(TSF_allnight_EnumLen)]
    global TSF_counter_Counter
    TSF_counter_Counter=0

def TSF_Time_meridian_Year():    #TSF_doc:現在時刻年4桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_Year]=TSF_meridian_Enum[TSF_meridian_Year] if TSF_meridian_Enum[TSF_meridian_Year] != TSF_Time_EnumNULL else TSF_diff_now.year
    return TSF_meridian_Enum[TSF_meridian_Year]
def TSF_Time_meridian_Yearlower():    #TSF_doc:現在時刻年下2桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_Yearlower]=TSF_meridian_Enum[TSF_meridian_Yearlower] if TSF_meridian_Enum[TSF_meridian_Yearlower] != TSF_Time_EnumNULL else TSF_diff_now.year%100
    return TSF_meridian_Enum[TSF_meridian_Yearlower]

def TSF_Time_meridian_Month():    #TSF_doc:現在時刻月2桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_Month]=TSF_meridian_Enum[TSF_meridian_Month] if TSF_meridian_Enum[TSF_meridian_Month] != TSF_Time_EnumNULL else TSF_diff_now.month
    return TSF_meridian_Enum[TSF_meridian_Month]

def TSF_Time_meridian_Weekday():    #TSF_doc:現在時刻曜1桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_Weekday]=TSF_meridian_Enum[TSF_meridian_Weekday] if TSF_meridian_Enum[TSF_meridian_Weekday] != TSF_Time_EnumNULL else TSF_diff_now.weekday()
    return TSF_meridian_Enum[TSF_meridian_Weekday]

def TSF_Time_meridian_Daymonth():    #TSF_doc:現在時刻日2桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_Daymonth]=TSF_meridian_Enum[TSF_meridian_Daymonth] if TSF_meridian_Enum[TSF_meridian_Daymonth] != TSF_Time_EnumNULL else TSF_diff_now.day
    return TSF_meridian_Enum[TSF_meridian_Daymonth]

def TSF_Time_meridian_Hour():    #TSF_doc:現在時刻時2桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_Hour]=TSF_meridian_Enum[TSF_meridian_Hour] if TSF_meridian_Enum[TSF_meridian_Hour] != TSF_Time_EnumNULL else TSF_diff_now.hour
    return TSF_meridian_Enum[TSF_meridian_Hour]

def TSF_Time_meridian_miNute():    #TSF_doc:現在時刻分2桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_miNute]=TSF_meridian_Enum[TSF_meridian_miNute] if TSF_meridian_Enum[TSF_meridian_miNute] != TSF_Time_EnumNULL else TSF_diff_now.minute
    return TSF_meridian_Enum[TSF_meridian_miNute]

def TSF_Time_meridian_Second():    #TSF_doc:現在時刻秒2桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_Second]=TSF_meridian_Enum[TSF_meridian_Second] if TSF_meridian_Enum[TSF_meridian_Second] != TSF_Time_EnumNULL else TSF_diff_now.second
    return TSF_meridian_Enum[TSF_meridian_Second]

def TSF_Time_meridian_miLlisecond():    #TSF_doc:現在時刻ミリ秒3桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_miLlisecond]=TSF_meridian_Enum[TSF_meridian_miLlisecond] if TSF_meridian_Enum[TSF_meridian_miLlisecond] != TSF_Time_EnumNULL else TSF_Time_meridian_micRosecond()//1000
    return TSF_meridian_Enum[TSF_meridian_miLlisecond]

def TSF_Time_meridian_micRosecond():    #TSF_doc:現在時刻マイクロ秒6桁の遅延処理。(TSFAPI)
    global TSF_meridian_Enum
    TSF_meridian_Enum[TSF_meridian_micRosecond]=TSF_meridian_Enum[TSF_meridian_micRosecond] if TSF_meridian_Enum[TSF_meridian_micRosecond] != TSF_Time_EnumNULL else TSF_diff_now.microsecond
    return TSF_meridian_Enum[TSF_meridian_micRosecond]

def TSF_Time_Counter(TSF_Time_countset=None):    #TSF_doc:カウンターを数える。(TSFAPI)
    global TSF_counter_Counter
    TSF_counter_Counter+=1
    if TSF_Time_countset != None:  TSF_counter_Counter=TSF_Time_countset
    return TSF_counter_Counter

def TSF_Time_getdaytime(TSF_daytimeformat="@4y@0m@0dm@wdec@0h@0n@0s"):    #TSFdoc:現在日時で上書き。(TSFAPI)
    TSF_tfList=TSF_daytimeformat.split("@@")
    for TSF_tfcount,TSF_tf in enumerate(TSF_tfList):
        TSF_tf=TSF_tf if not "@000y" in TSF_tf else TSF_tf.replace("@000y","{0:0>4}".format(TSF_Time_meridian_Year()))
        TSF_tf=TSF_tf if not "@___y" in TSF_tf else TSF_tf.replace("@___y","{0: >4}".format(TSF_Time_meridian_Year()))
        TSF_tf=TSF_tf if not "@4y" in TSF_tf else TSF_tf.replace("@4y","{0}".format(TSF_Time_meridian_Year()))
        TSF_tf=TSF_tf if not "@0y" in TSF_tf else TSF_tf.replace("@0y","{0:0>2}".format(TSF_Time_meridian_Yearlower()))
        TSF_tf=TSF_tf if not "@_y" in TSF_tf else TSF_tf.replace("@_y","{0: >2}".format(TSF_Time_meridian_Yearlower()))
        TSF_tf=TSF_tf if not "@2y" in TSF_tf else TSF_tf.replace("@2y","{0}".format(TSF_Time_meridian_Yearlower()))

        TSF_tf=TSF_tf if not "@0m" in TSF_tf else TSF_tf.replace("@0m","{0:0>2}".format(TSF_Time_meridian_Month()))
        TSF_tf=TSF_tf if not "@_m" in TSF_tf else TSF_tf.replace("@_m","{0: >2}".format(TSF_Time_meridian_Month()))
        TSF_tf=TSF_tf if not "@m" in TSF_tf else TSF_tf.replace("@m",str(TSF_Time_meridian_Month()))

        TSF_tf=TSF_tf if not "@wdj" in TSF_tf else TSF_tf.replace("@wdj",TSF_weekdayjp[TSF_Time_meridian_Weekday()])
        TSF_tf=TSF_tf if not "@wdec" in TSF_tf else TSF_tf.replace("@wdec",TSF_weekdayenc[TSF_Time_meridian_Weekday()])
        TSF_tf=TSF_tf if not "@wd" in TSF_tf else TSF_tf.replace("@wd",str(TSF_Time_meridian_Weekday()))

        TSF_tf=TSF_tf if not "@0dm" in TSF_tf else TSF_tf.replace("@0dm","{0:0>2}".format(TSF_Time_meridian_Daymonth()))
        TSF_tf=TSF_tf if not "@_dm" in TSF_tf else TSF_tf.replace("@_dm","{0: >2}".format(TSF_Time_meridian_Daymonth()))
        TSF_tf=TSF_tf if not "@dm" in TSF_tf else TSF_tf.replace("@dm",str(TSF_Time_meridian_Daymonth()))

        TSF_tf=TSF_tf if not "@0h" in TSF_tf else TSF_tf.replace("@0h","{0:0>2}".format(TSF_Time_meridian_Hour()))
        TSF_tf=TSF_tf if not "@_h" in TSF_tf else TSF_tf.replace("@_h","{0: >2}".format(TSF_Time_meridian_Hour()))
        TSF_tf=TSF_tf if not "@h" in TSF_tf else TSF_tf.replace("@h",str(TSF_Time_meridian_Hour()))

        TSF_tf=TSF_tf if not "@0n" in TSF_tf else TSF_tf.replace("@0n","{0:0>2}".format(TSF_Time_meridian_miNute()))
        TSF_tf=TSF_tf if not "@_n" in TSF_tf else TSF_tf.replace("@_n","{0: >2}".format(TSF_Time_meridian_miNute()))
        TSF_tf=TSF_tf if not "@n" in TSF_tf else TSF_tf.replace("@n",str(TSF_Time_meridian_miNute()))

        TSF_tf=TSF_tf if not "@0s" in TSF_tf else TSF_tf.replace("@0s","{0:0>2}".format(TSF_Time_meridian_Second()))
        TSF_tf=TSF_tf if not "@_s" in TSF_tf else TSF_tf.replace("@_s","{0: >2}".format(TSF_Time_meridian_Second()))
        TSF_tf=TSF_tf if not "@s" in TSF_tf else TSF_tf.replace("@s",str(TSF_Time_meridian_Second()))

        TSF_tf=TSF_tf if not "@00ls" in TSF_tf else TSF_tf.replace("@00ls","{0:0>3}".format(TSF_Time_meridian_miLlisecond()))
        TSF_tf=TSF_tf if not "@__ls" in TSF_tf else TSF_tf.replace("@__ls","{0: >3}".format(TSF_Time_meridian_miLlisecond()))
        TSF_tf=TSF_tf if not "@ls" in TSF_tf else TSF_tf.replace("@ls",str(TSF_Time_meridian_miLlisecond()))

        TSF_tf=TSF_tf if not "@00000rs" in TSF_tf else TSF_tf.replace("@00000rs","{0:0>6}".format(TSF_Time_meridian_micRosecond()))
        TSF_tf=TSF_tf if not "@_____rs" in TSF_tf else TSF_tf.replace("@_____rs","{0: >6}".format(TSF_Time_meridian_micRosecond()))
        TSF_tf=TSF_tf if not "@rs" in TSF_tf else TSF_tf.replace("@rs",str(TSF_Time_meridian_micRosecond()))

        TSF_tf=TSF_tf if not "@T" in TSF_tf else TSF_tf.replace("@T","\t")
        TSF_tf=TSF_tf if not "@E" in TSF_tf else TSF_tf.replace("@E","\n")
        TSF_tf=TSF_tf if not "@Z" in TSF_tf else TSF_tf.replace("@Z","")

        TSF_tf=TSF_tf if not "@000c" in TSF_tf else TSF_tf.replace("@000c","{0:0>4}".format(TSF_Time_Counter()))
        TSF_tf=TSF_tf if not "@___c" in TSF_tf else TSF_tf.replace("@___c","{0: >4}".format(TSF_Time_Counter()))
        TSF_tf=TSF_tf if not "@00c" in TSF_tf else TSF_tf.replace("@00c","{0:0>3}".format(TSF_Time_Counter()))
        TSF_tf=TSF_tf if not "@__c" in TSF_tf else TSF_tf.replace("@__c","{0: >3}".format(TSF_Time_Counter()))
        TSF_tf=TSF_tf if not "@0c" in TSF_tf else TSF_tf.replace("@0c","{0:0>2}".format(TSF_Time_Counter()))
        TSF_tf=TSF_tf if not "@_c" in TSF_tf else TSF_tf.replace("@_c","{0: >2}".format(TSF_Time_Counter()))
        TSF_tf=TSF_tf if not "@c" in TSF_tf else TSF_tf.replace("@c",str(TSF_Time_Counter()))
        TSF_tf=TSF_tf if not "@-1C" in TSF_tf else TSF_tf.replace("@-1C",str(TSF_Time_Counter(-1)))
        TSF_tf=TSF_tf if not "@0C" in TSF_tf else TSF_tf.replace("@0C",str(TSF_Time_Counter(0)))
        TSF_tf=TSF_tf if not "@C" in TSF_tf else TSF_tf.replace("@C",str(TSF_Time_Counter(TSF_Time_Counter())))

        TSF_tfList[TSF_tfcount]=TSF_tf
    TSF_daytimeformat="@".join(TSF_tfList)
    return TSF_daytimeformat


TSF_Initcalldebug=[TSF_Time_Initcards]
def TSF_Time_debug(TSF_sysargvs):    #TSFdoc:「TSF_Time」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Time.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "timecount:","#TSF_this","#TSF_fin."]),'T')
    TSF_Forth_setTSF("timecount:","\t".join([
        "timejump:","timesample:","#TSF_lenthe","0,1,[0]U","#TSF_join[]","#TSF_RPN","#TSF_peekNthe","#TSF_this","timecount:","#TSF_this"]),'T')
    TSF_Forth_setTSF("timejump:","\t".join([
        "#exit","timepop:"]),'T')
    TSF_Forth_setTSF("timepop:","\t".join([
        "timesample:","0","#TSF_pullNthe","#TSF_peekFthat","#TSF_calender","「[1]」→「[0]」","#TSF_join[]","#TSF_echo"]),'T')
    TSF_Forth_setTSF("timesample:","\t".join([
        "{$TSFcounter@c}",
        "@000y,@___y,@4y,@0y,@_y,@2y",
        "@0m,@_m,@m",
        "@wd",
        "@0dm,@_dm,@dm",
        "@0h,@_h,@h",
        "@0m,@_m,@m",
        "@0s,@_s,@s",
        "@00ls,@__ls,@ls",
        "@00000rs,@_____rs,@rs",
        "@4y@0m@0dm@wdec@0h@0n@0s",
        "{$TSFcounter@c}",
        ]),'N')
    TSF_debug_log=TSF_Forth_samplerun(__file__,True,TSF_debug_log)
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)

if __name__=="__main__":
    TSF_Time_debug(TSF_Io_argvs(["python","TSF_Time.py"]))


#! -- Copyright (c) 2017 ooblog --
#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
