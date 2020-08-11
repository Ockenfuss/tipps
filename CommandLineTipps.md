<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [General](#general)
  - [Execution](#execution)
  - [Variables](#variables)
    - [Definition](#definition)
    - [Environment variables](#environment-variables)
  - [Program logic](#program-logic)
  - [PATH](#path)
  - [Pipes and redirection](#pipes-and-redirection)
  - [Subshells](#subshells)
  - [Displaying text](#displaying-text)
  - [Searching](#searching)
  - [xargs](#xargs)
  - [Background jobs](#background-jobs)
  - [User managment](#user-managment)
- [Tmux](#tmux)

<!-- /code_chunk_output -->

# General
## Execution
```bash
./Test #Execute a binary
./Test.sh #Execute a shell script in a subshell
source ./Test.sh #Execute a script in this shell
. ./Test.sh #'.' is short for source
```
## Variables
### Definition
```bash
test=hallo #local variable. No spaces around =!
a=1
b=1
c=$(($a+$b))#$((...)) provides an arithmetic environment. Inside, expressions are evaluated in c style
test=$(ls) #store function output in variable !there are no spaces allowed around the "="!
test="$variable"variable2 #Insert the variable expression and directly add variable2
export test #export local var to global environment such that it is available in subshells
unset test #undefine a variable
```
### Environment variables
```bash
PS1; PS2 #the format of the bash prompt 1 and 2 (latter e.g. for multiline constructs)
```
## Program logic
```bash
if [[ $A -eq $B ]] #Actually, [[ is a small bash programm that evaluates the given expression
then
    ...
fi

for (( run=$STARTNUM; run<=$ENDNUM; run++ )); do
...
done
```

## PATH
not in .zshrc or similar, because these will be synchronized between computers via my git repo!
in ~/.profile (works only for bash login shells): 
`PATH="$HOME/bin:$HOME/.local/bin:$PATH"`
Alternative: create link in /usr/local/bin (not in /usr/bin, this is managed by the package manager)
## Pipes and redirection
```bash
Befehl1 | Befehl2 #Pipes: send stdout of the left command to stdin of the right command
#Remind: stderr is not sent to the right!
cmd> NewFile #Redirection: Redirect all the output from one command to a (new) file. Its content will be overwritten!
cmd>> File #Redirection with appending the new content
cmd>&1 #Redirect output to stdout. "0" is stdin, "1" is stdout, "2" is stderr
2>&1 #Redirect only errors to stdout
/dev/null #Black hole: Swallows all input redirected to it
```
## Subshells
```bash
(sleep 2; echo "hallo") #created by ()
(echo $BASH_SUBSHELL)& #can be sent to background
coproc sleep 10 #start command in background. Allows for communication.
```
## Displaying text
```bash
cat file #Concatenate concent of files and print to stdout. Often used to just print one file
more file #Display sequentially.
less file #Similar to more. Interactive view.
```
## Searching
```bash
grep -rni --include \*.py 'word' ./ #: For searches within files. -r: recursive -n: line number -i: ignore case --include: search only within if GLOB matches
find #: for searching a file/folder
```

## xargs
Usefull to feed stdout from one command as arguments to another command
```bash
command1 | xargs -p -i command2 -flag1 {} -flag2 #execute command2 with each output line from command1. With -i, "{}" is replaced by the output from command1. With -p, you get asked before execution.
```

## Background jobs
```bash
Ctrl-Z: Pause job
bg #Continue job in background
fg #bring job to foreground
jobs #list jobs
kill %1 # '1' is the Job ID you get by calling jobs: "[1] + Running ..."
```

## User managment
Users are listed in /etc/passwd file.
```bash
useradd -m test #Add user account. -m: with home directory containing files from /etc/skel
useradd -D #show defaults
userdel test #Remove entry from /etc/passwd
usermod #modify account in general
passwd #change password
```
Groups are in /etc/group
```bash
groupadd test #create a group
usermod -G test username #add user to group
```
Translate Permissions: r-x=>binary 101=>octal value 5; for user,group,other:e.g. 775
New files: subtract from default (666 for files, 777 for directories) the umask value (e.g. 002)
```bash
umask #list or set default with a umask
chmod u=rwx #set user (g group, o other) to rwx (+ add perm., - subtr. perm)
chown username file #change the owner of a file
```
SUID, SGID, sticky bit: three additional bits for every directory and file. Set default group for dir. and executing permissions for files. Can be used to create a shared directory for a group.

# Tmux
Terminal multiplexer. Allows to keep your session alive after remote logout.
Generally, most funcionality is availabel after you press your tmux leader key like <C-a>.
```shell
tmux ls #List active sessions
tmux a -t main #Attach to session main
tmux new -s SessionName #Create new session
<Leader> d #Detach from session
<Leader> : #start mode to enter commands (like in vim)
<Leader> : kill-session #close all panes and quit session
```