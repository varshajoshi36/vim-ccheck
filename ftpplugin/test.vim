"! ./world.sh
function! g:test#startChecker()
	imap <CR> :call G()

	let $VIMARGS='--servername ABC'
	echo $VIMARGS
endfunction

function! G()
          let result=getline(1,"$")
	  echo 'hopefully'
	  echo result	  
	  !vim $VIMARGS --remote-expr "g:a\#readF(result)"
endfunction




