set encoding=utf-8
scriptencoding utf-8
let s:kev_scriptdir = expand('<sfile>:p:h')

"「KanEditVim」の初期化。
function! KEV2setup()
    call KEV2pullmenu(0)
    let s:KEV2_choicekanamenuname = "「鍵盤"
    let s:KEV2_helpmenuname = "KEV2」"
    let s:KEV2_menuid = 10000
    let s:KEV2_inputkeys = ['1','2','3','4','5','6','7','8','9','0','-','^', 'q','w','e','r','t','y','u','i','o','p','@','[', 'a','s','d','f','g','h','j','k','l',';',':',']', 'z','x','c','v','b','n','m',',','.','/','\']
    let s:KEV2_inputkeys += ['!','"','#','$','%','&',"'",'(',')','~','=','|', 'Q','W','E','R','T','Y','U','I','O','P','`','{', 'A','S','D','F','G','H','J','K','L','+','*','}', 'Z','X','C','V','B','N','M','<','>','?','_']
    let s:KEV2_inputkanas = ["1(ぬ)","2(ふ)","3(あ)","4(う)","5(え)","6(お)","7(や)","8(ゆ)","9(よ)","0(わ)","-(ほ)","^(へ)","q(た)","w(て)","e(い)","r(す)","t(か)","y(ん)","u(な)","i(に)","o(ら)","p(せ)","@(゛)","[(゜)","a(ち)","s(と)","d(し)","f(は)","g(き)","h(く)","j(ま)","k(の)","l(り)",";(れ)",":(け)","](む)","z(つ)","x(さ)","c(そ)","v(ひ)","b(こ)","n(み)","m(も)",",(ね)",".(る)","/(め)","_(ろ)"]
    let s:KEV2_inputkanas += ["1(ヌ)","2(フ)","3(ア)","4(ウ)","5(エ)","6(オ)","7(ヤ)","8(ユ)","9(ヨ)","0(ワ)","-(ホ)","^(ヘ)","q(タ)","w(テ)","e(イ)","r(ス)","t(カ)","y(ン)","u(ナ)","i(ニ)","o(ラ)","p(セ)","@(ヶ)","[(ヵ)","a(チ)","s(ト)","d(シ)","f(ハ)","g(キ)","h(ク)","j(マ)","k(ノ)","l(リ)",";(レ)",":(ケ)","](ム)","z(ツ)","x(サ)","c(ソ)","v(ヒ)","b(コ)","n(ミ)","m(モ)",",(ネ)",".(ル)","/(メ)","_(ロ)"]
    let s:KEV2_inputkanas += ["1(ゔ)","2(ぶ)","3(ぁ)","4(ぅ)","5(ぇ)","6(ぉ)","7(ゃ)","8(ゅ)","9(ょ)","0(を)","-(ぼ)","^(べ)","q(だ)","w(で)","e(ぃ)","r(ず)","t(が)","y(っ)","u(ゑ)","i(ゐ)","o(ゎ)","p(ぜ)","@(ゞ)","[(ゝ)","a(ぢ)","s(ど)","d(じ)","f(ば)","g(ぎ)","h(ぐ)","j(ぱ)","k(…)","l(「)",";(」)",":(げ)","](ぷ)","z(づ)","x(ざ)","c(ぞ)","v(び)","b(ご)","n(ぴ)","m(ぽ)",",(、)",".(。)","/(ぺ)","_(〜)"]
    let s:KEV2_inputkanas += ["1(ヴ)","2(ブ)","3(ァ)","4(ゥ)","5(ェ)","6(ォ)","7(ャ)","8(ュ)","9(ョ)","0(ヲ)","-(ボ)","^(ベ)","q(ダ)","w(デ)","e(ィ)","r(ズ)","t(ガ)","y(ッ)","u(ヱ)","i(ヰ)","o(ヮ)","p(ゼ)","@(ヾ)","[(ヽ)","a(ヂ)","s(ド)","d(ジ)","f(パ)","g(ギ)","h(グ)","j(パ)","k(・)","l(『)",";(』)",":(ゲ)","](プ)","z(ヅ)","x(ザ)","c(ゾ)","v(ビ)","b(ゴ)","n(ピ)","m(ポ)",",(，)",".(．)","/(ペ)","_(ー)"]
    let s:KEV2_commandkanas = ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ", "た","て","い","す","か","ん","な","に","ら","せ","゛","゜", "ち","と","し","は","き","く","ま","の","り","れ","け","む", "つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ"]
    let s:KEV2_commandkanas += ["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ","タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","ヶ","ヵ","チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム","ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ"]
    let s:KEV2_commandkanas += ["ゔ","ぶ","ぁ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ","を","ぼ","べ","だ","で","ぃ","ず","が","っ","ゑ","ゐ","ゎ","ぜ","ゞ","ゝ","ぢ","ど","じ","ば","ぎ","ぐ","ぱ","…","「","」","げ","ぷ","づ","ざ","ぞ","び","ご","ぴ","ぽ","、","。","ぺ","〜"]
    let s:KEV2_commandkanas += ["ヴ","ブ","ァ","ゥ","ェ","ォ","ャ","ュ","ョ","ヲ","ボ","ベ","ダ","デ","ィ","ズ","ガ","ッ","ヱ","ヰ","ヮ","ゼ","ヾ","ヽ","ヂ","ド","ジ","バ","ギ","グ","パ","・","『","』","ゲ","ぷ","ヅ","ザ","ゾ","ビ","ゴ","ピ","ポ","，","．","ペ","ー"]
    let s:KEV2_inputESCs = {"\t":"<Tab>",' ':"<Space>",'<':"<lt>",'\':"<Bslash>",'|':"<Bar>",'-':"<Minus>",'.':"<Point>"}
    let s:KEV2_menuESCs = "\t\\:|< >.-"
    let s:KEV2_findESCs = ".*[]^%/\?~$"
    let s:KEV2_choicekana = "@(゛)"
    let s:KEV2_choicekanaidx = index(s:KEV2_inputkanas,s:KEV2_choicekana)
    let s:KEV2_dickana = "　"
    let s:KEV2_choicedicmenuname = escape(s:KEV2_choicekana . "{" . s:KEV2_dickana . "}",s:KEV2_menuESCs)
    let s:KEV2_keyslen = len(s:KEV2_inputkeys)/2
    let s:KEV2_key2kana = {}
    let s:KEV2_key2ESC = {}
    :for s:inputkey in range(len(s:KEV2_inputkeys))
        let s:KEV2_key2kana[s:KEV2_inputkeys[s:inputkey]] = s:KEV2_inputkanas[s:inputkey]
        let s:KEV2_key2ESC[s:KEV2_inputkeys[s:inputkey]] = get(s:KEV2_inputESCs,s:KEV2_inputkeys[s:inputkey],s:KEV2_inputkeys[s:inputkey])
    :endfor
    let s:KEV2_kanmap = {}
        let s:KEV2_kanmap["1(ぬ)"]=s:KEV2_commandkanas[(s:KEV2_keyslen*0):(s:KEV2_keyslen*1-1)]
        let s:KEV2_kanmap["1(ヌ)"]=s:KEV2_commandkanas[(s:KEV2_keyslen*1):(s:KEV2_keyslen*2-1)]
        let s:KEV2_kanmap["[(゜)"]=s:KEV2_commandkanas[(s:KEV2_keyslen*2):(s:KEV2_keyslen*3-1)]
        let s:KEV2_kanmap["[(ヵ)"]=s:KEV2_commandkanas[(s:KEV2_keyslen*3):(s:KEV2_keyslen*4-1)]
        let s:KEV2_kanmap["1(ゔ)"]=s:KEV2_commandkanas[(s:KEV2_keyslen*2):(s:KEV2_keyslen*3-1)]
        let s:KEV2_kanmap["1(ヴ)"]=s:KEV2_commandkanas[(s:KEV2_keyslen*0):(s:KEV2_keyslen*1-1)]
        let s:KEV2_kanmap["[(ヽ)"]=s:KEV2_commandkanas[(s:KEV2_keyslen*3):(s:KEV2_keyslen*4-1)]
        let s:KEV2_kanmap["[(ゝ)"]=s:KEV2_commandkanas[(s:KEV2_keyslen*1):(s:KEV2_keyslen*2-1)]
        :for s:inputkey in range(len(s:KEV2_inputkanas))
            let s:KEV2_inputkana=s:KEV2_inputkanas[s:inputkey]
            :if count(["1(ぬ)","1(ヌ)","[(゜)","[(ヵ)","1(ゔ)","1(ヴ)","[(ヽ)","[(ゝ)"],s:KEV2_inputkana) == 0
                let s:KEV2_kanmap[s:KEV2_inputkana]=(s:inputkey / s:KEV2_keyslen) % 2 ? s:KEV2_inputkeys[(s:KEV2_keyslen):] : s:KEV2_inputkeys[:(s:KEV2_keyslen-1)]
           :endif
           :if count(["@(ヾ)","@(ゞ)"],s:KEV2_inputkana) != 0
                :for s:widekey in range(len(s:KEV2_keyslen))
                    let s:KEV2_kanmap[s:KEV2_inputkana][s:widekey] = nr2char(char2nr(s:KEV2_kanmap[s:KEV2_inputkana][s:widekey])+0xfee0)
                :endfor
           :endif
        :endfor
    let s:KEV2_kanmapfilepath = s:kev_scriptdir . "/kanmap.tsf"
    :if filereadable(s:KEV2_kanmapfilepath)
        :for s:KEV2_kanmapfileline in readfile(s:KEV2_kanmapfilepath)
            let s:KEV2_kanmaplinelist = split(s:KEV2_kanmapfileline,"\t")
            :if len(s:KEV2_kanmaplinelist) >= 2
                let s:KEV2_kanmap[s:KEV2_kanmaplinelist[0]] = s:KEV2_kanmaplinelist[1:]
                :if len(s:KEV2_kanmaplinelist) < s:KEV2_keyslen
                    let s:KEV2_kanmap[s:KEV2_kanmaplinelist[0]] += s:KEV2_inputkeys[s:KEV2_keyslen-len(s:KEV2_kanmaplinelist):s:KEV2_keyslen]
                :endif
            :endif
        :endfor
    :endif
    execute "noremap <Plug>(KEV2setup) :call KEV2setup()<Enter>"
    execute "noremap <Plug>(KEV2help) :call KEV2help()<Enter>"
    execute "noremap <Plug>(KEV2filer) :call KEV2filer()<Enter>"
    execute "noremap <Plug>(KEV2exit) :call KEV2exit()<Enter>"
    :for s:inputkey in range(len(s:KEV2_inputkanas))
        execute "noremap <Plug>(KEV2imap_" . s:KEV2_inputkanas[s:inputkey] . ") :call KEV2imap(\"" . s:KEV2_inputkanas[s:inputkey] . "\")<Enter>"
        execute "noremap <Plug>(KEV2dic_" . s:KEV2_inputkanas[s:inputkey] . ") :call KEV2dic(\"" . s:KEV2_inputkanas[s:inputkey] . "\")<Enter>"
    :endfor
    execute "noremap <Plug>(KEV2kanagana0) :call KEV2kanagana(0)<Enter>"
    execute "noremap <Plug>(KEV2kanagana1) :call KEV2kanagana(1)<Enter>"
    map <silent> <Space><Space> a
    vmap <silent> <Space><Space> <Esc>
    imap <silent> <Space><Space> <Esc>
    imap <silent> <Space><S-Space> <C-V>　
    imap <silent> <S-Space><Space> <C-V><Tab>
    imap <silent> <S-Space><S-Space> <C-V><Space>
    call KEV2pushmenu()
endfunction

"鍵盤直接変更。
function! KEV2imap(KEV2_choicekana)
    let s:KEV2_choicekana = a:KEV2_choicekana
    call KEV2pullmenu(1)
    call KEV2pushmenu()
endfunction

"鍵盤静音濁音変更。
function! KEV2kanagana(KEV2_seidaku)
    let s:KEV2_choicekanaidx = index(s:KEV2_inputkanas,s:KEV2_choicekana)
    let s:KEV2_choicekana=s:KEV2_inputkanas[(a:KEV2_seidaku%2)*(s:KEV2_keyslen*2)+(s:KEV2_choicekanaidx%(s:KEV2_keyslen*2))]
    call KEV2pullmenu(1)
    call KEV2pushmenu()
endfunction

"辞書変更。
function! KEV2dic(KEV2_choicekana)
    echo a:KEV2_choicekana
    echo a:KEV2_choicekana
    echo a:KEV2_choicekana
    let s:KEV2_dickana = a:KEV2_choicekana
    call KEV2pullmenu(1)
    call KEV2pushmenu()
endfunction

"メニューなどの構築。
function! KEV2pushmenu()
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".01 " . s:KEV2_helpmenuname . ".ヘルプ(KEV2\\.txt) <Plug>(KEV2help)"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".09 " . s:KEV2_helpmenuname . ".-sep_find- :"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".80 " . s:KEV2_helpmenuname . ".履歴からファイルを開く <Plug>(KEV2filer)"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".89 " . s:KEV2_helpmenuname . ".-sep_filer- :"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".95 " . s:KEV2_helpmenuname . ".終了(「call\\ KEV2setup()」で再開) <Plug>(KEV2exit)"
    let s:KEV2_choicekanaidx = index(s:KEV2_inputkanas,s:KEV2_choicekana)
    let s:KEV2_choicedanapos = s:KEV2_keyslen*(s:KEV2_choicekanaidx/s:KEV2_keyslen)
    let s:KEV2_choicedicmenuname = escape(s:KEV2_choicekana . "{" . s:KEV2_dickana . "}",s:KEV2_menuESCs)
    :for s:inputkey in range(s:KEV2_keyslen)
        let s:kanchar = s:KEV2_kanmap[s:KEV2_choicekana][s:inputkey]
        let s:kanVchar = " <C-V>U" . printf("%08x",char2nr(s:kanchar))
        let s:menukey=s:KEV2_choicedanapos+s:inputkey
        let s:ganakey=(s:KEV2_choicedanapos/len(s:KEV2_inputkeys) ? 0 : len(s:KEV2_inputkeys))+(s:menukey%len(s:KEV2_inputkeys))
        :if s:KEV2_choicekanaidx%s:KEV2_keyslen == s:inputkey
             let s:menukey=s:KEV2_choicedanapos+( (s:KEV2_choicedanapos/s:KEV2_keyslen)%2 ? s:inputkey-s:KEV2_keyslen : s:inputkey+s:KEV2_keyslen )
        :endif
        let s:commandkana = s:KEV2_inputkanas[s:menukey]
        execute "amenu  <silent> " . (s:KEV2_menuid+0) . ".01 " . s:KEV2_choicekanamenuname . "."  . escape(s:commandkana,s:KEV2_menuESCs) . ( s:KEV2_choicekanaidx%s:KEV2_keyslen == s:inputkey ? "✓" : "" ) . " <Plug>(KEV2imap_" . s:commandkana . ")"
        execute "map <silent> <Space>" . s:KEV2_inputkeys[s:inputkey] . " <Plug>(KEV2imap_" . s:commandkana . ")a"
        execute "imap <silent> <Space>" . s:KEV2_inputkeys[s:inputkey] . " <C-o><Plug>(KEV2imap_" . s:commandkana . ")"
        execute "imenu  <silent> " . (s:KEV2_menuid+1) . ".01 " . s:KEV2_choicedicmenuname . "." . get(s:KEV2_inputESCs,s:kanchar,s:kanchar) . s:kanVchar
        execute "imap <silent> " . s:KEV2_inputkeys[s:inputkey] . s:kanVchar
        let s:inputESC = get(s:KEV2_inputESCs,s:KEV2_inputkeys[s:inputkey+s:KEV2_keyslen],s:KEV2_inputkeys[s:inputkey+s:KEV2_keyslen])
        let s:commandgana = s:KEV2_inputkanas[s:ganakey]
        execute "map <silent> <Space>" . s:inputESC . " <Plug>(KEV2imap_" . s:commandgana . ")a"
        execute "imap <silent> <Space>" . s:inputESC . " <C-o><Plug>(KEV2imap_" . s:commandgana . ")"
        execute "imap <silent> " . s:inputESC . " <C-o>/" . (s:kanchar != "|" ? escape(s:kanchar,s:KEV2_findESCs) : "<bar>") . "<Enter>"
        execute "map <silent> <S-Space>" . s:inputESC . " ?" . (s:kanchar != "|" ? escape(s:kanchar,s:KEV2_findESCs) : "<bar>") . "<Enter>"
        execute "imap <silent> <S-Space>" . s:inputESC . " <C-o>?" . (s:kanchar != "|" ? escape(s:kanchar,s:KEV2_findESCs) : "<bar>") . "<Enter>"
    :endfor
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".89 " . s:KEV2_choicekanamenuname . ".-sep_filer- :"
    :if s:KEV2_choicekanaidx < s:KEV2_keyslen*2
        execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".90 " . s:KEV2_choicekanamenuname . ".静音→濁音 <Plug>(KEV2kanagana1)"
    :else
        execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".90 " . s:KEV2_choicekanamenuname . ".濁音→静音 <Plug>(KEV2kanagana0)"
    :endif
endfunction

"メニューの撤去。
function! KEV2pullmenu(KEV2_redrawmenu)
    :if a:KEV2_redrawmenu
        execute "aunmenu  <silent> " . s:KEV2_choicekanamenuname
        execute "iunmenu  <silent> " . s:KEV2_choicedicmenuname
    :else
        :if exists("s:KEV2_choicekanamenuname")
            execute "aunmenu  <silent> " . s:KEV2_choicekanamenuname
            unlet! s:KEV2_choicekanamenuname
        :endif
        :if exists("s:KEV2_helpmenuname")
            execute "aunmenu  <silent> " . s:KEV2_choicedicmenuname
            unlet! s:KEV2_choicedicmenuname
        :endif
        :if exists("s:KEV2_helpmenuname")
            execute "aunmenu  <silent> " . s:KEV2_helpmenuname
            unlet! s:KEV2_helpmenuname
        :endif
    :endif
endfunction

"ヘルプファイル「KEV.txt」読込。
function! KEV2help()
    let s:KEV2_helpfilepath = s:kev_scriptdir . "/KEV2.txt"
    :if filereadable(s:KEV2_helpfilepath)
        execute "enew"
        execute "e " . s:KEV2_helpfilepath . " | :se ro"
    :endif
endfunction

"「KEV2」の撤去(helpコマンド類は残す)。
function! KEV2exit()
    call KEV2pullmenu(0)
    vunmap <silent> <Space><Space>
    unmap <silent> <Space><Space>
    iunmap <silent> <Space><Space>
    iunmap <silent> <Space><S-Space>
    iunmap <silent> <S-Space><Space>
    iunmap <silent> <S-Space><S-Space>
    :for s:inputkey in range(s:KEV2_keyslen)
        execute "unmap <silent> <Space>" . s:KEV2_inputkeys[s:inputkey]
        execute "iunmap <silent> <Space>" . s:KEV2_inputkeys[s:inputkey]
        execute "iunmap <silent> " . s:KEV2_inputkeys[s:inputkey]
        let s:inputESC = get(s:KEV2_inputESCs,s:KEV2_inputkeys[s:inputkey+s:KEV2_keyslen],s:KEV2_inputkeys[s:inputkey+s:KEV2_keyslen])
        execute "iunmap <silent> " . s:inputESC
        execute "unmap <silent> <Space>" . s:inputESC
        execute "iunmap <silent> <Space>" . s:inputESC
        execute "unmap <silent> <S-Space>" . s:inputESC
        execute "iunmap <silent> <S-Space>" . s:inputESC
    :endfor
endfunction

"履歴などからファイルを開く簡易ファイラー。
function! KEV2filer()
    cd $HOME
    let s:dirline = expand('%:p:h')
    execute "cd " . s:dirline
    let s:filelines = ["",s:dirline] + v:oldfiles
    let s:filelabels = ["ファイル履歴(01でフォルダ選択)※履歴はウィンドウの高さに合わせます。"]
    :for s:labelno in range(1,len(s:filelines)-2)
         let s:filelabels = s:filelabels + [ printf("%02d",s:labelno) . ":" . s:filelines[s:labelno] ]
    :endfor
    let s:filechoice = inputlist(s:filelabels[:max([1,min([&lines-2,len(s:filelabels)])])])
    :while 0 < s:filechoice && s:filechoice < len(s:filelines)
        echo "\n"
        :if isdirectory(s:filelines[s:filechoice])
            execute "cd " . s:filelines[s:filechoice]
            let s:dirline = getcwd()
        :elseif filereadable(s:filelines[s:filechoice])
            execute "enew"
            execute "e " . s:filelines[s:filechoice]
            :break
        :else
            echo "リーダブルではないファイルです「" . s:filelines[s:filechoice] . "」"
        :endif
        let s:filelines = ["",".."] + split(expand("./*"),"\n")
        let s:filelabels = ["「" . s:dirline . "」(01で親フォルダ選択)※ファイルクリックはズレるので注意。"]
        :for s:labelno in range(1,len(s:filelines)-1)
             let s:filelabels = s:filelabels + [ printf("%02d",s:labelno) . ":" . s:filelines[s:labelno] ]
        :endfor
        let s:filechoice = inputlist(s:filelabels)
    :endwhile
endfunction


call KEV2setup()
finish

"# Copyright (c) 2016-2017 ooblog
"# License: MIT
"# https://github.com/ooblog/TSF2KEV/blob/master/LICENSE
