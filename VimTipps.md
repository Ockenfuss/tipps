# Various Tipps for vim

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Various Tipps for vim](#various-tipps-for-vim)
  - [Navigation](#navigation)
  - [Editing](#editing)
  - [Visual mode](#visual-mode)
    - [Text Objects](#text-objects)
  - [Searching](#searching)
  - [Copy-Paste](#copy-paste)
  - [Commands](#commands)
  - [Marks](#marks)
- [Pure vi](#pure-vi)

<!-- /code_chunk_output -->


Setting up neovim (nvim):

Install plug.vim, a package manager which allows for plugin installation from inside your vimrc:
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim

Create if not existing the file:
~/.config/nvim/init.vim
Add in this file:
set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath=&runtimepath
source ~/.vimrc
Then execute in nvim:
:PlugInstall

## Navigation
```
hjkl #Move around
$ #Line ending
^ #Start of line
fy #go to next y
```
## Editing
```
i #Insert
a #Insert after cursor
o #Insert new line
O #Insert new line above
d + <move> #delete
3dd #delete 3 lines
```

## Visual mode
```
v #start visual mode
^v #start block visual mode. Useful for block comments
<shift>i #start insert for block
... #write
ESC #changes are applied to complete block
```

### Text Objects
General structure of commands in vim: `<number><command><motion or text object>`. Motions act from the cursor position, text objects act regardless of the cursor position. An `a` generally includes the surrounding delimiter, an `i` does not.
```
daw #delete word including spaces
diw #delete word without surrounding spaces
ci" #change everything within ""
yi} #yank everything within {}
da], di) #same for (), []
```


## Searching
```
/word #search for word
n #next occurence
1,$/search/replace/<g,i> #search and replace from first to last line. g: global, all occurences per line. i: case insensitive
```

## Copy-Paste
```
y #Yank (Copy)
p #Put (Paste)
yy #Yank line
```

## Commands
```
. #Repeat command
q #Start recording
```

## Marks
```
ma #set mark 'a'
'a #go to mark 'a'
d'a #delete until mark 'a'
```

# Pure vi
```
:set nu #add line numbering
:syntax on #syntax highlighting
```

