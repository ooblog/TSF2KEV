#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals
import random
import re
from TSF_Io import *

def TSF_Forth_1ststack():    #TSFdoc:最初のスタック名(TSFAPI)。
    return "TSF_Tab-Separated-Forth:"

def TSF_Forth_branchID():    #TSFdoc:TSFブランチ名(TSFAPI)。
    return "20170628W165418"

def TSF_Forth_grammarID():    #TSFdoc:TSF文法管理番号(TSFAPI)。
    return "2"

def TSF_Forth_foolangID():    #TSFdoc:TSF実装言語(TSFAPI)。
    return "Python"

random.seed()
def TSF_Forth_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:ワードを初期化する(TSFAPI)。
    TSF_Forth_importlist("TSF_Forth")
    TSF_Forth_cards={
        "#TSF_fin.":TSF_Forth_fin, "#TSFを終了。":TSF_Forth_fin,
        "#TSF_runagain":TSF_Forth_runagain, "#TSFを再走":TSF_Forth_runagain,
        "#TSF_runagainN":TSF_Forth_runagainN, "#TSFをコマンド付き再走":TSF_Forth_runagainN,
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
        "#TSF_join[]":TSF_Forth_joinsquarebrackets, "#括弧で連結":TSF_Forth_joinsquarebrackets,
        "#TSF_sandwichN":TSF_Forth_sandwichN, "#N枚挟んで1枚化":TSF_Forth_sandwichN,
        "#TSF_split":TSF_Forth_split, "#文字で分割":TSF_Forth_split,
        "#TSF_chars":TSF_Forth_chars, "#一文字ずつに分割":TSF_Forth_chars,
        "#TSF_charslen":TSF_Forth_charslen, "#文字数を数える":TSF_Forth_charslen,
        "#TSF_lenthe":TSF_Forth_lenthe, "#指定スタック枚数":TSF_Forth_lenthe,
        "#TSF_lenthis":TSF_Forth_lenthis, "#実行中スタック枚数":TSF_Forth_lenthis,
        "#TSF_lenthat":TSF_Forth_lenthat, "#積込先スタック枚数":TSF_Forth_lenthat,
        "#TSF_lenthey":TSF_Forth_lenthey, "#スタック一覧枚数":TSF_Forth_lenthey,
        "#TSF_peekFthe":TSF_Forth_peekFthe, "#指定スタック表択読込":TSF_Forth_peekFthe,
        "#TSF_peekFthis":TSF_Forth_peekFthis, "#実行中スタック表択読込":TSF_Forth_peekFthis,
        "#TSF_peekFthat":TSF_Forth_peekFthat, "#積込先スタック表択読込":TSF_Forth_peekFthat,
        "#TSF_peekFthey":TSF_Forth_peekFthey, "#スタック一覧表択読込":TSF_Forth_peekFthey,
        "#TSF_pokeFthe":TSF_Forth_pokeFthe, "#指定スタック表択上書":TSF_Forth_pokeFthe,
        "#TSF_pokeFthis":TSF_Forth_pokeFthis, "#実行中スタック表択上書":TSF_Forth_pokeFthis,
        "#TSF_pokeFthat":TSF_Forth_pokeFthat, "#積込先スタック表択上書":TSF_Forth_pokeFthat,
        "#TSF_pokeFthey":TSF_Forth_pokeFthey, "#スタック一覧表択上書":TSF_Forth_pokeFthey,
        "#TSF_pullFthe":TSF_Forth_pullFthe, "#指定スタック表択引抜":TSF_Forth_pullFthe,
        "#TSF_pullFthis":TSF_Forth_pullFthis, "#実行中スタック表択引抜":TSF_Forth_pullFthis,
        "#TSF_pullFthat":TSF_Forth_pullFthat, "#積込先スタック表択引抜":TSF_Forth_pullFthat,
        "#TSF_pullFthey":TSF_Forth_pullFthey, "#スタック一覧表択引抜":TSF_Forth_pullFthey,
        "#TSF_pushFthe":TSF_Forth_pushFthe, "#指定スタック表択差込":TSF_Forth_pushFthe,
        "#TSF_pushFthis":TSF_Forth_pushFthis, "#実行中スタック表択差込":TSF_Forth_pushFthis,
        "#TSF_pushFthat":TSF_Forth_pushFthat, "#積込先スタック表択差込":TSF_Forth_pushFthat,
        "#TSF_pushFthey":TSF_Forth_pushFthey, "#スタック一覧表択差込":TSF_Forth_pushFthey,
        "#TSF_peekNthe":TSF_Forth_peekNthe, "#指定スタック順択読込":TSF_Forth_peekNthe,
        "#TSF_peekNthis":TSF_Forth_peekNthis, "#実行中スタック順択読込":TSF_Forth_peekNthis,
        "#TSF_peekNthat":TSF_Forth_peekNthat, "#積込先スタック順択読込":TSF_Forth_peekNthat,
        "#TSF_peekNthey":TSF_Forth_peekNthey, "#スタック一覧順択読込":TSF_Forth_peekNthey,
        "#TSF_pokeNthe":TSF_Forth_pokeNthe, "#指定スタック順択上書":TSF_Forth_pokeNthe,
        "#TSF_pokeNthis":TSF_Forth_pokeNthis, "#実行中スタック順択上書":TSF_Forth_pokeNthis,
        "#TSF_pokeNthat":TSF_Forth_pokeNthat, "#積込先スタック順択上書":TSF_Forth_pokeNthat,
        "#TSF_pokeNthey":TSF_Forth_pokeNthey, "#スタック一覧順択上書":TSF_Forth_pokeNthey,
        "#TSF_pullNthe":TSF_Forth_pullNthe, "#指定スタック順択引抜":TSF_Forth_pullNthe,
        "#TSF_pullNthis":TSF_Forth_pullNthis, "#実行中スタック順択引抜":TSF_Forth_pullNthis,
        "#TSF_pullNthat":TSF_Forth_pullNthat, "#積込先スタック順択引抜":TSF_Forth_pullNthat,
        "#TSF_pullNthey":TSF_Forth_pullNthey, "#スタック一覧順択引抜":TSF_Forth_pullNthey,
        "#TSF_pushNthe":TSF_Forth_pushNthe, "#指定スタック順択差込":TSF_Forth_pushNthe,
        "#TSF_pushNthis":TSF_Forth_pushNthis, "#実行中スタック順択差込":TSF_Forth_pushNthis,
        "#TSF_pushNthat":TSF_Forth_pushNthat, "#積込先スタック順択差込":TSF_Forth_pushNthat,
        "#TSF_pushNthey":TSF_Forth_pushNthey, "#スタック一覧順択差込":TSF_Forth_pushNthey,
        "#TSF_peekCthe":TSF_Forth_peekCthe, "#指定スタック周択読込":TSF_Forth_peekCthe,
        "#TSF_peekCthis":TSF_Forth_peekCthis, "#実行中スタック周択読込":TSF_Forth_peekCthis,
        "#TSF_peekCthat":TSF_Forth_peekCthat, "#積込先スタック周択読込":TSF_Forth_peekCthat,
        "#TSF_peekCthey":TSF_Forth_peekCthey, "#スタック一覧周択読込":TSF_Forth_peekCthey,
        "#TSF_pokeCthe":TSF_Forth_pokeCthe, "#指定スタック周択上書":TSF_Forth_pokeCthe,
        "#TSF_pokeCthis":TSF_Forth_pokeCthis, "#実行中スタック周択上書":TSF_Forth_pokeCthis,
        "#TSF_pokeCthat":TSF_Forth_pokeCthat, "#積込先スタック周択上書":TSF_Forth_pokeCthat,
        "#TSF_pokeCthey":TSF_Forth_pokeCthey, "#スタック一覧周択上書":TSF_Forth_pokeCthey,
        "#TSF_pullCthe":TSF_Forth_pullCthe, "#指定スタック周択引抜":TSF_Forth_pullCthe,
        "#TSF_pullCthis":TSF_Forth_pullCthis, "#実行中スタック周択引抜":TSF_Forth_pullCthis,
        "#TSF_pullCthat":TSF_Forth_pullCthat, "#積込先スタック周択引抜":TSF_Forth_pullCthat,
        "#TSF_pullCthey":TSF_Forth_pullCthey, "#スタック一覧周択引抜":TSF_Forth_pullCthey,
        "#TSF_pushCthe":TSF_Forth_pushCthe, "#指定スタック周択差込":TSF_Forth_pushCthe,
        "#TSF_pushCthis":TSF_Forth_pushCthis, "#実行中スタック周択差込":TSF_Forth_pushCthis,
        "#TSF_pushCthat":TSF_Forth_pushCthat, "#積込先スタック周択差込":TSF_Forth_pushCthat,
        "#TSF_pushCthey":TSF_Forth_pushCthey, "#スタック一覧周択差込":TSF_Forth_pushCthey,
        "#TSF_peekMthe":TSF_Forth_peekMthe, "#指定スタック囲択読込":TSF_Forth_peekMthe,
        "#TSF_peekMthis":TSF_Forth_peekMthis, "#実行中スタック囲択読込":TSF_Forth_peekMthis,
        "#TSF_peekMthat":TSF_Forth_peekMthat, "#積込先スタック囲択読込":TSF_Forth_peekMthat,
        "#TSF_peekMthey":TSF_Forth_peekMthey, "#スタック一覧囲択読込":TSF_Forth_peekMthey,
        "#TSF_pokeMthe":TSF_Forth_pokeMthe, "#指定スタック囲択上書":TSF_Forth_pokeMthe,
        "#TSF_pokeMthis":TSF_Forth_pokeMthis, "#実行中スタック囲択上書":TSF_Forth_pokeMthis,
        "#TSF_pokeMthat":TSF_Forth_pokeMthat, "#積込先スタック囲択上書":TSF_Forth_pokeMthat,
        "#TSF_pokeMthey":TSF_Forth_pokeMthey, "#スタック一覧囲択上書":TSF_Forth_pokeMthey,
        "#TSF_pullMthe":TSF_Forth_pullMthe, "#指定スタック囲択引抜":TSF_Forth_pullMthe,
        "#TSF_pullMthis":TSF_Forth_pullMthis, "#実行中スタック囲択引抜":TSF_Forth_pullMthis,
        "#TSF_pullMthat":TSF_Forth_pullMthat, "#積込先スタック囲択引抜":TSF_Forth_pullMthat,
        "#TSF_pullMthey":TSF_Forth_pullMthey, "#スタック一覧囲択引抜":TSF_Forth_pullMthey,
        "#TSF_pushMthe":TSF_Forth_pushMthe, "#指定スタック囲択差込":TSF_Forth_pushMthe,
        "#TSF_pushMthis":TSF_Forth_pushMthis, "#実行中スタック囲択差込":TSF_Forth_pushMthis,
        "#TSF_pushMthat":TSF_Forth_pushMthat, "#積込先スタック囲択差込":TSF_Forth_pushMthat,
        "#TSF_pushMthey":TSF_Forth_pushMthey, "#スタック一覧囲択差込":TSF_Forth_pushMthey,
        "#TSF_swapBA":TSF_Forth_swapBA, "#カードBA交換":TSF_Forth_swapBA,
        "#TSF_swapCA":TSF_Forth_swapCA, "#カードCA交換":TSF_Forth_swapCA,
        "#TSF_swapCB":TSF_Forth_swapCB, "#カードCB交換":TSF_Forth_swapCB,
        "#TSF_swapAA":TSF_Forth_swapAA, "#カードAA交換":TSF_Forth_swapAA,
        "#TSF_swapCC":TSF_Forth_swapCC, "#カードCC交換":TSF_Forth_swapCC,
        "#TSF_clonethe":TSF_Forth_clonethe, "#指定スタックの複製":TSF_Forth_clonethe,
        "#TSF_clonethis":TSF_Forth_clonethis, "#実行中スタックの複製":TSF_Forth_clonethis,
        "#TSF_clonethat":TSF_Forth_clonethat, "#積込先スタックの複製":TSF_Forth_clonethat,
        "#TSF_clonethey":TSF_Forth_clonethey, "#スタック一覧の複製":TSF_Forth_clonethey,
        "#TSF_readtext":TSF_Forth_readtext, "#テキストを読込":TSF_Forth_readtext,
        "#TSF_mergethe":TSF_Forth_mergethe, "#TSFに合成":TSF_Forth_mergethe,
#        "#TSF_mergeUSE":TSF_Forth_mergeUSE, "#ユーズリストを用いてTSFに合成":TSF_Forth_mergeUSE,
#        "#TSF_mergeESC":TSF_Forth_mergeESC, "#エスケープリストを用いてTSFに合成":TSF_Forth_mergeESC,
        "#TSF_publishthe":TSF_Forth_publishthe, "#指定スタックをテキスト化":TSF_Forth_publishthe,
        "#TSF_publishthis":TSF_Forth_publishthis, "#実行中スタックをテキスト化":TSF_Forth_publishthis,
        "#TSF_publishthat":TSF_Forth_publishthat, "#積込先スタックをテキスト化":TSF_Forth_publishthat,
        "#TSF_remove":TSF_Forth_remove, "#ファイルを削除する":TSF_Forth_remove,
        "#TSF_savetext":TSF_Forth_savetext, "#テキストファイルに上書":TSF_Forth_savetext,
        "#TSF_writetext":TSF_Forth_writetext, "#テキストファイルに追記":TSF_Forth_writetext,
        "#TSF_branch":TSF_Forth_branch, "#TSFのブランチ名":TSF_Forth_branch,
        "#TSF_grammar":TSF_Forth_grammar, "#TSFの文法管理番号":TSF_Forth_grammar,
        "#TSF_foolang":TSF_Forth_foolang, "#TSFの実装言語":TSF_Forth_foolang,
        "#TSF_mainfile":TSF_Forth_mainfile, "#実行ファイル名":TSF_Forth_mainfile,
   }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Forth_fin():    #TSFdoc:TSFを終了する。0枚[]ドロー。
    global TSF_callptrD,TSF_callptrO
    TSF_callptrD={};  TSF_callptrO=[];
    return "#exit:"

TSF_runagainN=[""];
def TSF_Forth_runagain():    #TSFdoc:TSFを終了せず、次のTSFを読み込んで実行。1枚[tsf]ドロー。
    global TSF_runagainN
    TSF_runagainN=[TSF_Forth_drawthe()]
    TSF_Forth_fin()
    return "#exit:"

def TSF_Forth_runagainN():    #TSFdoc:TSFを終了せず、次のTSFを読み込んでパラメータも付けて実行。カード枚数+1枚[cardN…cardA,N]ドロー。
    global TSF_runagainN
    TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_runagainN=[]
    if TSF_len > 0:
        for TSF_count in range(TSF_len):
           TSF_runagainN.append(TSF_Forth_drawthe())
    TSF_Forth_fin()
    return "#exit:"

def TSF_Forth_countmax():    #TSFdoc:TSFスタックのカード数え上げ枚数の上限を指定。1枚[errmsg]ドロー。
    global TSF_Forth_stackMAX
    TSF_Forth_stackMAX=TSF_Io_RPNzero(TSF_Forth_drawthe())
    return ""

def TSF_Forth_this():    #TSFdoc:thisスタックの変更。1枚[this]ドロー。
    TSF_card=TSF_Forth_drawthe();
    if len(TSF_card) == 0 or TSF_card.startswith('#'):  TSF_cardnow="#exit"
    return TSF_card

def TSF_Forth_that():    #TSFdoc:thatスタックの変更。1枚[that]ドロー。
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
    if TSF_echo:
        TSF_echo_log=TSF_Forth_view(TSF_Forth_drawthe(),True,TSF_echo_log)
    else:
        TSF_Forth_view(TSF_Forth_drawthe())
    return ""

def TSF_Forth_viewthis():    #TSFdoc:実行中スタックを表示する。0枚ドロー。
    if TSF_echo:
        TSF_echo_log=TSF_Forth_view(TSF_Forth_drawthis(),True,TSF_echo_log)
    else:
        TSF_Forth_view(TSF_Forth_drawthis())
    return ""

def TSF_Forth_viewthat():    #TSFdoc:積込先スタックを表示する。0枚ドロー。
    if TSF_echo:
        TSF_echo_log=TSF_Forth_view(TSF_Forth_drawthat(),True,TSF_echo_log)
    else:
        TSF_Forth_view(TSF_Forth_drawthat())
    return ""

def TSF_Forth_viewthey():    #TSFdoc:スタック一覧を表示する。0枚ドロー。
    for TSF_the in TSF_stackO:
        TSF_Forth_view(TSF_the)
    return ""

def TSF_Forth_RPN():    #TSFdoc:RPN電卓。1枚[rpn]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Io_RPN(TSF_Forth_drawthe()))
    return ""

def TSF_Forth_echo():    #TSFdoc:カードの表示。1枚[echo]ドロー。
    global TSF_echo_log
    if TSF_echo:
        TSF_echo_log=TSF_Io_printlog(TSF_Forth_drawthe(),TSF_echo_log)
    else:
        TSF_Io_printlog(TSF_Forth_drawthe())
    return ""

def TSF_Forth_echoN():    #TSFdoc:カードの複数枚表示。RPN枚[echoN…echoA,N]ドロー。
    TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe())
    if TSF_len > 0:
        for TSF_count in range(TSF_len):
            TSF_Forth_echo()
    return ""

def TSF_Forth_argvs():    #TSFdoc:コマンドを積込む。0枚[]ドローしてコマンド枚数+1枚[argvN…argvA,N]リターン。
    TSF_len=len(TSF_mainandargvs[1:]) if len(TSF_mainandargvs) > 0 else 0
    if TSF_len > 0:
        for TSF_card in TSF_mainandargvs[1:]:
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_len))
    return ""

def TSF_Forth_argvsthe():    #TSFdoc:指定スタックを積込む。1枚[the]ドローしてカード枚数+1枚[cardN…cardA,N]リターン。
    TSF_the=TSF_Forth_drawthe()
    if TSF_the in TSF_stackD:
        for TSF_card in reversed(TSF_stackD[TSF_the]):
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
        TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackD[TSF_the])))
    else:
        TSF_Forth_return(TSF_Forth_drawthat(),"0")
    return ""

def TSF_Forth_argvsthis():    #TSFdoc:実行中スタックを積込む。0枚[]ドローしてカード枚数+1枚[cardN…cardA,N]リターン。
    TSF_the=TSF_Forth_drawthis()
    if TSF_the in TSF_stackD:
        for TSF_card in reversed(TSF_stackD[TSF_the]):
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
        TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackD[TSF_the])))
    else:
        TSF_Forth_return(TSF_Forth_drawthat(),"0")
    return ""

def TSF_Forth_argvsthat():    #TSFdoc:積込先スタックを積込む。0枚[]ドローしてカード枚数+1枚[cardN…cardA,N]リターン。
    TSF_the=TSF_Forth_drawthat()
    if TSF_the in TSF_stackD:
        for TSF_card in reversed(TSF_stackD[TSF_the]):
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
        TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackD[TSF_the])))
    else:
        TSF_Forth_return(TSF_Forth_drawthat(),"0")
    return ""

def TSF_Forth_argvsthey():    #TSFdoc:スタック一覧を積込む。0枚[]ドローしてカード枚数+1枚[cardN…cardA,N]リターン。
    if len(TSF_stackO) > 0:
        for TSF_card in reversed(TSF_stackO):
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
            TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackO)))
    else:
        TSF_Forth_return(TSF_Forth_drawthat(),"0")
    return ""

def TSF_Forth_reverseN():    #TSFdoc:カードN枚を逆順に積込。カード枚数+総数1枚[cardN…cardA,N]ドローしてカード枚数[cardN…cardA]リターン。
    TSF_stackR=[]
    TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe())
    if TSF_len > 0:
        for TSF_count in range(TSF_len):
            TSF_stackR.append(TSF_Forth_drawthe())
        for TSF_card in TSF_stackR:
            TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    return ""

def TSF_Forth_joinN():    #TSFdoc:カードN枚を連結する。カード枚数+総数1枚[cardN…cardA,N]ドローして1枚[joined]リターン。
    TSF_stackR=[]
    TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe())
    if TSF_len > 0:
        for TSF_count in range(TSF_len):
            TSF_stackR.append(TSF_Forth_drawthe())
        TSF_Forth_return(TSF_Forth_drawthat(),"".join(reversed(TSF_stackR)))
    return ""

def TSF_Forth_joinsquarebrackets():    #TSFdoc:カードN枚を角括弧で連結する。数式の元を1枚[calc]ドローして1枚[joined]リターン。
    TSF_calc=TSF_Forth_drawthe()
    for TSF_count in range(TSF_Forth_len(TSF_Forth_drawthat())):
        TSF_bracket="".join(["[",str(TSF_count),"]"])
        if TSF_bracket in TSF_calc:
            TSF_calc=TSF_calc.replace(TSF_bracket,TSF_Forth_drawthe())
        else:
            break;
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_calc)
    return ""

def TSF_Forth_sandwichN():    #TSFdoc:カードN枚を連結する。カード枚数+総数1枚+接続詞1枚[cardN…cardA,N,joint]ドローして1枚[joined]リターン。
    TSF_stackR=[]
    TSF_joint=TSF_Forth_drawthe()
    TSF_len=TSF_Io_RPNzero(TSF_Forth_drawthe())
    if TSF_len > 0:
        for TSF_count in range(TSF_len):
            TSF_stackR.append(TSF_Forth_drawthe())
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_joint.join(reversed(TSF_stackR)))
    return ""

def TSF_Forth_split():    #TSFdoc:文字列を分割する。続詞1枚[joint]ドローしてカード枚数+総数1枚[cardN…cardA,N]リターン。
    TSF_joint=TSF_Forth_drawthe()
    TSF_joined=TSF_Forth_drawthe()
    TSF_stackR=TSF_joined.split(TSF_tsvP)
    for TSF_card in reversed(TSF_stackR):
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    return ""

def TSF_Forth_chars():    #TSFdoc:文字列を一文字ずつに分割する。1枚[chars]ドローしてカード枚数+総数1枚[cardN…cardA,N]リターン。
    TSF_joined=TSF_Forth_drawthe()
    for TSF_card in reversed(TSF_joined):
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_joined)))
    return ""

def TSF_Forth_charslen():    #TSFdoc:文字数を数える。1枚[chars]ドローして1枚[N]リターン。
    TSF_joined=TSF_Forth_drawthe()
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_joined)))
    return ""

def TSF_Forth_len(TSF_the):    #TSFdoc:指定スタックの枚数を取得。(TSFAPI)。
    TSF_len=0
    if TSF_the in TSF_stackD:
        TSF_len=len(TSF_stackD[TSF_the])
    return TSF_len

def TSF_Forth_lenthe():    #TSFdoc:指定スタックの枚数を取得。1枚[the]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_Forth_len(TSF_Forth_drawthe())))
    return ""

def TSF_Forth_lenthis():    #TSFdoc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_Forth_len(TSF_Forth_drawthis())))
    return ""

def TSF_Forth_lenthat():    #TSFdoc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),str(TSF_Forth_len(TSF_Forth_drawthat())))
    return ""

def TSF_Forth_lenthey():    #TSFdoc:指定スタックの枚数を取得。0枚[]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_stackD)))
    return ""

def TSF_Forth_cardsFNCMVA(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL):    #TSFdoc:peek,poke,pull,pushの共通部品。カードの位置を取得。(TSFAPI)
    TSF_Plist=[]
    TSF_peek=TSF_peek if TSF_peek != None else 0
    TSF_seek=TSF_seek if TSF_seek != None else ""
    if TSF_the != "":
        TSF_cardsL=len(TSF_stackD[TSF_the]) if TSF_the in TSF_stackD else 0
        if TSF_FNCMVAQIRHL == 'F':
            if 0 < TSF_cardsL:
                TSF_Plist+=[max(TSF_cardsL-1,0)]
        elif TSF_FNCMVAQIRHL == 'N':
            if 0 <= TSF_peek < TSF_cardsL: TSF_Plist+=[TSF_peek];
        elif TSF_FNCMVAQIRHL == 'C':
            if 0 < TSF_cardsL:
                TSF_Plist+=[TSF_peek%TSF_cardsL if TSF_peek >=0 else TSF_cardsL-(abs(TSF_peek)%TSF_cardsL)]
        elif TSF_FNCMVAQIRHL == 'M':
            if 0 < TSF_cardsL:
                TSF_Plist+=[min(max(TSF_peek,0),TSF_cardsL-1)]
        elif TSF_FNCMVAQIRHL == 'V':
            if 0 <= TSF_peek < TSF_cardsL: TSF_Plist+=[TSF_cardsL-1-TSF_peek];
        elif TSF_FNCMVAQIRHL == 'A':
            if 0 < TSF_cardsL:
                TSF_Plist+=[random.randint(0,TSF_cardsL-1)]
        elif TSF_FNCMVAQIRHL == 'Q':
            if 0 < TSF_cardsL:
                for TSF_peek,TSF_card in enumerate(TSF_stackD[TSF_the]):
                    if TSF_seek==TSF_card: TSF_Plist+=[TSF_peek]
        elif TSF_FNCMVAQIRHL == 'I':
            if 0 < TSF_cardsL:
                for TSF_peek,TSF_card in enumerate(TSF_stackD[TSF_the]):
                    if TSF_seek in TSF_card: TSF_Plist+=[TSF_peek]
        elif TSF_FNCMVAQIRHL == 'R':
            if 0 < TSF_cardsL:
                for TSF_peekreg,TSF_card in enumerate(TSF_stackD[TSF_the]):
                    try:
                        rewrite_research=re.search(re.compile(TSF_seek),TSF_card)
                    except re.error:
                        break
                    else:
                        if TSF_regsearch: TSF_Plist+=[TSF_peekreg]
        elif TSF_FNCMVAQIRHL == 'H':
            pass
        elif TSF_FNCMVAQIRHL == 'L':
            pass
    else:
        TSF_cardsL=len(TSF_stackO)
        if TSF_FNCMVAQIRHL == 'F':
            if 0 < TSF_cardsL:
                TSF_Plist+=[max(TSF_cardsL-1,0)]
        elif TSF_FNCMVAQIRHL == 'N':
            if 0 <= TSF_peek < TSF_cardsL: TSF_Plist+=[TSF_peek];
        elif TSF_FNCMVAQIRHL == 'C':
            if 0 < TSF_cardsL:
                TSF_Plist+=[TSF_peek%TSF_cardsL if TSF_peek >=0 else TSF_cardsL-(abs(TSF_peek)%TSF_cardsL)]
        elif TSF_FNCMVAQIRHL == 'M':
            if 0 < TSF_cardsL:
                TSF_Plist+=[min(max(TSF_peek,0),TSF_cardsL-1)]
        elif TSF_FNCMVAQIRHL == 'V':
            if 0 <= TSF_peek < TSF_cardsL: TSF_Plist+=[TSF_cardsL-1-TSF_peek];
        elif TSF_FNCMVAQIRHL == 'A':
            if 0 < TSF_cardsL:
                TSF_Plist+=[random.randint(0,TSF_cardsL-1)]
        elif TSF_FNCMVAQIRHL == 'Q':
            for TSF_peek,TSF_card in enumerate(TSF_stackO):
                if TSF_seek==TSF_card: TSF_Plist+=[TSF_peek]
        elif TSF_FNCMVAQIRHL == 'I':
            for TSF_peek,TSF_card in enumerate(TSF_stackO):
                if TSF_seek in TSF_card: TSF_Plist+=[TSF_peek]
        elif TSF_FNCMVAQIRHL == 'R':
            for TSF_peekreg,TSF_card in enumerate(TSF_stackO):
                try:
                    rewrite_research=re.search(re.compile(TSF_seek),TSF_card)
                except re.error:
                    break
                else:
                    if TSF_regsearch: TSF_Plist+=[TSF_peekreg]
        elif TSF_FNCMVAQIRHL == 'H':
            pass
        elif TSF_FNCMVAQIRHL == 'L':
            pass
    return TSF_Plist

def TSF_Forth_peek(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL):    #TSFdoc:peekの共通部品。(TSFAPI)
    TSF_the=TSF_the if TSF_the != None else ""
    TSF_Plist=TSF_Forth_cardsFNCMVA(TSF_the,TSF_peek,"",TSF_FNCMVAQIRHL)
    TSF_pulllist=[]
    if TSF_the != "":
        for TSF_P in TSF_Plist:
            TSF_pulllist+=[TSF_stackD[TSF_the][TSF_P]]
    else:
        for TSF_P in TSF_Plist:
            TSF_pulllist+=[TSF_stackO[TSF_P]]
    return TSF_pulllist

def TSF_Forth_poke(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL,TSF_poke):    #TSFdoc:pokeの共通部品。(TSFAPI)
    TSF_the=TSF_the if TSF_the != None else ""
    TSF_Plist=TSF_Forth_cardsFNCMVA(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL)
    TSF_pulllist=[]
    if TSF_the != "":
        for TSF_P in TSF_Plist:
            TSF_stackD[TSF_the][TSF_P]=TSF_poke
    else:
        for TSF_P in TSF_Plist:
            TSF_pull=TSF_stackO[TSF_P];
            TSF_stackO[TSF_P]=TSF_poke
            TSF_stackP=TSF_stackD.pop(TSF_pull)
            TSF_stackD[TSF_poke]=TSF_stackP

def TSF_Forth_pull(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL):    #TSFdoc:pullの共通部品。(TSFAPI)
    TSF_the=TSF_the if TSF_the != None else ""
    TSF_Plist=TSF_Forth_cardsFNCMVA(TSF_the,TSF_peek,"",TSF_FNCMVAQIRHL)
    TSF_pulllist=[]
    if TSF_the != "":
        for TSF_P in reversed(TSF_Plist):
            TSF_pulllist+=[TSF_Forth_stackD()[TSF_the][TSF_P]]
            TSF_stackD[TSF_the].pop(TSF_P)
    else:
        for TSF_P in reversed(TSF_Plist):
            TSF_pull=TSF_stackO[TSF_P]
            TSF_pulllist+=[TSF_pull]
            TSF_stackD.pop(TSF_pull)
            TSF_stackO.pop(TSF_P)
    return TSF_pulllist

def TSF_Forth_push(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL,TSF_poke):    #TSFdoc:pushの共通部品。(TSFAPI)
    TSF_the=TSF_the if TSF_the != None else ""
    TSF_Plist=TSF_Forth_cardsFNCMVA(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL)
    TSF_pulllist=[]
    if TSF_the != "":
        for TSF_P in reversed(TSF_Plist):
            TSF_stackD[TSF_the].insert(TSF_P,TSF_poke)
    else:
        for TSF_P in reversed(TSF_Plist):
            TSF_pull=TSF_stackO[TSF_P];
            if not TSF_pull in TSF_stackD:
                TSF_stackD[TSF_pull]=[];
                TSF_stackO.insert(TSF_P,TSF_poke);

def TSF_Forth_returnFNCMVA(TSF_pulllist):    #TSFdoc:peek,pullの共通部品。FNCMVAは単独のカードを返す。(TSFAPI)
    if len(TSF_pulllist) > 0:
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_pulllist[0])
    else:
        TSF_Forth_return(TSF_Forth_drawthat(),"")

def TSF_Forth_returnQIRH(TSF_pulllist):    #TSFdoc:peek,pullの共通部品。QIRHは複数のカードを返す。(TSFAPI)
    for TSF_card in TSF_pulllist:
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_pulllist)))

def TSF_Forth_peekFthe():    #TSFdoc:指定スタックから表択でカードを読込。1枚[the]ドローして1枚[peek]リターン。
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthe(),-1,"",'F'))
    return ""

def TSF_Forth_peekFthis():    #TSFdoc:実行中スタックから表択でカードを読込。0枚[]ドローして1枚[peek]リターン。
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthis(),-1,"",'F'))
    return ""

def TSF_Forth_peekFthat():    #TSFdoc:積込先スタックから表択でカードを読込。0枚[]ドローして1枚[peek]リターン。
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthat(),-1,"",'F'))
    return ""

def TSF_Forth_peekFthey():    #TSFdoc:スタック一覧から表択でカードを読込。0枚[]ドローして1枚[peek]リターン。
    TSF_Forth_returnFNCMVA(TSF_Forth_peek("",-1,"",'F'))
    return ""

def TSF_Forth_pokeFthe():    #TSFdoc:指定スタックからカードを表択で上書。2枚[poke,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_poke(TSF_the,-1,"",'F',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeFthis():    #TSFdoc:実行中スタックから表択でカードを上書。1枚[poke]ドロー。
    TSF_Forth_poke(TSF_Forth_drawthis(),-1,"",'F',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeFthat():    #TSFdoc:積込先スタックから表択でカードを上書。1枚[poke]ドロー。
    TSF_Forth_poke(TSF_Forth_drawthat(),-1,"",'F',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeFthey():    #TSFdoc:スタック一覧から表択でカードを上書。1枚[poke]ドロー。
    TSF_Forth_poke("",-1,"",'F',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pullFthe():    #TSFdoc:指定スタックから表択でカードを引抜。1枚[the]ドローして1枚[pull]リターン。
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthe(),-1,"",'F'))
    return ""

def TSF_Forth_pullFthis():    #TSFdoc:実行中スタックから表択でカードを引抜。0枚[]ドローして1枚[pull]リターン。
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthis(),-1,"",'F'))
    return ""

def TSF_Forth_pullFthat():    #TSFdoc:積込先スタックから表択でカードを引抜。リターンすると引抜にならないので例外的にリターンされない。
#    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthat(),-1,"",'F'))
    TSF_Forth_draw(TSF_Forth_drawthat())
    return ""

def TSF_Forth_pullFthey():    #TSFdoc:スタック一覧から表択でカードを引抜。0枚[]ドローして1枚[pull]リターン。
    TSF_Forth_returnFNCMVA(TSF_Forth_pull("",-1,"",'F'))
    return ""

def TSF_Forth_pushFthe():    #TSFdoc:指定スタックからカードを表択で差込。2枚[push,the]ドロー。pushFは例外的に存在しないスタックにも直接pushできる。
#    TSF_Forth_push(TSF_the,-1,"",'F',TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_return(TSF_the,TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushFthis():    #TSFdoc:実行中スタックから表択でカードを差込。1枚[push]ドロー。
#    TSF_Forth_push(TSF_Forth_drawthis(),-1,"",'F',TSF_Forth_drawthe())
    TSF_Forth_return(TSF_Forth_drawthis(),TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushFthat():    #TSFdoc:積込先スタックから表択でカードを差込。1枚ドローするが、実質同じガードがリターンするので変化無し。
#    TSF_Forth_push(TSF_Forth_drawthat(),-1,"",'F',TSF_Forth_drawthe())
#    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushFthey():    #TSFdoc:スタック一覧から表択でカードを差込。1枚[push]ドロー。
    TSF_Forth_push("",-1,"",'F',TSF_Forth_drawthe())
    return ""

def TSF_Forth_peekNthe():    #TSFdoc:指定スタックから順択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthe(),TSF_peek,"",'N'))
    return ""

def TSF_Forth_peekNthis():    #TSFdoc:実行中スタックから順択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthis(),TSF_peek,"",'N'))
    return ""

def TSF_Forth_peekNthat():    #TSFdoc:積込先スタックから順択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthat(),TSF_peek,"",'N'))
    return ""

def TSF_Forth_peekNthey():    #TSFdoc:スタック一覧から順択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek("",TSF_peek,"",'N'))
    return ""

def TSF_Forth_pokeNthe():    #TSFdoc:指定スタックからカードを順択で上書。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_poke(TSF_the,TSF_peek,"",'N',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeNthis():    #TSFdoc:実行中スタックから順択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke(TSF_Forth_drawthis(),TSF_peek,"",'N',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeNthat():    #TSFdoc:積込先スタックから順択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke(TSF_Forth_drawthat(),TSF_peek,"",'N',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeNthey():    #TSFdoc:スタック一覧から順択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke("",TSF_peek,"",'N',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pullNthe():    #TSFdoc:指定スタックから順択でカードを引抜。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthe(),TSF_peek,"",'N'))
    return ""

def TSF_Forth_pullNthis():    #TSFdoc:実行中スタックから順択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthis(),TSF_peek,"",'N'))
    return ""

def TSF_Forth_pullNthat():    #TSFdoc:積込先スタックから順択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthat(),TSF_peek,"",'N'))
    return ""

def TSF_Forth_pullNthey():    #TSFdoc:スタック一覧から順択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull("",TSF_peek,"",'N'))
    return ""

def TSF_Forth_pushNthe():    #TSFdoc:指定スタックからカードを順択で差込。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_push(TSF_the,TSF_peek,"",'N',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushNthis():    #TSFdoc:実行中スタックから順択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push(TSF_Forth_drawthis(),TSF_peek,"",'N',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushNthat():    #TSFdoc:積込先スタックから順択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push(TSF_Forth_drawthat(),TSF_peek,"",'N',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushNthey():    #TSFdoc:スタック一覧から順択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push("",TSF_peek,"",'N',TSF_Forth_drawthe())
    return ""

def TSF_Forth_peekCthe():    #TSFdoc:指定スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthe(),TSF_peek,"",'C'))
    return ""

def TSF_Forth_peekCthis():    #TSFdoc:実行中スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthis(),TSF_peek,"",'C'))
    return ""

def TSF_Forth_peekCthat():    #TSFdoc:積込先スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthat(),TSF_peek,"",'C'))
    return ""

def TSF_Forth_peekCthey():    #TSFdoc:スタック一覧から周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek("",TSF_peek,"",'C'))
    return ""

def TSF_Forth_pokeCthe():    #TSFdoc:指定スタックからカードを周択で上書。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_poke(TSF_the,TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeCthis():    #TSFdoc:実行中スタックから周択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke(TSF_Forth_drawthis(),TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeCthat():    #TSFdoc:積込先スタックから周択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke(TSF_Forth_drawthat(),TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeCthey():    #TSFdoc:スタック一覧から周択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke("",TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pullCthe():    #TSFdoc:指定スタックから周択でカードを引抜。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthe(),TSF_peek,"",'C'))
    return ""

def TSF_Forth_pullCthis():    #TSFdoc:実行中スタックから周択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthis(),TSF_peek,"",'C'))
    return ""

def TSF_Forth_pullCthat():    #TSFdoc:積込先スタックから周択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthat(),TSF_peek,"",'C'))
    return ""

def TSF_Forth_pullCthey():    #TSFdoc:スタック一覧から周択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull("",TSF_peek,"",'C'))
    return ""

def TSF_Forth_pushCthe():    #TSFdoc:指定スタックからカードを周択で差込。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_push(TSF_the,TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushCthis():    #TSFdoc:実行中スタックから周択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push(TSF_Forth_drawthis(),TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushCthat():    #TSFdoc:積込先スタックから周択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push(TSF_Forth_drawthat(),TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushCthey():    #TSFdoc:スタック一覧から周択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push("",TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Forth_peekMthe():    #TSFdoc:指定スタックから囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthe(),TSF_peek,"",'M'))
    return ""

def TSF_Forth_peekMthis():    #TSFdoc:実行中スタックから囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthis(),TSF_peek,"",'M'))
    return ""

def TSF_Forth_peekMthat():    #TSFdoc:積込先スタックから囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek(TSF_Forth_drawthat(),TSF_peek,"",'M'))
    return ""

def TSF_Forth_peekMthey():    #TSFdoc:スタック一覧から囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_peek("",TSF_peek,"",'M'))
    return ""

def TSF_Forth_pokeMthe():    #TSFdoc:指定スタックからカードを囲択で上書。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_poke(TSF_the,TSF_peek,"",'M',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeMthis():    #TSFdoc:実行中スタックから囲択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke(TSF_Forth_drawthis(),TSF_peek,"",'M',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeMthat():    #TSFdoc:積込先スタックから囲択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke(TSF_Forth_drawthat(),TSF_peek,"",'M',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pokeMthey():    #TSFdoc:スタック一覧から囲択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_poke("",TSF_peek,"",'M',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pullMthe():    #TSFdoc:指定スタックから囲択でカードを引抜。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthe(),TSF_peek,"",'M'))
    return ""

def TSF_Forth_pullMthis():    #TSFdoc:実行中スタックから囲択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthis(),TSF_peek,"",'M'))
    return ""

def TSF_Forth_pullMthat():    #TSFdoc:積込先スタックから囲択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull(TSF_Forth_drawthat(),TSF_peek,"",'M'))
    return ""

def TSF_Forth_pullMthey():    #TSFdoc:スタック一覧から囲択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_returnFNCMVA(TSF_Forth_pull("",TSF_peek,"",'M'))
    return ""

def TSF_Forth_pushMthe():    #TSFdoc:指定スタックからカードを囲択で差込。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_push(TSF_the,TSF_peek,"",'M',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushMthis():    #TSFdoc:実行中スタックから囲択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push(TSF_Forth_drawthis(),TSF_peek,"",'M',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushMthat():    #TSFdoc:積込先スタックから囲択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push(TSF_Forth_drawthat(),TSF_peek,"",'M',TSF_Forth_drawthe())
    return ""

def TSF_Forth_pushMthey():    #TSFdoc:スタック一覧から囲択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_push("",TSF_peek,"",'M',TSF_Forth_drawthe())
    return ""


def TSF_Forth_swapBA():    #TSFdoc:カードAとカードBを交換する。2枚[cardB,cardA]ドローして2枚[cardA,cardB]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);
    return ""

def TSF_Forth_swapCA():    #TSFdoc:カードAとカードCを交換する。3枚[cardC,cardB,cardA]ドローして3枚[cardA,cardB,cardC]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();  TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);
    return ""

def TSF_Forth_swapCB():    #TSFdoc:カードBとカードCを交換する。3枚[cardC,cardB,cardA]ドローして3枚[cardB,cardC,cardA]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();  TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);
    return ""

def TSF_Forth_swapAA():    #TSFdoc:カードAをカードCの位置に沈下してカードBCを浮上。3枚[cardC,cardB,cardA]ドローして3枚[cardA,cardC,cardB]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();  TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);

def TSF_Forth_swapCC():    #TSFdoc:カードCをカードAの位置に浮上してカードBCを沈下。3枚[cardC,cardB,cardA]ドローして3枚[cardB,cardA,cardC]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();  TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);

def TSF_Forth_clone(TSF_clone,TSF_the):    #TSFdoc:スタックを複製する。(TSFAPI)
    if not TSF_clone in TSF_stackD:
        TSF_stackO.append(TSF_clone)
    if TSF_the in TSF_stackD:
        TSF_stackD[TSF_clone]=[TSF_card for TSF_card in TSF_stackD[TSF_the]]
    else:
        TSF_stackD[TSF_clone]=[]

def TSF_Forth_clonethe():    #TSF_doc:指定スタックを複製する。2枚[clone,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_Forth_clone(TSF_Forth_drawthe(),TSF_the)
    return ""

def TSF_Forth_clonethis():    #TSF_doc:実行中スタックを複製する。2枚[clone]ドロー。
    TSF_Forth_clone(TSF_Forth_drawthe(),TSF_Forth_drawthis())
    return ""

def TSF_Forth_clonethat():    #TSF_doc:積込先スタックを複製する。2枚[clone]ドロー。
    TSF_Forth_clone(TSF_Forth_drawthe(),TSF_Forth_drawthat())
    return ""

def TSF_Forth_clonethey():    #TSF_doc:スタック名一覧を複製する。2枚[clone]ドロー。
    TSF_stackD[TSF_Forth_drawthe()]=[TSF_card for TSF_card in TSF_stackO]
    return ""

def TSF_Forth_readtext():    #TSFdoc:ファイル名のスタックにテキストを読み込む。1枚[path]ドロー。
    TSF_path=TSF_Forth_drawthe()
    TSF_Forth_loadtext(TSF_path,TSF_path)
    return ""

def TSF_Forth_mergethe():    #TSFdoc:テキストをTSFとして読み込む。1枚[merge]ドロー。
    TSF_Forth_merge(TSF_Forth_drawthe(),[TSF_Forth_1ststack()])
    return ""

def TSF_Forth_publishthe():    #TSFdoc:指定スタックをテキスト化。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_publish_log=TSF_Forth_view(TSF_the,False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_the])
    return ""

def TSF_Forth_publishthis():    #TSFdoc:実行中スタックをテキスト化。1枚[path]ドロー。
    TSF_publish_log=TSF_Forth_view(TSF_Forth_drawthis(),False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_Forth_drawthis()])
    return ""

def TSF_Forth_publishthat():    #TSFdoc:積込先スタックをテキスト化。1枚[path]ドロー。
    TSF_publish_log=TSF_Forth_view(TSF_Forth_drawthat(),False,"")
    TSF_Forth_setTSF(TSF_Forth_drawthe(),TSF_Io_ESCencode(TSF_publish_log),TSF_styleD[TSF_Forth_drawthat()])
    return ""

def TSF_Forth_remove():    #TSFdoc:ファイルを削除する。1枚[path]ドロー。
    TSF_Io_savetext(TSF_Forth_drawthe())
    return ""

def TSF_Forth_savetext():    #TSFdoc:テキスト化スタックをファイルに保存する。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_text=TSF_Io_ESCdecode("\n".join(TSF_stackD[TSF_the])) if TSF_the in TSF_stackD else ""
    TSF_Io_savetext(TSF_Forth_drawthe(),TSF_text)
    return ""

def TSF_Forth_writetext():    #TSFdoc:テキスト化スタックをファイルに追記する。2枚[path,the]ドロー。
    TSF_the=TSF_Forth_drawthe()
    TSF_text=TSF_Io_ESCdecode("\n".join(TSF_stackD[TSF_the])) if TSF_the in TSF_stackD else ""
    TSF_Io_writetext(TSF_Forth_drawthe(),TSF_text)
    return ""

def TSF_Forth_branch():    #TSFdoc:TSFのブランチ名を確認する。0枚[]ドローして1枚[lang]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_branchID())
    return ""

def TSF_Forth_grammar():    #TSFdoc:TSFの文法管理番号を確認する。0枚[]ドローして1枚[lang]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_grammarID())
    return ""

def TSF_Forth_foolang():    #TSFdoc:TSFの実装言語を確認する。0枚[]ドローして1枚[lang]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_foolangID())
    return ""

def TSF_Forth_mainfile():    #TSFdoc:TSFの実装ファイルを確認する。0枚[]ドローして1枚[lang]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Forth_mainfilepath())
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
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    TSF_cardD={}
    TSF_stackD={}
    TSF_styleD={}
    TSF_callptrD={}
    TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO=[],[],[],[]
    TSF_stackthis,TSF_stackthat=TSF_Forth_1ststack(),TSF_Forth_1ststack()
    TSF_cardscount=0
    TSF_Forth_setTSF(TSF_Forth_1ststack(),"#TSF_fin.",'T')
#    TSF_mainandargvs=TSF_sysargvs
    TSF_Forth_mainandargvs(TSF_sysargvs)
    TSF_Initcards=[TSF_Forth_Initcards]+TSF_addcards
    for TSF_Initcall in TSF_Initcards:
        TSF_cardD,TSF_cardO=TSF_Initcall(TSF_cardD,TSF_cardO)

TSF_importlist=[]
def TSF_Forth_importlist(TSF_import=None):    #TSFdoc:モジュール一覧を管理する(TSFAPI)。
    if TSF_import != None and not TSF_import in TSF_importlist:
        TSF_importlist.append(TSF_import)
    return TSF_importlist

def TSF_Forth_style(TSF_the,TSF_style=None):    #TSFdoc:スタックの表示スタイルを指定する(TSFAPI)。
    global TSF_styleD
    if TSF_the in TSF_stackD:
        if TSF_style != None:
            if len(TSF_style)>0:
                TSF_styleD[TSF_the]=TSF_style[0]
        TSF_style=TSF_styleD[TSF_the]
    else:
        TSF_style='T'
    return TSF_style

def TSF_Forth_setTSF(TSF_the,TSF_text=None,TSF_style=None):    #TSFdoc:TSFの外からスタックにカードを積む/無を積むと削除。(TSFAPI)
    global TSF_stackD,TSF_styleD,TSF_stackO,TSF_styleO
    if TSF_style == None: TSF_style='T'
    if TSF_text != None:
        if not TSF_the in TSF_stackD:
            TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
        if TSF_style == '@':
            TSF_stackD[TSF_the]=TSF_text.rstrip("\n").split("\n")
            TSF_styleD[TSF_the]='N'
        else:
            TSF_stackD[TSF_the]=TSF_text.rstrip("\n").replace("\t","\n").split("\n")
            TSF_styleD[TSF_the]=TSF_style
    else:
        if TSF_the in TSF_stackD:  del TSF_stackD[TSF_the]
        if TSF_the in TSF_styleD:  del TSF_styleD[TSF_the]
        if TSF_the in TSF_stackO: TSF_stackO.pop(TSF_stackO.index(TSF_the))
        if TSF_the in TSF_styleO: TSF_styleO.pop(TSF_styleO.index(TSF_the))

def TSF_Forth_loadtext(TSF_the,TSF_path):    #TSFdoc:スタックにテキストファイルを読み込む。(TSFAPI)
    TSF_text=TSF_Io_loadtext(TSF_path)
    TSF_text=TSF_Io_ESCencode(TSF_text)
    TSF_Forth_setTSF(TSF_the,TSF_text,'N')
    return TSF_text

def TSF_Forth_merge(TSF_path,TSF_ESCstack=[],TSF_mergedel=False):    #TSFdoc:スタック内のテキストをTSFとして読み込む。(TSFAPI)
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    if TSF_path in TSF_stackD:
        TSF_the=TSF_Forth_1ststack()
        for TSF_card in TSF_stackD[TSF_path]:
#            if len(TSF_card) == 0 or TSF_card.startswith("#"): continue;
            if len(TSF_card) == 0: continue;
            if len(TSF_card) >= 2 and TSF_card.startswith("#!"): continue;
            TSF_line=TSF_Io_ESCdecode(TSF_card)
            if not TSF_line.startswith('\t'):
                TSF_lineL=TSF_line.split('\t')
                if not TSF_lineL[0] in TSF_ESCstack:
                    TSF_the=TSF_lineL[0]
                    if not TSF_the in TSF_stackD:
                        TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
                    TSF_stackD[TSF_the]=[]
                    TSF_styleD[TSF_the]='O' if len(TSF_lineL) >= 2 else 'T'
            if not TSF_the in TSF_ESCstack:
                TSF_lineL=TSF_line.split('\t')[1:]
                if not TSF_the in TSF_stackD:
                    TSF_stackO.append(TSF_the);  TSF_styleO.append(TSF_the);
                TSF_stackD[TSF_the].extend(TSF_lineL)
                if TSF_styleD[TSF_the] != 'O':
                    TSF_styleD[TSF_the]='T' if len(TSF_lineL) >= 2 else 'N'
        if TSF_mergedel:
             TSF_Forth_setTSF(TSF_path)

TSF_Forth_stackMAX=256
TSF_echo,TSF_echo_log=False,""
def TSF_Forth_run(TSF_run_log=None):    #TSFdoc:TSFデッキを走らせる。
    global TSF_cardD,TSF_stackD,TSF_styleD,TSF_callptrD,TSF_cardO,TSF_stackO,TSF_styleO,TSF_callptrO
    global TSF_stackthis,TSF_stackthat,TSF_cardscount
    global TSF_echo,TSF_echo_log
    global TSF_runagainN
    if TSF_run_log != None:
        TSF_echo,TSF_echo_log=True,TSF_run_log
    else:
        TSF_echo,TSF_echo_log=False,""
    while True:
        if not "#TSF_fin." in TSF_stackD[TSF_Forth_1ststack()]:
            TSF_Forth_return(TSF_Forth_1ststack(),"#TSF_fin.")
        while True:
            while TSF_cardscount < len(TSF_stackD[TSF_stackthis]) and TSF_cardscount < TSF_Forth_stackMAX:
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
                        while( TSF_stacknext in TSF_callptrO ):
    #                        TSF_callptrD.pop(TSF_callptrO[-1]);  TSF_callptrO.pop();
                            TSF_callptrD.pop(TSF_callptrO.pop())
                        if TSF_stackthis != TSF_stacknext:
                            TSF_callptrD[TSF_stackthis]=TSF_cardscount;  TSF_callptrO.append(TSF_stackthis);
                        else:
                            TSF_cardscount=0
                            TSF_callptrD[TSF_stackthis]=TSF_cardscount
                            continue
                        TSF_stackthis=TSF_stacknext
                        TSF_cardscount=0
            if len(TSF_callptrO) > 0:
                TSF_stackthis=TSF_callptrO[-1]; TSF_cardscount=TSF_callptrD[TSF_callptrO[-1]];
    #            TSF_callptrD.pop(TSF_callptrO[-1]);  TSF_callptrO.pop();
                TSF_callptrD.pop(TSF_callptrO.pop())
            else:
                break
        if os.path.isfile(TSF_runagainN[0]) and len(TSF_Forth_loadtext(TSF_runagainN[0],TSF_runagainN[0])):
            TSF_Forth_merge(TSF_runagainN[0],[],True)
            os.chdir(os.path.dirname(os.path.abspath(TSF_runagainN[0])))
            TSF_Forth_mainfilepath(os.path.abspath(TSF_runagainN[0]))
            TSF_Forth_mainandargvs([] if len(TSF_runagainN) < 2 else TSF_runagainN[1:]);  TSF_runagainN=[""];
            TSF_Forth_run(TSF_echo_log)
        else:
            break
    return TSF_echo_log

def TSF_Forth_view(TSF_the,TSF_view_io=True,TSF_view_log=""):    #TSFdoc:スタックの内容をテキスト表示(TSFAPI)。
    if TSF_view_log == None: TSF_view_log="";
    if TSF_the in TSF_stackD:
        TSF_style=TSF_styleD.get(TSF_the,'T')
        if TSF_style == 'O':
            TSF_view_logline="{0}\t{1}\n".format(TSF_the,"\t".join(TSF_stackD[TSF_the]))
        elif TSF_style == 'T':
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_the,"\t".join(TSF_stackD[TSF_the]))
        else:  # TSF_style == 'N':
            TSF_view_logline="{0}\n\t{1}\n".format(TSF_the,"\n\t".join(TSF_stackD[TSF_the]))
        TSF_view_log=TSF_Io_printlog(TSF_view_logline,TSF_log=TSF_view_log) if TSF_view_io == True else TSF_view_log+TSF_view_logline
    return TSF_view_log

def TSF_Forth_draw(TSF_the):    #TSFdoc:スタックから1枚ドロー。(TSFAPI)
    global TSF_stackD,TSF_stackO
    TSF_draw=""
    if TSF_the in TSF_stackD and len(TSF_stackD[TSF_the]):
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

def TSF_Forth_mainandargvs(TSF_argvs=None):    #TSFdoc:argvsの取得。(TSFAPI)
    global TSF_mainandargvs
    if TSF_argvs != None:
        TSF_mainandargvs=TSF_argvs
    return TSF_mainandargvs

TSF_mainfilepath=""
def TSF_Forth_mainfilepath(TSF_mainfile=None):    #TSF_doc:実行ファイル名を設定・取得(TSFAPI)。
    global TSF_mainfilepath
    if TSF_mainfile != None:
        TSF_mainfilepath=TSF_mainfile
    return TSF_mainfilepath

def TSF_Forth_stackD():    #TSFdoc:TSF_stackDの取得。(TSFAPI)
    global TSF_stackD
    return TSF_stackD

def TSF_Forth_stackO(TSF_Shuffle_stackO=None):    #TSFdoc:TSF_stackOの取得。(TSFAPI)
    global TSF_stackO
    if TSF_Shuffle_stackO != None:
        TSF_stackO=TSF_Shuffle_stackO
    return TSF_stackO


def TSF_Forth_samplerun(TSF_sample_sepalete=None,TSF_sample_viewthey=None,TSF_sample_log=None):    #TSFdoc:TSF実行。ソース表示やログ保存機能付き。
    TSF_sample_logsw=True if TSF_sample_log != None else False
    TSF_sample_log=TSF_sample_log if TSF_sample_log != None else ""
    if TSF_sample_sepalete != None:
        TSF_sample_log=TSF_Io_printlog("-- {0} source --".format(TSF_sample_sepalete),TSF_sample_log)
        for TSF_the in TSF_stackO:
            TSF_sample_log=TSF_Forth_view(TSF_the,True,TSF_sample_log)
        TSF_sample_log=TSF_Io_printlog("-- {0} run --".format(TSF_sample_sepalete),TSF_sample_log)
    if TSF_sample_logsw:
        TSF_sample_log=TSF_Forth_run(TSF_sample_log)
    else:
        TSF_Forth_run()
    if TSF_sample_viewthey == True:
        TSF_sample_log=TSF_Io_printlog("-- {0} viewthey --".format(TSF_sample_sepalete),TSF_sample_log)
        for TSF_the in TSF_stackO:
            TSF_sample_log=TSF_Forth_view(TSF_the,True,TSF_sample_log)
    return TSF_sample_log


TSF_Initcalldebug=[TSF_Forth_Initcards]
def TSF_Forth_debug(TSF_sysargvs):    #TSFdoc:「TSF_Forth」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Forth.log";
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug)

    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:","\t".join([
        "shuffleclone:","#TSF_this","#TSF_fin."]),'T')
    TSF_Forth_setTSF("shuffleclone:","\t".join([
        "adverbclone:","adverb:","#TSF_clonethe","shufflestacks:","#TSF_pullFthe","#TSF_this","adverbclone:","#TSF_argvsthe","#TSF_reverseN","adverbclone:","#TSF_lenthe"," ","#TSF_sandwichN","「#[2]」「[1]」「[0]」","#TSF_join[]","#TSF_echo","shufflejump:","shufflestacks:","#TSF_lenthe","0,1,[0]U","#TSF_join[]","#TSF_RPN","#TSF_peekNthe","#TSF_this"]),'T')
    TSF_Forth_setTSF("shufflejump:","\t".join([
        "#!exit:","shuffleclone:"]),'T')
    TSF_Forth_setTSF("verb:","\t".join(["peek","poke","push","pull"]),'O')
    TSF_Forth_setTSF("adverb:","\t".join(["F","N","C","M","V","A","Q","I","R","H","L"]),'O')
    TSF_Forth_setTSF("pronoun:","\t".join(["this","that","the","they"]),'O')
    TSF_Forth_setTSF("shufflestacks:","\t".join([
        "pushM:","pullM:","pokeM:","peekM:","pushC:","pullC:","pokeC:","peekC:","pushN:","pullN:","pokeN:","peekN:","pushF:","pullF:","pokeF:","peekF:"]),'T')
    TSF_Forth_setTSF("peekF:","\t".join(["TSF_peekFthe","adverbclone:","#TSF_peekFthe"]),'O')
    TSF_Forth_setTSF("pokeF:","\t".join(["TSF_pokeFthe","$poke","adverbclone:","#TSF_pokeFthe","$poke"]),'O')
    TSF_Forth_setTSF("pullF:","\t".join(["TSF_pullFthe","adverbclone:","#TSF_pullFthe"]),'O')
    TSF_Forth_setTSF("pushF:","\t".join(["TSF_pushFthe","$push","adverbclone:","#TSF_pushFthe","$push"]),'O')
    TSF_Forth_setTSF("peekN:","\t".join(["TSF_peekNthe","adverbclone:","1","#TSF_peekNthe"]),'O')
    TSF_Forth_setTSF("pokeN:","\t".join(["TSF_pokeNthe","$poke","adverbclone:","1","#TSF_pokeNthe","$poke"]),'O')
    TSF_Forth_setTSF("pullN:","\t".join(["TSF_pullNthe","adverbclone:","1","#TSF_pullNthe"]),'O')
    TSF_Forth_setTSF("pushN:","\t".join(["TSF_pushNthe","$push","adverbclone:","1","#TSF_pushNthe","$push"]),'O')
    TSF_Forth_setTSF("peekC:","\t".join(["TSF_peekCthe","adverbclone:","2","#TSF_peekCthe"]),'O')
    TSF_Forth_setTSF("pokeC:","\t".join(["TSF_pokeCthe","$poke","adverbclone:","2","#TSF_pokeCthe","$poke"]),'O')
    TSF_Forth_setTSF("pullC:","\t".join(["TSF_pullCthe","adverbclone:","2","#TSF_pullCthe"]),'O')
    TSF_Forth_setTSF("pushC:","\t".join(["TSF_pushCthe","$push","adverbclone:","2","#TSF_pushCthe","$push"]),'O')
    TSF_Forth_setTSF("peekM:","\t".join(["TSF_peekMthe","adverbclone:","3","#TSF_peekMthe"]),'O')
    TSF_Forth_setTSF("pokeM:","\t".join(["TSF_pokeMthe","$poke","adverbclone:","3","#TSF_pokeMthe","$poke"]),'O')
    TSF_Forth_setTSF("pullM:","\t".join(["TSF_pullMthe","adverbclone:","3","#TSF_pullMthe"]),'O')
    TSF_Forth_setTSF("pushM:","\t".join(["TSF_pushMthe","$push","adverbclone:","3","#TSF_pushMthe","$push"]),'O')

#    TSF_debug_log=TSF_Forth_samplerun(__file__,True,TSF_debug_log)
    TSF_debug_log=TSF_Forth_samplerun(__file__,False,TSF_debug_log)
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log)

if __name__=="__main__":
    TSF_Forth_debug(TSF_Io_argvs(["python","TSF_Forth.py"]))


#! -- Copyright (c) 2017 ooblog --
#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
