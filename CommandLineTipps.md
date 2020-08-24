<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [General](#general)
  - [Execution](#execution)
  - [Variables](#variables)
    - [Definition](#definition)
    - [Environment variables](#environment-variables)
  - [Program logic](#program-logic)
  - [Functions](#functions)
    - [Parameters](#parameters)
  - [Math](#math)
  - [PATH](#path)
  - [Pipes and redirection](#pipes-and-redirection)
  - [Subshells](#subshells)
  - [xargs](#xargs)
  - [Background jobs](#background-jobs)
  - [User managment](#user-managment)
- [Commands](#commands)
  - [Basic](#basic)
  - [Displaying text](#displaying-text)
  - [Modifying text](#modifying-text)
  - [Searching](#searching)
- [Tmux](#tmux)

<!-- /code_chunk_output -->

# General
Shell: Program which processes text serially and interprets them as shell commands

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
test=$(ls) #store function output in variable There are no spaces allowed around the "="!
test=`ls` #Alternative to $(). Note the difference between ` and '
test="$variable"variable2 #Insert the variable expression and directly add variable2
export test #export local var to global environment such that it is available in subshells
unset test #undefine a variable
```
### Environment variables
```bash
$? #Contains the exit status of the last command
PS1; PS2 #the format of the bash prompt 1 and 2 (latter e.g. for multiline constructs)
```
## Program logic
```bash
if [[ $A -eq $B ]] #Actually, [[ is a small bash program that evaluates the given expression
then
    ...
fi

for (( run=$STARTNUM; run<=$ENDNUM; run++ )); do
...
done
```

## Functions
```bash
test() { #Alternative: function name {...
  var1=1
  echo $1 #Use echo to return output. $1 contains the first argument.
  return 0 #return sets only the exit code (0-255)
}
res=`test`
```
### Parameters
```bash
$0 #Program name
$1 #First parameter
$* #Contains all parameters as a single string
$@ #contains all parameters in an array like matter (for param in "$@" do...)
shift #shift parameters left, i.e. 3=>2, 2=>1, 1=>removed
getopt ab:c -a -b test test2 -c #Output Options first, then parameters: -a -b test -c -- test2
```
## Math
````bash
$[10*20] #Math environment. Only integers, zsh supports full float! :)
result=`echo "scale=3; 1/9" | bc` #Use the bash calculator
````

## PATH
not in .zshrc or similar, because these will be synchronized between computers via my git repo!
in ~/.profile (works only for bash login shells): 
`PATH="$HOME/bin:$HOME/.local/bin:$PATH"`
Alternative: create link in /usr/local/bin (not in /usr/bin, this is managed by the package manager)
## Pipes and redirection
```bash
mkfifo pipefile #make a pipe type file
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
groups #show groups or user
groupadd test #create a group
usermod -G test username #add user to group
```
Translate Permissions: r-x=>binary 101=>octal value 5; for user,group,other:e.g. 775
New files: subtract from default (666 for files, 777 for directories) the umask value (e.g. 0002). Exception: New files are never executable
```bash
umask #list or set default with a umask
chmod u=rwx #set user (g group, o other) to rwx (+ add perm., - subtr. perm)
chown username file #change the owner of a file
```
SUID, GUID, sticky bit: three additional bits for every directory and file. Set with 4 digit octal number (e.g. 4755)
* SUID: execute with permissions of owner (if you have permissions to execute). See e.g. permissions of 'passwd', which needs to be executed as root since it has to change /etc/shadow. Only applies to binaries.
* GUID (applies to directories): owner of new files in the directory is the group, not the creator of the file. Can be used to create a shared directory for a group.
* sticky bit: only owner can delete file

# Commands

## Basic
```bash
cd, cp, mv, touch, ls #
man 5 passwd #Show manpage for commands, files,... They are organized in levels, see man man.
apropos keyword #Seach manpages short descriptions
yes test #Repeat string until program ends
wc -l file #Word/Line/Character count
```

## Displaying text
```bash
cat file #Concatenate concent of files and print to stdout. Often used to just print one file
tac file #cat inverse
head -1 file #show first lines
tail -20 file #Use -f to have a live view
more file #Display sequentially.
less file #Similar to more. Interactive view.
diff file1 file2 #compare files line by line
```

## Modifying text
```bash
nl file #show with line numbers
sort file #sort alphabetically. -n for numeric
uniq file #Remove double lines. They have to be adjacent!
```
## Searching
```bash
grep -rni --include \*.py 'word' ./ #: For searches within files. -r: recursive -n: line number -i: ignore case --include: search only within if GLOB matches
find #: for searching a file/folder
```

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