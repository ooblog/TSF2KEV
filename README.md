# プログラミング言語「TSF_Tab-Separated-Forth」開発中。

目標は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」の「[LTsv/kanedit.vim](LTsv/kanedit.vim "LTsv/kanedit.vim")」などをVim使わずに「TSF」だけで動かす事。実装はとりあえずPythonとD言語で。  
TSFはまだ開発中なので、漢直やkan5x5フォントをお探しの方は「[LTsv10kanedit](https://github.com/ooblog/LTsv10kanedit "ooblog/LTsv10kanedit: 「L:Tsv」の読み書きを中心としたモジュール群と漢字入力「kanedit」のPythonによる実装です(準備中)。")」をお使いください。  
開発途中のものでもいいから動くTSFをお探しの方は「[TSF1KEV](https://github.com/ooblog/TSF1KEV "プログラミング言語「TSF_Tab-Separated-Forth」試作。開発の舞台は「TSF2KEV」以降に移行。")」を参考。  


## TSF2KEVで仕様変更したい点、もしくは逆に強化する点など(予定)。

・Forthに習って命令文や関数の類をワードと呼称してたけど、TSFではカードと呼称したい。  
・カードと呼称することで、thatに一時的に積む数枚のカードと、カードの束であるスタックと、スタックの集合であるデッキを明確に区別できる。  
・デッキ呼称で、PythonやD言語に出力した時のTSFインタプリタのソースコードとTSFソースコードの区別ができる。TSFが書かれたTSVデータの方がデッキ呼称。  
・便宜上、thatスタックからカードをpopする事を「ドロー」、演算結果などをthatスタック末尾にpushする事を「リターン」と呼称する。  
・スタック間のカード移動は便宜上とりあえず「シャッフル」と呼称する場合がある。  
・文字コードは「UTF-8」改行は「LF」と固定する。「UTF-8\t#TSF_encoding」は圧縮。  
・Noneやnullを返せない言語も想定してカード関数の返り値は文字列型を返す。その影響でスタックを抜ける場合の「#exit #TSF_this」の仕様昇格(「#exit」そのものが強制されるわけではない)。  
・OrderedDictが存在しない言語も想定して連想配列と連想配列のキーの順序を別の変数で管理。連想配列すらない古い言語だとTSFテキストの直接書き替えの予感。  
・「#TSF_fin.」の終了コードを圧縮。helloworldは「Hello world\t#TSF_echo」までコンパクトに。  
・スタック代名詞はthis,that,the,theyの4つのth。TSF2KEVでは4つのp、peek,poke,pull,pushに揃える事で文法を覚えやすくしたい。  
・peek,poke,pull,pushに揃えるため「#TSF_carbonth*」も「#TSF_peekFth*」のように寄せる。「#TSF_delthe」系も圧縮して「#TSF_pullthey」のような形になる。  
・peekなどは更にCycle,liMit,eeVerse,rAndomおよびeQual,In,firSt,rEst,reseaRch,matcHer,Labelと種類が増えていく予感。派生はTSF_shuffleで扱う予定。  
・「#TSF_fin.」カード自動付加は「TSF_Forth_run()」の方に内蔵。  
・「#TSF_calcKN」とか「#TSF_calcDC」などは「#TSF_calc」に再編成される。次項で詳しく。  


## 「#TSF_RPN」と「#TSF_calc」の役割分担について(予定)。
・「#TSF_RPN」は分数も小数として計算する。スタックからの直読みもしない。括弧も使わない(逆ポーランド記法「1,3/m1|2-」)。速度優先。  
・「#TSF_calc」は分数は分数のまま計算してなるだけ丸め誤差回避を試みる。スタックからの直読みでpeek系のショートカット。数式の優先順位や括弧も使える「1/3-m1|2」。簡易さ優先。  
・「#TSF_RPN」と「#TSF_join[]」は別の関数カード。「#TSF_calc」は単独で「([2],[1],[0]T)」と「T」演算して連結できる予定。  
・「#TSF_calc」に小数表現「(p1|3D)」のような「D」演算子の導入で関数カード一本化。  
・「#TSF_calcKN」(かな)を「#TSF_calcJA」に置き換える。言語のロケールに寄せる。小数点の代わりに「円」を表示する。100分の1(％)は「銭」、1000分の1(‰)は「厘」表記、10000分の1(‱)は「毛」表記。  
・「m1|2」が「マイナス2分の1」なのはTSF1KEVから継続。次項が参考。  



## 参考用TSF1KEVの「TSF.py --about」抜粋。

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

