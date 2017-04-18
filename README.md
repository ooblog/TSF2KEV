# プログラミング言語「TSF_Tab-Separated-Forth」開発中。

目標は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」の「[LTsv/kanedit.vim](LTsv/kanedit.vim "LTsv/kanedit.vim")」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonとD言語で。  
TSFはまだ開発中なので、漢直やkan5x5フォントをお探しの方は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」をお使いください。  
開発途中のものでもいいから動くTSFをお探しの方は「[TSF1KEV](https://github.com/ooblog/TSF1KEV "プログラミング言語「TSF_Tab-Separated-Forth」試作。開発の舞台は「TSF2KEV」以降に移行。")」を参考。  


## TSF2KEVの「TSF.d --about」「TSF.py --about」より抜粋。

    TSF_Tab-Separated-Forth:
    	echoTSF:	#TSF_this	#TSF_fin.
    echoTSF:
    	aboutTSF:	#TSF_argvsthe	#TSF_reverseN	aboutTSF:	#TSF_lenthe	#TSF_echoN	echoRPN:	#TSF_this
    aboutTSF:
    	
    	○「TSF_Tab-Separated-Forth」の概要(開発予定の話も含みます)。
    	
    	　Forth風インタプリタ。単位はtsv文字列。文字列の事をカードと呼称。カードの束をスタックと呼称。スタックの集まりをデッキと呼称。
    	　ソースコード.tsfで文字から始まる行はスタック名、タブで始まる行はカード。スタック名の宣言とカードの積み込みはワンライナー記述も可能。
    	　改行のみもしくは「#」で始まる行は読み飛ばし。「#」は「#関数カード」として使うので「#」で始まるスタック名は予約ワード扱い。
    	
    	○TSFには4つの「th」スタック代名詞「this」「that」「the」「they」という概念が存在する。
    	
    	　「this」は実行中のスタック。#関数カードの指示通りにカードを「ドロー(積み下ろし)」したり「リターン(積み上げ)」したりする。
    	　#関数カードではないカードは後述の「that」スタックに積み上げられる。関数の返り値ではないのでリターンとは呼ばない。
    	　オーバーフローもしくは「#exit #TSF_this」のように存在しないスタックに入る行為でオーバーフローを発生させてスタックから抜ける。
    	　TSFにループ構文は存在しないので末尾再帰がループになる。同様にループの内側からループの外側スタックを呼び出してもコールスタックが破棄される。
    	　TSFにはif構文も存在しないので「#TSF_this」の飛び先を事前に書き換える形になる。条件演算子は「#TSF_RPN」「#TSF_calc」の中にある。
    	　「that」は積込先のスタック。#関数カードの返り値や#関数カード以外のカードが積み上げられる。
    	　「the」は指定スタック。変数や配列やテキスト保存先として扱ってるスタックが一時的に呼び出される場合の文字通り代名詞。
    	　「they」はスタック名一覧。スタック名一覧自体もカード束としてスタックの様に扱える場合がある。
    	
    echoRPN:
    	aboutRPNtest:	#TSF_this	aboutRPN:	#TSF_argvsthe	#TSF_reverseN	aboutRPN:	#TSF_lenthe	#TSF_echoN	echoCALC:	#TSF_this
    aboutRPNtest:
    	▽「1 3 m1|2」を「[2],[1]/[0]- #TSF_join[]」で連結→	1	3	m1|2	[2],[1]/[0]-	#TSF_join[]	#TSF_RPN	2	#TSF_joinN	#TSF_echo	▽「1 , 3 / m1|2 -」を「#TSF_join」で連結→	1	,	3	/	m1|2	-	6	#TSF_joinN	#TSF_RPN	2	#TSF_joinN	#TSF_echo
    aboutRPN:
    	
    	○「RPN」系小数電卓の概要。
    	
    	　TSFでは機能を絞って高速処理をめざすRPNと多機能をめざすcalcの2種類の電卓を用意。RPN(逆ポーランド記法)では括弧を用いません。
    	　RPNでは「1+2」は「1,2+」である。掛け算が先に演算されるなどの優先順序が存在する数式は「calc」を使う。
    	　演算子の「+」プラス「-」マイナスと符号の「p」プラス「m」マイナスは分けて表記。「1-(-2)」を「1,m2-」と表記する。
    	　演算子の「/」と分数の「|」も分けて表記。二分の一「1|2」は分数(0.5)だが１÷２の割り算として表現する場合は「1,2/」と表記する。
    	　分数小数を用いても計算結果が整数になる場合、および小数の丸めで整数になってしまった場合は整数表記になる。
    	　通常の割り算の他にも1未満を切り捨てる「\」、余りを求める「#」がある。
    	　RPNではゼロで割った時は「n|0」を出力して終了。条件演算子の可能性とかは考慮されない。
    	　「Z」はゼロ比較演算子(条件演算子)。「1,2,0Z」はゼロの時は真なので左の数値(1)、ゼロでない時は偽なので右の数値(2)を採用。
    	　「O」「o」「U」「u」も同様に、ゼロ以上(ゼロ含む)、ゼロより大きい、ゼロ以下(ゼロ含む)、ゼロ未満で左右の数値を選択。
    	、条件演算子は何に使うかというと「#TSF_this」の飛び先を変更するため「#TSF_peekthe」などと組み合わせます。
    	
    echoCALC:
    	aboutCALC:	#TSF_argvsthe	#TSF_reverseN	aboutCALC:	#TSF_lenthe	#TSF_echoN
    aboutCALC:
    	○「calc」系分数電卓は再開発中なので説明不足します(RPNと共通する内容は圧縮)。
    	
    	　calcは分数を用いる事で桁溢れをなるだけ回避する事を目標とします。
    	　calcでは分母「n|0」でも条件演算子の可能性などを考慮して計算は続行されます。
    	　「#TSF_join[]」などを別途用いる事無く数式「[2]/[1]-[0]」を直接渡したり「#TSF_this」の飛び先を直接指定できる様にする予定。

    ▽「1 3 m1|2」を「[2],[1]/[0]- #TSF_join[]」で連結→p0.833333
    ▽「1 , 3 / m1|2 -」を「#TSF_join」で連結→p0.833333


## TSF2KEVで未実装な箇所とかaboutに書いてない細かい話や仕様変更もしくは逆に強化する点など(予定)。

・文字コードは「UTF-8」改行は「LF」と固定。TSF1KEVにあった「UTF-8\t#TSF_encoding」は圧縮。  
・アンダーフローが発生しても長さゼロ文字列が帰ってくるだけ。ただし「TSF_Tab-Separated-Forth」の「#TSF_fin.」を消さないよう注意。  
・念のため「#TSF_countmax」(スタックのカード数え上げ枚数の上限)という安全装置は付けているけどいまいちスマートじゃない。  
・「#TSF_calc」には小数変換の「D」演算子や分岐先スタック名などテキストを温存する「T」演算子などを用意する予定。  
・PeekPokePushPullは更にCycle,liMit,eeVerse,rAndomおよびeQual,In,firSt,rEst,reseaRch,matcHer,Labelと種類が増えていく予感。派生は「TSF_shuffle」で扱う予定。  
・TSF1KEVにあった億千万電卓「#TSF_calcKN」(かな)は「#TSF_calcJA」のように言語ロケールに寄せる形で置き換える。。小数点の代わりに「円」を表示する。100分の1(％)は「銭」、1000分の1(‰)は「厘」表記、10000分の1(‱)は「毛」表記。  
・連想配列すらない言語を今時想定する必要があるのか不明なので優先度は低いが、TSFテキストを「L:Tsv」の時の様に直接書き替えるAPIも作って置きたい(未定)。  
・文字列の類似度がD言語で再現できるか未定なので当面後回しになるかも。  
・timeとかmatchとかも用意しないと「TSF_doc」が作れないのではがゆい。  


## calc等がまだ未実装なので参考用にTSF1KEVの「TSF.py --about」の抜粋も併記。

    TSF_Tab-Separated-Forth:
    	UTF-8	#TSF_encoding	30	#TSF_calcPR	main1:	#TSF_this	0	#TSF_fin.
    main1:
    	aboutTSF:	#TSF_echothe	main2:	#TSF_this
    main2:
    	#-- 分岐の材料、電卓その他数値取得のテスト --	 	2	#TSF_echoN	calcFXtest:	#TSF_this	calcDCtest:	#TSF_this	calcKNテスト:	#TSF_this	calenderテスト:	#TSF_this	matchテスト:	#TSF_this	shuffleテスト:	#TSF_this	 	#-- (小数の桁数が異なる理由は分数電卓を用いない計算は有効桁数が短いため) --	2	#TSF_echoN	main3:	#TSF_this
    main3:
    	aboutCalc:	#TSF_echothe
    aboutTSF:
    	「TSF_Tab-Separated-Forth」の概要。
    	スタックを積んでワード(関数)などで消化していくForth風インタプリタ。スタックの単位はtsv文字列。
    	文字から始まる行はスタック名、タブで始まる行はスタック内容。改行のみもしくは「#」で始まる行は読み飛ばし。
    	タブのみ行、項目の無い二重タブ、行末末尾タブ、は文字列長0のスタックが含まれるとみなされるので注意。
    	起動時スタック「TSF_Tab-Separated-Forth:」にargvsが追加される。「#TSF_fin.」が無い場合はargvsより先に追加される。
    	TSFでは先頭から順にワードを実行するthisスタックと末尾に引数などを積み上げ積み下げるthatスタックを別々に指定できる。
    	そもそもスタックが複数あり、他言語で言う所の変数はスタックで代用する。関数の引数や返り値もargvs同様にスタック経由。
    	存在しないthatスタックからの読込(存在するスタックのアンダーフロー含む)は文字列長0を返却する。
    	存在しないthisスタックの呼び出し(存在するスタックのオーバーフロー含む)は呼び出し元に戻って続きから再開。
    	ループは「#TSF_this」による再帰で組む。深い階層で祖先を「#TSF_this」すると子孫コールスタックはまとめて破棄される。
    	分岐は電卓(条件演算子など)で組む。「#TSF_this」の飛び先スタック名を「#TSF_peekthe」等で引っ張る際に「#TSF_calcFX」等の演算結果で選択する。
    calcFXtest:
    	「1 3 m1|2」を数式「[2]/[1]-[0]」で連結→	1	3	m1|2	[2]/[1]-[0]	#TSF_calcFX	2	#TSF_joinN	1	#TSF_echoN
    calcDCtest:
    	「1 / 3 - m1|2」を数式に連結(ついでに小数30桁デモ)→	1	/	3	-	m1|2	5	#TSF_joinN	#TSF_calcDC	2	#TSF_joinN	1	#TSF_echoN
    calcKNテスト:
    	「一割る三引く(マイナス二分の一)」(ついでに単位付き計算デモ)→	一割る三引く(マイナス二分の一)	#単位計算	2	#N個連結	1	#N行表示
    calenderテスト:
    	「@bt」SwatchBeat(スイスから時差8時間)→	-480	#TSF_diffminute	@bt	#TSF_calender	2	#TSF_joinN	1	#TSF_echoN
    matchテスト:
    	「いいまちがい」と「いいまつがい」の類似度→	いいまちがい	いいまつがい	#TSF_matcher	2	#TSF_joinN	1	#TSF_echoN
    shuffleテスト:
    	前半TSF概要の行数(スタック「aboutTSF:」の個数)→	aboutTSF:	#TSF_lenthe	2	#TSF_joinN	1	#TSF_echoN
    aboutCalc:
    	「calc」系分数電卓の概要(何らかの数値を取得したら何らかの計算して条件演算子に用いることもできる)。
    	「#TSF_calcFX」は分数表記。「#TSF_calcDC」は小数表記。「#TSF_calcKN」億以上の単位を漢字表記。全部基本的には分数計算。
    	「#TSF_calcPR」は有効桁数の調整。初期値は72桁(千無量大数)。「π」(円周率)「θ」(2*π)「ｅ」(ネイピア数)などは桁溢れ予防で68桁(一無量大数)。
    	「#TSF_calcRO」は端数処理の調整。初期値は「ROUND_DOWN」(0方向に丸める)。
    	「/」割り算と「|」分数は分けて表記。数値の正負も演算子の「+」プラス「-」マイナスと区別するため「p」プラス「m」マイナスと表記。
    	通常の割り算の他に1未満を切り捨てる「\」、余りを求める「#」、消費税計算用「%」演算子がある。掛け算は「*」演算子。
    	自然対数(logｅ)は「E」。常用対数(log10)は「L」。無理数は分数に丸められるので「E256/E2」や「L256/L2」が8にならない。
    	「81&3l」や「256の二進対数」という任意底対数の演算子は整数同士専用のアルゴリズムを使えるので「256&2l」が8になる。
    	「kM1~10」で1から10まで合計するような和数列(総和)が使える。同様に「kP1~10」で積数列(総乗)を用いて乗数や階乗の計算も可能。
    	(最大)公約数は「12&16G」。(最小)公倍数は「12&16g」。「&」のみを単独で使った場合は掛け算の同じ優先順位で加算する。
    	0で割るもしくは有効桁数溢れなど、何らかの事情で計算できない場合は便宜上「n|0」という事にする。「p」「m」は付かない。
    	「tan(θ*90|360)」なども何かしらの巨大な数ではなく0で割った「n|0」と表記したいがとりあえず未着手。
    	マイナスによる剰余は「#TSF_peekcyclethe」の挙動に似せる。つまり「5#m4」は「4-(5#4)」と計算するので3になる。PDCAサイクルのイメージ。
    	「2分の1を5乗」など日本語風表記で分数を扱う場合は「(2分の1)を5乗」と書かないと「2分の(1を5乗)」と解釈してしまう。
    	ゼロ比較演算子(条件演算子)は「Z」。「kZ1~0」の様な計算でkがゼロの時は真なので1、ゼロでない時は偽なので0。「n|0」の時は「n|0」。
    	条件演算子は0以上を調べる系「O」「o」、0以下を調べる系「U」「u」、0か調べる系「Z」「z」、「n|0」か調べる系「N」を用意。
    	電卓以外の分岐「#TSF_casestacks」などはHTML版ドキュメント「TSF_doc(仮)」の方で解説予定。

    #-- 分岐の材料、電卓その他数値取得のテスト --
    「1 3 m1|2」を数式「[2]/[1]-[0]」で連結→p5|6
    「1 / 3 - m1|2」を数式に連結(ついでに小数30桁デモ)→0.833333333333333333333333333333
    「一割る三引く(マイナス二分の一)」(ついでに単位付き計算デモ)→6分の5
    「@bt」SwatchBeat(スイスから時差8時間)→286.180555556
    「いいまちがい」と「いいまつがい」の類似度→0.833333333333
    前半TSF概要の行数(スタック「aboutTSF:」の個数)→11
    #-- (小数の桁数が異なる理由は分数電卓を用いない計算は有効桁数が短いため) --


## 動作環境。

「Tahrpup6.0.5,Python2.7.6,dmd2.073.0,vim.gtk7.4.52&#40;vim-gtk&#41;」および「Wine1.7.18,Python3.4.4,dmd2.073.0,gvim8.0.134&#40;KaoriYa&#41;」で開発中。  


## ライセンス・著作権など。

Copyright (c) 2017 ooblog  
License: MIT  
[https://github.com/ooblog/TSF2KEV/blob/master/LICENSE](LICENSE "https://github.com/ooblog/TSF2KEV/blob/master/LICENSE")  

