#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import re

from TSF_Io import *
from TSF_Forth import *


def TSF_Calc_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Calc")
    TSF_Forth_cards={
        "#TSF_calc":TSF_Calc_calc, "#分数計算":TSF_Calc_calc,
        "#TSF_calcJA":TSF_Calc_calcJA, "#分数計算(日本語)":TSF_Calc_calcJA,
#    TSF_words["#TSF_calcPR"]=TSF_calc_calcPR; TSF_words["#有効桁数"]=TSF_calc_calcPR
#    TSF_words["#TSF_calcRO"]=TSF_calc_calcRO; TSF_words["#端数処理"]=TSF_calc_calcRO
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Calc_calc():    #TSFdoc:分数計算する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsQQ(TSF_Forth_drawthe()))
    return ""

def TSF_Calc_calcJA():    #TSFdoc:分数計算(日本語表記)する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsJA(TSF_Forth_drawthe()))
    return ""

TSF_Calc_opeword={"恒河沙":"恒","阿僧祇":"阿","那由他":"那","不可思議":"思","無量大数":"量","無限":"∞",
    "模糊":"模","逡巡":"逡","須臾":"須","瞬息":"瞬","弾指":"弾","刹那":"刹","六徳":"徳","虚空":"空","清浄":"清","阿頼耶":"耶","阿摩羅":"摩","涅槃寂静":"涅",
    "円周率":"π","2π":"θ","２π":"θ","ネイピア数":"ｅ","プラス":"p","マイナス":"m","絶対値":"p"}
TSF_Calc_opechar={"１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9","０":"0",
    "一":"1","二":"2","三":"3","四":"4","五":"5","六":"6","七":"7","八":"8","九":"9","〇":"0",
    "壱":"1","弐":"2","参":"3","肆":"4","伍":"5","陸":"6","漆":"7","捌":"8","玖":"9","零":"0",
    "絶":"p","負":"m","分":"_","点":".","円":".","圓":".","陌":"百","佰":"百","阡":"千","仟":"千","萬":"万","仙":"銭","秭":"𥝱",
    "＋":"+","－":"-","×":"*","÷":"/","／":"/","＼":"\\","＃":"#","％":"%","＾":"^","｜":"|","＿":"_",
    "加":"+","減":"-","乗":"*","除":"/","捨":"\\","余":"#","比":"%","税":"%","冪":"^","分":"_",
    "足":"+","引":"-","掛":"*","割":"/","和":"+","差":"-","積":"*","商":"/","足":"+","引":"-","掛":"*","割":"/",
    "π":"y","周":"Y","θ":"Y","底":"e","ｅ":"e","常":"L","進":"l","対":"E","√":"R","根":"R",
}
#TSF_calc_okusendic={"万":"","億":"","兆":"","京":"","垓":"","𥝱":"","穣":"","溝":"","溝":"","澗":"","正":"","載":"","極":"","恒":"","阿":"","那":"","思":"","量":""}
TSF_Calc_okusenman="万億兆京垓𥝱穣溝澗正載極恒阿那思量"
TSF_Calc_okusenzero=['10000'+'0'*(o*4) for o in range(len(TSF_Calc_okusenman))]
TSF_Calc_okusendic=dict(zip(list(TSF_Calc_okusenman),TSF_Calc_okusenzero))
TSF_Calc_rinmoushi="厘毛糸忽微繊沙塵埃渺漠模逡須瞬弾刹徳空清耶摩涅"
TSF_Calc_rinmouzero=['1|1000'+'0'*o for o in range(len(TSF_Calc_rinmoushi))]
TSF_Calc_rinmoudic=dict(zip(list(TSF_Calc_rinmoushi),TSF_Calc_rinmouzero))
def TSF_Calc_bracketsJA(TSF_calcQ):    #TSF_doc:分数電卓の日本語処理。(TSFAPI)
    for TSF_opewordK,TSF_opewordV in TSF_calc_opeword.items():
        TSF_calcQ=TSF_calcQ.replace(TSF_opewordK,TSF_opewordV)
    for TSF_opecharK,TSF_opecharV in TSF_calc_opechar.items():
        TSF_calcQ=TSF_calcQ.replace(TSF_opecharK,TSF_opecharV)
    TSF_calcQ=re.sub(re.compile("([0-9百十]+?)銭"),"+(\\1)/100",TSF_calcQ)
    for TSF_okusenK,TSF_okusenV in TSF_calc_okusendic.items():
        TSF_calcQ=re.sub(re.compile("".join(["([0-9千百十]+?)",TSF_okusenK])),"".join(["(\\1)*",TSF_okusenV,"+"]),TSF_calcQ)
    for TSF_rinmouK,TSF_rinmouV in TSF_Calc_rinmoudic.items():
        TSF_calcQ=re.sub(re.compile("".join(["([0-9]+?)",TSF_rinmouK])),"".join(["(\\1)*",TSF_rinmouV,"+"]),TSF_calcQ)
    TSF_calcQ=re.sub(re.compile("([0-9]+?)千"),"(\\1*1000)+",TSF_calcQ)
    TSF_calcQ=re.sub(re.compile("([0-9]+?)百"),"(\\1*100)+",TSF_calcQ)
    TSF_calcQ=re.sub(re.compile("([0-9]+?)十"),"(\\1*10)+",TSF_calcQ)
    TSF_calcQ=TSF_calcA.replace('銭',"1|100+")
    TSF_calcQ=TSF_calcA.replace('十',"10+")
    TSF_calcQ=TSF_calcA.replace('百',"100+")
    TSF_calcQ=TSF_calcA.replace('千',"1000+")
    for TSF_okusenK,TSF_okusenV in TSF_calc_okusendic.items():
        TSF_calcQ=TSF_calcQ.replace(TSF_okusenK,"".join([TSF_okusenV,"+"]))
    TSF_calcA=TSF_Calc_bracketsQQ(TSF_calcQ)
    TSF_calcF="マイナス" if TSF_calcA.startswith('m') else ""
    if "." in TSF_calcA:
        TSF_calcRN,TSF_calcRD=TSF_calcA.replace('m','').replace('p','').split('.')
        TSF_calcA=TSF_calcA.replace('.','円')
    else:
        TSF_calcRN,TSF_calcRD=TSF_calcA.replace('m','').replace('p','').split('|')
        if int(TSF_calcRD) > 0:
            TSF_calcA="".join([TSF_calcF,TSF_calc_decimalizeKNcomma(TSF_calcRD),"分の",TSF_calc_decimalizeKNcomma(TSF_calcRN)])
            TSF_calcA=TSF_calcA.replace("1分の",'')
        else:
            TSF_calcA="n|0"
        TSF_calcA=TSF_calcA.replace('恒','恒河沙').replace('阿','阿僧祇').replace('那','那由他').replace('思','不可思議').replace('量','無量大数')
    return TSF_calcA

TSF_Calc_operator=",f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><"
def TSF_Calc_bracketsQQ(TSF_calcQ):    #TSF_doc:分数電卓のmain。括弧の内側を検索。(TSFAPI)
    TSF_calcA=""; TSF_calcbracketLR,TSF_calcbracketCAP=0,0
    for TSF_calcbracketQ in TSF_calcQ:
        TSF_calcA+=TSF_calcbracketQ if TSF_calcbracketQ in TSF_Calc_operator else ""
        if TSF_calcbracketQ == '(':
            TSF_calcbracketLR+=1
        if TSF_calcbracketQ == ')':
            TSF_calcbracketLR-=1
            if TSF_calcbracketLR<TSF_calcbracketCAP:
                TSF_calcbracketCAP=TSF_calcbracketLR
    if TSF_calcbracketLR > 0:
        TSF_calcA=TSF_calcA+')'*abs(TSF_calcbracketLR)
    if TSF_calcbracketLR < 0:
        TSF_calcA='('*abs(TSF_calcbracketLR)+TSF_calcA
    TSF_calcA='('*abs(TSF_calcbracketCAP)+TSF_calcA+')'*abs(TSF_calcbracketCAP)
    TSF_calc_bracketreg=re.compile("[(](?<=[(])[^()]*(?=[)])[)]")
    while "(" in TSF_calcA:
        for TSF_calcK in re.findall(TSF_calc_bracketreg,TSF_calcA):
            TSF_calcA=TSF_calcA.replace(TSF_calcK,TSF_Calc_function(TSF_calcK))
    TSF_calcA=TSF_calcA.replace(TSF_calcA,TSF_Calc_function(TSF_calcA))
    return TSF_calcA

def TSF_Calc_function(TSF_calcQ):    #TSFdoc:分数電卓の和集合積集合およびゼロ比較演算子系。(TSFAPI)
#    TSF_calcA=TSF_Calc_addition(TSF_calcQ)
    if "," in TSF_calcQ:
         TSF_calcA=TSF_Io_RPN(TSF_calcQ)
    else:
        TSF_calcA=TSF_calcQ
#        TSF_calcA=TSF_Calc_addition(TSF_calcQ)
    return TSF_calcA


TSF_Initcalldebug=[TSF_Calc_Initcards]
def TSF_Calc_debug(TSF_sysargvs):    #TSFdoc:「TSF_Calc」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Calc.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"PPPP:\t#TSF_this\tTSF_argvs:\t#TSF_that\t#TSF_argvs\t#TSF_fin.","T")

if __name__=="__main__":
    TSF_Calc_debug(TSF_Io_argvs(["python","TSF_Calc.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
