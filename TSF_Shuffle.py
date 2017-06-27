#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import division,print_function,absolute_import,unicode_literals

from TSF_Io import *
from TSF_Forth import *


def TSF_Shuffle_Initcards(TSF_cardsD,TSF_cardsO):    #TSFdoc:関数カードにDやPythonに翻訳する命令を追加する。(TSFAPI)
    TSF_Forth_importlist(TSF_import="TSF_Shuffle")
    TSF_Forth_cards={
        "#TSF_swapBA":TSF_Shuffle_swapBA, "#カードBA交換":TSF_Shuffle_swapBA,
        "#TSF_swapCA":TSF_Shuffle_swapCA, "#カードCA交換":TSF_Shuffle_swapCA,
        "#TSF_swapCB":TSF_Shuffle_swapCB, "#カードCB交換":TSF_Shuffle_swapCB,
        "#TSF_swapAA":TSF_Shuffle_swapAA, "#カードAA交換":TSF_Shuffle_swapAA,
        "#TSF_swapCC":TSF_Shuffle_swapCC, "#カードCC交換":TSF_Shuffle_swapCC,
        "#TSF_peekCthe":TSF_Shuffle_peekCthe, "#指定スタック周択読込":TSF_Shuffle_peekCthe,
        "#TSF_peekCthis":TSF_Shuffle_peekCthis, "#実行中スタック周択読込":TSF_Shuffle_peekCthis,
        "#TSF_peekCthat":TSF_Shuffle_peekCthat, "#積込先スタック周択読込":TSF_Shuffle_peekCthat,
        "#TSF_peekCthey":TSF_Shuffle_peekCthey, "#スタック一覧周択読込":TSF_Shuffle_peekCthey,
        "#TSF_pokeCthe":TSF_Shuffle_pokeCthe, "#指定スタック周択上書":TSF_Shuffle_pokeCthe,
        "#TSF_pokeCthis":TSF_Shuffle_pokeCthis, "#実行中スタック周択上書":TSF_Shuffle_pokeCthis,
        "#TSF_pokeCthat":TSF_Shuffle_pokeCthat, "#積込先スタック周択上書":TSF_Shuffle_pokeCthat,
        "#TSF_pokeCthey":TSF_Shuffle_pokeCthey, "#スタック一覧周択上書":TSF_Shuffle_pokeCthey,
        "#TSF_pullCthe":TSF_Shuffle_pullCthe, "#指定スタック周択引抜":TSF_Shuffle_pullCthe,
        "#TSF_pullCthis":TSF_Shuffle_pullCthis, "#実行中スタック周択引抜":TSF_Shuffle_pullCthis,
        "#TSF_pullCthat":TSF_Shuffle_pullCthat, "#積込先スタック周択引抜":TSF_Shuffle_pullCthat,
        "#TSF_pullCthey":TSF_Shuffle_pullCthey, "#スタック一覧周択引抜":TSF_Shuffle_pullCthey,
        "#TSF_pushCthe":TSF_Shuffle_pushCthe, "#指定スタック周択差込":TSF_Shuffle_pushCthe,
        "#TSF_pushCthis":TSF_Shuffle_pushCthis, "#実行中スタック周択差込":TSF_Shuffle_pushCthis,
        "#TSF_pushCthat":TSF_Shuffle_pushCthat, "#積込先スタック周択差込":TSF_Shuffle_pushCthat,
        "#TSF_pushCthey":TSF_Shuffle_pushCthey, "#スタック一覧周択差込":TSF_Shuffle_pushCthey,
        "#TSF_peekMthe":TSF_Shuffle_peekMthe, "#指定スタック囲択読込":TSF_Shuffle_peekMthe,
        "#TSF_peekMthis":TSF_Shuffle_peekMthis, "#実行中スタック囲択読込":TSF_Shuffle_peekMthis,
        "#TSF_peekMthat":TSF_Shuffle_peekMthat, "#積込先スタック囲択読込":TSF_Shuffle_peekMthat,
        "#TSF_peekMthey":TSF_Shuffle_peekMthey, "#スタック一覧囲択読込":TSF_Shuffle_peekMthey,
        "#TSF_pokeMthe":TSF_Shuffle_pokeMthe, "#指定スタック囲択上書":TSF_Shuffle_pokeMthe,
        "#TSF_pokeMthis":TSF_Shuffle_pokeMthis, "#実行中スタック囲択上書":TSF_Shuffle_pokeMthis,
        "#TSF_pokeMthat":TSF_Shuffle_pokeMthat, "#積込先スタック囲択上書":TSF_Shuffle_pokeMthat,
        "#TSF_pokeMthey":TSF_Shuffle_pokeMthey, "#スタック一覧囲択上書":TSF_Shuffle_pokeMthey,
        "#TSF_pullMthe":TSF_Shuffle_pullMthe, "#指定スタック囲択引抜":TSF_Shuffle_pullMthe,
        "#TSF_pullMthis":TSF_Shuffle_pullMthis, "#実行中スタック囲択引抜":TSF_Shuffle_pullMthis,
        "#TSF_pullMthat":TSF_Shuffle_pullMthat, "#積込先スタック囲択引抜":TSF_Shuffle_pullMthat,
        "#TSF_pullMthey":TSF_Shuffle_pullMthey, "#スタック一覧囲択引抜":TSF_Shuffle_pullMthey,
        "#TSF_pushMthe":TSF_Shuffle_pushMthe, "#指定スタック囲択差込":TSF_Shuffle_pushMthe,
        "#TSF_pushMthis":TSF_Shuffle_pushMthis, "#実行中スタック囲択差込":TSF_Shuffle_pushMthis,
        "#TSF_pushMthat":TSF_Shuffle_pushMthat, "#積込先スタック囲択差込":TSF_Shuffle_pushMthat,
        "#TSF_pushMthey":TSF_Shuffle_pushMthey, "#スタック一覧囲択差込":TSF_Shuffle_pushMthey,
#        "#TSF_peekVthe":TSF_Shuffle_peekVthe, "#指定スタック逆択読込":TSF_Shuffle_peekVthe,
#        "#TSF_peekVthis":TSF_Shuffle_peekVthis, "#実行中スタック逆択読込":TSF_Shuffle_peekVthis,
#        "#TSF_peekVthat":TSF_Shuffle_peekVthat, "#積込先スタック逆択読込":TSF_Shuffle_peekVthat,
#        "#TSF_peekVthey":TSF_Shuffle_peekVthey, "#スタック一覧逆択読込":TSF_Shuffle_peekVthey,
#        "#TSF_pokeVthe":TSF_Shuffle_pokeVthe, "#指定スタック逆択上書":TSF_Shuffle_pokeVthe,
#        "#TSF_pokeVthis":TSF_Shuffle_pokeVthis, "#実行中スタック逆択上書":TSF_Shuffle_pokeVthis,
#        "#TSF_pokeVthat":TSF_Shuffle_pokeVthat, "#積込先スタック逆択上書":TSF_Shuffle_pokeVthat,
#        "#TSF_pokeVthey":TSF_Shuffle_pokeVthey, "#スタック一覧逆択上書":TSF_Shuffle_pokeVthey,
#        "#TSF_pullVthe":TSF_Shuffle_pullVthe, "#指定スタック逆択引抜":TSF_Shuffle_pullVthe,
#        "#TSF_pullVthis":TSF_Shuffle_pullVthis, "#実行中スタック逆択引抜":TSF_Shuffle_pullVthis,
#        "#TSF_pullVthat":TSF_Shuffle_pullVthat, "#積込先スタック逆択引抜":TSF_Shuffle_pullVthat,
#        "#TSF_pullVthey":TSF_Shuffle_pullVthey, "#スタック一覧逆択引抜":TSF_Shuffle_pullVthey,
#        "#TSF_pushVthe":TSF_Shuffle_pushVthe, "#指定スタック逆択差込":TSF_Shuffle_pushVthe,
#        "#TSF_pushVthis":TSF_Shuffle_pushVthis, "#実行中スタック逆択差込":TSF_Shuffle_pushVthis,
#        "#TSF_pushVthat":TSF_Shuffle_pushVthat, "#積込先スタック逆択差込":TSF_Shuffle_pushVthat,
#        "#TSF_pushVthey":TSF_Shuffle_pushVthey, "#スタック一覧逆択差込":TSF_Shuffle_pushVthey,
#        "#TSF_peekAthe":TSF_Shuffle_peekAthe, "#指定スタック乱択読込":TSF_Shuffle_peekAthe,
#        "#TSF_peekAthis":TSF_Shuffle_peekAthis, "#実行中スタック乱択読込":TSF_Shuffle_peekAthis,
#        "#TSF_peekAthat":TSF_Shuffle_peekAthat, "#積込先スタック乱択読込":TSF_Shuffle_peekAthat,
#        "#TSF_peekAthey":TSF_Shuffle_peekAthey, "#スタック一覧乱択読込":TSF_Shuffle_peekAthey,
#        "#TSF_pokeAthe":TSF_Shuffle_pokeAthe, "#指定スタック乱択上書":TSF_Shuffle_pokeAthe,
#        "#TSF_pokeAthis":TSF_Shuffle_pokeAthis, "#実行中スタック乱択上書":TSF_Shuffle_pokeAthis,
#        "#TSF_pokeAthat":TSF_Shuffle_pokeAthat, "#積込先スタック乱択上書":TSF_Shuffle_pokeAthat,
#        "#TSF_pokeAthey":TSF_Shuffle_pokeAthey, "#スタック一覧乱択上書":TSF_Shuffle_pokeAthey,
#        "#TSF_pullAthe":TSF_Shuffle_pullAthe, "#指定スタック乱択引抜":TSF_Shuffle_pullAthe,
#        "#TSF_pullAthis":TSF_Shuffle_pullAthis, "#実行中スタック乱択引抜":TSF_Shuffle_pullAthis,
#        "#TSF_pullAthat":TSF_Shuffle_pullAthat, "#積込先スタック乱択引抜":TSF_Shuffle_pullAthat,
#        "#TSF_pullAthey":TSF_Shuffle_pullAthey, "#スタック一覧乱択引抜":TSF_Shuffle_pullAthey,
#        "#TSF_pushAthe":TSF_Shuffle_pushAthe, "#指定スタック乱択差込":TSF_Shuffle_pushAthe,
#        "#TSF_pushAthis":TSF_Shuffle_pushAthis, "#実行中スタック乱択差込":TSF_Shuffle_pushAthis,
#        "#TSF_pushAthat":TSF_Shuffle_pushAthat, "#積込先スタック乱択差込":TSF_Shuffle_pushAthat,
#        "#TSF_pushAthey":TSF_Shuffle_pushAthey, "#スタック一覧乱択差込":TSF_Shuffle_pushAthey,
#「Q」(eQual)スタックから同択、「I」(In)スタックから含択、「R」(reseaRch)スタックから規択、「H」(matcHer)スタックから似択、「L」(Label)スタックから札択、
    }
    for cardkey,cardfunc in TSF_Forth_cards.items():
        if not cardkey in TSF_cardsD:
            TSF_cardsD[cardkey]=cardfunc;  TSF_cardsO.append(cardkey);
    return TSF_cardsD,TSF_cardsO

def TSF_Shuffle_swapBA():    #TSFdoc:カードAとカードBを交換する。2枚[cardB,cardA]ドローして2枚[cardA,cardB]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);
    return ""

def TSF_Shuffle_swapCA():    #TSFdoc:カードAとカードCを交換する。3枚[cardC,cardB,cardA]ドローして3枚[cardA,cardB,cardC]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();  TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);
    return ""

def TSF_Shuffle_swapCB():    #TSFdoc:カードBとカードCを交換する。3枚[cardC,cardB,cardA]ドローして3枚[cardB,cardC,cardA]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();  TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);
    return ""

def TSF_Shuffle_swapAA():    #TSFdoc:カードAをカードCの位置に沈下してカードBCを浮上。3枚[cardC,cardB,cardA]ドローして3枚[cardA,cardC,cardB]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();  TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);

def TSF_Shuffle_swapCC():    #TSFdoc:カードCをカードAの位置に浮上してカードBCを沈下。3枚[cardC,cardB,cardA]ドローして3枚[cardB,cardA,cardC]リターン。
    TSF_swapA=TSF_Forth_drawthe();  TSF_swapB=TSF_Forth_drawthe();  TSF_swapC=TSF_Forth_drawthe();
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapB);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapA);  TSF_Forth_return(TSF_Forth_drawthat(),TSF_swapC);


def TSF_Shuffle_cardsFNCMVA(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL):    #TSFdoc:peek,poke,pull,pushの共通部品。カードの位置を取得。(TSFAPI)
    TSF_Plist=[]
    TSF_peek=TSF_peek if TSF_peek != None else 0
    TSF_seek=TSF_seek if TSF_seek != None else ""
    if TSF_the != "":
        if TSF_the in TSF_Forth_stackD():
            TSF_cardsL=len(TSF_Forth_stackD()[TSF_the])
            if 0 < TSF_cardsL:
                if TSF_FNCMVAQIRHL == 'F':
                    TSF_Plist+=[TSF_cardsL-1]
                elif TSF_FNCMVAQIRHL == 'N':
                    if 0 <= TSF_peek < TSF_cardsL: TSF_Plist+=[TSF_peek];
                elif TSF_FNCMVAQIRHL == 'C':
                    TSF_Plist+=[TSF_peek%TSF_cardsL if TSF_peek >=0 else TSF_cardsL-(abs(TSF_peek)%TSF_cardsL)]
                elif TSF_FNCMVAQIRHL == 'M':
                    TSF_Plist+=[min(max(TSF_peek,0),TSF_cardsL-1)]
                elif TSF_FNCMVAQIRHL == 'V':
                    if 0 <= TSF_peek < TSF_cardsL: TSF_Plist+=[TSF_cardsL-1-TSF_peek];
                elif TSF_FNCMVAQIRHL == 'A':
                    TSF_Plist+=[random.randint(0,TSF_cardsL-1)]
                elif TSF_FNCMVAQIRHL == 'Q':
                    for TSF_peek,TSF_card in enumerate(TSF_Forth_stackD()[TSF_the]):
                        if TSF_seek==TSF_card: TSF_Plist+=[TSF_peek]
                elif TSF_FNCMVAQIRHL == 'I':
                    for TSF_peek,TSF_card in enumerate(TSF_Forth_stackD()[TSF_the]):
                        if TSF_seek in TSF_card: TSF_Plist+=[TSF_peek]
                elif TSF_FNCMVAQIRHL == 'R':
                    for TSF_peekreg,TSF_card in enumerate(TSF_Forth_stackD()[TSF_the]):
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
        TSF_cardsL=len(TSF_Forth_stackO())
        if 0 < TSF_cardsL:
            if TSF_FNCMVAQIRHL == 'F':
                TSF_plist[0]=TSF_cardsL-1
            elif TSF_FNCMVAQIRHL == 'N':
                if 0 <= TSF_peek < TSF_cardsL: TSF_Plist[0]=TSF_peek;
            elif TSF_FNCMVAQIRHL == 'C':
                TSF_Plist[0]=TSF_peek%TSF_cardsL if TSF_peek >=0 else TSF_cardsL-(abs(TSF_peek)%TSF_cardsL)
            elif TSF_FNCMVAQIRHL == 'M':
                TSF_Plist[0]=min(max(TSF_peek,0),TSF_cardsL-1)
            elif TSF_FNCMVAQIRHL == 'V':
                if 0 <= TSF_peek < TSF_cardsL: TSF_Plist[0]=TSF_cardsL-1-TSF_peek;
            elif TSF_FNCMVAQIRHL == 'A':
                TSF_Plist[0]=random.randint(0,TSF_cardsL-1)
            elif TSF_FNCMVAQIRHL == 'Q':
                for TSF_peek,TSF_card in enumerate(TSF_Forth_stackO()):
                    if TSF_seek==TSF_card: TSF_Plist+=[TSF_peek]
            elif TSF_FNCMVAQIRHL == 'I':
                for TSF_peek,TSF_card in enumerate(TSF_Forth_stackO()):
                    if TSF_seek in TSF_card: TSF_Plist+=[TSF_peek]
            elif TSF_FNCMVAQIRHL == 'R':
                TSF_regsearch=None
                for TSF_peekreg,TSF_card in enumerate(TSF_Forth_stackO()):
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

def TSF_Shuffle_peek(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL):    #TSFdoc:peekの共通部品。(TSFAPI)
    TSF_the=TSF_the if TSF_the != None else ""
    TSF_Plist=TSF_Shuffle_cardsFNCMVA(TSF_the,TSF_peek,"",TSF_FNCMVAQIRHL)
    TSF_pulllist=[]
    if TSF_the != "":
        for TSF_P in TSF_Plist:
            TSF_pulllist+=[TSF_Forth_stackD()[TSF_the][TSF_P]]
    else:
        for TSF_P in TSF_Plist:
            TSF_pulllist+=[TSF_Forth_stackO()[TSF_P]]
    return TSF_pulllist

def TSF_Shuffle_poke(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL,TSF_poke):    #TSFdoc:pokeの共通部品。(TSFAPI)
    TSF_the=TSF_the if TSF_the != None else ""
    TSF_Plist=TSF_Shuffle_cardsFNCMVA(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL)
    TSF_pulllist=[]
    if TSF_the != "":
        for TSF_P in TSF_Plist:
            TSF_Forth_stackD()[TSF_the][TSF_P]=TSF_poke
    else:
        for TSF_P in TSF_Plist:
            TSF_Forth_stackO()[TSF_P]=TSF_poke

def TSF_Shuffle_pull(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL):    #TSFdoc:pullの共通部品。(TSFAPI)
    TSF_the=TSF_the if TSF_the != None else ""
    TSF_Plist=TSF_Shuffle_cardsFNCMVA(TSF_the,TSF_peek,"",TSF_FNCMVAQIRHL)
    TSF_pulllist=[]
    if TSF_the != "":
        for TSF_P in TSF_Plist:
            TSF_pulllist+=[TSF_Forth_stackD()[TSF_the][TSF_P]]
            TSF_Forth_stackD()[TSF_the].pop(TSF_P)
    else:
        for TSF_P in TSF_Plist:
            TSF_pulllist+=[TSF_Forth_stackO()[TSF_P]]
            TSF_pull=TSF_stackO[TSF_peek]
            TSF_Forth_stackO().pop(TSF_P)
            TSF_Forth_stackD().pop(TSF_pull)
    return TSF_pulllist

def TSF_Shuffle_push(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL,TSF_poke):    #TSFdoc:pushの共通部品。(TSFAPI)
    TSF_the=TSF_the if TSF_the != None else ""
    TSF_Plist=TSF_Shuffle_cardsFNCMVA(TSF_the,TSF_peek,TSF_seek,TSF_FNCMVAQIRHL)
    TSF_pulllist=[]
    if TSF_the != "":
        for TSF_P in TSF_Plist:
            TSF_Forth_stackD()[TSF_the].insert(TSF_P,TSF_poke)
    else:
        for TSF_P in TSF_Plist:
            TSF_Forth_stackO().insert(TSF_P,TSF_poke)
            TSF_Forth_stackD()[TSF_the]=[]

def TSF_Shuffle_returnFNCMVA(TSF_pulllist):    #TSFdoc:peek,pullの共通部品。FNCMVAは単独のカードを返す。(TSFAPI)
    if len(TSF_pulllist) > 0:
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_pulllist[0])
    else:
        TSF_Forth_return(TSF_Forth_drawthat(),"")

def TSF_Shuffle_returnQIRH(TSF_pulllist):    #TSFdoc:peek,pullの共通部品。QIRHは複数のカードを返す。(TSFAPI)
    for TSF_card in TSF_pulllist:
        TSF_Forth_return(TSF_Forth_drawthat(),TSF_card)
    TSF_Forth_return(TSF_Forth_drawthat(),str(len(TSF_pulllist)))

def TSF_Shuffle_peekCthe():    #TSFdoc:指定スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_peek(TSF_Forth_drawthe(),TSF_peek,"",'C'))
    return ""

def TSF_Shuffle_peekCthis():    #TSFdoc:実行中スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_peek(TSF_Forth_drawthis(),TSF_peek,"",'C'))
    return ""

def TSF_Shuffle_peekCthat():    #TSFdoc:積込先スタックから周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_peek(TSF_Forth_drawthat(),TSF_peek,"",'C'))
    return ""

def TSF_Shuffle_peekCthey():    #TSFdoc:スタック一覧から周択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_peek("",TSF_peek,"",'C'))
    return ""

def TSF_Shuffle_pokeCthe():    #TSFdoc:指定スタックからカードを周択で上書。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Shuffle_poke(TSF_the,TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeCthis():    #TSFdoc:実行中スタックから周択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_poke(TSF_Forth_drawthis(),TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeCthat():    #TSFdoc:積込先スタックから周択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_poke(TSF_Forth_drawthat(),TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeCthey():    #TSFdoc:スタック一覧から周択でカードを上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_poke("",TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pullCthe():    #TSFdoc:指定スタックから周択でカードを引抜。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_pull(TSF_Forth_drawthe(),TSF_peek,"",'C'))
    return ""

def TSF_Shuffle_pullCthis():    #TSFdoc:実行中スタックから周択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_pull(TSF_Forth_drawthis(),TSF_peek,"",'C'))
    return ""

def TSF_Shuffle_pullCthat():    #TSFdoc:積込先スタックから周択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_pull(TSF_Forth_drawthat(),TSF_peek,"",'C'))
    return ""

def TSF_Shuffle_pullCthey():    #TSFdoc:スタック一覧から周択でカードを引抜。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_returnFNCMVA(TSF_Shuffle_pull("",TSF_peek,"",'C'))
    return ""

def TSF_Shuffle_pushCthe():    #TSFdoc:指定スタックからカードを周択で差込。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Shuffle_push(TSF_the,TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pushCthis():    #TSFdoc:実行中スタックから周択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_push(TSF_Forth_drawthis(),TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pushCthat():    #TSFdoc:積込先スタックから周択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_push(TSF_Forth_drawthat(),TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pushCthey():    #TSFdoc:スタック一覧から周択でカードを差込。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_push("",TSF_peek,"",'C',TSF_Forth_drawthe())
    return ""



def TSF_Shuffle_peekM(TSF_the,TSF_peek):    #TSFdoc:指定スタックからスタック名を囲択で読込。(TSFAPI)
    TSF_pull=""
    if TSF_the in TSF_Forth_stackD():
        TSF_cardsN_len=len(TSF_Forth_stackD()[TSF_the])
        if 0 < TSF_cardsN_len:
            TSF_pull=TSF_Forth_stackD()[TSF_the][max(min(TSF_peek,TSF_cardsN_len-1),0)]
    return TSF_pull

def TSF_Shuffle_peekMthe():    #TSFdoc:指定スタックから囲択でカードを読込。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthe(),TSF_peek))
    return ""

def TSF_Shuffle_peekMthis():    #TSFdoc:実行中スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthis(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return ""

def TSF_Shuffle_peekMthat():    #TSFdoc:積込先スタックから囲択でカードを読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_peekM(TSF_Forth_drawthat(),TSF_Io_RPNzero(TSF_Forth_drawthe())));
    return ""

def TSF_Shuffle_peekMthey():    #TSFdoc:スタック一覧から最後尾スタック名を囲択で読込。1枚[peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_pull="";  TSF_cardsN_len=len(TSF_Forth_stackO())
    if TSF_the in TSF_Forth_stackO() and 0 < TSF_cardsN_len:
        TSF_pull=TSF_Forth_stackO()[max(min(TSF_peek,TSF_cardsN_len-1),0)]
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_pull)
    return ""

def TSF_Shuffle_pokeM(TSF_the,TSF_peek,TSF_poke):    #TSFdoc:指定スタックからカードを囲択で読込。(TSFAPI)
    if TSF_the in TSF_Forth_stackD():
        TSF_cardsN_len=len(TSF_Forth_stackD()[TSF_the])
        if 0 < TSF_cardsN_len:
            TSF_Forth_stackD()[TSF_the][max(min(TSF_peek,TSF_cardsN_len-1),0)]=TSF_poke

def TSF_Shuffle_pokeMthe():    #TSFdoc:指定スタックからカードを囲択で上書。3枚[poke,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Shuffle_pokeM(TSF_the,TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeMthis():    #TSFdoc:実行中スタックからカードを囲択で上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_pokeM(TSF_Forth_drawthis(),TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeMthat():    #TSFdoc:積込先スタックからカードを囲択で上書。2枚[poke,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_pokeM(TSF_Forth_drawthat(),TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pokeMthey():    #TSFdoc:スタック一覧からスタック名を囲択で上書。2枚[poke,peek]ドロー。
    TSF_cardsN_len=len(TSF_Forth_stackO())
    TSF_peek=max(min(TSF_Io_RPNzero(TSF_Forth_drawthe()),TSF_cardsN_len-1),0)
    TSF_poke=TSF_Forth_drawthe()
    if 0 < TSF_cardsN_len:
        TSF_pull=TSF_Forth_stackO()[TSF_peek]
        if TSF_pull!=TSF_poke:
            TSF_Forth_stackO()[TSF_peek]=TSF_poke
            TSF_stackR=TSF_Forth_stackD().pop(TSF_pull)
            TSF_Forth_stackD()[TSF_poke]=TSF_stackR
    return ""

def TSF_Shuffle_pullM(TSF_the,TSF_peek):    #TSFdoc:指定スタックからカードを囲択で引抜。(TSFAPI)
    TSF_pull="";  
    if TSF_the in TSF_Forth_stackD():
        TSF_cardsN_len=len(TSF_Forth_stackD()[TSF_the])
        if 0 < TSF_cardsN_len:
#            TSF_pull=TSF_Forth_stackD()[TSF_the].pop(max(min(TSF_peek,TSF_cardsN_len-1),0))
            TSF_pull=TSF_Forth_stackD()[TSF_the].pop(min(max(TSF_peek,0),TSF_cardsN_len-1))
    return TSF_pull

def TSF_Shuffle_pullMthe():    #TSFdoc:指定スタックからカードを囲択で引抜。2枚[the,peek]ドローして1枚[card]リターン。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_pullM(TSF_Forth_drawthe(),TSF_peek))
    return ""

def TSF_Shuffle_pullMthis():    #TSFdoc:実行中スタックからカードを囲択で引抜。1枚[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_pullM(TSF_Forth_drawthis(),TSF_Io_RPNzero(TSF_Forth_drawthe())))
    return ""

def TSF_Shuffle_pullMthat():    #TSFdoc:積込先スタックからカードを囲択で引抜。2枚[pull]←[peek]ドローして1枚[card]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Shuffle_pullM(TSF_Forth_drawthat(),TSF_Io_RPNzero(TSF_Forth_drawthe())))
    return ""

def TSF_Shuffle_pullMthey():    #TSFdoc:スタック一覧からスタック名を囲択で引抜。1枚[peek]ドローして1枚[card]リターン。
    TSF_pull="";  TSF_cardsN_len=len(TSF_Forth_stackO())
    TSF_peek=max(min(TSF_Io_RPNzero(TSF_Forth_drawthe()),TSF_cardsN_len-1),0)
    if 0 < TSF_cardsN_len:
        TSF_pull=TSF_Forth_stackO()[TSF_peek]
        TSF_Forth_stackO(TSF_Io_separatepullN(TSF_Forth_stackO(),TSF_peek))
        TSF_Forth_stackD()[TSF_the].pop(TSF_pull)
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_pull)
    return ""

def TSF_Shuffle_pushM(TSF_the,TSF_peek,TSF_push):    #TSFdoc:指定スタックにカードを囲択で差込。(TSFAPI)
    if TSF_the in TSF_Forth_stackD():
        TSF_cardsN_len=len(TSF_Forth_stackD()[TSF_the])
        TSF_Forth_stackD()[TSF_the]=TSF_Io_separatepushN(TSF_Forth_stackD()[TSF_the],max(min(TSF_peek,TSF_cardsN_len-1),0),TSF_push)

def TSF_Shuffle_pushMthe():    #TSFdoc:指定スタックにカードを囲択で差込。3枚[push,the,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_the=TSF_Forth_drawthe()
    TSF_Shuffle_pushM(TSF_the,TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pushMthis():    #TSFdoc:実行中スタックにカードを囲択で差込。2枚[push,peek]ドロー。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_pushM(TSF_Forth_drawthis(),TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pushMthat():    #TSFdoc:積込先スタックにカードを囲択で差込。2枚[push,peek]ドロー。1枚リターンの可能性。
    TSF_peek=TSF_Io_RPNzero(TSF_Forth_drawthe())
    TSF_Shuffle_pushM(TSF_Forth_drawthat(),TSF_peek,TSF_Forth_drawthe())
    return ""

def TSF_Shuffle_pushMthey():    #TSFdoc:スタック一覧にスタック名として囲択で差込。2枚[push,peek]ドロー。
    TSF_cardsN_len=len(TSF_Forth_stackO())
    TSF_peek=max(min(TSF_Io_RPNzero(TSF_Forth_drawthe()),TSF_cardsN_len-1),0)
    if not TSF_push in TSF_Forth_stackD():
        TSF_Forth_stackO(TSF_Io_separatepushN(TSF_Forth_stackO(),TSF_peek,TSF_push))
        TSF_Forth_stackD()[TSF_push]=[]
    return ""


TSF_Initcalldebug=[TSF_Shuffle_Initcards]
def TSF_Shuffle_debug(TSF_sysargvs):    #TSFdoc:「TSF_Shuffle」単体テスト風デバッグ。
    TSF_debug_log="";  TSF_debug_savefilename="debug/debug_py-Shuffle.log";
    TSF_debug_log=TSF_Io_printlog("--- {0} ---".format(__file__),TSF_debug_log)
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
    TSF_Shuffle_debug(TSF_Io_argvs(["python","TSF_Shuffle.py"]))


#! -- Copyright (c) 2017 ooblog --
#! License: MIT　https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
