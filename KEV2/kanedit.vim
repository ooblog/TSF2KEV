set encoding=utf-8
scriptencoding utf-8
let s:kev_scriptdir = expand('<sfile>:p:h')

"「KanEditVim2」の初期化。
function! KEV2setup()
    call KEV2pullmenu(1)
    let s:KEV2_menuid = 10000
    let s:KEV2_menumap = "「鍵盤"
    let s:KEV2_menudic = "文字"
    let s:KEV2_menuhelp = "KEV2」"
    let s:KEV2_inputkeys = ['1','2','3','4','5','6','7','8','9','0','-','^', 'q','w','e','r','t','y','u','i','o','p','@','[', 'a','s','d','f','g','h','j','k','l',';',':',']', 'z','x','c','v','b','n','m',',','.','/','\']
    let s:KEV2_inputkeys += ['!','"','#','$','%','&',"'",'(',')','~','=','|', 'Q','W','E','R','T','Y','U','I','O','P','`','{', 'A','S','D','F','G','H','J','K','L','+','*','}', 'Z','X','C','V','B','N','M','<','>','?','_']
    let s:KEV2_inputkeyslen = len(s:KEV2_inputkeys)
    let s:KEV2_keyslen = len(s:KEV2_inputkeys)/2
    let s:KEV2_commandkanas = ["ぬ","ふ","あ","う","え","お","や","ゆ","よ","わ","ほ","へ", "た","て","い","す","か","ん","な","に","ら","せ","゛","゜", "ち","と","し","は","き","く","ま","の","り","れ","け","む", "つ","さ","そ","ひ","こ","み","も","ね","る","め","ろ"]
    let s:KEV2_commandkanas += ["ヌ","フ","ア","ウ","エ","オ","ヤ","ユ","ヨ","ワ","ホ","ヘ","タ","テ","イ","ス","カ","ン","ナ","ニ","ラ","セ","ヶ","ヵ","チ","ト","シ","ハ","キ","ク","マ","ノ","リ","レ","ケ","ム","ツ","サ","ソ","ヒ","コ","ミ","モ","ネ","ル","メ","ロ"]
    let s:KEV2_commandkanas += ["ゔ","ぶ","ぁ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ","を","ぼ","べ","だ","で","ぃ","ず","が","っ","ゑ","ゐ","ゎ","ぜ","ゞ","ゝ","ぢ","ど","じ","ば","ぎ","ぐ","ぱ","…","「","」","げ","ぷ","づ","ざ","ぞ","び","ご","ぴ","ぽ","、","。","ぺ","〜"]
    let s:KEV2_commandkanas += ["ヴ","ブ","ァ","ゥ","ェ","ォ","ャ","ュ","ョ","ヲ","ボ","ベ","ダ","デ","ィ","ズ","ガ","ッ","ヱ","ヰ","ヮ","ゼ","ヾ","ヽ","ヂ","ド","ジ","バ","ギ","グ","パ","・","『","』","ゲ","ぷ","ヅ","ザ","ゾ","ビ","ゴ","ピ","ポ","，","．","ペ","ー"]
    let s:KEV2_mapkanas = ["1(ぬ)","2(ふ)","3(あ)","4(う)","5(え)","6(お)","7(や)","8(ゆ)","9(よ)","0(わ)","-(ほ)","^(へ)","q(た)","w(て)","e(い)","r(す)","t(か)","y(ん)","u(な)","i(に)","o(ら)","p(せ)","@(゛)","[(゜)","a(ち)","s(と)","d(し)","f(は)","g(き)","h(く)","j(ま)","k(の)","l(り)",";(れ)",":(け)","](む)","z(つ)","x(さ)","c(そ)","v(ひ)","b(こ)","n(み)","m(も)",",(ね)",".(る)","/(め)","_(ろ)"]
    let s:KEV2_mapkanas += ["1(ヌ)","2(フ)","3(ア)","4(ウ)","5(エ)","6(オ)","7(ヤ)","8(ユ)","9(ヨ)","0(ワ)","-(ホ)","^(ヘ)","q(タ)","w(テ)","e(イ)","r(ス)","t(カ)","y(ン)","u(ナ)","i(ニ)","o(ラ)","p(セ)","@(ヶ)","[(ヵ)","a(チ)","s(ト)","d(シ)","f(ハ)","g(キ)","h(ク)","j(マ)","k(ノ)","l(リ)",";(レ)",":(ケ)","](ム)","z(ツ)","x(サ)","c(ソ)","v(ヒ)","b(コ)","n(ミ)","m(モ)",",(ネ)",".(ル)","/(メ)","_(ロ)"]
    let s:KEV2_mapkanas += ["1(ゔ)","2(ぶ)","3(ぁ)","4(ぅ)","5(ぇ)","6(ぉ)","7(ゃ)","8(ゅ)","9(ょ)","0(を)","-(ぼ)","^(べ)","q(だ)","w(で)","e(ぃ)","r(ず)","t(が)","y(っ)","u(ゑ)","i(ゐ)","o(ゎ)","p(ぜ)","@(ゞ)","[(ゝ)","a(ぢ)","s(ど)","d(じ)","f(ば)","g(ぎ)","h(ぐ)","j(ぱ)","k(…)","l(「)",";(」)",":(げ)","](ぷ)","z(づ)","x(ざ)","c(ぞ)","v(び)","b(ご)","n(ぴ)","m(ぽ)",",(、)",".(。)","/(ぺ)","_(〜)"]
    let s:KEV2_mapkanas += ["1(ヴ)","2(ブ)","3(ァ)","4(ゥ)","5(ェ)","6(ォ)","7(ャ)","8(ュ)","9(ョ)","0(ヲ)","-(ボ)","^(ベ)","q(ダ)","w(デ)","e(ィ)","r(ズ)","t(ガ)","y(ッ)","u(ヱ)","i(ヰ)","o(ヮ)","p(ゼ)","@(ヾ)","[(ヽ)","a(ヂ)","s(ド)","d(ジ)","f(パ)","g(ギ)","h(グ)","j(パ)","k(・)","l(『)",";(』)",":(ゲ)","](プ)","z(ヅ)","x(ザ)","c(ゾ)","v(ビ)","b(ゴ)","n(ピ)","m(ポ)",",(，)",".(．)","/(ペ)","_(ー)"]
    let s:KEV2_mapkanaslen = len(s:KEV2_mapkanas)
    let s:KEV2_inputESCs = {"\t":"<Tab>",' ':"<Space>",'<':"<lt>",'\':"<Bslash>",'|':"<Bar>",'-':"<Minus>",'.':"<Point>"}
    let s:KEV2_menuESCs = "\t\\:|< >.-"
    let s:KEV2_findESCs = ".*[]^%/\?~$"
    let s:KEV2_mapkana = "@(゛)"
    let s:KEV2_dickana = "　"
    let s:KEV2_kanmap = {}
        :for s:mapkana in s:KEV2_mapkanas
            let s:KEV2_kanmap[s:mapkana]=(index(s:KEV2_mapkanas,s:mapkana)%2?s:KEV2_inputkeys[(s:KEV2_keyslen):]:s:KEV2_inputkeys[:(s:KEV2_keyslen-1)])
        :endfor
        let s:KEV2_kanmap["1(ぬ)"] = s:KEV2_commandkanas[(s:KEV2_keyslen*0):(s:KEV2_keyslen*1-1)]
        let s:KEV2_kanmap["1(ヌ)"] = s:KEV2_commandkanas[(s:KEV2_keyslen*1):(s:KEV2_keyslen*2-1)]
        let s:KEV2_kanmap["[(゜)"] = s:KEV2_commandkanas[(s:KEV2_keyslen*2):(s:KEV2_keyslen*3-1)]
        let s:KEV2_kanmap["[(ヵ)"] = s:KEV2_commandkanas[(s:KEV2_keyslen*3):(s:KEV2_keyslen*4-1)]
        let s:KEV2_kanmap["1(ゔ)"] = s:KEV2_commandkanas[(s:KEV2_keyslen*2):(s:KEV2_keyslen*3-1)]
        let s:KEV2_kanmap["1(ヴ)"] = s:KEV2_commandkanas[(s:KEV2_keyslen*0):(s:KEV2_keyslen*1-1)]
        let s:KEV2_kanmap["[(ヽ)"] = s:KEV2_commandkanas[(s:KEV2_keyslen*3):(s:KEV2_keyslen*4-1)]
        let s:KEV2_kanmap["[(ゝ)"] = s:KEV2_commandkanas[(s:KEV2_keyslen*1):(s:KEV2_keyslen*2-1)]
        :for s:widekey in range(s:KEV2_keyslen)
            let s:KEV2_kanmap["@(ヾ)"][s:widekey] = nr2char(char2nr(s:KEV2_kanmap["@(ヾ)"][s:widekey])+0xfee0)
            let s:KEV2_kanmap["@(ゞ)"][s:widekey] = nr2char(char2nr(s:KEV2_kanmap["@(ゞ)"][s:widekey])+0xfee0)
        :endfor
    let s:KEV2_kanmapfilepath = s:kev_scriptdir . "/kanmap.tsf"
    :if filereadable(s:KEV2_kanmapfilepath)
        :for s:kanmapfileline in readfile(s:KEV2_kanmapfilepath)
            let s:kanmaplinelist = split(s:kanmapfileline,"\t")
            :if len(s:kanmaplinelist) >= 2
                let s:KEV2_kanmap[s:kanmaplinelist[0]] = s:kanmaplinelist[1:]
                :if len(s:kanmaplinelist) < s:KEV2_keyslen
                    let s:KEV2_kanmap[s:kanmaplinelist[0]] += s:KEV2_inputkeys[(s:KEV2_keyslen-len(s:kanmaplinelist)):(s:KEV2_keyslen-1)]
                :endif
            :endif
        :endfor
    :endif
    execute "noremap <Plug>(KEV2setup) :call KEV2setup()<Enter>"
    execute "noremap <Plug>(KEV2help) :call KEV2help()<Enter>"
    execute "noremap <Plug>(KEV2filer) :call KEV2filer()<Enter>"
    execute "noremap <Plug>(KEV2exit) :call KEV2exit()<Enter>"
    execute "noremap <Plug>(KEV2kanagana0) :call KEV2kanagana(0)<Enter>"
    execute "noremap <Plug>(KEV2kanagana1) :call KEV2kanagana(1)<Enter>"
    :for s:commandkana in s:KEV2_commandkanas
        execute "noremap <Plug>(KEV2map_" . s:commandkana . ") :call KEV2map(\"" . s:commandkana . "\")<Enter>"
        execute "noremap <Plug>(KEV2dic_" . s:commandkana . ") :call KEV2dic(\"" . s:commandkana . "\")<Enter>"
    :endfor
    execute "noremap <Plug>(KEV2dic_　) :call KEV2dic(\"　\")<Enter>"
    map <silent> <Space><Space> a
    vmap <silent> <Space><Space> <Esc>
    imap <silent> <Space><Space> <Esc>
    imap <silent> <Space><S-Space> <C-V>　
    imap <silent> <S-Space><Space> <C-V><Tab>
    imap <silent> <S-Space><S-Space> <C-V><Space>
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".01 " . s:KEV2_menuhelp . ".ヘルプ(KEV2\\.txt) <Plug>(KEV2help)"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".09 " . s:KEV2_menuhelp . ".-sep_find- :"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".80 " . s:KEV2_menuhelp . ".履歴からファイルを開く <Plug>(KEV2filer)"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".89 " . s:KEV2_menuhelp . ".-sep_filer- :"
    execute "amenu  <silent> " . (s:KEV2_menuid+2) . ".95 " . s:KEV2_menuhelp . ".終了(「call\\ KEV2setup()」で再開) <Plug>(KEV2exit)"
    call KEV2pushmenu()
endfunction

"鍵盤変更。
function! KEV2map(KEV2_commandkana)
    let s:KEV2_mapkana = s:KEV2_mapkanas[index(s:KEV2_commandkanas,a:KEV2_commandkana)]
    call KEV2pullmenu(0)
    call KEV2pushmenu()
endfunction

"鍵盤静音濁音変更。
function! KEV2kanagana(KEV2_seidaku)
    let s:mapkanasidx = index(s:KEV2_mapkanas,s:KEV2_mapkana)
    let s:KEV2_mapkana=s:KEV2_mapkanas[(a:KEV2_seidaku%2)*(s:KEV2_keyslen*2)+(s:mapkanasidx%(s:KEV2_keyslen*2))]
    call KEV2pullmenu(0)
    call KEV2pushmenu()
endfunction

"辞書変更。
function! KEV2dic(KEV2_commandkana)
    :if count(s:KEV2_commandkanas,a:KEV2_commandkana)
        let s:KEV2_dickana = s:KEV2_kanmap[s:KEV2_mapkana][index(s:KEV2_commandkanas,a:KEV2_commandkana)%s:KEV2_keyslen]
    :else
        let s:KEV2_dickana = "　"
    :endif
    call KEV2pullmenu(0)
    call KEV2pushmenu()
endfunction

"メニューなどの構築。
function! KEV2pushmenu()
    let s:KEV2_menumap = escape("「" . s:KEV2_mapkana,s:KEV2_menuESCs)
    let s:KEV2_menudic = escape("『" . s:KEV2_dickana . "』",s:KEV2_menuESCs)
    let s:mapkanasidx = index(s:KEV2_mapkanas,s:KEV2_mapkana)
    let s:mapkanaspos = s:KEV2_keyslen*(s:mapkanasidx/s:KEV2_keyslen)
    let s:mapkanaskata = (s:mapkanasidx/s:KEV2_keyslen)%2
    let s:mapkanasdaku = s:mapkanasidx/s:KEV2_inputkeyslen
    :for s:inputkey in range(s:KEV2_keyslen)
        :if s:mapkanasidx%s:KEV2_keyslen == s:inputkey
            let s:mapchar = s:KEV2_commandkanas[s:mapkanaspos+( (s:mapkanaspos/s:KEV2_keyslen)%2 ? s:inputkey-s:KEV2_keyslen : s:inputkey+s:KEV2_keyslen )]
        :else
            let s:mapchar = s:KEV2_commandkanas[s:mapkanaspos+s:inputkey]
        :endif
        let s:dicchar = s:KEV2_kanmap[s:KEV2_mapkana][s:inputkey]
        let s:mapDchar = s:KEV2_commandkanas[s:mapkanaspos+s:inputkey]
        let s:mapGchar = s:KEV2_commandkanas[(s:mapkanasdaku ? 0: s:KEV2_inputkeyslen)+s:mapkanaskata*s:KEV2_keyslen+s:inputkey]
        let s:mapMchar = escape(s:KEV2_mapkanas[index(s:KEV2_commandkanas,s:mapchar)],s:KEV2_menuESCs)
        let s:dicVchar = " <C-V>U" . printf("%08x",char2nr(s:dicchar))
        let s:dicMchar = (s:dicchar != "|" ? (s:dicchar != "-" ? escape(s:dicchar,s:KEV2_menuESCs) : "<Minus>") : "<bar>")
        let s:inputESC = get(s:KEV2_inputESCs,s:KEV2_inputkeys[s:inputkey+s:KEV2_keyslen],s:KEV2_inputkeys[s:inputkey+s:KEV2_keyslen])
        let s:inputFIND = (s:dicchar != "|" ? escape(s:dicchar,s:KEV2_findESCs) : "<bar>") . "<Enter>"
        execute "amenu  <silent> " . (s:KEV2_menuid+0) . "." . (s:inputkey+1) . " " . s:KEV2_menumap . "." . s:mapMchar . ( s:mapkanasidx%s:KEV2_keyslen == s:inputkey ? "✓" : "" ) . " <Plug>(KEV2map_" . s:mapchar . ")a"
        execute "map <silent> <Space>" . s:KEV2_inputkeys[s:inputkey] . " <Plug>(KEV2map_" . s:mapchar . ")a"
        execute "imap <silent> <Space>" . s:KEV2_inputkeys[s:inputkey] . " <C-o><Plug>(KEV2map_" . s:mapchar . ")"
        execute "map <silent> <Space>" . s:inputESC . " <Plug>(KEV2map_" . s:mapGchar . ")a"
        execute "imap <silent> <Space>" . s:inputESC . " <C-o><Plug>(KEV2map_" . s:mapGchar . ")"
        execute "imenu  <silent> " . (s:KEV2_menuid+1) . "." . (s:inputkey+1) . " " . s:KEV2_menudic . "." . s:dicMchar . s:dicVchar
        execute "imap <silent> " . s:KEV2_inputkeys[s:inputkey] . s:dicVchar
        execute "imap <silent> " . s:inputESC . " <C-o>/" . s:inputFIND
        execute "map <silent> <S-Space>" . s:inputESC . " ?" . s:inputFIND . "a"
        execute "imap <silent> <S-Space>" . s:inputESC . " <C-o>?" . s:inputFIND
        execute "map <silent> <S-Space>" . s:KEV2_inputkeys[s:inputkey] . " <Plug>(KEV2dic_" . s:mapDchar . ")a"
        execute "imap <silent> <S-Space>" . s:KEV2_inputkeys[s:inputkey] . " <C-o><Plug>(KEV2dic_" . s:mapDchar . ")"
    :endfor
    execute "menu  <silent> " . (s:KEV2_menuid+0) . ".89 " . s:KEV2_menumap . ".-sep_kanagana- :"
    :if s:mapkanasidx < s:KEV2_inputkeyslen
        execute "amenu  <silent> " . (s:KEV2_menuid+0) . ".90 " . s:KEV2_menumap . ".静音→濁音 <Plug>(KEV2kanagana1)"
    :else
        execute "amenu  <silent> " . (s:KEV2_menuid+0) . ".90 " . s:KEV2_menumap . ".濁音→静音 <Plug>(KEV2kanagana0)"
    :endif
    execute "imenu  <silent> " . (s:KEV2_menuid+1) . ".89 " . s:KEV2_menudic . ".-sep_dic- :"
    execute "imenu  <silent> " . (s:KEV2_menuid+1) . ".90 " . s:KEV2_menudic . ".辞書を入力" . s:KEV2_menudic . " <C-V>U" . printf("%08x",char2nr(s:KEV2_dickana))
    execute "imenu  <silent> " . (s:KEV2_menuid+1) . ".95 " . s:KEV2_menudic . ".辞書を空白『　』 <C-o><Plug>(KEV2dic_　)"
endfunction

"メニューの撤去。
function! KEV2pullmenu(KEV2_exit)
    :if !a:KEV2_exit
        execute "aunmenu  <silent> " . s:KEV2_menumap
        execute "iunmenu  <silent> " . s:KEV2_menudic
    :else
        :if exists("s:KEV2_menumap")
            execute "aunmenu  <silent> " . s:KEV2_menumap
            unlet! s:KEV2_menumap
        :endif
        :if exists("s:KEV2_menudic")
            execute "iunmenu  <silent> " . s:KEV2_menudic
            unlet! s:KEV2_menudic
        :endif
        :if exists("s:KEV2_menuhelp")
            execute "aunmenu  <silent> " . s:KEV2_menuhelp
            unlet! s:KEV2_menuhelp
        :endif
    :endif
endfunction

"「KEV2」の撤去(helpコマンド類は残す)。
function! KEV2exit()
    call KEV2pullmenu(1)
    vunmap <silent> <Space><Space>
    unmap <silent> <Space><Space>
    iunmap <silent> <Space><Space>
    iunmap <silent> <Space><S-Space>
    iunmap <silent> <S-Space><Space>
    iunmap <silent> <S-Space><S-Space>
    :for s:inputkey in range(s:KEV2_keyslen)
        let s:inputESC = get(s:KEV2_inputESCs,s:KEV2_inputkeys[s:inputkey+s:KEV2_keyslen],s:KEV2_inputkeys[s:inputkey+s:KEV2_keyslen])
        execute "unmap <silent> <Space>" . s:KEV2_inputkeys[s:inputkey]
        execute "iunmap <silent> <Space>" . s:KEV2_inputkeys[s:inputkey]
        execute "unmap <silent> <Space>" . s:inputESC
        execute "iunmap <silent> <Space>" . s:inputESC
        execute "iunmap <silent> " . s:KEV2_inputkeys[s:inputkey]
        execute "iunmap <silent> " . s:inputESC
        execute "unmap <silent> <S-Space>" . s:inputESC
        execute "iunmap <silent> <S-Space>" . s:inputESC
    :endfor
endfunction

"ヘルプファイル「KEV.txt」読込。
function! KEV2help()
    let s:KEV2_helpfilepath = s:kev_scriptdir . "/KEV2.txt"
    :if filereadable(s:KEV2_helpfilepath)
        execute "enew"
        execute "e " . s:KEV2_helpfilepath . " | :se ro"
    :endif
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
