function! a#Hi(command)
	"echom 'hello'
	"return 'hello'
	"return '3'
	"i"
	"return a:text
	"return '3'
	 "redir =>outpuit
	 
	" redir >> t.txt
	 	"silent exe a:command
	 
	 "redir END
         "return output	 
	 redir => output
             silent exe a:command
         redir END

         return output	
		
endfunction
"call a#Hi('echo "nehal"')
"call a#Hi('echo "cmps"')

function! g:a#Hello(text)

	"echo a:text
	"echo 
	 "echo text[0:2]
	 echo a:text
	 "echo @% 

endfunction	

"call g:a#Hello('hip')

function! g:a#readF()
	redir! temp1.txt
	
		let l=readfile("temp.txt")
	      "execute 'silent edit ' . a:text	
	     "let temp1 = split(l, ",")  
	      	"for elem in l
			"let temp1 = split(elem, ",")
		"echo temp1
	      	"endfor
	      "let l=getbufline(a:text,1,"$")
		echo l
		"writefile("temp.txt","temp1.txt")
	redir END
	"return output
endfunction

