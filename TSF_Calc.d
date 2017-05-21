#! /usr/bin/env rdmd

import std.stdio;
import std.string;
import std.conv;
import std.math;
import std.bigint;
import std.regex;
import std.algorithm;
import std.typecons;
import std.array;

import TSF_Io;
import TSF_Forth;


void TSF_Calc_Initcards(ref string function()[string] TSF_cardsD,ref string[] TSF_cardsO){    //#TSFdoc:関数カードに文字列置換などの命令を追加する。(TSFAPI)
    TSF_Forth_importlist("TSF_Calc");
    string function()[string] TSF_Forth_cards=[
        "#TSF_calc":&TSF_Calc_calc, "#分数計算":&TSF_Calc_calc,
        "#TSF_-calc":&TSF_Calc_calcMinus, "#分数計算(符号マイナスのみ)":&TSF_Calc_calcMinus,
        "#TSF_calcJA":&TSF_Calc_calcJA, "#分数計算(日本語)":&TSF_Calc_calcJA,
//        "#TSF_precision":&TSF_Calc_precision, "#有効桁数":&TSF_Calc_precision,
//        "#TSF_rounding":&TSF_Calc_rounding, "#端数処理":&TSF_Calc_rounding,
    ];
    foreach(string cardkey,string function() cardfunc;TSF_Forth_cards){
        if( cardkey !in TSF_cardsD ){
            TSF_cardsD[cardkey]=cardfunc; TSF_cardsO~=[cardkey];
        }
    } 
    TSF_Calc_opeorder=["恒河沙","阿僧祇","那由他","不可思議","無量大数","無限",
        "模糊","逡巡","須臾","瞬息","弾指","刹那","六徳","虚空","清浄","阿頼耶","阿摩羅","涅槃寂静",
        "円周率","2π","円周","ネイピア数","ルート","プラス","マイナス","絶対値",
        "足す","引く","掛ける","割る","分の",
    ];
    TSF_Calc_opeword=["恒河沙":"恒","阿僧祇":"阿","那由他":"那","不可思議":"思","無量大数":"量","無限":"∞",
        "模糊":"模","逡巡":"逡","須臾":"須","瞬息":"瞬","弾指":"弾","刹那":"刹","六徳":"徳","虚空":"空","清浄":"清","阿頼耶":"耶","阿摩羅":"摩","涅槃寂静":"涅",
        "円周率":"π","2π":"θ","円周":"θ","ネイピア数":"ｅ","ルート":"√","プラス":"+","マイナス":"-","絶対値":"!",
        "足す":"足","引く":"引","掛ける":"掛","割る":"割","分の":"_",
    ];
    TSF_Calc_opechar=["１":"1","２":"2","３":"3","４":"4","５":"5","６":"6","７":"7","８":"8","９":"9","０":"0",
        "一":"1","二":"2","三":"3","四":"4","五":"5","六":"6","七":"7","八":"8","九":"9","〇":"0",
        "壱":"1","弐":"2","参":"3","肆":"4","伍":"5","陸":"6","漆":"7","捌":"8","玖":"9","零":"0",
        "絶":"p","負":"m","分":"_","点":".","円":".","圓":".","陌":"百","佰":"百","阡":"千","仟":"千","萬":"万","仙":"銭","秭":"𥝱",
        "＋":"+","－":"-","×":"*","÷":"/","／":"/","＼":"\\","＃":"#","％":"%","＾":"^","｜":"|","＿":"_",
        "加":"+","減":"-","乗":"*","除":"/","捨":"\\","余":"#","比":"%","税":"%","冪":"^","分":"_",
        "足":"+","引":"-","掛":"*","割":"/","和":"+","差":"-","積":"*","商":"/","足":"+","引":"-","掛":"*","割":"/",
        "π":"y","周":"Y","θ":"Y","底":"e","ｅ":"e","常":"L","進":"l","対":"E","√":"R","根":"R",
    ];
    string TSF_Calc_order="*(10000";
    string[] TSF_Calc_okusenman=["万","億","兆","京","垓","𥝱","穣","溝","澗","正","載","極","恒","阿","那","思","量"];
    string[] TSF_Calc_rinmoushi=["厘","毛","糸","忽","微","繊","沙","塵","埃","渺","漠","模","逡","須","瞬","弾","刹","徳","空","清","耶","摩","涅"];
    foreach(string okusen;TSF_Calc_okusenman){
        TSF_Calc_okusendic[okusen]=TSF_Calc_order~")"; TSF_Calc_order~="0000";
//        TSF_CalcReg_okusen[okusen]=regex("([0-9千百十]+?)"~okusen);
        TSF_CalcReg_okusen[okusen]="([0-9千百十]+?)"~okusen;
    }
    TSF_Calc_order="/(1000";
    foreach(string rinmou;TSF_Calc_rinmoushi){
        TSF_Calc_rinmoudic[rinmou]=TSF_Calc_order~")"; TSF_Calc_order~="0";
//        TSF_CalcReg_rinmou[rinmou]=regex("([0-9]+?)"~rinmou);
        TSF_CalcReg_rinmou[rinmou]="([0-9]+?)"~rinmou;
    }
    TSF_Calc_okusenyen=["円"]~TSF_Calc_okusenman;
    TSF_Calc_rinmouyen=["円","割","銭"]~TSF_Calc_rinmoushi;
    TSF_Calc_precisionMAX=100;
}

string TSF_Calc_calcsquarebrackets(string TSF_calcQ,string TSF_calcBL,string TSF_calcBR){    //#TSFdoc:スタックからpeek(読込)ショートカット角括弧で連結する。(TSFAPI)
    string TSF_calcA=TSF_calcQ,TSF_calcK="";
    foreach(string TSF_stacksK,string[] TSF_stacksV;TSF_Forth_stackD()){
        TSF_calcK=TSF_calcBL~TSF_stacksK;
        if( count(TSF_calcA,TSF_calcK) ){
            foreach(size_t TSF_stackC,string TSF_stackQ;TSF_stacksV){
                TSF_calcK=TSF_calcBL~TSF_stacksK~to!string(TSF_stackC)~TSF_calcBR;
                if( count(TSF_calcA,TSF_calcK) ){
                    TSF_calcA=replace(TSF_calcA,TSF_calcK,TSF_stackQ);
                }
            }
        }
    }
    return TSF_calcA;
}

string TSF_Calc_calc(){    //#TSFdoc:分数計算する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsQQ(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")));
    return "";
}

string TSF_Calc_calcMinus(){    //#TSFdoc:分数計算する。符号pmを省略する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsQQM(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")));
    return "";
}

string TSF_Calc_calcJA(){    //#TSFdoc:分数計算する。カード枚数+数式1枚[cardN…cardA←calc]ドローして1枚[N]リターン。
    TSF_Forth_return(TSF_Forth_drawthat(),TSF_Calc_bracketsJA(TSF_Calc_calcsquarebrackets(TSF_Forth_drawthe(),"[","]")));
    return "";
}

long TSF_Calc_precisionMAX;
string TSF_Calc_precision(){    //#TSF_doc:電卓の有効桁数を変更する。1枚[precision]ドロー。
    TSF_Calc_precisionMAX=to!long(fmin(fmax(TSF_Io_RPNzero(TSF_Forth_drawthe()),5),1000));
    return "";
}


string TSF_Calc_bracketsJA(string TSF_calcQ){    //#TSF_doc:分数電卓の日本語処理。(TSFAPI)
    string TSF_calcA=TSF_Calc_bracketsQQ(TSF_calcQ);
//    writeln(format("TSF_calcA %s",TSF_calcA));
    string TSF_calcF=TSF_calcA.front=='m'?"マイナス":"";
    if( TSF_calcA.front!='n' ){
        if( count(TSF_calcA,".") ){
            string[] TSF_calcND=replace(replace(TSF_calcA,"p",""),"m","").split(".");
            string TSF_calcNstr=TSF_calcND[0],TSF_calcDstr=TSF_calcND[$-1];
            TSF_calcNstr=TSF_calc_comma_okusen(TSF_calcNstr,TSF_Calc_okusenyen,4,true).stripLeft('0');
            TSF_calcNstr=replace(TSF_calcNstr,"円","");
            TSF_calcDstr=TSF_calc_comma_rinmou(TSF_calcDstr,TSF_Calc_rinmouyen,1,true);
            TSF_calcDstr=TSF_calcDstr.replace("割","");
            TSF_calcA=TSF_calcNstr~TSF_calcDstr;
            if( TSF_calcA.front=='円' ){ TSF_calcA=TSF_calcA.replace("円",""); }
            TSF_calcA=TSF_calcA.replace("模","模糊").replace("逡","逡巡").replace("須","須臾").replace("瞬","弾指").replace("弾","弾指").replace("刹","刹那");
            TSF_calcA=TSF_calcA.replace("徳","六徳").replace("空","虚空").replace("清","清浄").replace("耶","阿頼耶").replace("摩","阿摩羅").replace("涅","涅槃寂静");
        }
        else{
            string[] TSF_calcND=replace(replace(TSF_calcA,"p",""),"m","").split("|");
            string TSF_calcNstr,TSF_calcDstr;
            if( TSF_calcND.length>=2 ){
                TSF_calcNstr=TSF_calcND[0]; TSF_calcDstr=TSF_calcND[$-1];
            }
            else{
                TSF_calcNstr=TSF_calcND[0]; TSF_calcDstr="1";
            }
            TSF_calcNstr=TSF_calc_comma_okusen(TSF_calcNstr,TSF_Calc_okusenyen,4,true).stripLeft('0');
            TSF_calcDstr=TSF_calc_comma_okusen(TSF_calcDstr,TSF_Calc_okusenyen,4,true).stripLeft('0');
            TSF_calcDstr=replace(TSF_calcDstr,"円","");
            TSF_calcA=join([TSF_calcDstr,TSF_calcNstr],"分の");
            if( TSF_calcDstr=="1"){
                TSF_calcA=TSF_calcA.replace("1分の","");
            }
            else{
                TSF_calcA=TSF_calcA.replace("円","");
            }
        }
        TSF_calcA=TSF_calcA.replace("恒","恒河沙").replace("阿","阿僧祇").replace("那","那由他").replace("思","不可思議").replace("量","無量大数");
        TSF_calcA=TSF_calcF~TSF_calcA;
    }
    return TSF_calcA;
}

auto TSF_CalcReg_ascii=regex("^[\x20-\x7E]+$");
string[string] TSF_Calc_opeword,TSF_Calc_opechar,TSF_Calc_okusendic,TSF_Calc_rinmoudic;
string[] TSF_Calc_opeorder,TSF_Calc_okusenyen,TSF_Calc_rinmouyen;
//Regex[string] TSF_CalcReg_okusen,TSF_CalcReg_rinmou;
string[string] TSF_CalcReg_okusen,TSF_CalcReg_rinmou;
auto TSF_CalcReg_senCpercent=regex("([0-9百十]+?)銭"),TSF_CalcReg_senKkilo=regex("([0-9]+?)千"),TSF_CalcReg_hyakuH=regex("([0-9]+?)百"),TSF_CalcReg_juuD=regex("([0-9]+?)十");
string TSF_calc_commacut_JA(string TSF_calcQ){    //#TSF_doc:整数のコンマ削除(漢数字をアラビア数字に)。(TSFAPI)
    string TSF_calcA=TSF_calcQ;
    if( !match(TSF_calcA,TSF_CalcReg_ascii) ){
        foreach(string TSF_opewordK;TSF_Calc_opeorder){
            TSF_calcA=replace(TSF_calcA,TSF_opewordK,TSF_Calc_opeword[TSF_opewordK]);
        }
        foreach(string TSF_opecharK,string TSF_opecharV;TSF_Calc_opechar){
            TSF_calcA=replace(TSF_calcA,TSF_opecharK,TSF_opecharV);
        }
//        TSF_calcA=replace(TSF_calcA,regex("([0-9百十]+?)銭"),"+($1)/(100)");
        TSF_calcA=replace(TSF_calcA,TSF_CalcReg_senCpercent,"+($1)/(100)");
        foreach(string TSF_okusenK,string TSF_okusenV;TSF_Calc_okusendic){
//            TSF_calcA=replace(TSF_calcA,regex("([0-9千百十]+?)"~TSF_okusenK),"+($1)"~TSF_okusenV);
            TSF_calcA=replace(TSF_calcA,regex(TSF_CalcReg_okusen[TSF_okusenK]),"+($1)"~TSF_okusenV);
        }
        foreach(string TSF_rinmouK,string TSF_rinmouV;TSF_Calc_rinmoudic){
//            TSF_calcA=replace(TSF_calcA,regex("([0-9]+?)"~TSF_rinmouK),"+($1)"~TSF_rinmouV);
            TSF_calcA=replace(TSF_calcA,regex(TSF_CalcReg_rinmou[TSF_rinmouK]),"+($1)"~TSF_rinmouV);
        }
//        TSF_calcA=replace(TSF_calcA,regex("([0-9]+?)千"),"+$1*(1000)");
//        TSF_calcA=replace(TSF_calcA,regex("([0-9]+?)百"),"+$1*(100)");
//        TSF_calcA=replace(TSF_calcA,regex("([0-9]+?)十"),"+$1*(10)");
        TSF_calcA=replace(TSF_calcA,TSF_CalcReg_senKkilo,"+$1*(1000)");
        TSF_calcA=replace(TSF_calcA,TSF_CalcReg_hyakuH,"+$1*(100)");
        TSF_calcA=replace(TSF_calcA,TSF_CalcReg_juuD,"+$1*(10)");
        TSF_calcA=replace(TSF_calcA,"銭","+(1|100)");
        TSF_calcA=replace(TSF_calcA,"十","+(10)");
        TSF_calcA=replace(TSF_calcA,"百","+(100)");
        TSF_calcA=replace(TSF_calcA,"千","+(1000)");
        foreach(string TSF_okusenK,string TSF_okusenV;TSF_Calc_okusendic){
            TSF_calcA=replace(TSF_calcA,TSF_okusenK,TSF_okusenV~"+");
        }
    }
    return TSF_calcA;
}

string TSF_calc_comma_okusen(string TSF_calcQ,string[] TSF_calcT,long TSF_calcC,bool TSF_calcZ){    //#TSF_doc:整数にコンマ(漢数字)処理。(TSFAPI)
    string TSF_calcA="";
    size_t TSF_calcCptr=0;
    string TSF_calc_zero=""; foreach(long i;0..TSF_calcC){ TSF_calc_zero~="0"; }
    foreach_reverse(size_t TSF_calcM,char TSF_calcK;TSF_calcQ){
        if( (TSF_calcQ.length-1-TSF_calcM)%TSF_calcC!=0 ){
            TSF_calcA=join([to!string(TSF_calcK),TSF_calcA],"");
        }
        else{
            TSF_calcA=join([to!string(TSF_calcK),TSF_calcA],(TSF_calcCptr<TSF_calcT.length)?TSF_calcT[TSF_calcCptr]:",");
            if( (TSF_calcZ==true)&&(count(TSF_calcA,TSF_calc_zero)>0)&&(TSF_calcCptr<TSF_calcT.length) ){
                TSF_calcA=TSF_calcA.replace(TSF_calcT[TSF_calcCptr]~TSF_calc_zero,TSF_calcT[TSF_calcCptr]);
            }
            TSF_calcCptr+=1;
        }
    }
    return TSF_calcA;
}

string TSF_calc_comma_rinmou(string TSF_calcQ,string[] TSF_calcT,long TSF_calcC,bool TSF_calcZ){    //#TSF_doc:小数にコンマ(漢数字)処理。(TSFAPI)
    string TSF_calcA="";
    size_t TSF_calcCptr=0;
    string TSF_calc_zero=""; foreach(long i;0..TSF_calcC){ TSF_calc_zero~="0"; }
    foreach(size_t TSF_calcM,char TSF_calcK;TSF_calcQ){
        if( TSF_calcM%TSF_calcC!=0 ){
            TSF_calcA=join([TSF_calcA,to!string(TSF_calcK)],"");
        }
        else{
            TSF_calcA=join([TSF_calcA,to!string(TSF_calcK)],(TSF_calcCptr<TSF_calcT.length)?TSF_calcT[TSF_calcCptr]:",");
            if( (TSF_calcZ==true)&&(count(TSF_calcA,TSF_calc_zero)>0)&&(TSF_calcCptr<TSF_calcT.length) ){
                TSF_calcA=TSF_calcA.replace(TSF_calc_zero~TSF_calcT[TSF_calcCptr],"");
            }
            TSF_calcCptr++;
        }
    }
    TSF_calcA=join([TSF_calcA,(TSF_calcCptr<TSF_calcT.length)?TSF_calcT[TSF_calcCptr]:","]);
    if( (TSF_calcZ==true)&&(count(TSF_calcA,TSF_calc_zero)>0)&&(TSF_calcCptr<TSF_calcT.length) ){
        TSF_calcA=TSF_calcA.replace(TSF_calc_zero~TSF_calcT[TSF_calcCptr],"");
    }
    return TSF_calcA;
}

auto TSF_CalcReg_bracketreg=regex("[(](?<=[(])[^()]*(?=[)])[)]");
string TSF_Calc_bracketsQQ(string TSF_calcQ){    //#TSF_doc:分数電卓のmain。括弧の内側を検索。(TSFAPI)
    string TSF_calcA=TSF_calc_commacut_JA(TSF_calcQ);  long TSF_calcBLR=0,TSF_calcBCAP=0;
    while( count(TSF_calcA,"(") || count(TSF_calcA,")") ){
        TSF_calcBLR=0; TSF_calcBCAP=0;
        foreach(char TSF_calcB;TSF_calcQ){
            if( TSF_calcB=='(' ){ TSF_calcBLR+=1; }
            if( TSF_calcB==')' ){ TSF_calcBLR-=1;
                if( TSF_calcBLR<TSF_calcBCAP ){ TSF_calcBCAP=TSF_calcBLR; }
            }
        }
        if( TSF_calcBLR>0 ){
            foreach(long i;0..abs(TSF_calcBLR)){ TSF_calcA=TSF_calcA~")"; }
        }
        if( TSF_calcBLR<0 ){
            foreach(long i;0..abs(TSF_calcBLR)){ TSF_calcA="("~TSF_calcA; }
        }
        if( TSF_calcBCAP>0 ){
            foreach(long i;0..TSF_calcBCAP){ TSF_calcA="("~TSF_calcA~")"; }
        }
        foreach(TSF_calcK;match(TSF_calcA,TSF_CalcReg_bracketreg)){
            TSF_calcA=TSF_calcA.replace(TSF_calcK.hit,TSF_Calc_function(TSF_calcK.hit));
        }
    }
    TSF_calcA=replace(TSF_calcA,TSF_calcA,TSF_Calc_function(TSF_calcA));
    if( TSF_calcA.length ){
        if( count(":",TSF_calcA.back)==0 ){
            if( count("n0pm",TSF_calcA.front)==0 ){
                TSF_calcA=TSF_calcA.front=='-'?TSF_calcA.replace("-","m"):"p"~TSF_calcA;
            }
        }
    }
    return TSF_calcA;
}

string TSF_Calc_bracketsQQM(string TSF_calcQ){    //#TSF_doc:分数電卓のPM符号省略。(TSFAPI)
    string TSF_calcA=TSF_Calc_bracketsQQ(TSF_calcQ);
    TSF_calcA=TSF_calcA.replace("p","").replace("m","-");
    return TSF_calcA;
}


auto TSF_Calc_FLR(string TSF_calcQ,string TSF_calcO){    //#三項演算子と「~」を用いてタプルに分割。(TSFAPI)
    string TSF_calcF,TSF_calcL,TSF_calcR;
    string[] TSF_calcQsplits=TSF_calcQ.split(TSF_calcO);
    TSF_calcF=TSF_Io_RPN(replace(TSF_Calc_addition(TSF_calcQsplits[0]),"-","m"));
    if( count(TSF_calcQsplits[$-1],'~') ){
        string[] TSF_calcLRsplits=TSF_calcQsplits[$-1].split('~');
        TSF_calcL=TSF_calcLRsplits[0];  TSF_calcR=TSF_calcLRsplits[$-1];
    }
    else{
        TSF_calcL=TSF_calcQsplits[$-1];  TSF_calcR=TSF_calcQsplits[$-1];
    }
    return Tuple!(string,string,string)(TSF_calcF,TSF_calcL,TSF_calcR);
}

string TSF_Calc_function(string TSF_calcQ){    //#TSFdoc:分数電卓の和集合積集合およびゼロ比較演算子系。(TSFAPI)
    string TSF_calcA=TSF_calcQ;
    string TSF_calcK=stripRight(stripLeft(TSF_calcQ,'('),')');
    if( count(TSF_calcK,",") ){
         TSF_calcA=TSF_Io_RPN(TSF_calcK);
    }
    else if( count(TSF_calcK,"Z~") ){
        auto TSF_calcFLR=TSF_Calc_FLR(TSF_calcK,"Z~");  string TSF_calcF=TSF_calcFLR[0],TSF_calcL=TSF_calcFLR[1],TSF_calcR=TSF_calcFLR[2];
        TSF_calcA=TSF_Calc_addition(TSF_calcF.front=='0'?TSF_calcL:TSF_calcR);
    }
    else if( count(TSF_calcK,"z~") ){
        auto TSF_calcFLR=TSF_Calc_FLR(TSF_calcK,"z~");  string TSF_calcF=TSF_calcFLR[0],TSF_calcL=TSF_calcFLR[1],TSF_calcR=TSF_calcFLR[2];
        TSF_calcA=TSF_Calc_addition(TSF_calcF.front!='0'?TSF_calcL:TSF_calcR);
    }
    else if( count(TSF_calcK,"O~") ){
        auto TSF_calcFLR=TSF_Calc_FLR(TSF_calcK,"O~");  string TSF_calcF=TSF_calcFLR[0],TSF_calcL=TSF_calcFLR[1],TSF_calcR=TSF_calcFLR[2];
        TSF_calcA=TSF_Calc_addition((TSF_calcF.front=='p')||(TSF_calcF.front=='0')?TSF_calcL:TSF_calcR);
    }
    else if( count(TSF_calcK,"o~") ){
        auto TSF_calcFLR=TSF_Calc_FLR(TSF_calcK,"o~");  string TSF_calcF=TSF_calcFLR[0],TSF_calcL=TSF_calcFLR[1],TSF_calcR=TSF_calcFLR[2];
        TSF_calcA=TSF_Calc_addition(TSF_calcF.front=='p'?TSF_calcL:TSF_calcR);
    }
    else if( count(TSF_calcK,"U~") ){
        auto TSF_calcFLR=TSF_Calc_FLR(TSF_calcK,"U~");  string TSF_calcF=TSF_calcFLR[0],TSF_calcL=TSF_calcFLR[1],TSF_calcR=TSF_calcFLR[2];
        TSF_calcA=TSF_Calc_addition((TSF_calcF.front=='m')||(TSF_calcF.front=='0')?TSF_calcL:TSF_calcR);
    }
    else if( count(TSF_calcK,"u~") ){
        auto TSF_calcFLR=TSF_Calc_FLR(TSF_calcK,"u~");  string TSF_calcF=TSF_calcFLR[0],TSF_calcL=TSF_calcFLR[1],TSF_calcR=TSF_calcFLR[2];
        TSF_calcA=TSF_Calc_addition(TSF_calcF.front=='m'?TSF_calcL:TSF_calcR);
    }
    else if( count(TSF_calcK,"N~") ){
        auto TSF_calcFLR=TSF_Calc_FLR(TSF_calcK,"N~");  string TSF_calcF=TSF_calcFLR[0],TSF_calcL=TSF_calcFLR[1],TSF_calcR=TSF_calcFLR[2];
        TSF_calcA=TSF_Calc_addition(TSF_calcF.front=='n'?TSF_calcL:TSF_calcR);
    }
    else{
        TSF_calcA=TSF_Calc_addition(TSF_calcK);
    }
    return TSF_calcA;
}

string TSF_Calc_addition(string TSF_calcQ){    //#TSF_doc:分数電卓の足し算引き算・消費税計算等。(TSFAPI)
    string TSF_calcA=TSF_calcQ;
    if( (TSF_calcA.length>0)&&(TSF_calcA.back==':') ){
        return TSF_calcA;
    }
    BigInt TSF_calcLN=BigInt(0),TSF_calcLD=BigInt(1);
    string TSF_calcQreplace=TSF_calcQ.replace("-+","+m").replace("+-","+m");
    TSF_calcQreplace=TSF_calcQreplace.replace("+","\t+").replace("-","\t-").replace("%","\t%");
    string[] TSF_calcQsplits=TSF_calcQreplace.strip('\t').split("\t");
    char TSF_calcO;
    string TSF_calcRN,TSF_calcRD;
    opeexit_addition: foreach(string TSF_calcQmulti;TSF_calcQsplits){
        TSF_calcO=' ';
        foreach(char TSF_calcOpe;"+-%"){
            TSF_calcO=count(TSF_calcQmulti,TSF_calcOpe)?TSF_calcOpe:TSF_calcO;
        }
        string[] TSF_calcRND=TSF_Calc_multiplication(TSF_calcQmulti.strip('+').strip('-').strip('%')).split("|");
        TSF_calcRN=TSF_calcRND[0]; TSF_calcRD=TSF_calcRND[$-1];
        if( BigInt(TSF_calcRD)==0 ){
            TSF_calcA="n|0";
            TSF_calcLN=BigInt(0); TSF_calcLD=BigInt(0);
            break;
        }
        else{
            switch( TSF_calcO ){
                case '%':
                    BigInt TSF_calcPN=TSF_calcLN*BigInt(TSF_calcRN);
                    BigInt TSF_calcPD=TSF_calcLD*BigInt(TSF_calcRD)*BigInt("100");
                    BigInt TSF_calcG=BigInt(TSF_Calc_LCM(to!string(TSF_calcLD),to!string(TSF_calcPD)));
                    TSF_calcLN=TSF_calcLN*TSF_calcG/TSF_calcLD+BigInt(TSF_calcPN)*TSF_calcG/BigInt(TSF_calcPD);
                    TSF_calcLD=TSF_calcG;
                break;
                case '-':
                    BigInt TSF_calcG=BigInt(TSF_Calc_LCM(to!string(TSF_calcLD),TSF_calcRD));
                    TSF_calcLN=TSF_calcLN*TSF_calcG/TSF_calcLD-BigInt(TSF_calcRN)*TSF_calcG/BigInt(TSF_calcRD);
                    TSF_calcLD=TSF_calcG;
                break;
                case '+': default:
                    BigInt TSF_calcG=BigInt(TSF_Calc_LCM(to!string(TSF_calcLD),TSF_calcRD));
                    TSF_calcLN=TSF_calcLN*TSF_calcG/TSF_calcLD+BigInt(TSF_calcRN)*TSF_calcG/BigInt(TSF_calcRD);
                    TSF_calcLD=TSF_calcG;
                break;
            }
        }
    }
    TSF_calcA=TSF_Calc_bigtostr(to!string(TSF_calcLN),to!string(TSF_calcLD),(TSF_calcLN<0?1:0));
    return TSF_calcA;
}

string TSF_Calc_multiplication(string TSF_calcQ){    //#TSF_doc:分数電卓の掛け算割り算等。公倍数公約数、最大値最小値も扱う。(TSFAPI)
    BigInt TSF_calcLN=BigInt(1),TSF_calcLD=BigInt(1);
    string TSF_calcA=TSF_calcQ;
    string TSF_calcQreplace=TSF_calcQ.replace("*","\t*").replace("/","\t/").replace("\\","\t\\").replace("#","\t#").replace(">","\t>").replace("<","\t<");
    string[] TSF_calcQsplits=TSF_calcQreplace.strip('\t').split('\t');
    if( TSF_calcQsplits.length==0 ){ TSF_calcQsplits.length=1; TSF_calcQsplits[0]=""; }
    char TSF_calcO;
    string TSF_calcRN,TSF_calcRD;
    opeexit_multiplication: foreach(string TSF_calcQmulti;TSF_calcQsplits){
        TSF_calcO=' ';
        foreach(char TSF_calcOpe;"*/\\#<>"){
            TSF_calcO=count(TSF_calcQmulti,TSF_calcOpe)?TSF_calcOpe:TSF_calcO;
        }
        string[] TSF_calcRND=TSF_Calc_fractalize(TSF_calcQmulti.strip('*').strip('/').strip('\\').strip('#').strip('<').strip('>')).split('|');
        TSF_calcRN=TSF_calcRND[0]; TSF_calcRD=TSF_calcRND[$-1];
        if( BigInt(TSF_calcRD)==0 ){
            TSF_calcA="n|0";
            TSF_calcLN=BigInt(0); TSF_calcLD=BigInt(0);
            break;
        }
        else{
            switch( TSF_calcO ){
                case '/':
                    TSF_calcLN=TSF_calcLN*BigInt(TSF_calcRD);
                    TSF_calcLD=TSF_calcLD*BigInt(TSF_calcRN);
                    if( TSF_calcLD<0 ){ TSF_calcLN=-TSF_calcLN; TSF_calcLD=-TSF_calcLD; }
                break;
                case '\\':
                    TSF_calcLN=TSF_calcLN*BigInt(TSF_calcRD);
                    TSF_calcLD=TSF_calcLD*BigInt(TSF_calcRN);
                    if( TSF_calcLD<0 ){ TSF_calcLN=-TSF_calcLN; TSF_calcLD=-TSF_calcLD; }
                    TSF_calcLN=TSF_calcLN/TSF_calcLD;  TSF_calcLD=1;
                break;
                case '#':
                    BigInt TSF_calcG=BigInt(TSF_Calc_LCM(to!string(TSF_calcLD),TSF_calcRD));
                    TSF_calcLN=TSF_calcLN*TSF_calcG/TSF_calcLD;
                    TSF_calcLD=TSF_calcLD*TSF_calcG/TSF_calcLD;
                    BigInt TSF_calcRM=BigInt(TSF_calcRN)*TSF_calcG/BigInt(TSF_calcRD);
                    if( BigInt(TSF_calcRM)==0 ){
                        TSF_calcA="n|0";
                        TSF_calcLN=BigInt(0); TSF_calcLD=BigInt(0);
                        break opeexit_multiplication;
                    }
                    else if( TSF_calcRM>0 ){
                        TSF_calcLN=TSF_calcLN%TSF_calcRM;
                    }
                    else{
                        if( TSF_calcLN%abs(TSF_calcRM)!=0 ){
                            TSF_calcLN=abs(TSF_calcRM)-TSF_calcLN%abs(TSF_calcRM);
                        }
                        else{
                            TSF_calcLN=0;
                        }
                    }
                break;
                case '>':
                    BigInt TSF_calcG=BigInt(TSF_Calc_LCM(to!string(TSF_calcLD),TSF_calcRD));
                    BigInt TSF_calcLM=TSF_calcLN*TSF_calcG/TSF_calcLD;
                    BigInt TSF_calcRM=BigInt(TSF_calcRN)*TSF_calcG/BigInt(TSF_calcRD);
                    if( TSF_calcLM>TSF_calcRM ){
                        TSF_calcLN=BigInt(TSF_calcRN); TSF_calcLD=BigInt(TSF_calcRD);
                    }
                break;
                case '<':
                    BigInt TSF_calcG=BigInt(TSF_Calc_LCM(to!string(TSF_calcLD),TSF_calcRD));
                    BigInt TSF_calcLM=TSF_calcLN*TSF_calcG/TSF_calcLD;
                    BigInt TSF_calcRM=BigInt(TSF_calcRN)*TSF_calcG/BigInt(TSF_calcRD);
                    if( TSF_calcLM<TSF_calcRM ){
                        TSF_calcLN=BigInt(TSF_calcRN); TSF_calcLD=BigInt(TSF_calcRD);
                    }
                break;
                case '*': default:
                    TSF_calcLN=TSF_calcLN*BigInt(TSF_calcRN);
                    TSF_calcLD=TSF_calcLD*BigInt(TSF_calcRD);
                break;
            }
        }
    }
    TSF_calcA=TSF_Calc_bigtostr(to!string(TSF_calcLN),to!string(TSF_calcLD),(TSF_calcLN<0?1:0));
    return TSF_calcA;
}

string TSF_Calc_fractalize(string TSF_calcQ){    //#TSF_doc:分数電卓なので小数を分数に。ついでに平方根や三角関数も。0で割る、もしくは桁が限界越えたときなどは「n|0」を返す。(TSFAPI)
    string TSF_calcA=TSF_calcQ;
    string[] TSF_calcND;  string TSF_calcNstr,TSF_calcDstr;
    if( count(TSF_calcA,'_') ){
        TSF_calcND=TSF_calcA.split("_");
        TSF_calcNstr=TSF_calcND[0]; TSF_calcDstr=TSF_calcND[$-1];
        TSF_calcA=join([TSF_calcDstr,TSF_calcNstr],"|");
    }
    TSF_calcA=count(TSF_calcA,"|")?TSF_calcA:TSF_calcA~"|1";
    long TSF_calcM=TSF_calcA.count("!")==0?TSF_calcA.count("m")+TSF_calcA.count("-"):0;
    TSF_calcA=TSF_calcA.replace("p","").replace("m","").replace("-","").replace("!","");
    TSF_calcND=TSF_calcA.split("|");
    TSF_calcNstr=TSF_calcND[0]; TSF_calcDstr=TSF_calcND[$-1];
    TSF_calcNstr=count(TSF_calcNstr,".")?TSF_calcNstr:TSF_calcNstr~".";
    TSF_calcDstr=count(TSF_calcDstr,".")?TSF_calcDstr:TSF_calcDstr~".";
    long TSF_calcNint=TSF_calcNstr.length-1-lastIndexOf(TSF_calcNstr,".");
    long TSF_calcDint=TSF_calcDstr.length-1-lastIndexOf(TSF_calcDstr,".");
    long TSF_calcNDint=to!long(fmin(TSF_calcNint,TSF_calcDint));
    TSF_calcNstr=TSF_calcNstr.stripLeft('0').replace(".","");  foreach(long i;0..TSF_calcDint-TSF_calcNDint){ TSF_calcNstr~="0"; }
    TSF_calcDstr=TSF_calcDstr.stripLeft('0').replace(".","");  foreach(long i;0..TSF_calcNint-TSF_calcNDint){ TSF_calcDstr~="0"; }
    TSF_calcA=TSF_Calc_bigtostr(TSF_calcNstr,TSF_calcDstr,TSF_calcM);
    return TSF_calcA;
}

string TSF_Calc_bigtostr(string TSF_calcN,string TSF_calcD,long TSF_calcM){    //TSF_doc:計算結果を通分する。(TSFAPI)
    string TSF_calcA="n|0";
    if( TSF_calcD!="" ){
        if( TSF_calcN == "" ){ TSF_calcN="0"; }
        try{
            BigInt TSF_calcGbig=BigInt(TSF_Calc_GCM(TSF_calcN,TSF_calcD));
            if( TSF_calcGbig!=0 ){
                BigInt TSF_calcNbig=BigInt(TSF_calcN)/TSF_calcGbig;
                BigInt TSF_calcDbig=BigInt(TSF_calcD)/TSF_calcGbig;
                TSF_calcNbig=TSF_calcM%2?-abs(TSF_calcNbig):abs(TSF_calcNbig);
                TSF_calcA=to!string(TSF_calcNbig)~"|"~to!string(TSF_calcDbig);
            }
            else{
                TSF_calcA="n|0";
            }
        }
        catch(ConvException e){
            TSF_calcA="n|0";
        }
    }
    else{
        TSF_calcA="n|0";
    }
    return TSF_calcA;
}

string TSF_Calc_GCM(string TSF_calcN,string TSF_calcD){    //#TSF_doc:最大公約数の計算。(TSFAPI)
    string TSF_calcA="n|0";
    BigInt TSF_calcMbig,TSF_calcNbig,TSF_calcMNbig;
    try{
        TSF_calcMbig=abs(BigInt(TSF_calcN));
        TSF_calcNbig=abs(BigInt(TSF_calcD));
        if( TSF_calcMbig<TSF_calcNbig ){
            TSF_calcMNbig=TSF_calcMbig;  TSF_calcMbig=TSF_calcNbig;  TSF_calcNbig=TSF_calcMNbig;
        }
        while( TSF_calcNbig>0 ){
            TSF_calcMNbig=TSF_calcMbig%TSF_calcNbig;  TSF_calcMbig=TSF_calcNbig;  TSF_calcNbig=TSF_calcMNbig;
        }
        TSF_calcA=to!string(TSF_calcMbig);
    }
    catch(ConvException e){
        TSF_calcA="n|0";
    }
    return TSF_calcA;
}

string TSF_Calc_LCM(string TSF_calcN,string TSF_calcD){    //#TSF_doc:最小公倍数の計算(TSFAPI)。
    string TSF_calcA="n|0";
    BigInt TSF_calcGbig=BigInt(TSF_Calc_GCM(TSF_calcN,TSF_calcD));
    if( TSF_calcGbig!=0 ){
        try{
            TSF_calcA=to!string(abs(BigInt(TSF_calcN)*BigInt(TSF_calcD))/abs(BigInt(TSF_calcGbig)));
        }
        catch(ConvException e){
            TSF_calcA="n|0";
        }
    }
    else{
        TSF_calcA="n|0";
    }
    return TSF_calcA;
}

void function(ref string function()[string],ref string[])[] TSF_Initcalldebug=[&TSF_Calc_Initcards];
void TSF_Calc_debug(string[] TSF_sysargvs){    //#TSFdoc:「TSF_Calc」単体テスト風デバッグ。
    string TSF_debug_log="";  string TSF_debug_savefilename="debug/debug_d-Calc.log";
    TSF_debug_log=TSF_Io_printlog(format("--- %s ---",__FILE__),TSF_debug_log);
    TSF_Forth_initTSF(TSF_sysargvs,TSF_Initcalldebug);
    TSF_Forth_setTSF("TSF_Tab-Separated-Forth:",join([
        "calccount:","#TSF_this","#TSF_fin."],"\t"),'T');
    TSF_Forth_setTSF("calccount:",join([
        "calcjump:","calcsample:","#TSF_lenthe","0,1,[0]U","#TSF_join[]","#TSF_RPN","#TSF_peekNthe","#TSF_this","calccount:","#TSF_this"],"\t"),'T');
    TSF_Forth_setTSF("calcjump:",join([
        "#exit","calcpop:"],"\t"),'T');
    TSF_Forth_setTSF("calcpop:",join([
        "calcsample:","0","#TSF_pullNthe","#TSF_peekFthat","#TSF_calc","「[1]」→「[0]」","#TSF_join[]","#TSF_echo"],"\t"),'T');
    TSF_Forth_setTSF("calcpeekdata:",join([
        "009","108","207","306","405","504","603","702","801","900"],"\t"),'T');
    TSF_Forth_setTSF("calcjumpdata:",join([
        "True:","False:"],"\t"),'T');
    TSF_Forth_setTSF("calcsample:",join([
        "0|0","0|0,","0/0","0,0/",",0","0",
        "2,3+","2,3-","2,3*","2,3/","(2,3-),5+",
        "[calcpeekdata:8]",
        "4|6","3.5|0.05","5|6*m2|4","5|6/m2|4","5|6\\m2|4","5|6#p2|4","5|6#m2|4",
        "10#5","10#m5","10#7","10#m7","5#p4","5#m4","5,4#","5,m4#",
        "5|6>2|3","2|3>5|6","5|6<2|3","2|3<5|6",
        "2+3","2-3","5|6+p2|3","5|6-p2|3","5|6+m2|3","5|6-m2|3","100%p8",
        "100%m8","100*(100+8)/100","100*(100-8)/100","100,8%",
        ",m4!","m4!",
        "m1Z~[calcpeekdata:0]~[calcpeekdata:1]","0Z~[calcpeekdata:0]~[calcpeekdata:1]","p1Z~[calcpeekdata:0]~[calcpeekdata:1]",
        "m1Z~[calcjumpdata:0]~[calcjumpdata:1]","0Z~[calcjumpdata:0]~[calcjumpdata:1]","p1Z~[calcjumpdata:0]~[calcjumpdata:1]",
        "m1Z~True:~False:","0Z~True:~False:","p1Z~True:~False:",
        "0|1N~True:~False:","n|0N~True:~False:",
        "2/3","2|3","2_3","3/2","3|2","3_2",
        ],"\t"),'N');
    TSF_debug_log=TSF_Forth_samplerun(__FILE__,true,TSF_debug_log);
    TSF_Io_savetext(TSF_debug_savefilename,TSF_debug_log);
}

unittest {
    TSF_Calc_debug(TSF_Io_argvs(["dmd","TSF_Calc.d"]));
}


// Copyright (c) 2017 ooblog
// License: MIT
// https://github.com/ooblog/TSF2KEV/blob/master/LICENSE


