#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *
from TSF_Trans import *


def TSF_sample_help():    #TSFdoc:「sample_help.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "help:","#TSF_argvsthe","#TSF_reverseN","help:","#TSF_lenthe","#TSF_echoN","#TSF_fin."]),"T")
    TSF_Forth_setTSF("help:","\t".join([
        "usage: ./TSF.py [command|file.tsf] [argvs] ...",
        "commands & samples:",
        "  --help        this commands view",
        "  --python      TSF to Python",
        "  --dlang       TSF to D",
        "  --about       about TSF mini guide",
        "  --helloworld  \"Hello world  #TSF_echo\" sample",
        "  --RPN         decimal RPN calculator \"1,3/m1|2-\"-> 0.8333... "]),"N")
    TSF_sample_run("TSF_sample_help")

def TSF_sample_run(TSF_sample_sepalete=None,TSF_sample_viewthey=None):    #TSFdoc:TSF実行。コマンド実行の場合はソースも表示。
    if TSF_sample_sepalete != None:
        TSF_Io_printlog("-- {0} source --".format(TSF_sample_sepalete))
        TSF_Forth_viewthey()
        TSF_Io_printlog("-- {0} run --".format(TSF_sample_sepalete))
    TSF_Forth_run()
    if TSF_sample_viewthey != None:
        TSF_Io_printlog("-- {0} viewthey --".format(TSF_sample_sepalete))
        TSF_Forth_viewthey()

def TSF_sample_Helloworld():    #TSFdoc:「sample_helloworld.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "Hello world","#TSF_echo"]),"T")
    TSF_sample_run("TSF_sample_Helloworld")

def TSF_sample_about():    #TSFdoc:「sample_aboutTSF.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "echoTSF:","#TSF_this","#TSF_fin."]),"T")
    TSF_Forth_setTSF("echoTSF:","\t".join([
        "aboutTSF:","#TSF_argvsthe","#TSF_reverseN","aboutTSF:","#TSF_lenthe","#TSF_echoN","echoRPN:","#TSF_this"]),"T")
    TSF_Forth_setTSF("aboutTSF:","\t".join([
        "",
        "○「TSF_Tab-Separated-Forth」の概要(開発予定の話も含みます)。",
        "",
        "　Forth風インタプリタ。単位はtsv文字列。文字列の事をカードと呼称。カードの束をスタックと呼称。スタックの集まりをデッキと呼称。",
        "　ソースコード.tsfで文字から始まる行はスタック名、タブで始まる行はカード。スタック名の宣言とカードの積み込みはワンライナー記述も可能。",
        "　改行のみもしくは「#」で始まる行は読み飛ばし。「#」は「#関数カード」として使うので「#」で始まるスタック名は予約ワード扱い。",
        "",
        "○TSFには4つの「th」スタック代名詞「this」「that」「the」「they」という概念が存在する。",
        "",
        "　「this」は実行中のスタック。#関数カードの指示通りにカードを「ドロー(積み下ろし)」したり「リターン(積み上げ)」したりする。",
        "　#関数カードではないカードは後述の「that」スタックに積み上げられる。関数の返り値ではないのでリターンとは呼ばない。",
        "　オーバーフローもしくは「#exit #TSF_this」のように存在しないスタックに入る行為でオーバーフローを発生させてスタックから抜ける。",
        "　TSFにループ構文は存在しないので末尾再帰がループになる。同様にループの内側からループの外側スタックを呼び出してもコールスタックが破棄される。",
        "　TSFにはif構文も存在しないので「#TSF_this」の飛び先を事前に書き換える形になる。条件演算子は「#TSF_RPN」「#TSF_calc」の中にある。",
        "　「that」は積込先のスタック。#関数カードの返り値や#関数カード以外のカードが積み上げられる。",
        "　「the」は指定スタック。変数や配列やテキスト保存先として扱ってるスタックが一時的に呼び出される場合の文字通り代名詞。",
        "　「they」はスタック名一覧。スタック名一覧自体もカード束としてスタックの様に扱える場合がある。",
        ""]),"N")
    TSF_Forth_setTSF("echoRPN:","\t".join([
        "aboutRPNtest:","#TSF_this","aboutRPN:","#TSF_argvsthe","#TSF_reverseN","aboutRPN:","#TSF_lenthe","#TSF_echoN","echoCALC:","#TSF_this"]),"T")
    TSF_Forth_setTSF("aboutRPNtest:","\t".join([
        "▽「1 3 m1|2」を「[2],[1]/[0]- #TSF_join[]」で連結→","1","3","m1|2","[2],[1]/[0]-","#TSF_join[]","#TSF_RPN","2","#TSF_joinN","#TSF_echo","▽「1 , 3 / m1|2 -」を「#TSF_join」で連結→","1",",","3","/","m1|2","-","6","#TSF_joinN","#TSF_RPN","2","#TSF_joinN","#TSF_echo"]),"T")
    TSF_Forth_setTSF("aboutRPN:","\t".join([
        "",
        "○「RPN」系小数電卓の概要。",
        "",
        "　TSFでは機能を絞って高速処理をめざすRPNと多機能をめざすcalcの2種類の電卓を用意。RPN(逆ポーランド記法)では括弧を用いません。",
        "　RPNでは「1+2」は「1,2+」である。掛け算が先に演算されるなどの優先順序が存在する数式は「calc」を使う。",
        "　演算子の「+」プラス「-」マイナスと符号の「p」プラス「m」マイナスは分けて表記。「1-(-2)」を「1,m2-」と表記する。",
        "　演算子の「/」と分数の「|」も分けて表記。二分の一「1|2」は分数(0.5)だが１÷２の割り算として表現する場合は「1,2/」と表記する。",
        "　分数小数を用いても計算結果が整数になる場合、および小数の丸めで整数になってしまった場合は整数表記になる。",
        "　通常の割り算の他にも1未満を切り捨てる「\\」、余りを求める「#」がある。",
        "　RPNではゼロで割った時は「n|0」を出力して終了。条件演算子の可能性とかは考慮されない。",
        "　「Z」はゼロ比較演算子(条件演算子)。「1,2,0Z」はゼロの時は真なので左の数値(1)、ゼロでない時は偽なので右の数値(2)を採用。",
        "　「O」「o」「U」「u」も同様に、ゼロ以上(ゼロ含む)、ゼロより大きい、ゼロ以下(ゼロ含む)、ゼロ未満で左右の数値を選択。",
        "、条件演算子は何に使うかというと「#TSF_this」の飛び先を変更するため「#TSF_peekthe」などと組み合わせます。",
        ""]),"N")
    TSF_Forth_setTSF("echoCALC:","\t".join([
        "aboutCALC:","#TSF_argvsthe","#TSF_reverseN","aboutCALC:","#TSF_lenthe","#TSF_echoN"]),"T")
    TSF_Forth_setTSF("aboutCALC:","\t".join([
        "○「calc」系分数電卓は再開発中なので説明不足します(RPNと共通する内容は圧縮)。",
        "",
        "　calcは分数を用いる事で桁溢れや丸め誤差をなるだけ回避する事を目標とします。",
        "　calcでは分母「n|0」でも条件演算子の可能性などを考慮して計算は続行されます。",
        "　「#TSF_join[]」などを別途用いる事無く数式「[2]/[1]-[0]」を直接渡したり「#TSF_this」の飛び先を直接指定できる様にする予定。",
        ""]),"N")
    TSF_sample_run("TSF_sample_about")

def TSF_sample_RPN():    #TSFdoc:「sample_RPN.tsf」コマンド版。
    TSF_Forth_setTSF("RPN:","\t".join([
        "#TSF_RPN","#TSF_echo"]),"T")
    TSF_Forth_setTSF("RPNsetup:","\t".join([
        "RPNargvs:","#TSF_that","#TSF_argvs",",","#TSF_sandwichN","RPNjump:","RPNargvs:","#TSF_lenthe","#TSF_peekNthe","#TSF_this"]),"T")
    TSF_Forth_setTSF("RPNjump:","\t".join([
        "RPNdefault:","RPNdefault:","RPN:"]),"T")
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "RPNsetup:","#TSF_this","#TSF_fin."]),"T")
    TSF_Forth_setTSF("RPNdefault:","\t".join([
        "1,3/m1|2-","RPN:","#TSF_this"]),"T")
    TSF_sample_run("TSF_sample_RPN")


TSF_sysargvs=TSF_Io_argvs(sys.argv)
TSF_Initcallrun=[TSF_Forth_Initcards,TSF_Trans_Initcards]
TSF_Forth_initTSF(TSF_sysargvs[1:],TSF_Initcallrun)
TSF_bootcommand="" if len(TSF_sysargvs) < 2 else TSF_sysargvs[1]
if os.path.isfile(TSF_bootcommand) and len(TSF_Forth_loadtext(TSF_bootcommand,TSF_bootcommand)):
    TSF_Forth_merge(TSF_bootcommand,[],True)
    os.chdir(os.path.dirname(os.path.normpath(TSF_bootcommand)))
    TSF_sample_run()
elif TSF_bootcommand in ["--py","--python","--Python"]:
    if len(TSF_sysargvs) >= 4:
        TSF_Trans_generator_python(TSF_sysargvs[2],TSF_sysargvs[3])
    elif len(TSF_sysargvs) >= 3:
        TSF_Trans_generator_python(TSF_sysargvs[2])
elif TSF_bootcommand in ["--py","--d","--D","--dlang"]:
    if len(TSF_sysargvs) >= 4:
        TSF_Trans_generator_dlang(TSF_sysargvs[2],TSF_sysargvs[3])
    elif len(TSF_sysargvs) >= 3:
        TSF_Trans_generator_dlang(TSF_sysargvs[2])
elif TSF_bootcommand in ["--help","--commands"]:
    TSF_sample_help()
elif TSF_bootcommand in ["--about","--aboutTSF"]:
    TSF_sample_about()
elif TSF_bootcommand in ["--hello","--helloworld","--Helloworld"]:
    TSF_sample_Helloworld()
elif TSF_bootcommand in ["--RPN","--rpn"]:
    TSF_sample_RPN()
else:
    TSF_sample_help()
sys.exit(0)


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
