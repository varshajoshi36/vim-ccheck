
function! g:c#startChecker()
       inoremap <CR> <esc> :call G()
       "! ./world.sh
	let $VIMARGS='--servername ABC'
        echo $VIMARGS
endfunction
call g:c#startChecker()

function! ReadF()

        let l=readfile("temp.txt")
              "execute 'silent edit ' . a:text
             "let temp1 = split(l, ",")
                "for elem in l
                        "let temp1 = split(elem, ",")
                "echo temp1
                "endfor
              "let l=getbufline(a:text,1,"$")
        echo l
endfunction

function! G()
        "!cat &varn >temp.txt
        "echo 'in here'
        "let g:filePath="/home/training/.vim/autoload/temp.txt"
        ":execute "0read " . fnameescape(g:filePath)
        "let lines=getline(1,"$")
        "echo lines
        "nnoremap o :!vim $VIMARGS --remote temp.txt
        "vim --servername ABC --remote-expr "a#Hello(0read)"
         "exe "!start cmd /c "
          let currbuff = bufnr(bufname("%"))
          echo 'buffer'
          echo currbuff
          let edited=currbuff.".vim"
          echo edited
          echo 'end'
          let result=getbufline(1,"$")
          echo 'hopefully'
          echo result
	  let result1=['1','2']
	  call writefile(result,"temp.txt")
         !vim $VIMARGS --remote-expr "g:a\#readF()"
endfunction

