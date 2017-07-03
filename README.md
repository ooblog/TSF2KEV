# プログラミング言語「TSF_Tab-Separated-Forth」開発中。
## TSF超ザックリ説明。

TSFはForth風インタプリタです。CSV→TSV→TSF。  
構文は文字列をタブで区切るだけ(#!コメント行と#!関数カードでシバン「#!」を用いる程度)。  
![TSF syntax image](https://github.com/ooblog/TSF2KEV/blob/master/docs/TSF_512x384.png "TSF2KEV/TSF_512x384.png at master ooblog/TSF2KEV")  

## 言語が生まれた経緯。

漢直(漢字直接入力)の漢字配列やkan5x5フォントのグリフエディタの単漢字辞書など漢字データ管理でTSV(LTSVを更にアレンジしたL:Tsv)を用いてました(「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」を参考)。  
実装を[HSP](http://hsp.tv/ "HSPTV!（HSP( Hot Soup Processor )ソフトウェアの配布）")→[BaCon](http://www.basic-converter.org/ "BaCon - BASIC to C converter")→[Python](https://www.python.org/ "Welcome to Python.org")で何度か作り直す紆余曲折を経て今度は[D言語](https://dlang.org/ "Home - D Programming Language")で作り直す流れでしたが、言語の変更が強いられる度に一から作り直すのはしんどい。  
なので、TSVにデータ(プログラム含む)を入力するだけで動作するスクリプトが欲しくなったので開発中です。  
プログラム本体をTSFで作れば、OSや言語などの環境差異はTSF実装の方で吸収させるという戦法を想定。  
当面の目標は「[TSF2KEV/kanedit.vim](https://github.com/ooblog/TSF2KEV/blob/master/KEV2/kanedit.vim "TSF2KEV/kanedit.vim at master ooblog/TSF2KEV")」のような漢直をVimスクリプトの力を借りずに使わずに「TSF」だけで動かす事。  

## TSF言語の簡易説明「sample_aboutTSF.tsf」。

「[sample_aboutTSF.tsf](https://github.com/ooblog/TSF2KEV/blob/master/sample/sample_aboutTSF.tsf "TSF2KEV/sample_aboutTSF.tsf at master ooblog/TSF2KEV")」自体もTSFで書かれてるので、文中数式を「TSF sample/sample_aboutTSF.tsf」で動作確認したり、  
D言語やPythonに変換して「./TSF.d --about」「./TSF.py --about」のように内蔵コマンド化もできます。  
TSF言語の詳細説明はHTML版のドキュメント「[TSF2KEV(https://ooblog.github.io/TSF2KEV/)](https://ooblog.github.io/TSF2KEV/ "「TSF2KEV」はプログラミング言語「TSF_Tab-Separated-Forth」のD言語とPythonによる実装です。")」で執筆中。  


    #! /usr/bin/env TSF    
    TSF_Tab-Separated-Forth:    
    	echoTSF:	#!TSF_this	#!TSF_fin.    
    echoTSF:    
    	aboutTSF:	#!TSF_argvsthe	#!TSF_echoN	echoRPNcalc:	#!TSF_this    
    aboutTSF:    
    	    
    	○「TSF_Tab-Separated-Forth」の簡略説明。    
    	    
    	　Forth風インタプリタ。単位はtsv文字列。文字列の事をカードと呼称。カードの束をスタックと呼称。スタックの集まりをデッキと呼称。    
    	　文字から始まる行はスタック名。タブで始まる行はカードの束。シバン「#!」で始まる行(改行のみの行含む)はコメント扱いで読み飛ばし。    
    	    
    	○TSF構文には4つの「th」スタック代名詞(冠詞含む)「this」「that」「the」「they」が存在。    
    	    
    	　「this」は実行中のスタック。#関数カードの指示通りにカードを「ドロー(積み下ろし)」したり「リターン(積み上げ)」したりする。    
    	　「that」は積込先のスタック。#関数カードの返り値や#関数カード以外のカードが積み上げられる。    
    	　「the」は指定スタック。変数や配列やテキスト保存先として扱いたいスタックを一時的に呼び出す。    
    	　「they」はスタック名一覧。新規スタック作成や既存スタック削除の時、スタック名一覧自体をスタックの様に扱って整理する事もできる。    
    	    
    	○TSF構文のスタック操作には4つの「p」スタック動詞「peek」「poke」「pull」「push」が存在。    
    	    
    	　「peek」スタックからカードを読み込む。読込先スタックはそのままに「that」スタックにカードが積まれるのでカードが増殖する形になる。    
    	　「poke」スタックにカードを書き込む。スタックのカードは上書きされるので上書きされたカードが消失する形になる。    
    	　「pull」スタックからカードを引き抜く。通常は引抜先スタックから「that」スタックにカードが移動する形になる。    
    	　「push」スタックにカードを差し込む。通常は引抜先スタックに「that」スタックからカードが移動する形になる。    
    	    
    	○TSF構文の副詞「FNCMVAQIRHL」と可算名詞「SDO」などの説明はaboutでは簡略。    
    	    
    	　#関数カードの、ドロー(積み下ろし)は「pullFthat」リターン(積み上げ)は「pushFthat」してるとも言える。    
    	　代名詞と動詞の間にある「F」などが副詞。スタックに最後に積まれたカード、表面カードを選択するので表択。    
    	　「peekNthe」等の「N」は積まれた順に番号を割り振り番号で読込カード指定するので順択、というようにどのカードをppppするのか明記します。    
    	    
    	○TSF式として2種類の電卓「#!TSF_RPN」「#!TSF_calc」が存在。    
    	　calcでは括弧や分数なども使えます。RPNは括弧を処理しない上に小数のみなので高速です。    
    	　calcの括弧内外でRPNを使う事は可能です。コンマ「,」を用いるとRPNとみなされます。    
    	　TSFには変数がないので「#!TSF_joinN」「#!TSF_join[]」などを用いてカードを連結して式文字列を作ります。    
    	    
    echoRPNcalc:    
    	aboutRPNtest:	#!TSF_this	aboutRPNcalc:	#!TSF_argvsthe	#!TSF_echoN	echoURL:	#!TSF_this    
    aboutRPNtest:    
    	▽「1 3 m1|2」を「[2],[1]/[0]- #!TSF_join[]」で連結した「1,3/m1|2-」を「#!TSF_RPN」電卓→    
    	1	3	m1|2	[2],[1]/[0]-	#!TSF_join[]	#!TSF_RPN	2	#!TSF_joinN	#!TSF_echo    
    #!「#!TSF_RPN」電卓→p0.833333333333    
    	▽「1 , 3 / m1|2 -」を「6 #!TSF_join」で連結した「1,3/m1|2-」を「#!TSF_RPN」電卓→    
    	1	,	3	/	m1|2	-	6	#!TSF_joinN	#!TSF_RPN	2	#!TSF_joinN	#!TSF_echo    
    #!「#!TSF_RPN」電卓→p0.833333333333    
    	▽「1 3 m1|2」を「[2]/[1]-[0] #!TSF_join[]」で連結した「1/3-m1|2」を「#!TSF_calc」電卓→    
    	1	3	m1|2	[2]/[1]-[0]	#!TSF_join[]	#!TSF_calc	2	#!TSF_joinN	#!TSF_echo    
    #!「#!TSF_calc」電卓→p5|6    
    	▽「1 / 3 - m1|2 」を「5 #!TSF_join」で連結した「1/3-m1|2」を「#!TSF_calc」電卓→    
    	1	/	3	-	m1|2	5	#!TSF_joinN	#!TSF_calc	2	#!TSF_joinN	#!TSF_echo    
    #!「#!TSF_calc」電卓→p5|6    
    	▽「#!TSF_calc」のショートカット文法で「[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2]」(演算内容は「1/3-m1|2」)→    
    	[aboutCALCdata:0]/[aboutCALCdata:1]-[aboutCALCdata:2]	#!TSF_calc	2	#!TSF_joinN	#!TSF_echo    
    #!「#!TSF_calc」電卓→p5|6    
    aboutCALCdata:    
    	1	3	m1|2    
    aboutRPNcalc:    
    	    
    	○「#!TSF_RPN」と「#!TSF_calc」の共通点や差異の補足。    
    	　演算子の「+」プラス「-」マイナスと符号の「p」プラス「m」マイナスは分けて表記。割り算の「/」と分数の「|」も分けて表記。    
    	　calcの出力結果は基本分数ですが、「,(1|3)」のように括弧の外側でコンマを使う事で計算結果をRPNに渡す事ができます。    
    	　条件演算子がRPNでは「Z」「z」「O」「o」「U」「u」ですがcalcでは「Z~」「z~」「O~」「o~」「U~」「u~」「N~」とチルダ追加です。    
    	　calcで追加した条件演算子「N~」は分母ゼロ「n|0」分岐用です。RPNではゼロ割り算発生時点で分母ゼロ「n|0」を出力します。    
    	　calcには演算を抑止する「:」演算子が含まれてるので条件演算子の結果にスタック名を直接指定する事でIF構文の代替になります。    
    	    
    echoURL:    
    	aboutURL:	#!TSF_argvsthe	#!TSF_echoN    
    aboutURL:    
    	○TSFの詳しい説明はローカルの「docs/index.html」かWeb上の「https://ooblog.github.io/TSF2KEV/」を確認してください(執筆中)。    
    	    
    	　Web版もTSF付属のローカル版も「docs/TSFindex.tsf」から「sample/TSFdoc.tsf」を用いて生成されてます。    
    	　TSFを用いると簡潔なプログラムが書けます。そしてこの「sample/sample_aboutTSF.tsf」文書自体もTSF言語で書かれてます。    
    	    
    	#! -- Copyright (c) 2017 ooblog --    
    	#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE

## TSF2KEVで未実装な箇所や気が付いたバグやドキュメント未整備な箇所など(ToDoリスト風)。

☑#!コメント行と#!関数カードの構文をシバンに統一してみたけど様子見。「#!TSF_*」の「TSF_」部分の省略は見送り。「GTK_」「DOM_」とかGUI関数と区別視認性の予感。  
☑ハウリング(thisとthatが同じで出口が壊れてるとスタックが無限蓄積の危険性)対策のため「#!TSF_countmax」(スタックのカード数え上げ枚数の上限初期値256)という安全装置は付けているけどいまいちスマートじゃない。  
☑PPPP処理を「TSF_Forth.&#42;」に一本化。スタックやデッキ(文字列リスト)の処理が複数モジュールにまたがるとスコープの問題で言語の組み込み関数で直接編集できなくなるため。  
☑分数の小数変換を「,(1|3)」と説明したのに「(,1|3)」で小数が分数になると説明しないのは、極論0.333…と0.3が区別できないので1|3と3|10が区別できなくなる恐れ。  
☐浮動小数の丸め指示「#!TSF_calcRO」の扱いが未定。言語毎に小数の実装などにに差異があるはず。  
☐浮動小数ではない分数の小数変換専用の#関数カードも必要だけど未着手。  
☐「#!TSF_calcJA」で指数が表示されたり「銭」の扱いが不十分。  
☐「#!TSF_calc」で「(1/3)-(m1|2)」の様に括弧で負数を囲むと符号反転に失敗する。  
☐字列の類似度「H」(matcHer)がD言語で再現できるか未定なので当面後回しになるかも。  
☐自然対数(logｅ)は「E&#126;」。常用対数(log10)は「L&#126;」。二進対数(log2)は「l&#126;」の予定。「256l&#126;2」を8にするも「256L&#126;2」や「256E&#126;2」が8になってくれない症状は継続の予感。  
☐「tan(θ&#42;90|360)」なども何かしらの巨大な数ではなく0で割った「n|0」と表記したいがとりあえず未着手。  
☐「kM&#126;1&#126;10」で1から10まで合計するような和数列(総和)、「kP&#126;1&#126;10」で積数列(総乗)を用いて乗数や階乗の計算の予定。  
☐Calcの動作がそもそも重いのでCalcJAが超重いorz  
☐D言語で現在時刻(StopWatchではなく「現在時刻」)のミリ秒以下を取得する方法が不明oxL ので「@ls」「@rs」系が0を返す。  
☐TSFにはまだ直接関係しないKEV(漢直)の話だけど、操作性を簡潔にするためα鍵盤を廃止して一文字検索と辞書変更のみのスマートな仕様にしたい。  
☐「TSF --about」の簡易説明では漢直方面に触れられないのでHTML版ドキュメント「[TSF2KEV(https://ooblog.github.io/TSF2KEV/)](https://ooblog.github.io/TSF2KEV/ "「TSF2KEV」はプログラミング言語「TSF_Tab-Separated-Forth」のD言語とPythonによる実装です。")」の整備をもっと強化。  

## 動作環境(開発環境)。

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
