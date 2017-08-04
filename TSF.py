#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

#import sys
#import os
#os.chdir(sys.path[0])
#sys.path.append("TSFpy")
from TSF_Io import *
from TSF_Forth import *
#from TSF_Shuffle import *
from TSF_Calc import *
from TSF_Time import *
from TSF_Urlpath import *
from TSF_Match import *
from TSF_Trans import *


def TSF_sample_help():    #TSFdoc:「sample_help.tsf」コマンド版「TSF --help」。<br>ファイル名などのパラメーターが無い場合にもコマンド一覧が表示される。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "replace:","#!TSF_this","help:","#!TSF_argvsthe","#!TSF_echoN","#!TSF_fin."]),'T')
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
        "  --helloworld  \"Hello world  #!TSF_echo\" sample",
        "  --fizzbuzz    Fizz(#3) Buzz(#5) Fizz&Buzz(#15) sample",
        "  --zundoko     Zun Zun Zun Zun Doko VeronCho sample",
        "  --99bear      99 Bottles of Beer 9 Bottles sample",
        "  --quine       quine (TSF,Python,D... selfsource) sample",
        ]),'N')
    TSF_Forth_setTSF("replace:","\t".join([
        "help:","{calender}","@4y@0m@0dm@wdec@0h@0n@0s","#!TSF_calender","#!TSF_replacesQON"]),'T')
    TSF_Forth_samplerun("TSF_sample_help")
#        "  --zundoko     Zun Zun Zun Zun Doko VeronCho sample",
#        "  --fibonacci   Fibonacci number 0,1,1,2,3,5,8,13,21,55... sample",
#        "  --prime       prime numbers 2,3,5,7,11,13,17,19,23,29... sample",

def TSF_sample_Helloworld():    #TSFdoc:「sample_helloworld.tsf」コマンド版「TSF --helloworld」。<br>「#!TSF_fin.」の省略テストも兼用なので「"Hello world #!TSF_echo」のみ。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "Hello world","#!TSF_echo"]),'T')
    TSF_Forth_samplerun("TSF_sample_Helloworld")

def TSF_sample_TSFdoc():    #TSFdoc:「TSFdoc.tsf」コマンド版「TSF --doc」。<br>「sample/README.tsf」や「docs/TSFindex.tsf」が呼び出すTSFdocは「sample/TSFdoc.tsf」なので注意<br>(コマンドとして内蔵のTSFdocなどはD言語やPythonなのでTSFから呼び出せない)。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#!TSF_argvs","#!TSF_pullFthat","#!TSF_peekFthat","#!TSF_existfile","[0]Z~TSFdocs_help:~TSFdocs_merge:","#!TSF_join[]","#!TSF_calc","#!TSF_this","#!TSF_fin.","README.tsf"]),'T')
    TSF_Forth_setTSF("TSFdocs_help:","\t".join([
        "usage: TSF [--TSFdoc | sample/TSFdoc.tsf] README.tsf","#!TSF_echo","#!TSF_fin."]),'T')
    TSF_Forth_setTSF("TSFdocs_merge:","\t".join([
        "#!TSF_peekFthat","#!TSF_readtext","#!TSF_peekFthat","#!TSF_mergethe","#!TSF_peekFthat","#!TSF_basepath","TSFdocs_imports:","#!TSF_lenthe","[0]Z~TSFdocs_loop:~TSFdocs_import:","#!TSF_join[]","#!TSF_calc","#!TSF_this"]),'T')
    TSF_Forth_setTSF("TSFdocs_import:","\t".join([
        "TSFdocs_imports:","#!TSF_pullFthe","#!TSF_peekFthat","[0](import)","#!TSF_join[]","#!TSF_echo","#!TSF_peekFthat","#!TSF_readtext","#!TSF_peekFthat","#!TSF_mergethe","#!TSF_peekFthat","#!TSF_fileext","TSFimport_ext:","TSFimport_regex:","#!TSF_casesQON","#!TSF_this","TSFdocs_imports:","#!TSF_lenthe","[0]Z~TSFdocs_loop:~TSFdocs_import:","#!TSF_join[]","#!TSF_calc","#!TSF_this"]),'T')
    TSF_Forth_setTSF("TSFdocs_loop:","\t".join([
        "TSFdocs_files:","#!TSF_pullFthe","#!TSF_peekFthat","[0](save)","#!TSF_join[]","#!TSF_echo","TSF_carbondoc:","TSFdocs_basedocs:","#!TSF_pullFthe","#!TSF_clonethe","TSF_carbontags:","TSFdocs_tags:","#!TSF_clonethe","TSFtags_loop:","#!TSF_this","#!TSF_peekFthat","TSF_carbondoc:","#!TSF_savetext","TSFdocs_files:","#!TSF_lenthe","[0]Z~#!exit:~TSFdocs_loop:","#!TSF_join[]","#!TSF_calc","#!TSF_this"]),'T')
    TSF_Forth_setTSF("TSFtags_loop:","\t".join([
        "TSF_carbondoc:","TSF_carbontags:","#!TSF_pullFthe","#!TSF_peekFthat","TSFdocs_files:","#!TSF_lenthe","#!TSF_peekMthe","#!TSF_calender","#!TSF_docsQ","TSF_carbontags:","#!TSF_lenthe","[0]Z~#!exit:~TSFtags_loop:","#!TSF_join[]","#!TSF_calc","#!TSF_this"]),'T')
    TSF_Forth_samplerun("TSF_sample_TSFdoc")

def TSF_sample_about():    #TSFdoc:「sample_aboutTSF.tsf」コマンド版「TSF --about」。<br>TSF言語の簡易説明。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "echoTSF:","#!TSF_this","#!TSF_fin."]),'T')
    TSF_Forth_setTSF("echoTSF:","\t".join([
        "aboutTSF:","#!TSF_argvsthe","#!TSF_echoN","echoRPNcalc:","#!TSF_this"]),'T')
    TSF_Forth_setTSF("aboutTSF:","\t".join([
        "",
        "○「TSF_Tab-Separated-Forth」の簡略説明。",
        "",
        "　Forth風インタプリタ。単位はtsv文字列。文字列の事をカードと呼称。カードの束をスタックと呼称。スタックの集まりをデッキと呼称。",
        "　文字から始まる行はスタック名。タブで始まる行はカードの束。シバン「#!」で始まる行(改行のみの行含む)はコメント扱いで読み飛ばし。",
        "",
        "○TSF構文には4つの「th」スタック代名詞(冠詞含む)「this」「that」「the」「they」が存在。",
        "",
        "　「this」は実行中のスタック。#関数カードの指示通りにカードを「ドロー(積み下ろし)」したり「リターン(積み上げ)」したりする。",
        "　「that」は積込先のスタック。#関数カードの返り値や#関数カード以外のカードが積み上げられる。",
        "　「the」は指定スタック。変数や配列やテキスト保存先として扱いたいスタックを一時的に呼び出す。",
        "　「they」はスタック名一覧。新規スタック作成や既存スタック削除の時、スタック名一覧自体をスタックの様に扱って整理する事もできる。",
        "",
        "○TSF構文のスタック操作には4つの「p」スタック動詞「peek」「poke」「pull」「push」が存在。",
        "",
        "　「peek」スタックからカードを読み込む。読込先スタックはそのままに「that」スタックにカードが積まれるのでカードが増殖する形になる。",
        "　「poke」スタックにカードを書き込む。スタックのカードは上書きされるので上書きされたカードが消失する形になる。",
        "　「pull」スタックからカードを引き抜く。通常は引抜先スタックから「that」スタックにカードが移動する形になる。",
        "　「push」スタックにカードを差し込む。通常は引抜先スタックに「that」スタックからカードが移動する形になる。",
        "",
        "○TSF構文の副詞「FNCMVAQIRHL」と可算名詞「SDO」などの説明はaboutでは簡略。",
        "",
        "　#関数カードの、ドロー(積み下ろし)は「pullFthat」リターン(積み上げ)は「pushFthat」してるとも言える。",
        "　代名詞と動詞の間にある「F」などが副詞。スタックに最後に積まれたカード、表面カードを選択するので表択。",
        "　「peekNthe」等の「N」は積まれた順に番号を割り振り番号で読込カード指定するので順択、というようにどのカードをppppするのか明記します。",
        "",
        "○TSF式として2種類の電卓「#!TSF_RPN」「#!TSF_calc」が存在。",
        "　calcでは括弧や分数なども使えます。RPNは括弧を処理しない上に小数のみなので高速です。",
        "　calcの括弧内外でRPNを使う事は可能です。コンマ「,」を用いるとRPNとみなされます。",
        "　TSFには変数がないので「#!TSF_joinN」「#!TSF_join[]」などを用いてカードを連結して式文字列を作ります。",
        ""]),'N')
    TSF_Forth_setTSF("echoRPNcalc:","\t".join([
        "aboutRPNtest:","#!TSF_this","aboutRPNcalc:","#!TSF_argvsthe","#!TSF_echoN","echoURL:","#!TSF_this"]),'T')
    TSF_Forth_setTSF("aboutRPNtest:","\t".join([
        "▽「1 3 m1|2」を「[2],[1]/[0]- #!TSF_join[]」で連結した「1,3/m1|2-」を「#!TSF_RPN」電卓→","1","3","m1|2","[2],[1]/[0]-","#!TSF_join[]","#!TSF_RPN","2","#!TSF_joinN","#!TSF_echo","▽「1 , 3 / m1|2 -」を「6 #!TSF_join」で連結した「1,3/m1|2-」を「#!TSF_RPN」電卓→","1",",","3","/","m1|2","-","6","#!TSF_joinN","#!TSF_RPN","2","#!TSF_joinN","#!TSF_echo","▽「1 3 m1|2」を「[2]/[1]-[0] #!TSF_join[]」で連結した「1/3-m1|2」を「#!TSF_calc」電卓→","1","3","m1|2","[2]/[1]-[0]","#!TSF_join[]","#!TSF_calc","2","#!TSF_joinN","#!TSF_echo","▽「1 / 3 - m1|2 」を「5 #!TSF_join」で連結した「1/3-m1|2」を「#!TSF_calc」電卓→","1","/","3","-","m1|2","5","#!TSF_joinN","#!TSF_calc","2","#!TSF_joinN","#!TSF_echo","▽「#!TSF_calc」のショートカット文法で「[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2]」(演算内容は「1/3-m1|2」)→","[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2]","#!TSF_calc","2","#!TSF_joinN","#!TSF_echo"]),'T')
    TSF_Forth_setTSF("aboutCALCdata:","\t".join([
        "1","3","m1|2"]),'T')
    TSF_Forth_setTSF("aboutRPNcalc:","\t".join([
        "",
        "○「#!TSF_RPN」と「#!TSF_calc」の共通点や差異の補足。",
        "　演算子の「+」プラス「-」マイナスと符号の「p」プラス「m」マイナスは分けて表記。割り算の「/」と分数の「|」も分けて表記。",
        "　calcの出力結果は基本分数ですが、「,(1|3)」のように括弧の外側でコンマを使う事で計算結果をRPNに渡す事ができます。",
        "　条件演算子がRPNでは「Z」「z」「O」「o」「U」「u」ですがcalcでは「Z~」「z~」「O~」「o~」「U~」「u~」「N~」とチルダ追加です。",
        "　calcで追加した条件演算子「N~」は分母ゼロ「n|0」分岐用です。RPNではゼロ割り算発生時点で分母ゼロ「n|0」を出力します。",
        "　calcには演算を抑止する「:」演算子が含まれてるので条件演算子の結果にスタック名を直接指定する事でIF構文の代替になります。",
        ""]),'N')
    TSF_Forth_setTSF("echoURL:","\t".join([
        "aboutURL:","#!TSF_argvsthe","#!TSF_echoN"]),'T')
    TSF_Forth_setTSF("aboutURL:","\t".join([
        "○TSFの詳しい説明はローカルの「docs/index.html」かWeb上の「https://ooblog.github.io/TSF2KEV/」を確認してください(執筆中)。",
        "",
        "　Web版もTSF付属のローカル版も「docs/TSFindex.tsf」から「sample/TSFdoc.tsf」を用いて生成されてます。",
        "　TSFを用いると簡潔なプログラムが書けます。そしてこの「sample/sample_aboutTSF.tsf」文書自体もTSF言語で書かれてます。",
        "",
        "#! -- Copyright (c) 2017 ooblog --",
        "#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE"]),'N')
    TSF_Forth_samplerun("TSF_sample_about")

def TSF_sample_RPN():    #TSFdoc:「sample_RPN.tsf」コマンド版「TSF --RPN [1,3/m1|2-]」。<br>後置記法(逆ポーランド記法)による括弧を使わない電卓。結果は小数。<br>
    TSF_Forth_setTSF("RPN:","\t".join([
        "#!TSF_RPN","#!TSF_echo"]),'T')
    TSF_Forth_setTSF("RPNsetup:","\t".join([
        "RPNargvs:","#!TSF_that","#!TSF_argvs",",","#!TSF_sandwichN","RPNjump:","RPNargvs:","#!TSF_lenthe","#!TSF_peekNthe","#!TSF_this"]),'T')
    TSF_Forth_setTSF("RPNjump:","\t".join([
        "RPNdefault:","RPNdefault:","RPN:"]),'T')
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "RPNsetup:","#!TSF_this","#!TSF_fin."]),'T')
    TSF_Forth_setTSF("RPNdefault:","\t".join([
        "1,3/m1|2-","RPN:","#!TSF_this"]),'T')
    TSF_Forth_samplerun("TSF_sample_RPN")

def TSF_sample_calc():    #TSFdoc:「sample_calc.tsf」コマンド版「TSF --calc [1/3-m1|2]」。<br>中置記法による括弧を用いる電卓。結果は分数。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "calcsetup:","#!TSF_this","#!TSF_fin."]),'T')
    TSF_Forth_setTSF("calcsetup:","\t".join([
        "calcargvs:","#!TSF_that","#!TSF_argvs",",","#!TSF_sandwichN","calcjump:","calcargvs:","#!TSF_lenthe","#!TSF_peekNthe","#!TSF_this"]),'T')
    TSF_Forth_setTSF("calcjump:","\t".join([
        "calcdefault:","calcdefault:","calc:"]),'T')
    TSF_Forth_setTSF("calcdefault:","\t".join([
        "1/3-m1|2","calc:","#!TSF_this"]),'T')
    TSF_Forth_setTSF("calc:","\t".join([
        "#!TSF_calc","#!TSF_echo"]),'T')
    TSF_Forth_samplerun("TSF_sample_calc")

def TSF_sample_calcJA():    #TSFdoc:「sample_calc.tsf」コマンド版「TSF --calc [一割る三引くマイナス二分の一]」。<br>中置記法による括弧を用いる電卓。結果は漢数字(〇一二三四五六七八九の表示はアラビア数字も用いる)。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "calcsetup:","#!TSF_this","#!TSF_fin."]),'T')
    TSF_Forth_setTSF("calcsetup:","\t".join([
        "calcdef:","#!TSF_that","#!TSF_argvs","#!TSF_pullFthat","#!TSF_calcJA","#!TSF_echo"]),'T')
    TSF_Forth_setTSF("calcdef:","\t".join([
        "1/3-m1|2"]),'N')
    TSF_Forth_samplerun("TSF_sample_calcJA")

def TSF_sample_calender():    #TSFdoc:「sample_calender.tsf」コマンド版「TSF --calender」。<br>現在時刻を「@4y@0m@0dm@wdec@0h@0n@0s」形式で表示(@wdecは曜日MTWRFSU表記)。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#!TSF_argvs","#!TSF_pullFthat","calender:","#!TSF_this","#!TSF_fin.","@4y@0m@0dm@wdec@0h@0n@0s"]),'T')
    TSF_Forth_setTSF("calender:","\t".join([
        "#!TSF_calender","#!TSF_echo"]),'T')
    TSF_Forth_samplerun("TSF_sample_calender")

def TSF_sample_FizzBuzz():    #TSFdoc:「sample_fizzbuzz.tsf」コマンド版「TSF --fizzbuzz [20]」。<br>3の倍数の時はFizz、5の倍数の時はBuzzを表示する。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#!TSF_argvs","#!TSF_pullFthat","FZcount:","#!TSF_pushFthe","FBloop:","#!TSF_this","#!TSF_fin.","20"]),'T')
    TSF_Forth_setTSF("FBloop:","\t".join([
        "FZcount:",",([FZcount:0]+1)","#!TSF_-calc","FZcount:","0","#!TSF_pokeNthe","([FZcount:0]#3Z~1~0)+([FZcount:0]#5Z~2~0)","#!TSF_calc","#!TSF_peekNthe","#!TSF_echo","[FZcount:4]-[FZcount:0]o~FBloop:~#!exit:","#!TSF_calc","#!TSF_this"]),'T')
    TSF_Forth_setTSF("FZcount:","\t".join([
        "0","Fizz","Buzz","Fizz&Buzz"]),'T')
    TSF_Forth_samplerun("TSF_sample_FizzBuzz")

def TSF_sample_zundoko():    #TSFdoc:「sample_zundoko.tsf」コマンド版「TSF --zundoko [4]」。<br>「zun zun zun zun doko」になるまで「zun」と「doko」をランダム表示。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#!TSF_argvs","#!TSF_pullFthat","ZDcount:","0","#!TSF_pokeNthe","ZDreset:","#!TSF_this","#!TSF_fin.","4"]),'T')
    TSF_Forth_setTSF("ZDreset:","\t".join([
        "0","ZDcount:","#!TSF_pokeFthe","ZunDoko:","#!TSF_this"]),'T')
    TSF_Forth_setTSF("ZunDoko:","\t".join([
        "ZDjump:","#!TSF_peekAthe","#!TSF_this","[ZDcount:0]O~ZunDoko:~#exit:","#!TSF_calc","#!TSF_this"]),'T')
    TSF_Forth_setTSF("ZDjump:","\t".join([
        "Zun:","Doko:"]),'T')
    TSF_Forth_setTSF("Zun:","\t".join([
        "Zun","#!TSF_echo","[ZDcount:1],1+","#!TSF_calc","ZDcount:","#!TSF_pokeFthe"]),'T')
    TSF_Forth_setTSF("Doko:","\t".join([
        "Doko","#!TSF_echo","[ZDcount:0]-[ZDcount:1]Z~VeronCho:~ZDreset:","#!TSF_calc","#!TSF_this"]),'T')
    TSF_Forth_setTSF("VeronCho:","\t".join([
        "VeronCho","#!TSF_echo","-1","ZDcount:","0","#!TSF_pokeNthe"]),'T')
    TSF_Forth_setTSF("ZDcount:","\t".join([
        "4","0"]),'T')
    TSF_Forth_samplerun("TSF_sample_zundoko")

def TSF_sample_99beer():    #TSFdoc:「sample_99beer.tsf」コマンド版「TSF --99bear [9]」。<br>99 Bottles of Beer(http://99-bottles-of-beer.net/lyrics.html)を出力する。長いので初期値は9に設定。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "#!TSF_argvs","#!TSF_pullFthat","bottlessetup:","#!TSF_this","#!TSF_fin.","9"]),'T')
    TSF_Forth_setTSF("bottlessetup:","\t".join([
        "onthewallint:","#!TSF_pushFthe","onthewallint:","#!TSF_that","#!TSF_peekFthat","#!TSF_peekFthat","callbottles:","#!TSF_this"]),'T')
    TSF_Forth_setTSF("callbottles:","\t".join([
        "#!TSF_swapBA","#!TSF_pullFthat","#!TSF_peekFthat","[0],1-","#!TSF_join[]","#!TSF_-calc","N-bottles:","bottlescall:","[onthewallint:1]","#!TSF_calc","#!TSF_peekMthe","#!TSF_clonethe","N-bottles:","onthewallstr:","onthewallint:","#!TSF_replacesQSN","N-bottles:","#!TSF_argvsthe","#!TSF_echoN","[onthewallint:1]o~callbottles:~#!exit:","#!TSF_calc","#!TSF_this"]),'T')
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

def TSF_sample_quine():    #TSFdoc:「sample_quine.tsf」コマンド版「TSF --quine」。<br>「sample_quine.tsf」は「sample_quine.tsf」自身を出力する。<br>同様に「trans_quine.d」の時は「trans_quine.d」、「trans_quine.py」の時は「trans_quine.py」を出力する。<br>コマンド「TSF --quine」時も「sample_quine.tsf」を出力。<br>
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "quine_echo:","#!TSF_this","#!TSF_fin."]),'T')
    TSF_Forth_setTSF("quine_echo:","\t".join([
        "#!TSF_mainfile","#!TSF_fileext","quine_ext:","quine_view:","#!TSF_casesQON","#!TSF_this"]),'T')
    TSF_Forth_setTSF("quine_ext:","\t".join([
        ".tsf",".py",".d"]),'T')
    TSF_Forth_setTSF("quine_view:","\t".join([
        "quine_TSF:","quine_Python:","quine_D:","#!exit:"]),'T')
    TSF_Forth_setTSF("quine_TSF:","\t".join([
        "#! /usr/bin/env TSF","#!TSF_echo","#!TSF_viewthey"]),'T')
    TSF_Forth_setTSF("quine_Python:","\t".join([
        "#!TSF_Python"]),'N')
    TSF_Forth_setTSF("quine_D:","\t".join([
        "#!TSF_D-lang"]),'N')
    TSF_Forth_samplerun("TSF_sample_quine")

#TSFdoc:D言語のmain関数。ここでは「TSF --dlang」「TSF --python」コマンドの解説。<br>「TSF --dlang helloworld.d helloworld.d」「TSF --python helloworld.tsf helloworld.py」のようにTSFをD言語やPythonに変換した風(インタプリタを呼び出す形)にすることができる。<br>D言語の場合「TSF_DMDcompile.sh helloworld.d」で実行バイナリも作成可能。<br>
TSF_sysargvs=TSF_Io_argvs(sys.argv)
TSF_Initcallrun=[TSF_Forth_Initcards,TSF_Calc_Initcards,TSF_Time_Initcards,TSF_Urlpath_Initcards,TSF_Match_Initcards,TSF_Trans_Initcards]
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
elif TSF_bootcommand in ["--zun","--doko","--zundoko"]:
    TSF_sample_zundoko()
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
