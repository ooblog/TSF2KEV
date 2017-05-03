#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

import re
import math
import decimal

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

def TSF_Calc_calcsquarebrackets(TSF_calcQ,TSF_calcBL,TSF_calcBR):     #TSFdoc:スタックからpeek(読込)ショートカット角括弧で連結する。(TSFAPI)
    TSF_calcA=TSF_calcQ
    for TSF_stacksK,TSF_stacksV in TSF_Forth_stackD().items():
        TSF_calcK="".join([TSF_calcBL,TSF_stacksK])
        if TSF_calcK in TSF_calcA:
            for TSF_stackC,TSF_stackQ in enumerate(TSF_stacksV):
                TSF_calcK="".join([TSF_calcBL,TSF_stacksK,str(TSF_stackC),TSF_calcBR])
                if TSF_calcK in TSF_calcA:
                    TSF_calcA=TSF_calcA.replace(TSF_calcK,TSF_stackQ)
    return TSF_calcA

def TSF_Calc_calc():    #TSFdoc:分数計算する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsQQ(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")))
    return ""

def TSF_Calc_calcJA():    #TSFdoc:分数計算(日本語表記)する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsJA(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")))
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

def TSF_Calc_bracketsQQ(TSF_calcQ):    #TSF_doc:分数電卓のmain。括弧の内側を検索。(TSFAPI)
    TSF_calcA=TSF_calcQ; TSF_calcBLR,TSF_calcBCAP=0,0
    TSF_calc_bracketreg=re.compile("[(](?<=[(])[^()]*(?=[)])[)]")
    while "(" in TSF_calcA or ")" in TSF_calcA:
        TSF_calcBLR,TSF_calcBCAP=0,0
        for TSF_calcB in TSF_calcA:
            if TSF_calcB == '(':
                TSF_calcBLR+=1
            if TSF_calcB == ')':
                TSF_calcBLR-=1
                if TSF_calcBLR<TSF_calcBCAP:
                    TSF_calcbracketCAP=TSF_calcBLR
        if TSF_calcBLR > 0:
            TSF_calcA=TSF_calcA+')'*abs(TSF_calcBLR)
        if TSF_calcBLR < 0:
            TSF_calcA='('*abs(TSF_calcBLR)+TSF_calcA
        TSF_calcA='('*abs(TSF_calcBCAP)+TSF_calcA+')'*abs(TSF_calcBCAP)
        for TSF_calcK in re.findall(TSF_calc_bracketreg,TSF_calcA):
            TSF_calcA=TSF_calcA.replace(TSF_calcK,TSF_Calc_function(TSF_calcK))
    TSF_calcA=TSF_calcA.replace(TSF_calcA,TSF_Calc_function(TSF_calcA))
    if len(TSF_calcA):
        if not TSF_calcA[-1] in ":":
            if not TSF_calcA[0] in "n0pm":
                TSF_calcA=TSF_calcA.replace("-","m") if TSF_calcA.startswith('-') else "".join(["p",TSF_calcA])
    return TSF_calcA


def TSF_Calc_FLR(TSF_calcQ,TSF_calcO):    #三項演算子と「~」を用いてタプルに分割。(TSFAPI)
    TSF_calcQsplits=TSF_calcQ.split(TSF_calcO)
    TSF_calcF=TSF_calcQsplits[0]
    if "~" in TSF_calcQsplits[-1]:
        TSF_calcLRsplits=TSF_calcQsplits[-1].split('~')
        TSF_calcL=TSF_calcLRsplits[0];  TSF_calcR=TSF_calcLRsplits[-1];
    else:
        TSF_calcL=TSF_calcQsplits[-1];  TSF_calcR=TSF_calcQsplits[-1];
    return TSF_Io_RPN(TSF_Calc_addition(TSF_calcF)).replace('p','').replace('m','-'),TSF_calcL,TSF_calcR

#ZzOoUuNMPAtan2atan#SinCosTansctREL#^Gg
def TSF_Calc_function(TSF_calcQ):    #TSFdoc:分数電卓の和集合積集合およびゼロ比較演算子系。(TSFAPI)
    TSF_calcK=TSF_calcQ.lstrip("(").rstrip(")")
    if "," in TSF_calcK:
        TSF_calcA=TSF_Io_RPN(TSF_calcK)
    elif "Z~" in TSF_calcK:
       TSF_calcF,TSF_calcL,TSF_calcR=TSF_Calc_FLR(TSF_calcK,"Z~")
       TSF_calcA="n|0" if TSF_calcF == "n|0" else TSF_Calc_addition(TSF_calcL if float(TSF_calcF) == 0 else TSF_calcR)
    elif "z~" in TSF_calcK:
       TSF_calcF,TSF_calcL,TSF_calcR=TSF_Calc_FLR(TSF_calcK,"z~")
       TSF_calcA="n|0" if TSF_calcF == "n|0" else TSF_Calc_addition(TSF_calcL if float(TSF_calcF) != 0 else TSF_calcR)
    elif "O" in TSF_calcK:
       TSF_calcF,TSF_calcL,TSF_calcR=TSF_Calc_FLR(TSF_calcK,"O~")
       TSF_calcA="n|0" if TSF_calcF == "n|0" else TSF_Calc_addition(TSF_calcL if float(TSF_calcF) >= 0 else TSF_calcR)
    elif "o~" in TSF_calcK:
       TSF_calcF,TSF_calcL,TSF_calcR=TSF_Calc_FLR(TSF_calcK,"o~")
       TSF_calcA="n|0" if TSF_calcF == "n|0" else TSF_Calc_addition(TSF_calcL if float(TSF_calcF) > 0 else TSF_calcR)
    elif "U~" in TSF_calcK:
       TSF_calcF,TSF_calcL,TSF_calcR=TSF_Calc_FLR(TSF_calcK,"U~")
       TSF_calcA="n|0" if TSF_calcF == "n|0" else TSF_Calc_addition(TSF_calcL if float(TSF_calcF) <= 0 else TSF_calcR)
    elif "u~" in TSF_calcK:
        TSF_calcF,TSF_calcL,TSF_calcR=TSF_Calc_FLR(TSF_calcK,"u~")
        TSF_calcA="n|0" if TSF_calcF == "n|0" else TSF_Calc_addition(TSF_calcL if float(TSF_calcF) < 0 else TSF_calcR)
    elif "N~" in TSF_calcK:
        TSF_calcF,TSF_calcL,TSF_calcR=TSF_Calc_FLR(TSF_calcK,"N~")
        TSF_calcA=TSF_Calc_addition(TSF_calcL if TSF_calcF == "n|0" else TSF_calcR)
    else:
        TSF_calcA=TSF_Calc_addition(TSF_calcK)
    return TSF_calcA

def TSF_Calc_addition(TSF_calcQ):    #TSF_doc:分数電卓の足し算引き算・消費税計算等。(TSFAPI)
    TSF_calcA=TSF_calcQ
    if len(TSF_calcA) > 0 and TSF_calcA.endswith(':'):
        return TSF_calcA
    TSF_calcLN,TSF_calcLD=decimal.Decimal(0),decimal.Decimal(1)
    TSF_calcQreplace=TSF_calcQ.replace('+','\t+').replace('-','\t-').replace('%','\t%')
    TSF_calcQsplits=TSF_calcQreplace.strip('\t').split('\t')
    for TSF_calcQmulti in TSF_calcQsplits:
        TSF_calcO=" "
        for TSF_calcOpe in "+-%":
            TSF_calcO=TSF_calcOpe if TSF_calcOpe in TSF_calcQmulti else TSF_calcO
        TSF_calcRND=TSF_Calc_multiplication(TSF_calcQmulti.lstrip("+-%")).split('|')
        TSF_calcRN,TSF_calcRD=TSF_calcRND[0],TSF_calcRND[-1];
        if decimal.Decimal(TSF_calcRD) == 0:
            TSF_calcA="n|0"
            TSF_calcLN,TSF_calcLD=decimal.Decimal(0),decimal.Decimal(0)
            break
        elif TSF_calcO == "%":
            TSF_calcPN=TSF_calcLN*decimal.Decimal(TSF_calcRN)
            TSF_calcPD=TSF_calcLD*decimal.Decimal(TSF_calcRD)*decimal.Decimal(100)
            TSF_calcG=decimal.Decimal(TSF_Calc_LCM(str(TSF_calcLD),str(TSF_calcPD)))
            TSF_calcLN=TSF_calcLN*TSF_calcG//TSF_calcLD+TSF_calcPN*TSF_calcG//TSF_calcPD
            TSF_calcLD=TSF_calcG
        elif TSF_calcO == "-":
            TSF_calcG=decimal.Decimal(TSF_Calc_LCM(str(TSF_calcLD),TSF_calcRD))
            TSF_calcLN=TSF_calcLN*TSF_calcG//TSF_calcLD-decimal.Decimal(TSF_calcRN)*TSF_calcG//decimal.Decimal(TSF_calcRD)
            TSF_calcLD=TSF_calcG
        else:  # TSF_calcO == '+'
            TSF_calcG=decimal.Decimal(TSF_Calc_LCM(str(TSF_calcLD),TSF_calcRD))
            TSF_calcLN=TSF_calcLN*TSF_calcG//TSF_calcLD+decimal.Decimal(TSF_calcRN)*TSF_calcG//decimal.Decimal(TSF_calcRD)
            TSF_calcLD=TSF_calcG
    TSF_calcA=TSF_Calc_bigtostr(str(TSF_calcLN),str(TSF_calcLD),(1 if TSF_calcLN < 0 else 0))
    return TSF_calcA

def TSF_Calc_multiplication(TSF_calcQ):    #TSF_doc:分数電卓の掛け算割り算等。公倍数公約数、最大値最小値も扱う。(TSFAPI)
    TSF_calcLN,TSF_calcLD=decimal.Decimal(1),decimal.Decimal(1)
    TSF_calcA=TSF_calcQ
    TSF_calcQreplace=TSF_calcQ.replace("*","\t*").replace("/","\t/").replace("\\","\t\\").replace("#","\t#").replace(">","\t>").replace("<","\t<")
    TSF_calcQsplits=TSF_calcQreplace.strip('\t').split('\t')
    for TSF_calcQmulti in TSF_calcQsplits:
        TSF_calcO=" "
        for TSF_calcOpe in "*/\\#<>":
            TSF_calcO=TSF_calcOpe if TSF_calcOpe in TSF_calcQmulti else TSF_calcO
        TSF_calcRND=TSF_Calc_fractalize(TSF_calcQmulti.lstrip("*/\\#<>")).split('|')
        TSF_calcRN,TSF_calcRD=TSF_calcRND[0],TSF_calcRND[-1];
        if decimal.Decimal(TSF_calcRD) == 0:
            TSF_calcA="n|0"
            TSF_calcLN,TSF_calcLD=decimal.Decimal(0),decimal.Decimal(0)
            break
        elif TSF_calcO == "/":
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRN)
            if TSF_calcLD < 0: TSF_calcLN,TSF_calcLD=-TSF_calcLN,-TSF_calcLD
        elif TSF_calcO == "\\":
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRD)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRN)
            if TSF_calcLD < 0: TSF_calcLN,TSF_calcLD=-TSF_calcLN,-TSF_calcLD
            TSF_calcLN,TSF_calcLD=TSF_calcLN//TSF_calcLD,1
        elif TSF_calcO == '#':
            TSF_calcG=decimal.Decimal(TSF_Calc_LCM(str(TSF_calcLD),TSF_calcRD))
            TSF_calcLN=TSF_calcLN*TSF_calcG//TSF_calcLD
            TSF_calcLD=TSF_calcG
            TSF_calcRM=decimal.Decimal(TSF_calcRN)*TSF_calcG//decimal.Decimal(TSF_calcRD)
            if TSF_calcRM == 0:
                TSF_calcA="n|0"
                TSF_calcLN,TSF_calcLD=decimal.Decimal(0),decimal.Decimal(0)
                break
            elif TSF_calcRM > 0:
                TSF_calcLN=TSF_calcLN%TSF_calcRM
            else:
                if TSF_calcLN%abs(TSF_calcRM) != 0:
                    TSF_calcLN=abs(TSF_calcRM)-TSF_calcLN%abs(TSF_calcRM)
                else:
                    TSF_calcLN=0
        elif TSF_calcO == '>':
            TSF_calcG=decimal.Decimal(TSF_Calc_LCM(str(TSF_calcLD),TSF_calcRD))
            TSF_calcLM=TSF_calcLN*TSF_calcG//TSF_calcLD
            TSF_calcRM=decimal.Decimal(TSF_calcRN)*TSF_calcG//decimal.Decimal(TSF_calcRD)
            if TSF_calcLM > TSF_calcRM:
                TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcRN),decimal.Decimal(TSF_calcRD)
        elif TSF_calcO == '<':
            TSF_calcG=decimal.Decimal(TSF_Calc_LCM(str(TSF_calcLD),TSF_calcRD))
            TSF_calcLM=TSF_calcLN*TSF_calcG//TSF_calcLD
            TSF_calcRM=decimal.Decimal(TSF_calcRN)*TSF_calcG//decimal.Decimal(TSF_calcRD)
            if TSF_calcLM < TSF_calcRM:
                TSF_calcLN,TSF_calcLD=decimal.Decimal(TSF_calcRN),decimal.Decimal(TSF_calcRD)
        else:  # TSF_calcO == '*':
            TSF_calcLN=TSF_calcLN*decimal.Decimal(TSF_calcRN)
            TSF_calcLD=TSF_calcLD*decimal.Decimal(TSF_calcRD)
    TSF_calcA=TSF_Calc_bigtostr(str(TSF_calcLN),str(TSF_calcLD),(1 if TSF_calcLN < 0 else 0))
    return TSF_calcA

def TSF_Calc_fractalize(TSF_calcQ):    #TSF_doc:分数電卓なので小数を分数に。ついでに平方根や三角関数も。0で割る、もしくは桁が限界越えたときなどは「n|0」を返す。(TSFAPI)
    TSF_calcA=TSF_calcQ
    TSF_calcA=TSF_calcA if "|" in TSF_calcA else "|".join([TSF_calcA,"1"])
    TSF_calcM=TSF_calcA.count("m")+TSF_calcA.count("-") if not "!" in TSF_calcA else 0
    TSF_calcA=TSF_calcA.replace("p","").replace("m","").replace("-","").replace("!","")
    TSF_calcND=TSF_calcA.split("|"); TSF_calcNstr,TSF_calcDstr=TSF_calcND[0],TSF_calcND[-1];
    TSF_calcNstr=TSF_calcNstr if "." in TSF_calcNstr else "".join([TSF_calcNstr,"."])
    TSF_calcDstr=TSF_calcDstr if "." in TSF_calcDstr else "".join([TSF_calcDstr,"."])
    TSF_calcNint=len(TSF_calcNstr)-1-TSF_calcNstr.rfind(".")
    TSF_calcDint=len(TSF_calcDstr)-1-TSF_calcDstr.rfind(".")
    TSF_calcNDint=min(TSF_calcNint,TSF_calcDint)
    TSF_calcNstr=TSF_calcNstr.lstrip("0").replace(".","");  TSF_calcNstr="".join([TSF_calcNstr,"0"*(TSF_calcDint-TSF_calcNDint)])
    TSF_calcDstr=TSF_calcDstr.lstrip("0").replace(".","");  TSF_calcDstr="".join([TSF_calcDstr,"0"*(TSF_calcNint-TSF_calcNDint)])
    TSF_calcA=TSF_Calc_bigtostr(TSF_calcNstr,TSF_calcDstr,TSF_calcM)
    return TSF_calcA

def TSF_Calc_bigtostr(TSF_calcN,TSF_calcD,TSF_calcM):    #TSF_doc:計算結果を通分する。(TSFAPI)
    if TSF_calcD != "":
        if TSF_calcN == "": TSF_calcN="0"
        try:
            TSF_calcGbig=decimal.Decimal(TSF_Calc_GCM(TSF_calcN,TSF_calcD))
            if TSF_calcGbig!=0:
                TSF_calcNbig=decimal.Decimal(TSF_calcN)//TSF_calcGbig
                TSF_calcDbig=decimal.Decimal(TSF_calcD)//TSF_calcGbig
                TSF_calcNbig=-abs(TSF_calcNbig) if TSF_calcM%2 else abs(TSF_calcNbig)
                TSF_calcA="|".join([str(TSF_calcNbig),str(TSF_calcDbig)])
            else:
                TSF_calcA="n|0"
        except decimal.InvalidOperation:
            TSF_calcA="n|0"
    else:
        TSF_calcA="n|0"
    return TSF_calcA

def TSF_Calc_GCM(TSF_calcN,TSF_calcD):    #TSF_doc:最大公約数の計算。(TSFAPI)
    try:
        TSF_calcMbig,TSF_calcNbig=abs(decimal.Decimal(TSF_calcN)),abs(decimal.Decimal(TSF_calcD))
        if TSF_calcMbig < TSF_calcNbig:
            TSF_calcMbig,TSF_calcNbig=TSF_calcNbig,TSF_calcMbig
        while TSF_calcNbig > 0:
            TSF_calcMbig,TSF_calcNbig=TSF_calcNbig,TSF_calcMbig%TSF_calcNbig
        TSF_calcA=str(TSF_calcMbig)
    except decimal.InvalidOperation:
        TSF_calcA="n|0"
    return TSF_calcA

def TSF_Calc_LCM(TSF_calcN,TSF_calcD):    #TSF_doc:最小公倍数の計算(TSFAPI)。
    TSF_calcGbig=decimal.Decimal(TSF_Calc_GCM(TSF_calcN,TSF_calcD))
    if TSF_calcGbig!=0:
        try:
            TSF_calcA=str(abs(decimal.Decimal(TSF_calcN)*decimal.Decimal(TSF_calcD))//abs(TSF_calcGbig))
        except decimal.InvalidOperation:
            TSF_calcA="n|0"
    else:
        TSF_calcA="n|0"
    return TSF_calcA

TSF_Initcalldebug=[TSF_Calc_Initcards]
def TSF_Calc_debug(TSF_sysargvs):    #TSFdoc:「TSF_Calc」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Calc.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "calccount:","#TSF_this","#TSF_fin."]),"T")
    TSF_Forth_setTSF("calccount:","\t".join([
        "calcjump:","calcsample:","#TSF_lenthe","0,1,[0]U","#TSF_join[]","#TSF_RPN","#TSF_peekNthe","#TSF_this","calccount:","#TSF_this"]),"T")
    TSF_Forth_setTSF("calcjump:","\t".join([
        "#exit","calcpop:"]),"T")
    TSF_Forth_setTSF("calcpop:","\t".join([
        "calcsample:","0","#TSF_pullNthe","#TSF_peekFthat","#TSF_calc","「[1]」→「[0]」","#TSF_join[]","#TSF_echo"]),"T")
    TSF_Forth_setTSF("calcpeekdata:","\t".join([
        "009","108","207","306","405","504","603","702","801","900"]),"T")
    TSF_Forth_setTSF("calcjumpdata:","\t".join([
        "True:","False:"]),"T")
    TSF_Forth_setTSF("calcsample:","\t".join([
        "0|0","0|0,","0/0","0,0/",",0","0",
        "2,3+","2,3-","2,3*","2,3/","(2,3-),5+",
        "[calcpeekdata:8]",
        "4|6","3.5|0.05","5|6*m2|4","5|6/m2|4","5|6\\m2|4","5|6#p2|4","5|6#m2|4",
        "10#5","10#m5","10#7","10#m7","5#p4","5#m4","5,4#","5,m4#",
        "5|6>2|3","2|3>5|6","5|6<2|3","2|3<5|6",
        "2+3","2-3","5|6+p2|3","5|6-p2|3","5|6+m2|3","5|6-m2|3","100%p8",
        "100%m8","100*(100+8)/100","100*(100-8)/100","100,8%",
        ",m4!","m4!",
        "m1Z~[calcpeekdata:0]~[calcpeekdata:1]","0Z~[calcpeekdata:0]~[calcpeekdata:1]","p1Z~[calcpeekdata:0]~[calcpeekdata:1]",
        "m1Z~[calcjumpdata:0]~[calcjumpdata:1]","0Z~[calcjumpdata:0]~[calcjumpdata:1]","p1Z~[calcjumpdata:0]~[calcjumpdata:1]",
        "m1Z~True:~False:","0Z~True:~False:","p1Z~True:~False:",
        "0|1N~True:~False:","n|0N~True:~False:"]),"N")
    TSF_debug_log=TSF_Forth_samplerun(__file__,True,TSF_debug_log)
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)

if __name__=="__main__":
    TSF_Calc_debug(TSF_Io_argvs(["python","TSF_Calc.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF1KEV/blob/master/LICENSE
