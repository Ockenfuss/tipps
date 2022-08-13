# Various Tipps for vim

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Various Tipps for vim](#various-tipps-for-vim)
  - [Navigation](#navigation)
  - [Editing](#editing)
  - [Visual mode](#visual-mode)
    - [Block visual mode](#block-visual-mode)
    - [Text Objects](#text-objects)
  - [Searching](#searching)
  - [Copy-Paste](#copy-paste)
    - [Registers](#registers)
  - [Commands](#commands)
  - [Marks](#marks)
- [Neovim and Plugins](#neovim-and-plugins)
  - [Nerdtree](#nerdtree)
  - [Easymotion](#easymotion)
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
CTRL+O, CTRL+I #go to last or next cursor position
'' or `` #similarly, go to last or next cursor position
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
^v #visual mode for full lines. Useful for block comments
<shift>i #start insert for block
... #write
ESC #changes are applied to complete block
o #while in visual mode, 'o' moves the cursor to the start/end of the selected block
p #while in visual mode, 'p' replaced the selected text with the yanked text
~ #while in visual mode, '~' will swap all casing in the selected block
```

### Block visual mode
```
CTRL+V #start block visual mode
I #insert in front of block.
A #insert at the end of the block
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
s,abc,def,g #The character that follows 's' is the delimiter character
```

## Copy-Paste
```
y #Yank (Copy)
p #Put (Paste)
yy #Yank line
```

### Registers
```
: reg #See the content of all registers
"ayy #yank content of current line in register a
"bP #Paste content of register b above current line
"cc3w #Change three words, putting the previous content in register c
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

# Neovim and Plugins
## Nerdtree

## Easymotion
This plugin is contained automatically in vim for vscode.
```
<leader><leader>+f+character #highlight this character to jump to it.
```

## Surround
This plugin is contained automatically in vim for vscode.
```
d s <existing> #delete surrounding
c s <existing> <desired> #replace surrounding
S <desired> #surround selection in visual mode
```

# Pure vi
```
:set nu #add line numbering
:syntax on #syntax highlighting
```

