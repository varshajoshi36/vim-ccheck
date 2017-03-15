#! /usr/bin/python
import vim
import string

def test():
    #print vim.current.buffer[-1]
    html = string.join(vim.current.buffer, "\n")
    #print "html", html
    print "****"

test()
