#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

#import sys
#import os
#os.chdir(sys.path[0])
#sys.path.append("TSFpy")
from TSF_Io import *
from TSF_Forth import *
from TSF_Shuffle import *
from TSF_Calc import *
from TSF_Time import *
from TSF_Urlpath import *
from TSF_Match import *
from TSF_Trans import *


def TSF_sample_help():    #TSFdoc:「sample_help.tsf」コマンド版「TSF --help」。<br>ファイル名などのパラメーターが無い場合にもコマンド一覧が表示される。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "replace:","#TSF_this","help:","#TSF_argvsthe","#TSF_echoN","#TSF_fin."]),'T')
    TSF_Forth_setTSF("help:","\t".join([
        "usage: ./TSF [command|file.tsf] [argvs] ...",
        "commands & samples:",
        "  --help        this commands view",
        "  --about       about TSF mini guide",
        "  --doc         TSF and more documentation tool",
        "  --python      TSF to Python",
        "  --dlang       TSF to D",
        "  --RPN         decimal RPN calculator \"1,3/m1|2-\"-> 0.8333... ",
        "  --calc        fraction calculator \"1/3-m1|2\"-> p5|6",
        "  --calender    \"@4y@0m@0dm@wdec@0h@0n@0s\"-> {calender}",
        "  --helloworld  \"Hello world  #TSF_echo\" sample",
        "  --fizzbuzz    Fizz(#3) Buzz(#5) Fizz&Buzz(#15) sample",
        "  --99bear      99 Bottles of Beer 9 Bottles sample",
        "  --quine       quine (TSF,Python,D... selfsource) sample",
        ]),'N')
    TSF_Forth_setTSF("replace:","\t".join([
        "help:","{calender}","@4y@0m@0dm@wdec@0h@0n@0s","#TSF_calender","#TSF_replacesQON"]),'T')
    TSF_Forth_samplerun("TSF_sample_help")
#        "  --zundoko     Zun Zun Zun Zun Doko VeronCho sample",
#        "  --fibonacci   Fibonacci number 0,1,1,2,3,5,8,13,21,55... sample",
#        "  --prime       prime numbers 2,3,5,7,11,13,17,19,23,29... sample",

def TSF_sample_Helloworld():    #TSFdoc:「sample_helloworld.tsf」コマンド版「TSF --helloworld」。<br>「"Hello world #TSF_echo」のみ。「#TSF_fin.」の省略テストも兼用。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "Hello world","#TSF_echo"]),'T')
    TSF_Forth_samplerun("TSF_sample_Helloworld")

def TSF_sample_TSFdoc():    #TSFdoc:「TSFdoc.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#TSF_argvs","#TSF_pullFthat","#TSF_peekFthat","#TSF_existfile","[0]Z~TSFdocs_help:~TSFdocs_merge:","#TSF_join[]","#TSF_calc","#TSF_this","#TSF_fin.","README.tsf"]),'T')
    TSF_Forth_setTSF("TSFdocs_help:","\t".join([
        "usage: TSF [--TSFdoc | sample/TSFdoc.tsf] README.tsf","#TSF_echo","#TSF_fin."]),'T')
    TSF_Forth_setTSF("TSFdocs_merge:","\t".join([
        "#TSF_peekFthat","#TSF_readtext","#TSF_peekFthat","#TSF_mergethe","#TSF_peekFthat","#TSF_basepath","TSFdocs_imports:","#TSF_lenthe","[0]Z~TSFdocs_loop:~TSFdocs_import:","#TSF_join[]","#TSF_calc","#TSF_this"]),'T')
    TSF_Forth_setTSF("TSFdocs_import:","\t".join([
        "TSFdocs_imports:","#TSF_pullFthe","#TSF_peekFthat","[0](import)","#TSF_join[]","#TSF_echo","#TSF_peekFthat","#TSF_readtext","#TSF_peekFthat","#TSF_mergethe","#TSF_peekFthat","#TSF_fileext","TSFimport_ext:","TSFimport_regex:","#TSF_casesQON","#TSF_this","TSFdocs_imports:","#TSF_lenthe","[0]Z~TSFdocs_loop:~TSFdocs_import:","#TSF_join[]","#TSF_calc","#TSF_this"]),'T')
    TSF_Forth_setTSF("TSFdocs_loop:","\t".join([
        "TSFdocs_files:","#TSF_pullFthe","#TSF_peekFthat","[0](save)","#TSF_join[]","#TSF_echo","TSF_carbondoc:","TSFdocs_basedocs:","#TSF_pullFthe","#TSF_clonethe","TSF_carbontags:","TSFdocs_tags:","#TSF_clonethe","TSFtags_loop:","#TSF_this","#TSF_peekFthat","TSF_carbondoc:","#TSF_savetext","TSFdocs_files:","#TSF_lenthe","[0]Z~#!exit:~TSFdocs_loop:","#TSF_join[]","#TSF_calc","#TSF_this"]),'T')
    TSF_Forth_setTSF("TSFtags_loop:","\t".join([
        "TSF_carbondoc:","TSF_carbontags:","#TSF_pullFthe","#TSF_peekFthat","TSFdocs_files:","#TSF_lenthe","#TSF_peekMthe","#TSF_calender","#TSF_docsQ","TSF_carbontags:","#TSF_lenthe","[0]Z~#!exit:~TSFtags_loop:","#TSF_join[]","#TSF_calc","#TSF_this"]),'T')
    TSF_Forth_samplerun("TSF_sample_TSFdoc")

def TSF_sample_about():    #TSFdoc:「sample_aboutTSF.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "echoTSF:","#TSF_this","#TSF_fin."]),'T')
    TSF_Forth_setTSF("echoTSF:","\t".join([
        "aboutTSF:","#TSF_argvsthe","#TSF_echoN","echoRPNcalc:","#TSF_this"]),'T')
    TSF_Forth_setTSF("aboutTSF:","\t".join([
        "",
        "○「TSF_Tab-Separated-Forth」の簡略説明。",
        "",
        "　Forth風インタプリタ。単位はtsv文字列。文字列の事をカードと呼称。カードの束をスタックと呼称。スタックの集まりをデッキと呼称。",
        "　文字から始まる行はスタック名。タブで始まる行はカードの束。シバン「#!」で始まる行(改行のみの行含む)はコメント扱いで読み飛ばし。",
        "",
        "○TSF構文には4つの「th」、スタック代名詞「this」「that」「the」「they」が存在。",
        "",
        "　「this」は実行中のスタック。#関数カードの指示通りにカードを「ドロー(積み下ろし)」したり「リターン(積み上げ)」したりする。",
        "　「that」は積込先のスタック。#関数カードの返り値や#関数カード以外のカードが積み上げられる。",
        "　「the」は指定スタック。変数や配列やテキスト保存先として扱ってるスタックが一時的に呼び出される場合の文字通り代名詞。",
        "　「they」はスタック名一覧。スタック名一覧自体もカード束としてスタックの様に扱える場合がある。",
        "",
        "○TSF構文のスタック操作に4つの「p」、スタック動詞「peek」「poke」「pull」「push」が存在する。",
        "",
        "　「peek」スタックからカードを読み込む。読込先スタックはそのままに「that」スタックにカードが積まれるのでカードが増殖る形になる。",
        "　「poke」スタックにカードを書き込む。スタックのカードは上書きされるので上書きされたカードが消失する形になる。",
        "　「pull」スタックからカードを引き抜く。引抜先スタックから「that」スタックにカードが移動する形になる。",
        "　「push」スタックにカードを差し込む。引抜先スタックに「that」スタックからカードが移動する形になる。",
        "",
        "○TSF構文の副詞「FNCMVAQIRHL」と数量詞「SDO」などの説明は省略。",
        "",
        "　※#関数カードの、ドロー(積み下ろし)は「pullFthat」リターン(積み上げ)は「pushFthat」してるとも言える。",
        "",
        "○TSFの式の解説前にとりあえず分数計算や漢数字のテストなど。",
        ""]),'N')
    TSF_Forth_setTSF("echoRPNcalc:","\t".join([
        "aboutRPNtest:","#TSF_this","aboutRPNcalc:","#TSF_argvsthe","#TSF_echoN","echoURL:","#TSF_this"]),'T')
    TSF_Forth_setTSF("aboutRPNtest:","\t".join([
        "▽「1 3 m1|2」を「[2],[1]/[0]- #TSF_join[]」で連結して「#TSF_RPN」→","1","3","m1|2","[2],[1]/[0]-","#TSF_join[]","#TSF_RPN","2","#TSF_joinN","#TSF_echo","▽「1 , 3 / m1|2 -」を「6 #TSF_join」で連結して「#TSF_RPN」→","1",",","3","/","m1|2","-","6","#TSF_joinN","#TSF_RPN","2","#TSF_joinN","#TSF_echo","▽「1 3 m1|2」を「[2]/[1]-[0] #TSF_join[]」で連結して「#TSF_calc」→","1","3","m1|2","[2]/[1]-[0]","#TSF_join[]","#TSF_calc","2","#TSF_joinN","#TSF_echo","▽「1 / 3 - m1|2 」を「5 #TSF_join」で連結して「#TSF_calc」→","1","/","3","-","m1|2","5","#TSF_joinN","#TSF_calc","2","#TSF_joinN","#TSF_echo","▽スタックからショートカットで「[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2] を「#TSF_calc」→","[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2]","#TSF_calc","2","#TSF_joinN","#TSF_echo","▽漢数字テスト「億千万」を「#TSF_calcJA」→","億千万","#TSF_calcJA","2","#TSF_joinN","#TSF_echo","▽漢数字テスト「六分の五」を「#TSF_calcJA」→","６分の５","#TSF_calcJA","2","#TSF_joinN","#TSF_echo","▽日時テスト「@4y年@0m月@0dm日(@wdj)@0h時@0n分@0s秒」を「#TSF_calender」→","@4y年@0m月@0dm日(@wdj)@0h時@0n分@0s秒","#TSF_calender","2","#TSF_joinN","#TSF_echo"]),'T')
    TSF_Forth_setTSF("aboutCALCdata:","\t".join([
        "1","3","m1|2"]),'T')
    TSF_Forth_setTSF("aboutRPNcalc:","\t".join([
        "",
        "○「#TSF_RPN」逆ポーランド小数電卓の概要。",
        "",
        "　TSFの数式に高速処理を目指すRPNと多機能を備えるcalcの2種類の電卓を用意。",
        "　RPNでは「1+2」は「1,2+」になる。数値同士はコンマで区切る。掛け算が先に演算されるなど優先順序が存在する数式は「calc」を使う。",
        "　演算子の「+」プラス「-」マイナスと符号の「p」プラス「m」マイナスは分けて表記。「1-(-2)」も「1,m2-」と表記する。",
        "　演算子の「/」と分数の「|」も分けて表記。分数二分の一「1|2」は小数「0.5」だが１÷２の割り算として表現する場合は「1,2/」と表記する。",
        "　通常の割り算の他にも1未満を切り捨てる「\\」、余りを求める「#」がある。マイナス剰余は「5#m4」だと「4-(5#4)」のように計算する。",
        "　計算結果が整数になる場合、および小数の丸めで整数になってしまった場合は整数表記になる。",
        "　RPNではゼロ「0|1」で割った時は分母ゼロ「n|0」を出力して終了。計算続行はされないので注意。",
        "　「Z」はゼロ比較演算子(条件演算子)。「1,2,0Z」はゼロの時は真なので左の数値(1)、ゼロでない時は偽なので右の数値(2)を採用。",
        "　「O」「o」「U」「u」も同様に、ゼロ以上(ゼロ含む)、ゼロより大きい、ゼロ以下(ゼロ含む)、ゼロ未満で左右の数値を選択。",
        "　条件演算子とスタック名(演算を抑止する「:」演算子)を組み合わせる事で、「#TSF_this」に渡すスタック名を分岐できます(IF構文の代替)。",
        "",
        "○「#TSF_calc」系分数電卓の概要(RPNと共通する内容は圧縮)。",
        "",
        "　calcは括弧や分数なども使えます。RPN電卓も混在できます。分数を用いる事で桁溢れや丸め誤差をなるだけ回避する事を目標とします。",
        "　分数を小数に変換するには「,(1|3)」のように括弧の外側でコンマを使う事でcalcの計算結果をRPNで処理する形になります。",
        "　calcではRPNとは事なり、括弧が無くても「小数の分数化＞掛け算系＞足し算系＞条件演算子」のような計算順序が存在します。",
        "　calcでは式に直接スタック名を「[data:2]/[data:1]-[data:0]」できるので、「#TSF_peekNthe」「#TSF_join[]」をショートカットできます。",
        "　スタック名ショートカット実現のため「Z~」「z~」「O~」「o~」「U~」「u~」「N~」と条件演算子にチルダ追加。「N~」は「n|0」のチェック用途。",
        "　「#TSF_-calc」を用いると計算結果の符号を「p」「m」から「-」のみに変更できる。",
        "　「#TSF_calcJA」を用いると億千万円銭など通貨的な助数詞を扱う。100分の1(％)は「銭」、1000分の1(‰)は「厘」表記、1万分の1(‱)は「毛」表記。",
        ""]),'N')
    TSF_Forth_setTSF("echoURL:","\t".join([
        "aboutURL:","#TSF_argvsthe","#TSF_echoN"]),'T')
    TSF_Forth_setTSF("aboutURL:","\t".join([
        "○TSFの詳しい説明はローカルの「docs/index.html」かWeb上の「https://ooblog.github.io/TSF2KEV/」を確認してください。",
        "",
        "　Web版もTSF付属のローカル版も「docs/TSFindex.tsf」から「sample/TSFdoc.tsf」を用いて生成されてます。",
        "　TSFを用いると簡潔なプログラムが書けます。そしてこの「sample/sample_aboutTSF.tsf」文書自体もTSF言語で書かれてます。",
        "",
        "#! -- Copyright (c) 2017 ooblog --",
        "#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE"]),'N')
    TSF_Forth_samplerun("TSF_sample_about")

def TSF_sample_RPN():    #TSFdoc:「sample_RPN.tsf」コマンド版。
    TSF_Forth_setTSF("RPN:","\t".join([
        "#TSF_RPN","#TSF_echo"]),'T')
    TSF_Forth_setTSF("RPNsetup:","\t".join([
        "RPNargvs:","#TSF_that","#TSF_argvs",",","#TSF_sandwichN","RPNjump:","RPNargvs:","#TSF_lenthe","#TSF_peekNthe","#TSF_this"]),'T')
    TSF_Forth_setTSF("RPNjump:","\t".join([
        "RPNdefault:","RPNdefault:","RPN:"]),'T')
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "RPNsetup:","#TSF_this","#TSF_fin."]),'T')
    TSF_Forth_setTSF("RPNdefault:","\t".join([
        "1,3/m1|2-","RPN:","#TSF_this"]),'T')
    TSF_Forth_samplerun("TSF_sample_RPN")

def TSF_sample_calc():    #TSFdoc:「sample_calc.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "calcsetup:","#TSF_this","#TSF_fin."]),'T')
    TSF_Forth_setTSF("calcsetup:","\t".join([
        "calcargvs:","#TSF_that","#TSF_argvs",",","#TSF_sandwichN","calcjump:","calcargvs:","#TSF_lenthe","#TSF_peekNthe","#TSF_this"]),'T')
    TSF_Forth_setTSF("calcjump:","\t".join([
        "calcdefault:","calcdefault:","calc:"]),'T')
    TSF_Forth_setTSF("calcdefault:","\t".join([
        "1/3-m1|2","calc:","#TSF_this"]),'T')
    TSF_Forth_setTSF("calc:","\t".join([
        "#TSF_calc","#TSF_echo"]),'T')
    TSF_Forth_samplerun("TSF_sample_calc")

def TSF_sample_calcJA():    #TSFdoc:「sample_calcJA.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "calcsetup:","#TSF_this","#TSF_fin."]),'T')
    TSF_Forth_setTSF("calcsetup:","\t".join([
        "calcdef:","#TSF_that","#TSF_argvs","#TSF_pullFthat","#TSF_calcJA","#TSF_echo"]),'T')
    TSF_Forth_setTSF("calcdef:","\t".join([
        "1/3-m1|2"]),'N')
    TSF_Forth_samplerun("TSF_sample_calcJA")

def TSF_sample_calender():    #TSFdoc:「sample_calender.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#TSF_argvs","#TSF_pullFthat","calender:","#TSF_this","#TSF_fin.","@4y@0m@0dm@wdec@0h@0n@0s"]),'T')
    TSF_Forth_setTSF("calender:","\t".join([
        "#TSF_calender","#TSF_echo"]),'T')
    TSF_Forth_samplerun("TSF_sample_calender")

def TSF_sample_FizzBuzz():    #TSFdoc:「sample_fizzbuzz.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#TSF_argvs","#TSF_pullFthat","FZcount:","#TSF_pushFthe","FBloop:","#TSF_this","#TSF_fin.","20"]),'T')
    TSF_Forth_setTSF("FBloop:","\t".join([
        "FZcount:",",([FZcount:0]+1)","#TSF_-calc","FZcount:","0","#TSF_pokeNthe","([FZcount:0]#3Z~1~0)+([FZcount:0]#5Z~2~0)","#TSF_calc","#TSF_peekNthe","#TSF_echo","[FZcount:4]-[FZcount:0]o~FBloop:~#!exit:","#TSF_calc","#TSF_this"]),'T')
    TSF_Forth_setTSF("FZcount:","\t".join([
        "0","Fizz","Buzz","Fizz&Buzz"]),'T')
    TSF_Forth_samplerun("TSF_sample_FizzBuzz")

def TSF_sample_99beer():    #TSFdoc:「sample_99beer.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#TSF_argvs","#TSF_pullFthat","bottlessetup:","#TSF_this","#TSF_fin.","9"]),'T')
    TSF_Forth_setTSF("bottlessetup:","\t".join([
        "onthewallint:","#TSF_pushFthe","onthewallint:","#TSF_that","#TSF_peekFthat","#TSF_peekFthat","callbottles:","#TSF_this"]),'T')
    TSF_Forth_setTSF("callbottles:","\t".join([
        "#TSF_swapBA","#TSF_pullFthat","#TSF_peekFthat","[0],1-","#TSF_join[]","#TSF_-calc","N-bottles:","bottlescall:","[onthewallint:1]","#TSF_calc","#TSF_peekMthe","#TSF_clonethe","N-bottles:","onthewallstr:","onthewallint:","#TSF_replacesQSN","N-bottles:","#TSF_argvsthe","#TSF_echoN","[onthewallint:1]o~callbottles:~#!exit:","#TSF_calc","#TSF_this"]),'T')
    TSF_Forth_setTSF("onthewallstr:","\t".join([
        "{buybottles}","{drink}","{drinked}"]),'T')
    TSF_Forth_setTSF("bottlescall:","\t".join([
        "nomorebottles:","1bottle:","2bottles:","3ormorebottles:"]),'T')
    TSF_Forth_setTSF("3ormorebottles:","\t".join([
        "{drink} bottles of beer on the wall, {drink} bottles of beer.",
        "Take one down and pass it around, {drinked} bottles of beer on the wall."]),'N')
    TSF_Forth_setTSF("2bottles:","\t".join([
        "{drink} bottles of beer on the wall, {drink} bottles of beer.",
        "Take one down and pass it around, 1 bottle of beer on the wall."]),'N')
    TSF_Forth_setTSF("1bottle:","\t".join([
        "{drink} bottle of beer on the wall, {drink} bottle of beer.",
        "Take one down and pass it around, no more bottles of beer on the wall."]),'N')
    TSF_Forth_setTSF("nomorebottles:","\t".join([
        "No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, {buybottles} bottles of beer on the wall."]),'N')
    TSF_Forth_samplerun("TSF_sample_99beer")

def TSF_sample_quine():    #TSFdoc:「sample_quine.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "quine_echo:","#TSF_this","#TSF_fin."]),'T')
    TSF_Forth_setTSF("quine_echo:","\t".join([
        "#TSF_mainfile","#TSF_fileext","quine_ext:","quine_view:","#TSF_casesQON","#TSF_this"]),'T')
    TSF_Forth_setTSF("quine_ext:","\t".join([
        ".tsf",".py",".d"]),'T')
    TSF_Forth_setTSF("quine_view:","\t".join([
        "quine_TSF:","quine_Python:","quine_D:","#!exit:"]),'T')
    TSF_Forth_setTSF("quine_TSF:","\t".join([
        "#! /usr/bin/env TSF","#TSF_echo","#TSF_viewthey"]),'T')
    TSF_Forth_setTSF("quine_Python:","\t".join([
        "#TSF_Python"]),'N')
    TSF_Forth_setTSF("quine_D:","\t".join([
        "#TSF_D-lang"]),'N')
    TSF_Forth_samplerun("TSF_sample_quine")

TSF_sysargvs=TSF_Io_argvs(sys.argv)
TSF_Initcallrun=[TSF_Forth_Initcards,TSF_Shuffle_Initcards,TSF_Calc_Initcards,TSF_Time_Initcards,TSF_Urlpath_Initcards,TSF_Match_Initcards,TSF_Trans_Initcards]
TSF_Forth_initTSF(TSF_sysargvs[1:],TSF_Initcallrun)
TSF_bootcommand="" if len(TSF_sysargvs) < 2 else TSF_sysargvs[1]
if os.path.isfile(TSF_bootcommand) and len(TSF_Forth_loadtext(TSF_bootcommand,TSF_bootcommand)):
    TSF_Forth_merge(TSF_bootcommand,[],True)
    os.chdir(os.path.dirname(os.path.abspath(TSF_bootcommand)))
    TSF_Forth_mainfilepath(os.path.abspath(TSF_bootcommand))
    TSF_Forth_samplerun()
elif TSF_bootcommand in ["--py","--python","--Python"]:
    if len(TSF_sysargvs) >= 4:
        TSF_Forth_mainfilepath(os.path.abspath(TSF_sysargvs[3]))
        TSF_Trans_generator_python(TSF_sysargvs[2],TSF_sysargvs[3])
    elif len(TSF_sysargvs) >= 3:
        TSF_Forth_mainfilepath(os.path.abspath(TSF_sysargvs[2]))
        TSF_Trans_generator_python(TSF_sysargvs[2])
    else:
        print("usage: ./TSF --py base.tsf [output.py]")
elif TSF_bootcommand in ["--d","--D","--dlang"]:
    if len(TSF_sysargvs) >= 4:
        TSF_Forth_mainfilepath(os.path.abspath(TSF_sysargvs[3]))
        TSF_Trans_generator_dlang(TSF_sysargvs[2],TSF_sysargvs[3])
    elif len(TSF_sysargvs) >= 3:
        TSF_Forth_mainfilepath(os.path.abspath(TSF_sysargvs[2]))
        TSF_Trans_generator_dlang(TSF_sysargvs[2])
    else:
        print("usage: ./TSF --d base.tsf [output.d]")
elif TSF_bootcommand in ["--doc","--TSFdoc"]:
    TSF_sample_TSFdoc()
elif TSF_bootcommand in ["--help","--commands"]:
    TSF_sample_help()
elif TSF_bootcommand in ["--about","--aboutTSF"]:
    TSF_sample_about()
elif TSF_bootcommand in ["--hello","--helloworld","--Helloworld"]:
    TSF_sample_Helloworld()
elif TSF_bootcommand in ["--RPN","--rpn"]:
    TSF_sample_RPN()
elif TSF_bootcommand in ["--CALC","--Calc","--calc"]:
    TSF_sample_calc()
elif TSF_bootcommand in ["--calcJA"]:
    TSF_sample_calcJA()
elif TSF_bootcommand in ["--calender","--time","--date"]:
    TSF_sample_calender()
elif TSF_bootcommand in ["--fizz","--buzz","--fizzbuzz","--FizzBuzz"]:
    TSF_sample_FizzBuzz()
elif TSF_bootcommand in ["--99beer","--9beer","--beer99","--beer9","--beer","--99","--9"]:
    TSF_sample_99beer()
elif TSF_bootcommand in ["--quine","--Quine"]:
    TSF_Forth_mainfilepath("sample/sample_quine.tsf")
    TSF_sample_quine()
else:
    TSF_sample_help()
sys.exit(0)


#! -- Copyright (c) 2017 ooblog --
#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
