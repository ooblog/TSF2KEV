#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
#import random
#import re
from TSF_Io import *

def TSF_Forth_1ststack():    #TSFdoc:最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_version():    #TSFdoc:TSFバージョン(ブランチ)名(TSFAPI)。
    return "20170327M153945"

def TSF_Forth_Initcards(TSF_cardsD,TSF_cardsO):    #TSF_doc:ワードを初期化する(TSFAPI)。
    TSF_Forth_cards={
        "#TSF_fin.":TSF_Forth_fin, "#TSFを終了。":TSF_Forth_fin,
        "#TSF_countmax":TSF_Forth_countmax, "#カード数え上げ上限":TSF_Forth_countmax,
        "#TSF_this":TSF_Forth_this, "#スタック実行":TSF_Forth_this,
        "#TSF_that":TSF_Forth_that, "#スタック積込":TSF_Forth_that,
        "#TSF_stylethe":TSF_Forth_stylethe, "#指定スタックにスタイル指定":TSF_Forth_stylethe,
        "#TSF_stylethis":TSF_Forth_stylethis, "#実行中スタックにスタイル指定":TSF_Forth_stylethis,
        "#TSF_stylethat":TSF_Forth_stylethat, "#積込先スタックにスタイル指定":TSF_Forth_stylethat,
        "#TSF_stylethey":TSF_Forth_stylethey, "#全スタックにスタイル指定":TSF_Forth_stylethey,
        "#TSF_viewthe":TSF_Forth_viewthe, "#指定スタック表示":TSF_Forth_viewthe,
        "#TSF_viewthis":TSF_Forth_viewthis, "#実行中スタック表示":TSF_Forth_viewthis,
        "#TSF_viewthat":TSF_Forth_viewthat, "#積込先スタック表示":TSF_Forth_viewthat,
        "#TSF_viewthey":TSF_Forth_viewthey, "#スタック一覧表示":TSF_Forth_viewthey,
        "#TSF_RPN":TSF_Forth_RPN, "#逆ポーランド電卓で計算":TSF_Forth_RPN, "#小数計算":TSF_Forth_RPN,
        "#TSF_echo":TSF_Forth_echo, "#カードを表示":TSF_Forth_echo,
        "#TSF_echoN":TSF_Forth_echoN, "#N枚カードを表示":TSF_Forth_echoN,
        "#TSF_argvs":TSF_Forth_argvs, "#コマンド積込":TSF_Forth_argvs,
        "#TSF_argvsthe":TSF_Forth_argvsthe, "#指定スタック積込":TSF_Forth_argvsthe,
        "#TSF_argvsthis":TSF_Forth_argvsthis, "#実行中スタック積込":TSF_Forth_argvsthis,
        "#TSF_argvsthat":TSF_Forth_argvsthat, "#積込先スタック積込":TSF_Forth_argvsthat,
        "#TSF_argvsthey":TSF_Forth_argvsthey, "#スタック一覧積込":TSF_Forth_argvsthey,
        "#TSF_reverseN":TSF_Forth_reverseN, "#N枚逆順積込":TSF_Forth_reverseN,
        "#TSF_joinN":TSF_Forth_joinN, "#N枚1枚化":TSF_Forth_joinN,
#    TSF_words["#TSF_joinN"]=TSF_match_joinN; TSF_words["#N個連結"]=TSF_match_joinN
#    TSF_words["#TSF_betweenN"]=TSF_match_betweenN; TSF_words["#挟んでN個連結"]=TSF_match_betweenN
#    TSF_words["#TSF_split"]=TSF_match_split; TSF_words["#文字で分割"]=TSF_match_split
#    TSF_words["#TSF_chars"]=TSF_match_chars; TSF_words["#一文字ずつに分離"]=TSF_match_chars
#    TSF_words["#TSF_charslen"]=TSF_match_charslen; TSF_words["#文字数取得"]=TSF_match_charslen
#    TSF_words["#TSF_brackets"]=TSF_calc_brackets; TSF_words["#数式に連結"]=TSF_calc_brackets
        "#TSF_lenthe":TSF_Forth_lenthe, "#指定スタック枚数":TSF_Forth_lenthe,
        "#TSF_lenthis":TSF_Forth_lenthis, "#実行中スタック枚数":TSF_Forth_lenthis,
        "#TSF_lenthat":TSF_Forth_lenthat, "#積込先スタック枚数":TSF_Forth_lenthat,
        "#TSF_lenthey":TSF_Forth_lenthey, "#スタック一覧枚数":TSF_Forth_lenthey,
        "#TSF_peekFthe":TSF_Forth_peekFthe, "#指定スタック表面読込":TSF_Forth_peekFthe,
        "#TSF_peekFthis":TSF_Forth_peekFthis, "#実行中スタック表面読込":TSF_Forth_peekFthis,
        "#TSF_peekFthat":TSF_Forth_peekFthat, "#積込先スタック表面読込":TSF_Forth_peekFthat,
        "#TSF_peekFthey":TSF_Forth_peekFthey, "#スタック一覧表面読込":TSF_Forth_peekFthey,
        "#TSF_peekNthe":TSF_Forth_peekNthe, "#指定スタック読込":TSF_Forth_peekNthe,
        "#TSF_peekNthis":TSF_Forth_peekNthis, "#実行中スタック読込":TSF_Forth_peekNthis,
        "#TSF_peekNthat":TSF_Forth_peekNthat, "#積込先スタック読込":TSF_Forth_peekNthat,
        "#TSF_peekNthey":TSF_Forth_peekNthey, "#スタック一覧読込":TSF_Forth_peekNthey,
#        "#TSF_pokeFthe":TSF_Forth_pokeFthe, "#指定スタック上書":TSF_Forth_pokeFthe,
#        "#TSF_pokeFthis":TSF_Forth_pokeFthis, "#実行中スタック上書":TSF_Forth_pokeFthis,
#        "#TSF_pokeFthat":TSF_Forth_pokeFthat, "#積込先スタック上書":TSF_Forth_pokeFthat,
#        "#TSF_pokeFthey":TSF_Forth_pokeFthey, "#スタック一覧上書":TSF_Forth_pokeFthey,
#        "#TSF_pokeNthe":TSF_Forth_pokeNthe, "#指定スタック上書":TSF_Forth_pokeNthe,
#        "#TSF_pokeNthis":TSF_Forth_pokeNthis, "#実行中スタック上書":TSF_Forth_pokeNthis,
#        "#TSF_pokeNthat":TSF_Forth_pokeNthat, "#積込先スタック上書":TSF_Forth_pokeNthat,
#        "#TSF_pokeNthey":TSF_Forth_pokeNthey, "#スタック一覧上書":TSF_Forth_pokeNthey,
        "#TSF_pullFthe":TSF_Forth_pullFthe, "#指定スタック表面引抜":TSF_Forth_pullFthe,
        "#TSF_pulltFhis":TSF_Forth_pullFthis, "#実行中スタック表面引抜":TSF_Forth_pullFthis,
        "#TSF_pullFthat":TSF_Forth_pullFthat, "#積込先スタック表面引抜":TSF_Forth_pullFthat,
        "#TSF_pullFthey":TSF_Forth_pullFthey, "#スタック一覧表面引抜":TSF_Forth_pullFthey,
#        "#TSF_pullNthe":TSF_Forth_pullNthe, "#指定スタック引抜":TSF_Forth_pullNthe,
#        "#TSF_pulltNhis":TSF_Forth_pullNthis, "#実行中スタック引抜":TSF_Forth_pullNthis,
#        "#TSF_pullNthat":TSF_Forth_pullNthat, "#積込先スタック引抜":TSF_Forth_pullNthat,
#        "#TSF_pullNthey":TSF_Forth_pullNthey, "#スタック一覧引抜":TSF_Forth_pullNthey,
#        "#TSF_pushFthe":TSF_Forth_pushFthe, "#指定スタック差込":TSF_Forth_pushFthe,
#        "#TSF_pushFthis":TSF_Forth_pushFthis, "#実行中スタック差込":TSF_Forth_pushFthis,
#        "#TSF_pushFthat":TSF_Forth_pushFthat, "#積込先スタック差込":TSF_Forth_pushFthat,
#        "#TSF_pushFthey":TSF_Forth_pushFthey, "#スタック一覧差込":TSF_Forth_pushFthey,
#        "#TSF_pushNthe":TSF_Forth_pushNthe, "#指定スタック差込":TSF_Forth_pushNthe,
#        "#TSF_pushNthis":TSF_Forth_pushNthis, "#実行中スタック差込":TSF_Forth_pushNthis,
#        "#TSF_pushNthat":TSF_Forth_pushNthat, "#積込先スタック差込":TSF_Forth_pushNthat,
#        "#TSF_pushNthey":TSF_Forth_pushNthey, "#スタック一覧差込":TSF_Forth_pushNthey,
        "#TSF_readtext":TSF_Forth_readtext, "#テキストを読込":TSF_Forth_readtext,
        "#TSF_mergethe":TSF_Forth_mergethe, "#TSFに合成":TSF_Forth_mergethe,
        "#TSF_publishthe":TSF_Forth_publishthe, "#指定スタックをテキスト化":TSF_Forth_publishthe,
        "#TSF_publishthis":TSF_Forth_publishthis, "#実行中スタックをテキスト化":TSF_Forth_publishthis,
        "#TSF_publishthat":TSF_Forth_publishthat, "#積込先スタックをテキスト化":TSF_Forth_publishthat,
        "#TSF_remove":TSF_Forth_remove, "#ファイルを削除する":TSF_Forth_remove,
        "#TSF_savetext":TSF_Forth_savetext, "#テキストファイルに上書":TSF_Forth_savetext,
        "#TSF_writetext":TSF_Forth_writetext, "#テキストファイルに追記":TSF_Forth_writetext,
   }
#match:Cycle,liMit,Reverse,rAndom,Label
#        "#TSF_peekLthe":TSF_Forth_peekLthe, "#指定スタックラベルで読込":TSF_Forth_peekLthe,
#        "#TSF_peekLthis":TSF_Forth_peekLthis, "#実行中スタックラベルで読込":TSF_Forth_peekLthis,
#        "#TSF_peekLthat":TSF_Forth_peekLthat, "#積込先スタックラベルで読込":TSF_Forth_peekLthat,
#        "#TSF_peekLthey":TSF_Forth_peekLthey, "#スタック一覧ラベルで読込":TSF_Forth_peekLthey,
#        "#TSF_pokeLthe":TSF_Forth_pokeLthe, "#指定スタックラベルで上書":TSF_Forth_pokeLthe,
#        "#TSF_pokeLthis":TSF_Forth_pokeLthis, "#実行中スタックラベルで上書":TSF_Forth_pokeLthis,
#        "#TSF_pokeLthat":TSF_Forth_pokeLthat, "#積込先スタックラベルで上書":TSF_Forth_pokeLthat,
#        "#TSF_pokeLthey":TSF_Forth_pokeLthey, "#スタック一覧ラベルで上書":TSF_Forth_pokeLthey,
#        "#TSF_pullLthe":TSF_Forth_pullLthe, "#指定スタックラベルで引抜":TSF_Forth_pullLthe,
#        "#TSF_pullLthis":TSF_Forth_pullLthis, "#実行中スタックラベルで引抜":TSF_Forth_pullLthis,
#        "#TSF_pullLthat":TSF_Forth_pullLthat, "#積込先スタックラベルで引抜":TSF_Forth_pullLthat,
#        "#TSF_pullLthey":TSF_Forth_pullLthey, "#スタック一覧ラベルで引抜":TSF_Forth_pullLthey,
#        "#TSF_pushLthe":TSF_Forth_pushLthe, "#指定スタックラベルで差込":TSF_Forth_pushLthe,
#        "#TSF_pushLthis":TSF_Forth_pushLthis, "#実行中スタックラベルで差込":TSF_Forth_pushLthis,
#        "#TSF_pushLthat":TSF_Forth_pushLthat, "#積込先スタックラベルで差込":TSF_Forth_pushLthat,
#        "#TSF_pushLthey":TSF_Forth_pushLthey, "#スタック一覧ラベルで差込":TSF_Forth_pushLthey,
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Forth_fin():    #TSFdoc:TSF終了時のオプションを指定する。1枚[errmsg]ドロー。
    global TSF_fincode
    global TSF_callptrD,TSF_callptrO
    TSF_callptrD={};  TSF_callptrO=[];
    return "#exit"

def TSF_Forth_countmax():    #TSFdoc:TSFスタックのカード数え上げ枚数の上限を指定。1枚[errmsg]ドロー。
    global TSF_stackmax
    TSF_stackmax=TSF_Io_RPNzero(TSF_Forth_drawthe())
    return ""

def TSF_Forth_this():    #TSF_doc:thisスタックの変更。1枚[this]ドロー。
    TSF_card=TSF_Forth_drawthe();
    if len(TSF_card) == 0 or TSF_card.startswith('#'):  TSF_cardnow="#exit"
    return TSF_card

def TSF_Forth_that():    #TSF_doc:thatスタックの変更。1枚[that]ドロー。
    TSF_Forth_drawthat(TSF_Forth_drawthe())
    return ""

def TSF_Forth_stylethe():    #TSFdoc:指定したスタックの表示方法を指定する。2枚[style,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_style(TSF_the,TSF_Forth_drawthe())
    return ""

def TSF_Forth_stylethis():    #TSFdoc:実行中スタックの表示方法を指定する。1枚[style]ドロー。
    TSF_Forth_style(TSF_Forth_drawthis(),TSF_Forth_drawthe())
    return ""

def TSF_Forth_stylethat():    #TSFdoc:積込先スタックの表示方法を指定する。1枚[style]ドロー。
    TSF_Forth_style(TSF_Forth_drawthat(),TSF_Forth_drawthe())
    return ""

def TSF_Forth_stylethey():    #TSFdoc:全スタックの表示方法を一括指定。1枚[style]ドロー。
    TSF_style=TSF_Forth_drawthe()
    for TSF_the in TSF_stackO:
        TSF_Forth_style(TSF_the,TSF_style)
    return ""

def TSF_Forth_viewthe():    #TSFdoc:指定スタックを表示する。1枚[the]ドロー。
    TSF_Forth_view(TSF_Forth_drawthe())
    return ""

def TSF_Forth_viewthis():    #TSFdoc:実行中スタックを表示する。0枚ドロー。
    TSF_Forth_view(TSF_Forth_drawthis())
    return ""

def TSF_Forth_viewthat():    #TSFdoc:積込先スタックを表示する。0枚ドロー。
    TSF_Forth_view(TSF_Forth_drawthat())
    return ""

def TSF_Forth_viewthey():    #TSFdoc:スタック一覧を表示する。0枚ドロー。
    for TSF_the in TSF_stackO:
        TSF_Forth_view(TSF_the)
    return ""

def TSF_Forth_RPN():    #TSF_doc:RPN電卓。1枚[rpn]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Io_RPN(TSF_Forth_drawthe()))
    return ""

def TSF_Forth_echo():    #TSF_doc:カードの表示。1枚[echo]ドロー。
    global TSF_echo_log
    if TSF_echo:
        TSF_echo_log=TSF_Io_printlog(TSF_Forth_drawthe(),TSF_echo_log)
    else:
        TSF_Io_printlog(TSF_Forth_drawthe())
    return ""

def TSF_Forth_echoN():    #TSF_doc:カードの複数枚表示。RPN枚[echoN…echoA,N]ドロー。
    TSF_echoRPN=TSF_Io_RPNzero(TSF_Forth_drawthe())
    if TSF_echoRPN > 0:
        for TSF_count in range(TSF_echoRPN):
            TSF_Forth_echo()
    return ""

def TSF_Forth_argvs():    #TSF_doc:コマンドを積込む。0枚[]ドローしてコマンド枚数+1枚[argvN…argvA,N]リターン。
    TSF_len=len(TSF_mainandargvs[1:]) if len(TSF_mainandargvs) > 0 else 0
    if TSF_len > 0:
        for TSF_card in TSF_mainandargvs[1:]:
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_len))
    return ""

def TSF_Forth_argvsthe():    #TSF_doc:指定スタックを積込む。1枚[the]ドローしてスタック枚数+1枚[cardN…cardA,N]リターン。
    TSF_the=TSF_Forth_drawthe()
    if TSF_the in TSF_stackD:
        for TSF_card in TSF_stackD[TSF_the]:
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackD[TSF_the])))
    return ""

def TSF_Forth_argvsthis():    #TSF_doc:実行中スタックを積込む。0枚[]ドローしてスタック枚数+1枚[cardN…cardA,N]リターン。
    TSF_the=TSF_Forth_drawthis()
    if TSF_the in TSF_stackD:
        for TSF_card in TSF_stackD[TSF_the]:
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackD[TSF_the])))
    return ""

def TSF_Forth_argvsthat():    #TSF_doc:積込先スタックを積込む。0枚[]ドローしてスタック枚数+1枚[cardN…cardA,N]リターン。
    TSF_the=TSF_Forth_drawthat()
    if TSF_the in TSF_stackD:
        for TSF_card in TSF_stackD[TSF_the]:
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackD[TSF_the])))
    return ""

def TSF_Forth_argvsthey():    #TSF_doc:スタック一覧を積込む。0枚[]ドローしてスタック枚数+1枚[cardN…cardA,N]リターン。
    for TSF_card in TSF_stackO:
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackO)))
    return ""

def TSF_Forth_reverseN():    #TSF_doc:カードN枚を逆順に積込。カード枚数+1枚[cardN…cardA,N]ドローしてカード枚数[cardN…cardA]リターン。
    TSF_stackR=[]
    TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe())
    if TSF_len > 0:
        for TSF_count in range(TSF_len):
            TSF_stackR.append(TSF_Forth_drawthe())
        for TSF_card in TSF_stackR:
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    return ""

def TSF_Forth_joinN():    #TSF_doc:カードN枚を連結する。カード枚数+1枚[cardN…cardA,N]ドローして1枚[joined]リターン。
    TSF_stackR=[]
    TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe())
    if TSF_len > 0:
        for TSF_count in range(TSF_len):
            TSF_stackR.append(TSF_Forth_drawthe())
        TSF_Forth_return(TSF_Forth_drawthat(),"".join(reversed(TSF_stackR)))
    return ""

def TSF_Forth_len(TSF_the):    #TSF_doc:指定スタックの枚数を取得。(TSFAPI)。
    TSF_len=0
    if TSF_the in TSF_stackD:
        TSF_len=len(TSF_stackD[TSF_the])
    return TSF_len

def TSF_Forth_lenthe():    #TSF_doc:指定スタックの枚数を取得。1枚[the]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_Forth_len(TSF_Forth_drawthe())))
    return ""

def TSF_Forth_lenthis():    #TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_Forth_len(TSF_Forth_drawthis())))
    return ""

def TSF_Forth_lenthat():    #TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_Forth_len(TSF_Forth_drawthat())))
    return ""

def TSF_Forth_lenthey():    #TSF_doc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackD)))
    return ""

def TSF_Forth_peekF(TSF_the):    #TSF_doc:指定スタックから表面カードを読込。(TSFAPI)。
    TSF_pull=""
    if TSF_the in TSF_stackD and 0 < len(TSF_stackD[TSF_the]):
        TSF_pull=TSF_stackD[TSF_the][-1]
    return TSF_pull

def TSF_Forth_peekFthe():   #TSF_doc:指定スタックから表面カードを読込。1枚[the]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekF(TSF_Forth_drawthe()))
    return ""

def TSF_Forth_peekFthis():   #TSF_doc:実行中スタックから表面カードを読込。0枚[]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekF(TSF_Forth_drawthis()))
    return ""

def TSF_Forth_peekFthat():   #TSF_doc:積込先スタックから表面カードを読込(旧「#TSF_carbonthat」に該当)。0枚[]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekF(TSF_Forth_drawthat()))
    return ""

def TSF_Forth_peekFthey():   #TSF_doc:スタック一覧から表面カードを読込。0枚[]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_stackO[-1] if len(TSF_stackO) else "")
    return ""

def TSF_Forth_peekN(TSF_the,TSF_peek):    #TSF_doc:指定スタックからカードを数値で読込。(TSFAPI)。
    TSF_pull=""
    if TSF_the in TSF_stackD and 0 <= TSF_peek < len(TSF_stackD[TSF_the]):
        TSF_pull=TSF_stackD[TSF_the][TSF_peek]
    return TSF_pull

def TSF_Forth_peekNthe():   #TSF_doc:指定スタックからカードを数値で読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekN(TSF_Forth_drawthe(),TSF_peek))
    return ""

def TSF_Forth_peekNthis():   #TSF_doc:実行中スタックからカードを数値で読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekN(TSF_Forth_drawthis(),TSF_Io_RPNzero(TSF_Forth_drawthe())))
    return ""

def TSF_Forth_peekNthat():   #TSF_doc:積込先スタックからカードを数値で読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_peekN(TSF_Forth_drawthat(),TSF_Io_RPNzero(TSF_Forth_drawthe())))
    return ""

def TSF_Forth_peekNthey():   #TSF_doc:スタック一覧からカードを数値で読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Io_separatepeekN(TSF_stackO,TSF_Io_RPNzero(TSF_Forth_drawthe())))
    return ""

def TSF_Forth_pullF(TSF_the):    #TSF_doc:指定スタックから表面カードを引抜。(TSFAPI)
    TSF_pull=""
    if TSF_the in TSF_stackD:
        TSF_pull=TSF_stackD[TSF_the].pop()
    return TSF_pull

def TSF_Forth_pullFthe():    #TSF_doc:指定スタックから表面カードを引抜。1枚[the]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_pullF(TSF_Forth_drawthe()))
    return ""

def TSF_Forth_pullFthis():    #TSF_doc:実行中スタックから表面カードを引抜。0枚[]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_pullF(TSF_Forth_drawthis()))
    return ""

def TSF_Forth_pullFthat():    #TSF_doc:積込先スタックから表面カードを引抜のみ(リターンしない)。1枚[card]ドロー。
    TSF_Forth_pullF(TSF_Forth_drawthat())
    return ""

def TSF_Forth_pullFthey():    #TSF_doc:スタック一覧から表面カードを引抜。0枚[]ドローして1枚[card]リターン。
    TSF_pull=""
    if len(TSF_stackO):
        TSF_pull=TSF_stackO.pop()
        TSF_stackD.pop(TSF_pull)
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_pull)
    return ""

def TSF_Forth_readtext():    #TSF_doc:ファイル名のスタックにテキストを読み込む。1枚[path]ドロー。
    TSF_path=TSF_Forth_drawthe()
    TSF_Forth_loadtext(TSF_path,TSF_path)
    return ""

def TSF_Forth_mergethe():    #TSF_doc:テキストをTSFとして読み込む。1枚[merge]ドロー。
    TSF_Forth_merge(TSF_Forth_drawthe(),[TSF_Forth_1ststack()])
    return ""

def TSF_Forth_publishthe():    #TSF_doc:指定スタックをテキスト化。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_publish_log=TSF_Forth_view(TSF_the,False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_the])
    return ""

def TSF_Forth_publishthis():    #TSF_doc:実行中スタックをテキスト化。1枚[path]ドロー。
    TSF_publish_log=TSF_Forth_view(TSF_Forth_drawthis(),False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_Forth_drawthis()])
    return ""

def TSF_Forth_publishthat():    #TSF_doc:積込先スタックをテキスト化。1枚[path]ドロー。
    TSF_publish_log=TSF_Forth_view(TSF_Forth_drawthat(),False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_Forth_drawthat()])
    return ""

def TSF_Forth_remove():    #TSF_doc:ファイルを削除する。1枚[path]ドロー。
    TSF_Io_savetext(TSF_Forth_drawthe())
    return ""

def TSF_Forth_savetext():    #TSF_doc:テキスト化スタックをファイルに保存する。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_text=TSF_Io_ESCdecode("\n".join(TSF_stackD[TSF_the])) if TSF_the in TSF_stackD else ""
    TSF_Io_savetext(TSF_Forth_drawthe(),TSF_text)
    return ""

def TSF_Forth_writetext():    #TSF_doc:テキスト化スタックをファイルに追記する。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_text=TSF_Io_ESCdecode("\n".join(TSF_stackD[TSF_the])) if TSF_the in TSF_stackD else ""
    TSF_Io_writetext(TSF_Forth_drawthe(),TSF_text)
    return ""


TSF_mainandargvs=[]
TSF_cardD={}
TSF_stackD={}
TSF_styleD={}
TSF_callptrD={}
TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO=[],[],[],[]
TSF_stackthis,TSF_stackthat=TSF_Forth_1ststack(),TSF_Forth_1ststack()
TSF_cardscount=0
def TSF_Forth_initTSF(TSF_sysargvs=[],TSF_addcards=[]):    #TSFdoc:スタックやカードなどをまとめて初期化する(TSFAPI)。
    global TSF_mainandargvs
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    TSF_cardD={}
    TSF_stackD={}
    TSF_styleD={}
    TSF_callptrD={}
    TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO=[],[],[],[]
    TSF_stackthis,TSF_stackthat=TSF_Forth_1ststack(),TSF_Forth_1ststack()
    TSF_cardscount=0
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"#TSF_fin.","T")
    TSF_mainandargvs=TSF_sysargvs
    TSF_Initcards=[TSF_Forth_Initcards]+TSF_addcards
    for TSF_Initcall in TSF_Initcards:
        TSF_cardD,TSF_cardO=TSF_Initcall(TSF_cardD,TSF_cardO)

def TSF_Forth_style(TSF_the,TSF_style=None):    #TSF_doc:スタックの表示スタイルを指定する(TSFAPI)。
    global TSF_styles
    if TSF_the in TSF_stackD:
        if TSF_style != None:
            TSF_styleD[TSF_the]=TSF_style
        TSF_style=TSF_styleD[TSF_the]
    else:
        TSF_style=""
    return TSF_style

def TSF_Forth_setTSF(TSF_the,TSF_text=None,TSF_style=None):    #TSFdoc:TSFの外からスタックにカードを積む/無を積むと削除。(TSFAPI)
    global TSF_stackD,TSF_styleD,TSF_stackO,TSF_styleO
    if TSF_style == None: TSF_style="T"
    if TSF_text != None:
        if not TSF_the in TSF_stackD:
            TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
        TSF_stackD[TSF_the]=TSF_text.rstrip('\n').replace('\t','\n').split('\n')
        TSF_styleD[TSF_the]=TSF_style
    else:
        if TSF_the in TSF_stackD:  del TSF_stackD[TSF_the]
        if TSF_the in TSF_styleD:  del TSF_styleD[TSF_the]
        if TSF_the in TSF_stackO: TSF_stackO.pop(TSF_stackO.index(TSF_the))
        if TSF_the in TSF_styleO: TSF_styleO.pop(TSF_styleO.index(TSF_the))

def TSF_Forth_loadtext(TSF_the,TSF_path):    #TSF_doc:スタックにテキストファイルを読み込む。(TSFAPI)
    TSF_text=TSF_Io_loadtext(TSF_path)
    TSF_text=TSF_Io_ESCencode(TSF_text)
    TSF_Forth_setTSF(TSF_the,TSF_text,"N")
    return TSF_text

def TSF_Forth_merge(TSF_path,TSF_ESCstack=[],TSF_mergedel=False):    #TSF_doc:スタック内のテキストをTSFとして読み込む。(TSFAPI)
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    if TSF_path in TSF_stackD:
        TSF_the=TSF_Forth_1ststack()
        for TSF_card in TSF_stackD[TSF_path]:
            if len(TSF_card) == 0 or TSF_card.startswith("#"): continue;
            TSF_line=TSF_Io_ESCdecode(TSF_card)
            if not TSF_line.startswith('\t'):
                TSF_lineL=TSF_line.split('\t')
                if not TSF_lineL[0] in TSF_ESCstack:
                    TSF_the=TSF_lineL[0]
                    if not TSF_the in TSF_stackD:
                        TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
                    TSF_stackD[TSF_the]=[]
                    TSF_styleD[TSF_the]="O" if len(TSF_lineL) >= 2 else ""
            if not TSF_the in TSF_ESCstack:
                TSF_lineL=TSF_line.split('\t')[1:]
                if not TSF_the in TSF_stackD:
                    TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
                TSF_stackD[TSF_the].extend(TSF_lineL)
                if TSF_styleD[TSF_the] != "O":
                    TSF_styleD[TSF_the]="T" if len(TSF_lineL) >= 2 else "N"
        if TSF_mergedel:
             TSF_Forth_setTSF(TSF_path)

TSF_stackmax=256
TSF_echo,TSF_echo_log=False,""
def TSF_Forth_run(TSF_run_log=None):    #TSFdoc:TSFデッキを走らせる。
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    global TSF_echo,TSF_echo_log
    if TSF_run_log != None:
        TSF_echo,TSF_echo_log=True,TSF_run_log
    else:
        TSF_echo,TSF_echo_log=False,""
    if not "#TSF_fin." in TSF_stackD[TSF_Forth_1ststack()]:
        TSF_Forth_return(TSF_Forth_1ststack(),"#TSF_fin.")
    while True:
        while TSF_cardscount < len(TSF_stackD[TSF_stackthis]) and TSF_cardscount < TSF_stackmax:
            TSF_cardnow=TSF_stackD[TSF_stackthis][TSF_cardscount];  TSF_cardscount+=1;
            if not TSF_cardnow in TSF_cardD:
                TSF_Forth_return(TSF_stackthat,TSF_cardnow)
            else:
                TSF_stacknext=TSF_cardD[TSF_cardnow]()
                if TSF_stacknext == "":
                    continue
                elif not TSF_stacknext in TSF_stackD:
                    break
                else:
                    while TSF_stacknext in TSF_callptrO:
                        TSF_callptrD.pop(TSF_callptrO.pop())
                    TSF_callptrD[TSF_stackthis]=TSF_cardscount;  TSF_callptrO.append(TSF_stackthis);
                    TSF_stackthis=TSF_stacknext
                    TSF_cardscount=0
        if len(TSF_callptrO) > 0:
            TSF_stackthis=TSF_callptrO[-1]; TSF_cardscount=TSF_callptrD[TSF_callptrO[-1]];
            TSF_callptrD.pop(TSF_callptrO.pop())
        else:
            break
    return TSF_echo_log

def TSF_Forth_view(TSF_the,TSF_view_io=True,TSF_view_log=""):    #TSFdoc:スタックの内容をテキスト表示(TSFAPI)。
    if TSF_view_log == None: TSF_view_log="";
    if TSF_the in TSF_stackD:
        TSF_style=TSF_styleD.get(TSF_the,"T")
        if TSF_style == "O":
            TSF_view_logline="{0}\t{1}\n".format(TSF_the,"\t".join(TSF_stackD[TSF_the]))
        elif TSF_style == "T":
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_the,"\t".join(TSF_stackD[TSF_the]))
        else:  # TSF_style == "N":
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_the,"\n\t".join(TSF_stackD[TSF_the]))
        TSF_view_log=TSF_Io_printlog(TSF_view_logline,TSF_log=TSF_view_log) if TSF_view_io == True else TSF_view_log+TSF_view_logline
    return TSF_view_log

def TSF_Forth_draw(TSF_the):    #TSFdoc:スタックから1枚ドロー。(TSFAPI)
    global TSF_stackD,TSF_stackO
    TSF_draw=""
    if len(TSF_stackD[TSF_the]) and len(TSF_the) and TSF_the in TSF_stackD:
        TSF_draw=TSF_stackD[TSF_the].pop()
    return TSF_draw

def TSF_Forth_drawthe():    #TSFdoc:theスタックの取得(thatから1枚ドロー)。(TSFAPI)
    return TSF_Forth_draw(TSF_stackthat)

def TSF_Forth_drawthis(TSF_the=None):    #TSFdoc:thisスタックの取得(thatから0枚ドロー)。(TSFAPI)
    global TSF_stackthis
    if TSF_the != None:
        TSF_stackthis=TSF_the
    return TSF_stackthis

def TSF_Forth_drawthat(TSF_the=None):    #TSFdoc:thatスタックの取得(thatから0枚ドロー)。(TSFAPI)
    global TSF_stackthat
    if TSF_the != None:
        TSF_stackthat=TSF_the
    return TSF_stackthat

def TSF_Forth_return(TSF_the,TSF_card):    #TSFdoc:theスタックに1枚リターン。(TSFAPI)
    if not TSF_the in TSF_stackD:
        TSF_stackO.append(TSF_the)
        TSF_stackD[TSF_the]=[]
    TSF_stackD[TSF_the].append(TSF_card)


TSF_Initcalldebug=[TSF_Forth_Initcards]
def TSF_Io_debug(TSF_sysargvs):    #TSFdoc:「TSF_Forth」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_pyForth.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"PPPP:\t#TSF_this\tTSF_argvs:\t#TSF_that\t#TSF_argvs\t#TSF_fin.","T")
    TSF_Forth_setTSF("PPPP:","this:Peek\tthat:Poke\tthe:Pull\tthey:Push\t2\t#TSF_echoN\tlen:\t#TSF_this","T")
    TSF_Forth_setTSF("len:","len:\t#TSF_that\tlen:\t#TSF_lenthe\t#TSF_lenthis\t#TSF_lenthat\t#TSF_lenthey\t#exit\t#TSF_this","T")
    for TSF_the in TSF_stackO:
        TSF_debug_log=TSF_Forth_view(TSF_the,True,TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("--- run ---",TSF_debug_log)
    TSF_debug_log=TSF_Forth_run(TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("--- fin. ---",TSF_debug_log)
    for TSF_the in TSF_stackO:
        TSF_debug_log=TSF_Forth_view(TSF_the,True,TSF_debug_log)
    TSF_debug_log=TSF_Io_printlog("--- {0} > {1} ---".format(__file__,TSF_debug_savefilename),TSF_debug_log)
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)
    return TSF_debug_log


if __name__=="__main__":
    TSF_Io_debug(TSF_Io_argvs(["python","TSF_Forth.py"]))


# Copyright (c) 2017 ooblog
# License: MIT
# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
