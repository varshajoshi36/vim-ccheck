execute pathogen#infect()
set nocompatible

filetype plugin on
filetype indent on
syntax on
"map <5> :echo 'Current time is ' . strftime('%c')<CR>
	"execute pathogen#interpose('autoload/test.vim')
"au FileType c setl sw=2 sts=2 et
"autocmd BufRead,BufNewFile   *.c,*.h,*.java set noic cin noexpandtab
"autocmd BufRead,BufNewFile   *.pl syntax on
"autocmd filetype python execute pathogen#infect()
filetype plugin indent on
syntax on

"set nocompatible
"execute pathogen#infect()    " breaks filetype detection
"call pathogen#runtime_append_all_bundles()

"filetype plugin indent on
"syntax on
