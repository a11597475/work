
C:\Users\Administrator\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu22.04LTS_79rhkp1fndgsc\LocalState\rootfs\home\min


C:\Users\Administrator\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu22.04LTS_79rhkp1fndgsc\LocalState\rootfs
# work
"imap ( ()<ESC>i  
"inoremap [ []<ESC>i  
"inoremap { {<CR>}<ESC>i 
"inoremap < <><ESC>i  
"inoremap ' ''<ESC>i  
"inoremap " ""i 
inoremap ( ()<ESC>i
inoremap [ []<ESC>i
inoremap { {<CR>}<ESC>kA<CR>
inoremap < <><ESC>i
inoremap ' ''<ESC>i
inoremap " ""<ESC>i
set nu
set tabstop=4
set ruler
set ai
set autoindent
set hlsearch
set scroll=10
set mouse=c
syntax on
hi Search term=standout cterm=bold ctermfg=7 ctermbg=1
"hi Search term=standout ctermfg=1
set clipboard^=unnamed,unnamedplus
set foldmethod=syntax

" ==============================================
"  General settings
" ==============================================
set nocp
set ru
"  使用cindent
set cin
set cino = :0g0t0(sus
set sm
set ai
"  缩近
set sw=4
set ts=4
"  不展开tab为空格，反之set et
set noet
set lbr
set hls
"set backspace = indent , eol , start
set whichwrap = b , s , < , > , [ , ]
set fo+ = mB
set selectmode =
set mousemodel = popup
set keymodel =
set selection = inclusive



set matchpairs+ = <:>
