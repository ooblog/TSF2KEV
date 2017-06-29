# プログラミング言語「TSF_Tab-Separated-Forth」開発中。

目標は「[TSF2KEV/kanedit.vim](https://github.com/ooblog/TSF2KEV/blob/master/KEV2/kanedit.vim "TSF2KEV/kanedit.vim at master ooblog/TSF2KEV")」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonとD言語で。  
TSFはまだ開発中なので、漢直やkan5x5フォントをお探しの方は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」をお使いください。  
未整備の箇所もあるけどHTML版のドキュメント「[TSF2KEV(https://ooblog.github.io/TSF2KEV/)](https://ooblog.github.io/TSF2KEV/ "「TSF2KEV」はプログラミング言語「TSF_Tab-Separated-Forth」のD言語とPythonによる実装です。")」も制作中。  
![TSF syntax image](https://github.com/ooblog/TSF2KEV/blob/master/docs/TSF_512x384.png "TSF2KEV/TSF_512x384.png at master ooblog/TSF2KEV")  

## 簡易版TSF解説「sample_aboutTSF.tsf」。
「[sample_aboutTSF.tsf](https://github.com/ooblog/TSF2KEV/blob/master/sample/sample_aboutTSF.tsf "TSF2KEV/sample_aboutTSF.tsf at master ooblog/TSF2KEV")」は「./TSF.d --about」「./TSF.py --about」でも確認できます。  

    #! /usr/bin/env TSF    
    TSF_Tab-Separated-Forth:    
    	echoTSF:	#TSF_this	#TSF_fin.    
    echoTSF:    
    	aboutTSF:	#TSF_argvsthe	#TSF_echoN	echoRPNcalc:	#TSF_this    
    aboutTSF:    
    	    
    	○「TSF_Tab-Separated-Forth」の簡略説明。    
    	    
    	　Forth風インタプリタ。単位はtsv文字列。文字列の事をカードと呼称。カードの束をスタックと呼称。スタックの集まりをデッキと呼称。    
    	　文字から始まる行はスタック名。タブで始まる行はカードの束。シバン「#!」で始まる行(改行のみの行含む)はコメント扱いで読み飛ばし。    
    	    
    	○TSF構文には4つの「th」、スタック代名詞「this」「that」「the」「they」が存在。    
    	    
    	　「this」は実行中のスタック。#関数カードの指示通りにカードを「ドロー(積み下ろし)」したり「リターン(積み上げ)」したりする。    
    	　「that」は積込先のスタック。#関数カードの返り値や#関数カード以外のカードが積み上げられる。    
    	　「the」は指定スタック。変数や配列やテキスト保存先として扱ってるスタックが一時的に呼び出される場合の文字通り代名詞。    
    	　「they」はスタック名一覧。スタック名一覧自体もカード束としてスタックの様に扱える場合がある。    
    	    
    	○TSF構文のスタック操作に4つの「p」、スタック動詞「peek」「poke」「pull」「push」が存在する。    
    	    
    	　「peek」スタックからカードを読み込む。読込先スタックはそのままに「that」スタックにカードが積まれるのでカードが増殖る形になる。    
    	　「poke」スタックにカードを書き込む。スタックのカードは上書きされるので上書きされたカードが消失する形になる。    
    	　「pull」スタックからカードを引き抜く。引抜先スタックから「that」スタックにカードが移動する形になる。    
    	　「push」スタックにカードを差し込む。引抜先スタックに「that」スタックからカードが移動する形になる。    
    	    
    	○TSF構文の副詞「FNCMVAQIRHL」と数量詞「SDO」などの説明は省略。    
    	    
    	　※#関数カードの、ドロー(積み下ろし)は「pullFthat」リターン(積み上げ)は「pushFthat」してるとも言える。    
    	    
    	○TSFの式の解説前にとりあえず分数計算や漢数字のテストなど。    
    	    
    echoRPNcalc:    
    	aboutRPNtest:	#TSF_this	aboutRPNcalc:	#TSF_argvsthe	#TSF_echoN	echoURL:	#TSF_this    
    aboutRPNtest:    
    	▽「1 3 m1|2」を「[2],[1]/[0]- #TSF_join[]」で連結して「#TSF_RPN」→	1	3	m1|2	[2],[1]/[0]-	#TSF_join[]	#TSF_RPN	2	#TSF_joinN	#TSF_echo    
    	▽「1 , 3 / m1|2 -」を「6 #TSF_join」で連結して「#TSF_RPN」→	1	,	3	/	m1|2	-	6	#TSF_joinN	#TSF_RPN	2	#TSF_joinN	#TSF_echo    
    	▽「1 3 m1|2」を「[2]/[1]-[0] #TSF_join[]」で連結して「#TSF_calc」→	1	3	m1|2	[2]/[1]-[0]	#TSF_join[]	#TSF_calc	2	#TSF_joinN	#TSF_echo    
    	▽「1 / 3 - m1|2 」を「5 #TSF_join」で連結して「#TSF_calc」→	1	/	3	-	m1|2	5	#TSF_joinN	#TSF_calc	2	#TSF_joinN	#TSF_echo    
    	▽スタックからショートカットで「[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2] を「#TSF_calc」→	[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2]	#TSF_calc	2	#TSF_joinN	#TSF_echo    
    	▽漢数字テスト「億千万」を「#TSF_calcJA」→	億千万	#TSF_calcJA	2	#TSF_joinN	#TSF_echo    
    	▽漢数字テスト「六分の五」を「#TSF_calcJA」→	６分の５	#TSF_calcJA	2	#TSF_joinN	#TSF_echo    
    	▽日時テスト「@4y年@0m月@0dm日(@wdj)@0h時@0n分@0s秒」を「#TSF_calender」→	@4y年@0m月@0dm日(@wdj)@0h時@0n分@0s秒	#TSF_calender	2	#TSF_joinN	#TSF_echo    
    aboutCALCdata:    
    	1	3	m1|2    
    aboutRPNcalc:    
    	    
    	○「#TSF_RPN」逆ポーランド小数電卓の概要。    
    	    
    	　TSFの数式に高速処理を目指すRPNと多機能を備えるcalcの2種類の電卓を用意。    
    	　RPNでは「1+2」は「1,2+」になる。数値同士はコンマで区切る。掛け算が先に演算されるなど優先順序が存在する数式は「calc」を使う。    
    	　演算子の「+」プラス「-」マイナスと符号の「p」プラス「m」マイナスは分けて表記。「1-(-2)」も「1,m2-」と表記する。    
    	　演算子の「/」と分数の「|」も分けて表記。分数二分の一「1|2」は小数「0.5」だが１÷２の割り算として表現する場合は「1,2/」と表記する。    
    	　通常の割り算の他にも1未満を切り捨てる「\」、余りを求める「#」がある。マイナス剰余は「5#m4」だと「4-(5#4)」のように計算する。    
    	　計算結果が整数になる場合、および小数の丸めで整数になってしまった場合は整数表記になる。    
    	　RPNではゼロ「0|1」で割った時は分母ゼロ「n|0」を出力して終了。計算続行はされないので注意。    
    	　「Z」はゼロ比較演算子(条件演算子)。「1,2,0Z」はゼロの時は真なので左の数値(1)、ゼロでない時は偽なので右の数値(2)を採用。    
    	　「O」「o」「U」「u」も同様に、ゼロ以上(ゼロ含む)、ゼロより大きい、ゼロ以下(ゼロ含む)、ゼロ未満で左右の数値を選択。    
    	　条件演算子とスタック名(演算を抑止する「:」演算子)を組み合わせる事で、「#TSF_this」に渡すスタック名を分岐できます(IF構文の代替)。    
    	    
    	○「#TSF_calc」系分数電卓の概要(RPNと共通する内容は圧縮)。    
    	    
    	　calcは括弧や分数なども使えます。RPN電卓も混在できます。分数を用いる事で桁溢れや丸め誤差をなるだけ回避する事を目標とします。    
    	　分数を小数に変換するには「,(1|3)」のように括弧の外側でコンマを使う事でcalcの計算結果をRPNで処理する形になります。    
    	　calcではRPNとは事なり、括弧が無くても「小数の分数化＞掛け算系＞足し算系＞条件演算子」のような計算順序が存在します。    
    	　calcでは式に直接スタック名を「[data:2]/[data:1]-[data:0]」できるので、「#TSF_peekNthe」「#TSF_join[]」をショートカットできます。    
    	　スタック名ショートカット実現のため「Z~」「z~」「O~」「o~」「U~」「u~」「N~」と条件演算子にチルダ追加。「N~」は「n|0」のチェック用途。    
    	　「#TSF_-calc」を用いると計算結果の符号を「p」「m」から「-」のみに変更できる。    
    	　「#TSF_calcJA」を用いると億千万円銭など通貨的な助数詞を扱う。100分の1(％)は「銭」、1000分の1(‰)は「厘」表記、1万分の1(‱)は「毛」表記。    
    	    
    echoURL:    
    	aboutURL:	#TSF_argvsthe	#TSF_echoN    
    aboutURL:    
    	○TSFの詳しい説明はローカルの「docs/index.html」かWeb上の「https://ooblog.github.io/TSF2KEV/」を確認してください。    
    	    
    	　Web版もTSF付属のローカル版も「docs/TSFindex.tsf」から「sample/TSFdoc.tsf」を用いて生成されてます。    
    	　TSFを用いると簡潔なプログラムが書けます。そしてこの「sample/sample_aboutTSF.tsf」文書自体もTSF言語で書かれてます。    
    	    
    	#! -- Copyright (c) 2017 ooblog --    
    	#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE

## 「TSF. --about」の「RPN」「Calc」テスト部分の抜粋。

    ▽「1 3 m1|2」を「[2],[1]/[0]- #TSF_join[]」で連結して「#TSF_RPN」→p0.833333
    ▽「1 , 3 / m1|2 -」を「6 #TSF_join」で連結して「#TSF_RPN」→p0.833333
    ▽「1 3 m1|2」を「[2]/[1]-[0] #TSF_join[]」で連結して「#TSF_calc」→p5|6
    ▽「1 / 3 - m1|2 」を「5 #TSF_join」で連結して「#TSF_calc」→p5|6
    ▽スタックからショートカットで「[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2] を「#TSF_calc」→p5|6
    ▽漢数字テスト「億千万」を「#TSF_calcJA」→1億1000万円
    ▽日時テスト「@4y年@0m月@0dm日(@wdj)@0h時@0n分@0s秒」を「#TSF_calender」→2017年06月19日(月)02時42分14秒

## TSF2KEVで未実装な箇所など(予定)。

☐PPPP処理が「TSF_Io_separate&#42;」に残存してるので「TSF_Forth.&#42;」に一本化したい(工事中)。  
☐HTML版ドキュメント「[TSF2KEV(https://ooblog.github.io/TSF2KEV/)](https://ooblog.github.io/TSF2KEV/ "「TSF2KEV」はプログラミング言語「TSF_Tab-Separated-Forth」のD言語とPythonによる実装です。")」の整備を進めて「TSF --about」の簡易解説やこの「README.md」自体ももっとコンパクトにすべき。  
☑文字コードは「UTF-8」改行は「LF」と固定。TSF1KEVにあった「UTF-8\t#TSF_encoding」は圧縮。  
☑L:Tsvではタブの個数は関係なかったけどTSFではゼロ長文字列も扱うのでタブの重複に注意。  
☑アンダーフローが発生しても長さゼロ文字列が帰ってくるだけ。ただし「TSF_Tab-Separated-Forth」の「#TSF_fin.」を消さないよう注意。  
☑ハウリング(thisとthatが同じで出口が壊れてるとスタックが無限蓄積の危険性)対策のため「#TSF_countmax」(スタックのカード数え上げ枚数の上限初期値256)という安全装置は付けているけどいまいちスマートじゃない。  
☐浮動小数の丸め指示「#TSF_calcRO」の扱いが未定。言語毎に小数の実装などにに差異があるはず。  
☐浮動小数ではない分数の小数変換専用の#関数カードも必要だけど未着手。  
☑分数の小数変換を「,(1|3)」と説明したのに「(,1|3)」で小数が分数になると説明しないのは、極論0.333…と0.3が区別できないので1|3と3|10が区別できなくなる恐れ。  
☐字列の類似度「H」(matcHer)がD言語で再現できるか未定なので当面後回しになるかも。  
☐自然対数(logｅ)は「E&#126;」。常用対数(log10)は「L&#126;」。二進対数(log2)は「l&#126;」の予定。「256l&#126;2」を8にするも「256L&#126;2」や「256E&#126;2」が8になってくれない症状は継続の予感。  
☐「tan(θ&#42;90|360)」なども何かしらの巨大な数ではなく0で割った「n|0」と表記したいがとりあえず未着手。  
☐「kM&#126;1&#126;10」で1から10まで合計するような和数列(総和)、「kP&#126;1&#126;10」で積数列(総乗)を用いて乗数や階乗の計算の予定。  
☐Calcの動作がそもそも重いorz  
☐D言語で現在時刻(StopWatchではなく「現在時刻」)のミリ秒以下を取得する方法が不明oxL ので「@ls」「@rs」系が0を返す。  
☐TSFにはまだ直接関係しないKEV(漢直)の話だけど、操作性を簡潔にするためα鍵盤を廃止して一文字検索と辞書変更のみのスマートな仕様にしたい。  

## Vimシンタックスの設定など。

 シンタックスファイル「[vimsyntax/tsf.vim](https://github.com/ooblog/TSF2KEV/blob/master/vimsyntax/tsf.vim "TSF2KEV/tsf.vim at master ooblog/TSF2KEV")」を「~/.vim/syntax/tsf.vim」にコピーする(syntaxフォルダは作成する)。  
「./TSF_DMDcompile.sh」を用いてD言語でコンパイルした「./TSF」を「&#126;/my-applications/bin/TSF」としてコピーする(puppy linux Ubuntu Tahrの場合。環境毎に「echo $PATH」は異なる)。  
Vimの「メニュー→編集(E)→起動時の設定(S)」で「&#126;/.vimrc」を開いて「filetype=tsf」や「:!TSF %」を追記する。  
ついでに「[TSF2KEV/kanedit.vim](https://github.com/ooblog/TSF2KEV/blob/master/KEV2/kanedit.vim "TSF2KEV/kanedit.vim at master ooblog/TSF2KEV")」の設定もおまけで書いてみた。  


    syntax on
    au BufRead,BufNewFile *.tsf set filetype=tsf
    autocmd BufNewFile,BufRead *.tsf nnoremap <F5> :!TSF %<CR>
    command KEVtsf  :source &#126;/TSF2KEV/KEV2/kanedit.vim

## 動作環境。

「Tahrpup6.0.5,Python2.7.6,dmd2.074.0,vim.gtk7.4.52(vim-gtk)」および  
「Wine1.7.18,Python3.4.4,dmd2.074.0,gvim8.0.134(KaoriYa)」で開発中。  

* Tahrpup6.0.5(Puppy Linux)
    * [http://puppylinux.com/](http://puppylinux.com/ "Puppy Linux Home")
* Python 3.4.4
    * [https://www.python.org/downloads/release/python-344/](https://www.python.org/downloads/release/python-344/ "Python Release Python 3.4.4 | Python.org")
* DMD 2.074.0
    * [https://dlang.org/download.html](https://dlang.org/download.html "Downloads - D Programming Language")
* vim-gtk(Ubuntu trusty)
    * [https://packages.ubuntu.com/trusty/vim-gtk](https://packages.ubuntu.com/trusty/vim-gtk "Ubuntu – trusty の vim-gtk パッケージに関する詳細")
* Vim — KaoriYa
    * [https://www.kaoriya.net/software/vim/](https://www.kaoriya.net/software/vim/ "Vim — KaoriYa")
* Portable Wine(shinobar.server-on.net)
    * [http://shinobar.server-on.net/puppy/opt/wine-portable-HELP_ja.html](http://shinobar.server-on.net/puppy/opt/wine-portable-HELP_ja.html "Portable Wine")

## ライセンス・著作権など。

&#35;! -- Copyright (c) 2017 ooblog --  
&#35;! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE  
