#! /usr/bin/env rdmd

import std.stdio;
import std.file;
import std.path;
import std.array;
import std.algorithm;
import core.vararg;
import std.typecons;
import std.string;

import TSF_Io;
import TSF_Forth;
import TSF_Shuffle;
import TSF_Calc;
//import TSF_Time;
import TSF_Match;
import TSF_Trans;


void TSF_sample_help(){    //#TSFdoc:「sample_help.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "help:","#TSF_argvsthe","#TSF_echoN","#TSF_fin."],"\t"),"T");
    TSF_Forth_setTSF("help:",join([
        "usage: ./TSF [command|file.tsf] [argvs] ...",
        "commands & samples:",
        "  --help        this commands view",
        "  --python      TSF to Python",
        "  --dlang       TSF to D",
        "  --about       about TSF mini guide",
        "  --helloworld  \"Hello world  #TSF_echo\" sample",
        "  --RPN         decimal RPN calculator \"1,3/m1|2-\"-> 0.8333... ",
        "  --calc        fraction calculator \"1/3-m1|2\"-> p5|6",
        "  --fizzbuzz    Fizz(#3) Buzz(#5) Fizz&Buzz(#15) sample",
        "  --99bear      99 Bottles of Beer 9 Bottles sample"],"\t"),"N");
    TSF_Forth_samplerun("TSF_sample_help");
}

void TSF_sample_Helloworld(){    //#TSFdoc:「sample_helloworld.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "Hello world","#TSF_echo"],"\t"),"T");
    TSF_Forth_samplerun("TSF_sample_Helloworld");
}

void TSF_sample_about(){    //#TSFdoc:「sample_aboutTSF.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "echoTSF:","#TSF_this","#TSF_fin."],"\t"),"T");
    TSF_Forth_setTSF("echoTSF:",join([
        "aboutTSF:","#TSF_argvsthe","#TSF_echoN","echoRPNcalc:","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("aboutTSF:",join([
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
        "　TSFにループ構文は存在しないので末尾再帰がループになる。末尾だけじゃなくループの外側スタックを呼び出しても呼び出し先までのコールスタックが破棄される。",
        "　TSFにはif構文も存在しないけど「#TSF_calc」の条件演算子や「#TSF_this」の飛び先に「#TSF_peekNthe」などを組み合わせる事で分岐は可能。",
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
        ""],"\t"),"N");
    TSF_Forth_setTSF("echoRPNcalc:",join([
        "aboutRPNtest:","#TSF_this","aboutRPNcalc:","#TSF_argvsthe","#TSF_echoN","echoTIME:","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("aboutRPNtest:",join([
        "▽「1 3 m1|2」を「[2],[1]/[0]- #TSF_join[]」で連結して「#TSF_RPN」→","1","3","m1|2","[2],[1]/[0]-","#TSF_join[]","#TSF_RPN","2","#TSF_joinN","#TSF_echo","▽「1 , 3 / m1|2 -」を「6 #TSF_join」で連結して「#TSF_RPN」→","1",",","3","/","m1|2","-","6","#TSF_joinN","#TSF_RPN","2","#TSF_joinN","#TSF_echo","▽「1 3 m1|2」を「[2]/[1]-[0] #TSF_join[]」で連結して「#TSF_calc」→","1","3","m1|2","[2]/[1]-[0]","#TSF_join[]","#TSF_calc","2","#TSF_joinN","#TSF_echo","▽「1 / 3 - m1|2 」を「5 #TSF_join」で連結して「#TSF_calc」→","1","/","3","-","m1|2","5","#TSF_joinN","#TSF_calc","2","#TSF_joinN","#TSF_echo","▽スタックからショートカットで「[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2] を「#TSF_calc」→","[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2]","#TSF_calc","2","#TSF_joinN","#TSF_echo","▽漢数字テスト「億千万」を「#TSF_calcJA」→","億千万","#TSF_calcJA","2","#TSF_joinN","#TSF_echo"],"\t"),"T");
    TSF_Forth_setTSF("aboutCALCdata:",join([
        "1","3","m1|2"],"\t"),"T");
    TSF_Forth_setTSF("aboutRPNcalc:",join([
        "",
        "○「#TSF_RPN」逆ポーランド小数電卓の概要。",
        "",
        "　TSFでは高速処理を目指すRPNと多機能に備えるcalcの2種類の電卓を用意。",
        "　RPNでは「1+2」は「1,2+」になる。数値同士はコンマで区切る。掛け算が先に演算されるなど優先順序が存在する数式は「calc」を使う。",
        "　演算子の「+」プラス「-」マイナスと符号の「p」プラス「m」マイナスは分けて表記。「1-(-2)」も「1,m2-」と表記する。",
        "　演算子の「/」と分数の「|」も分けて表記。分数二分の一「1|2」は小数「0.5」だが１÷２の割り算として表現する場合は「1,2/」と表記する。",
        "　通常の割り算の他にも1未満を切り捨てる「\\」、余りを求める「#」がある。マイナス剰余は「5#m4」だと「4-(5#4)」のように計算する。",
        "　計算結果が整数になる場合、および小数の丸めで整数になってしまった場合は整数表記になる。",
        "　RPNではゼロ「0|1」で割った時は分母ゼロ「n|0」を出力して終了。計算続行はされないので注意。",
        "　「Z」はゼロ比較演算子(条件演算子)。「1,2,0Z」はゼロの時は真なので左の数値(1)、ゼロでない時は偽なので右の数値(2)を採用。",
        "　「O」「o」「U」「u」も同様に、ゼロ以上(ゼロ含む)、ゼロより大きい、ゼロ以下(ゼロ含む)、ゼロ未満で左右の数値を選択。",
        "　条件演算子とスタック名(演算を行わない「:」演算子)を組み合わせる事で、「#TSF_this」に渡すスタック名を分岐できます。",
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
        ""],"\t"),"N");
    TSF_Forth_setTSF("echoTIME:",join([
        "aboutTIMEtest:","#TSF_this","aboutTIME:","#TSF_argvsthe","#TSF_echoN"],"\t"),"T");
    TSF_Forth_setTSF("aboutTIMEtest:",join([
        "▽「time」系は準備中","#TSF_echo"],"\t"),"T");
    TSF_Forth_setTSF("aboutTIME:",join([
        "",
        "○「time」系分数電卓も再開発中につき説明不足になります。",
        "",
        "　時刻取得の方法が文字列置換なので、改行やタブ文字などもエスケープ置換も予定。",
        "　時刻の取得ついでに乱数の取得も一ヶ所に集める予定。",
        ""],"\t"),"N");
    TSF_Forth_samplerun("TSF_sample_about");
}

void TSF_sample_RPN(){    //#TSFdoc:「sample_RPN.tsf」コマンド版。
    TSF_Forth_setTSF("RPN:",join([
        "#TSF_RPN","#TSF_echo"],"\t"),"T");
    TSF_Forth_setTSF("RPNsetup:",join([
        "RPNargvs:","#TSF_that","#TSF_argvs",",","#TSF_sandwichN","RPNjump:","RPNargvs:","#TSF_lenthe","#TSF_peekNthe","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("RPNjump:",join([
        "RPNdefault:","RPNdefault:","RPN:"],"\t"),"T");
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "RPNsetup:","#TSF_this","#TSF_fin."],"\t"),"T");
    TSF_Forth_setTSF("RPNdefault:",join([
        "1,3/m1|2-","RPN:","#TSF_this"],"\t"),"T");
    TSF_Forth_samplerun("TSF_sample_RPN");
}

void TSF_sample_calc(){    //#TSFdoc:「sample_calc.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "calcsetup:","#TSF_this","#TSF_fin."],"\t"),"T");
    TSF_Forth_setTSF("calcsetup:",join([
        "calcargvs:","#TSF_that","#TSF_argvs",",","#TSF_sandwichN","calcjump:","calcargvs:","#TSF_lenthe","#TSF_peekNthe","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("calcjump:",join([
        "calcdefault:","calcdefault:","calc:"],"\t"),"T");
    TSF_Forth_setTSF("calcdefault:",join([
        "1/3-m1|2","calc:","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("calc:",join([
        "#TSF_calc","#TSF_echo"],"\t"),"T");
    TSF_Forth_samplerun("TSF_sample_calc");
}

void TSF_sample_calcJA(){    //#TSFdoc:「sample_calcJA.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "calcsetup:","#TSF_this","#TSF_fin."],"\t"),"T");
    TSF_Forth_setTSF("calcsetup:",join([
        "calcdef:","#TSF_that","#TSF_argvs","#TSF_pullFthat","#TSF_calcJA","#TSF_echo"],"\t"),"T");
    TSF_Forth_setTSF("calcdef:",join([
        "1/3-m1|2"],"\t"),"N");
    TSF_Forth_samplerun("TSF_sample_calc");
}

void TSF_sample_FizzBuzz(){    //#TSFdoc:「sample_fizzbuzz.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "FBsetup:","#TSF_this","#TSF_fin."],"\t"),"T");
    TSF_Forth_setTSF("FBsetup:",join([
        "FZcount:","#TSF_that","#TSF_argvs","#TSF_pullFthat","#TSF_peekFthat","FZcount:","4","#TSF_pokeNthe","FBloop:","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("FBloop:",join([
        "FZcount:",",([FZcount:0]+1)","#TSF_calc","FZcount:","0","#TSF_pokeNthe","([FZcount:0]#3Z~1~0)+([FZcount:0]#5Z~2~0)","#TSF_calc","#TSF_peekNthe","#TSF_echo","[FZcount:4]-[FZcount:0]o~FBloop:~#exit:","#TSF_calc","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("FZcount:",join([
        "0","Fizz","Buzz","Fizz&Buzz","20"],"\t"),"T");
    TSF_Forth_samplerun("TSF_sample_calc");
}

void TSF_sample_99beer(){    //#TSFdoc:「sample_99beer.tsf」コマンド版。
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "#TSF_argvs","#TSF_pullFthat","bottlessetup:","#TSF_this","#TSF_fin.","9"],"\t"),"T");
    TSF_Forth_setTSF("bottlessetup:",join([
        "onthewallint:","#TSF_pushFthe","onthewallint:","#TSF_that","#TSF_peekFthat","#TSF_peekFthat","callbottles:","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("callbottles:",join([
        "#TSF_swapBA","#TSF_pullFthat","#TSF_peekFthat","[0],1-","#TSF_join[]","#TSF_-calc","N-bottles:","bottlescall:","[onthewallint:1]","#TSF_calc","#TSF_peekMthe","#TSF_clonethe","N-bottles:","onthewallstr:","onthewallint:","#TSF_replacesN","N-bottles:","#TSF_argvsthe","#TSF_echoN","[onthewallint:1]o~callbottles:~#exit:","#TSF_calc","#TSF_this"],"\t"),"T");
    TSF_Forth_setTSF("onthewallstr:",join([
        "{buybottles}","{drink}","{drinked}"],"\t"),"T");
    TSF_Forth_setTSF("bottlescall:",join([
        "nomorebottles:","1bottle:","2bottles:","3ormorebottles:"],"\t"),"T");
    TSF_Forth_setTSF("3ormorebottles:",join([
        "{drink} bottles of beer on the wall, {drink} bottles of beer.",
        "Take one down and pass it around, {drinked} bottles of beer on the wall."],"\t"),"N");
    TSF_Forth_setTSF("2bottles:",join([
        "{drink} bottles of beer on the wall, {drink} bottles of beer.",
        "Take one down and pass it around, 1 bottle of beer on the wall."],"\t"),"N");
    TSF_Forth_setTSF("1bottle:",join([
        "{drink} bottle of beer on the wall, {drink} bottle of beer.",
        "Take one down and pass it around, no more bottles of beer on the wall."],"\t"),"N");
    TSF_Forth_setTSF("nomorebottles:",join([
        "No more bottles of beer on the wall, no more bottles of beer.",
        "Go to the store and buy some more, {buybottles} bottles of beer on the wall."],"\t"),"N");
    TSF_Forth_samplerun("TSF_sample_99beer");
}

void main(string[] sys_argvs){
    string[] TSF_sysargvs=TSF_Io_argvs(sys_argvs);
    void function(ref string function()[string],ref string[])[] TSF_Initcallrun=[&TSF_Forth_Initcards,&TSF_Shuffle_Initcards,&TSF_Calc_Initcards,&TSF_Match_Initcards,&TSF_Trans_Initcards];
    string TSF_bootcommand=TSF_sysargvs.length<2?"":TSF_sysargvs[1];
    TSF_Forth_initTSF(TSF_sysargvs[1..$],TSF_Initcallrun);
    if( exists(TSF_bootcommand) && TSF_Forth_loadtext(TSF_bootcommand,TSF_bootcommand).length>0 ){
        TSF_Forth_merge(TSF_bootcommand,null,true);
        chdir(dirName(absolutePath(TSF_bootcommand)));
        TSF_Forth_samplerun();
    }
    else if( count(["--py","--python","--Python"],TSF_bootcommand) ){
        if( TSF_sysargvs.length>=4 ){
            TSF_Trans_generator_python(TSF_sysargvs[2],TSF_sysargvs[3]);
        }
        else if( TSF_sysargvs.length>=3 ){
            TSF_Trans_generator_python(TSF_sysargvs[2]);
        }
    }
    else if( count(["--py","--d","--D","--dlang"],TSF_bootcommand) ){
        if( TSF_sysargvs.length>=4 ){
            TSF_Trans_generator_dlang(TSF_sysargvs[2],TSF_sysargvs[3]);
        }
        else if( TSF_sysargvs.length>=3 ){
            TSF_Trans_generator_dlang(TSF_sysargvs[2]);
        }
    }
    else if( count(["--help","--commands"],TSF_bootcommand) ){
        TSF_sample_help();
    }
    else if( count(["--about","--aboutTSF"],TSF_bootcommand) ){
        TSF_sample_about();
    }
    else if( count(["--hello","--helloworld","--Helloworld"],TSF_bootcommand) ){
        TSF_sample_Helloworld();
    }
    else if( count(["--RPN","--rpn"],TSF_bootcommand) ){
        TSF_sample_RPN();
    }
    else if( count(["--CALC","--Calc","--calc"],TSF_bootcommand) ){
        TSF_sample_calc();
    }
    else if( count(["--calcJA"],TSF_bootcommand) ){
        TSF_sample_calcJA();
    }
    else if( count(["--fizz","--buzz","--fizzbuzz","--FizzBuzz"],TSF_bootcommand) ){
        TSF_sample_FizzBuzz();
    }
    else if( count(["--99beer","--9beer","--beer99","--beer9","--beer","--99","--9"],TSF_bootcommand) ){
        TSF_sample_99beer();
    }
    else{
        TSF_sample_help();
    }
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
