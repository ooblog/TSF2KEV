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
#from TSF_Time import *
from TSF_Match import *
from TSF_Trans import *


def TSF_sample_help():    #TSFdoc:「sample_help.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "help:","#TSF_argvsthe","#TSF_echoN","#TSF_fin."]),"T")
    TSF_Forth_setTSF("help:","\t".join([
        "usage: ./TSF.py [command|file.tsf] [argvs] ...",
        "commands & samples:",
        "  --help        this commands view",
        "  --python      TSF to Python",
        "  --dlang       TSF to D",
        "  --about       about TSF mini guide",
        "  --helloworld  \"Hello world  #TSF_echo\" sample",
        "  --RPN         decimal RPN calculator \"1,3/m1|2-\"-> 0.8333... "]),"N")
    TSF_Forth_samplerun("TSF_sample_help")

def TSF_sample_Helloworld():    #TSFdoc:「sample_helloworld.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "Hello world","#TSF_echo"]),"T")
    TSF_Forth_samplerun("TSF_sample_Helloworld")

def TSF_sample_about():    #TSFdoc:「sample_aboutTSF.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "echoTSF:","#TSF_this","#TSF_fin."]),"T")
    TSF_Forth_setTSF("echoTSF:","\t".join([
        "aboutTSF:","#TSF_argvsthe","#TSF_echoN","echoRPN:","#TSF_this"]),"T")
    TSF_Forth_setTSF("aboutTSF:","\t".join([
        "",
        "○「TSF_Tab-Separated-Forth」の概要(開発予定の話も含みます)。",
        "",
        "　Forth風インタプリタ。単位はtsv文字列。文字列の事をカードと呼称。カードの束をスタックと呼称。スタックの集まりをデッキと呼称。",
        "　ソースコード.tsfで文字から始まる行はスタック名、タブで始まる行はカード。スタック名の宣言とカードの積み込みはワンライナー記述も可能。",
        "　改行のみもしくは「#」で始まる行は読み飛ばし。「#」は「#関数カード」として使うので「#」で始まるスタック名は予約ワード扱い。",
        "",
        "○TSFには4つの「th」、スタック代名詞「this」「that」「the」「they」という概念が存在する(theは厳密には冠詞だが便宜上代名詞扱い)。",
        "",
        "　「this」は実行中のスタック。#関数カードの指示通りにカードを「ドロー(積み下ろし)」したり「リターン(積み上げ)」したりする。",
        "　#関数カードではないカードは後述の「that」スタックに積み上げられる。関数の返り値ではないのでリターンとは呼ばない。",
        "　オーバーフローもしくは「#exit #TSF_this」のように存在しないスタックに入る行為でオーバーフローを発生させてスタックから抜ける。",
        "　TSFにループ構文は存在しないので末尾再帰がループになる。同様にループの内側からループの外側スタックを呼び出してもコールスタックが破棄される。",
        "　TSFにはif構文も存在しないので「#TSF_this」の飛び先を事前に書き換える形になる。条件演算子は「#TSF_RPN」「#TSF_calc」の中にある。",
        "　「that」は積込先のスタック。#関数カードの返り値や#関数カード以外のカードが積み上げられる。",
        "　「the」は指定スタック。変数や配列やテキスト保存先として扱ってるスタックが一時的に呼び出される場合の文字通り代名詞。",
        "　「they」はスタック名一覧。スタック名一覧自体もカード束としてスタックの様に扱える場合がある。",
        "",
        "○TSFのスタック操作に4つの「p」、スタック動詞「peek」「poke」「pull」「push」が存在する。",
        "",
        "　「peek」スタックからカードを読み込む。読込先スタックはそのままに「that」スタックにカードが積まれるのでカードが増殖る形になる。",
        "　「poke」スタックにカードを書き込む。スタックのカードは上書きされるので上書きされたカードが消失する形になる。",
        "　「pull」スタックからカードを引き抜く。引抜先スタックから「that」スタックにカードが移動する形になる。",
        "　「push」スタックにカードを差し込む。引抜先スタックに「that」スタックからカードが移動する形になる。",
        "",
        "　※ドローは「pullFthat」、リターンは「pushFthat」、してるとも言える。",
        "",
        "○TSFのスタック操作で選択するカード位置の副詞「F,N,C,M,V,A…」を用意する予定。※「F」「N」「M」以外の副詞は準備中です。",
        "",
        "　「F」(Front)スタックから表択、一番上に積まれたカード(tsv表現では末尾の文字列)を選択。",
        "　「N」(Number)スタックから順択、一番下のカード(tsv表現では右端の文字列)をゼロとして数値指定で選択。",
        "　「C」(Cycle)スタックから周択、「N」のカウント数がスタックを上回る場合、ゼロから数え直す。",
        "　「M」(liMit)スタックから囲択、「N」のカウント数がスタックを上回る場合、「F」と同様。下回る場合ゼロ。",
        "　「V」(reVerse)スタックから逆択、「N」のカウントが逆順になる。一番上のカード(tsv表現では左端の文字列)をゼロとして数値指定で選択。",
        "　「A」(rAndom)スタックから乱択、ランダムに選択。乱数の定義が絡む場合は「N」を用いて別な所から乱数を準備すべき。",
        "　「Q」(eQual)スタックから同択、文字列と同じカードを選択。カードの枚数は動詞による。",
        "　「I」(In)スタックから含択、文字列が含まれるカードを選択。カードの枚数は動詞による。",
        "　「R」(reseaRch)スタックから規択、正規表現に該当するカードを選択。カードの枚数は動詞による。TSFを実装する言語毎に正規表現の方言が存在する問題。",
        "　「H」(matcHer)スタックから似択、文字列の一致度が一定数以上のカードを選択。Python以外の言語で一致度の基準が未定義。",
        "　「L」(Label)スタックから札択、ラベル付カードを選択。L:Tsvを読み込む場合などに使用。",
        ""]),"N")
    TSF_Forth_setTSF("echoRPN:","\t".join([
        "aboutRPNtest:","#TSF_this","aboutRPN:","#TSF_argvsthe","#TSF_echoN","echoCALC:","#TSF_this"]),"T")
    TSF_Forth_setTSF("aboutRPNtest:","\t".join([
        "▽「1 3 m1|2」を「[2],[1]/[0]- #TSF_join[]」で連結→","1","3","m1|2","[2],[1]/[0]-","#TSF_join[]","#TSF_RPN","2","#TSF_joinN","#TSF_echo","▽「1 , 3 / m1|2 -」を「#TSF_join」で連結→","1",",","3","/","m1|2","-","6","#TSF_joinN","#TSF_RPN","2","#TSF_joinN","#TSF_echo"]),"T")
    TSF_Forth_setTSF("aboutRPN:","\t".join([
        "",
        "○「RPN」系小数電卓の概要。",
        "",
        "　TSFでは機能を絞って高速処理をめざすRPNと多機能をめざすcalcの2種類の電卓を用意。RPN(逆ポーランド記法)では括弧を用いません。",
        "　RPNでは「1+2」は「1,2+」になる。数値同士はコンマで区切る。掛け算が先に演算されるなど優先順序が存在する数式は「calc」を使う。",
        "　演算子の「+」プラス「-」マイナスと符号の「p」プラス「m」マイナスは分けて表記。「1-(-2)」を「1,m2-」と表記する。",
        "　演算子の「/」と分数の「|」も分けて表記。分数二分の一「1|2」は小数「0.5」だが１÷２の割り算として表現する場合は「1,2/」と表記する。",
        "　計算結果が整数になる場合、および小数の丸めで整数になってしまった場合は整数表記になる。",
        "　通常の割り算の他にも1未満を切り捨てる「\\」、余りを求める「#」がある。",
        "　RPNではゼロで割った時は「n|0」を出力して終了。条件演算子の可能性とかは考慮されない。",
        "　「Z」はゼロ比較演算子(条件演算子)。「1,2,0Z」はゼロの時は真なので左の数値(1)、ゼロでない時は偽なので右の数値(2)を採用。",
        "　「O」「o」「U」「u」も同様に、ゼロ以上(ゼロ含む)、ゼロより大きい、ゼロ以下(ゼロ含む)、ゼロ未満で左右の数値を選択。",
        "　条件演算子は何に使うかというと「#TSF_this」の飛び先を変更するため「#TSF_peekthe」などと組み合わせます。",
        ""]),"N")
    TSF_Forth_setTSF("echoCALC:","\t".join([
        "aboutCALCtest:","#TSF_this","aboutCALC:","#TSF_argvsthe","#TSF_echoN","echoTIME:","#TSF_this"]),"T")
    TSF_Forth_setTSF("aboutCALCtest:","\t".join([
        "▽「calc」系準備中","#TSF_echo"]),"T")
    TSF_Forth_setTSF("aboutCALC:","\t".join([
        "",
        "○「calc」系分数電卓は再開発中につき説明不足になります(RPNと共通する内容は圧縮)。",
        "",
        "　calcは括弧と分数も使えます。RPN(小数)も混在できます。分数を用いる事で桁溢れや丸め誤差をなるだけ回避する事を目標とします。",
        "　calcではRPNとは事なり、括弧が無くても「小数の分数化＞掛け算系＞足し算系＞条件演算子」のような計算順序が存在します。",
        "　calcでは「n|0」が発生しても条件演算子や後述する「@」の可能性などを考慮して計算は続行されます。",
        "　「#TSF_peekNthe」や「#TSF_join[]」などを別途用いる事無く「[data:2]/[data:1]-[data:0]」のようにショートカットできます。",
        "　「@」演算子導入と条件演算子の組み合わせで「#TSF_this」の飛び先を直接指定できる様にする予定。",
        "　億千万円銭など通貨的な助数詞を扱う「#TSF_calcJA」なども予定。",
        ""]),"N")
    TSF_Forth_setTSF("echoTIME:","\t".join([
        "aboutTIMEtest:","#TSF_this","aboutTIME:","#TSF_argvsthe","#TSF_echoN"]),"T")
    TSF_Forth_setTSF("aboutTIMEtest:","\t".join([
        "▽「time」系は準備中","#TSF_echo"]),"T")
    TSF_Forth_setTSF("aboutTIME:","\t".join([
        "",
        "○「time」系分数電卓も再開発中につき説明不足になります。",
        "",
        "　時刻取得の方法が文字列置換なので、改行やタブ文字なども置換。",
        "　大抵の言語では乱数の生成がマシン時刻に依存してるはずなので時刻の取得と乱数の取得も一ヶ所に集める予定。",
        ""]),"N")
    TSF_Forth_samplerun("TSF_sample_about")

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
    TSF_Forth_samplerun("TSF_sample_RPN")


TSF_sysargvs=TSF_Io_argvs(sys.argv)
TSF_Initcallrun=[TSF_Forth_Initcards,TSF_Shuffle_Initcards,TSF_Calc_Initcards,TSF_Match_Initcards,TSF_Trans_Initcards]
TSF_Forth_initTSF(TSF_sysargvs[1:],TSF_Initcallrun)
TSF_bootcommand="" if len(TSF_sysargvs) < 2 else TSF_sysargvs[1]
if os.path.isfile(TSF_bootcommand) and len(TSF_Forth_loadtext(TSF_bootcommand,TSF_bootcommand)):
    TSF_Forth_merge(TSF_bootcommand,[],True)
    os.chdir(os.path.dirname(os.path.normpath(TSF_bootcommand)))
    TSF_Forth_samplerun()
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
