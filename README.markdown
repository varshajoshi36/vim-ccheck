# Ccheck vim plugin

Ccheck is a simpe vim plugin which helps you detect syntatctic errors in your C
code in vim itself. 

## Instalation

If you don't have a preferred installation method, we recommend installing
[pathogen.vim](https://github.com/tpope/vim-pathogen), and then simply copy and
paste:

    cd ~/.vim/bundle 
    git clone https://github.com/varshajoshi36/vim-ccheck.git


## Usage

As the plugin is intended to be used with c code, it can be invoked only in .c
files. To invoke the Ccheck plugin, in your Normal mode of vim, run following
command:

:Ccheck

The plugin will read the code in the current vim file and will point out errors
if any.
