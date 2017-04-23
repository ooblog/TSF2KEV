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
    TSF_Forth_return(TSF_calc_bracketsQQ(TSF_Forth_drawthe()));
    return ""

def TSF_Calc_calcJA():    #TSFdoc:分数計算(日本語表記)する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_calc_bracketsJA(TSF_Forth_drawthe()));
    return ""

#TSF_calc_opewide="f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><" \
#                "銭十百千万億兆京垓𥝱穣溝澗正載極恒阿那思量" \
#                "１２３４５６７８９０｜．" "絶負分点円圓" "一二三四五六七八九〇" "壱弐参肆伍陸漆捌玖零" \
#                "＋－×÷／＼＃％" "加減乗除比税" "足引掛割" "和差積商" "陌阡萬仙秭" \
#                "（）()｛｝{}［］[]「」｢｣『』Σ但※列Π囲～〜値とを約倍" \
#                "乗常進対√根π周θｅ底∞無桁"
#TSF_calc_opehalf="f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><" \
#                "銭十百千万億兆京垓𥝱穣溝澗正載極恒阿那思量" \
#                "1234567890|." "!m$..." "1234567890" "1234567890" \
#                "+-*//\\#%" "+-*/%%" "+-*/" "+-*/" "百千万銭𥝱" \
#                "()()()()()()()()()MMMMP~~~k&&Gg" \
#                "^LlERRyyYeennf"
def TSF_calc_bracketsJA(TSF_calcQ):    #TSF_doc:分数電卓のmain。括弧の内側を検索(TSFAPI)。
    #TSF_calcQ=TSF_calcQ
    TSF_calcA=TSF_calc_bracketsQQ(TSF_calcQ)
    #TSF_calcA=TSF_calcA
    return TSF_calcA

#TSF_calc_opewide="f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><" \
#                "銭十百千万億兆京垓𥝱穣溝澗正載極恒阿那思量" \
#                "１２３４５６７８９０｜．" "絶負分点円圓" "一二三四五六七八九〇" "壱弐参肆伍陸漆捌玖零" \
#                "＋－×÷／＼＃％" "加減乗除比税" "足引掛割" "和差積商" "陌阡萬仙秭" \
#                "（）()｛｝{}［］[]「」｢｣『』Σ但※列Π囲～〜値とを約倍" \
#                "乗常進対√根π周θｅ底∞無桁"
#TSF_calc_opehalf="f1234567890.pm!|$ELRSsCcTtyYen+-*/\\#%(MPFZzOoUuN~k)&GglAa^><" \
#                "銭十百千万億兆京垓𥝱穣溝澗正載極恒阿那思量" \
#                "1234567890|." "!m$..." "1234567890" "1234567890" \
#                "+-*//\\#%" "+-*/%%" "+-*/" "+-*/" "百千万銭𥝱" \
#                "()()()()()()()()()MMMMP~~~k&&Gg" \
#                "^LlERRyyYeennf"
def TSF_calc_bracketsQQ(TSF_calcQ):    #TSF_doc:分数電卓のmain。括弧の内側を検索(TSFAPI)。
    TSF_calcA="n|0"
#    TSF_calcA=TSF_calc_bracketsbalance(TSF_calcQ);
#    for TSF_calcbracketQ in TSF_calcQ:
#        TSF_calcA+=TSF_calc_operator.get(TSF_calcbracketQ,'')
#        if TSF_calcbracketQ == '(':
#            TSF_calcbracketLR+=1
#        if TSF_calcbracketQ == ')':
#            TSF_calcbracketLR-=1
#            if TSF_calcbracketLR<TSF_calcbracketCAP:
#                TSF_calcbracketCAP=TSF_calcbracketLR
#    if TSF_calcbracketLR > 0:
#        TSF_calcA=TSF_calcA+')'*abs(TSF_calcbracketLR)
#    if TSF_calcbracketLR < 0:
#        TSF_calcA='('*abs(TSF_calcbracketLR)+TSF_calcA

    TSF_calc_bracketreg=re.compile("[(](?<=[(])[^()]*(?=[)])[)]")
#    while "(" in TSF_calcA:
#        for TSF_calcK in re.findall(TSF_calc_bracketreg,TSF_calcA):
#            TSF_calcA=TSF_calcA.replace(TSF_calcK,TSF_calc_function(TSF_calcK,TSF_calcQQ))
#    TSF_calcA=TSF_calcA.replace(TSF_calcA,TSF_calc_function(TSF_calcA,TSF_calcQQ))
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
