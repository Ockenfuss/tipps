<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [General](#general)
  - [Execution](#execution)
  - [Variables](#variables)
    - [Definition](#definition)
    - [Arrays](#arrays)
    - [Environment variables](#environment-variables)
    - [Aliases](#aliases)
  - [Program logic](#program-logic)
    - [Branching](#branching)
    - [Loops](#loops)
      - [For loops](#for-loops)
    - [Boolean operators](#boolean-operators)
    - [Unary operators](#unary-operators)
    - [Comparison operators](#comparison-operators)
  - [Functions](#functions)
    - [Parameters](#parameters)
  - [Math](#math)
  - [PATH](#path)
  - [Pipes and redirection](#pipes-and-redirection)
  - [Subshells](#subshells)
  - [xargs](#xargs)
  - [User managment](#user-managment)
- [Commands](#commands)
  - [Basic](#basic)
  - [Displaying text](#displaying-text)
    - [Files](#files)
  - [User interaction](#user-interaction)
  - [Modifying text](#modifying-text)
  - [Searching](#searching)
  - [Filesystem](#filesystem)
    - [Partitions & Creation](#partitions-creation)
  - [Filepaths](#filepaths)
  - [Process Handling](#process-handling)
    - [Background jobs](#background-jobs)
  - [Archiving](#archiving)
  - [Networking](#networking)
  - [Automated Execution](#automated-execution)
  - [Mail](#mail)
  - [Images](#images)
  - [Backup](#backup)
- [Examples](#examples)
- [Shells](#shells)
  - [Settings](#settings)
  - [Bash](#bash)
  - [ZSH](#zsh)
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
test=VAR1 #local variable. No spaces around =!
echo $VAR1 #read variable
echo '$VAR1' #within '', the string is not interpreted by the shell.
echo "${VAR1}" #for security and clarity, it is better to add {} around the name
c=$(($a+$b))#$((...)) provides an arithmetic environment. Inside, expressions are evaluated in c style
test=$(ls) #store function output in variable There are no spaces allowed around the "="!
test=`ls` #Alternative to $(). Note the difference between ` and '
test="$variable"variable2 #Insert the variable expression and directly add variable2
export test #export local var to global environment, which is copied to every child process (such that it is available in subshells)
unset test #undefine a variable
```
### Arrays
```bash
a=(1 2 3 4) #set array elements
a=($(seq 0 10)) #create with seq
a[1]="eins" #set single element
echo ${a[0]} #access element
echo ${a[@]} #print all elements
echo ${#a[@]} #print number of elements
echo ${!a[@]} #print the keys of the elements
```
Associative array: kind of like a dictionary
```bash
declare -A arr
arr=([key1]=val1 [key2]=val2)
echo ${arr[key2]}
```

### Environment variables
```bash
env #show environment variables
$? #Contains the exit status of the last command
PS1; PS2 #the format of the bash prompt 1 and 2 (latter e.g. for multiline constructs)
```
### Aliases
```bash
alias ll='ls -la' #
```
## Program logic

### Branching
```bash
if [[ $A -eq $B ]]; then #Actually, [[ is a small bash program that evaluates the given expression
  cmd
elif [ -f file ]; then
  cmd
else
  cmd
fi
```

```bash
case $VAR in
  a) 
    cmd
    cmd
    ;;
  b) cmd ;;
esac
```
### Loops
#### For loops
```bash
for A in 1 2 3 4; do echo $A; done #simple for loop over list
for (( run=$STARTNUM; run<=$ENDNUM; run++ )); do #C style environment
...
done
```
### Boolean operators
They are lazy: ` [ -f file ] && delete ` deletes only if file exists

### Unary operators
-d: exists and is directory
-f: exists and is regular file
-h: symbolic link
-w: writable
-r: readable
-x: executable
-u: user bit set
-g: group bit set
-k: sticky bit set
-z: true if string length zero
[ string ] : true if length of string nonzero
  

### Comparison operators
Number  | String
-eq     | =  
-ne     | !=
-le     | <=
-ge     | >=
-gt     | >
-lt     | <



## Functions
```bash
test() { #Alternative: function name {...
  var1=1
  echo $1 #Use echo to return output. $1 contains the first argument.
  return 0 #return sets only the exit code (0-255)
}
res=`test` #save function output in variable
set #show all defined functions
```
### Parameters
```bash
$0 #Program name
$1 #First parameter
$* #Contains all parameters as a single string
$@ #contains all parameters in an array like matter (for param in "$@" do...)
shift #shift parameters left, i.e. 3=>2, 2=>1, 1=>removed
```
## Math
````bash
$[10*20] #Math environment. Only integers, zsh supports full float! :)
$((10*20)) #also math environment
result=`echo "scale=3; 1/9" | bc` #Use the bash calculator. scale: floating point precision used. 
````

## PATH
not in .zshrc or similar, because these will be synchronized between computers via my git repo!
in ~/.profile (works only for bash login shells): 
`PATH="$HOME/bin:$HOME/.local/bin:$PATH"`
Alternative: create link in /usr/local/bin (not in /usr/bin, this is managed by the package manager)
## Pipes and redirection
```bash
mkfifo pipefile #make a pipe type file.
Befehl1 | Befehl2 #Pipes: send stdout of the left command to stdin of the right command
#Remind: stderr is not sent to the right!
cmd> NewFile #Redirection: Redirect all the output from one command to a (new) file. Its content will be overwritten!
cmd>> File #Redirection with appending the new content
cmd>&1 #Redirect output to stdout. "0" is stdin, "1" is stdout, "2" is stderr
2>&1 #Redirect only errors to stdout
cat << 'ENDKEY' #Multiline input which you can send to stdin. 'ENDKEY' signals the multiline ending.
test
ENDKEY
/dev/null #Black hole: Swallows all input redirected to it
command | tee file #print to command line and to file
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

## User managment
Users are listed in /etc/passwd file.
```bash
useradd -m test #Add user account. -m: with home directory containing files from /etc/skel
useradd -D #show defaults
userdel test #Remove entry from /etc/passwd
usermod #modify account in general
passwd #change password
su - username #start a shell as the specified user. '-' creates a login shell similar to real login.
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
cd, cp, mv, touch, ls #really basic stuff
man 5 passwd #Show manpage for commands, files,... They are organized in levels, see man man.
apropos keyword #Seach manpages short descriptions
yes test #Repeat string until program ends
wc -l file #Word/Line/Character count
stat file #show file status and file attributes
```

## Displaying text
```bash
echo -ne "Hello\tWorld" #-n: no new line at end. -e: Interpret escape sequences
printf "%20s%10i %3.2f" "Hello" 10 20.1234 #C Style formatting
```
### Files
```bash
cat file #Concatenate concent of files and print to stdout. Often used to just print one file
tac file #cat inverse
head -1 file #show first lines
tail -20 file #Use -f to have a live view
more file #Display sequentially.
less file #Similar to more. Interactive view.
diff file1 file2 #compare files line by line
```

## User interaction
```bash
read TEST #Stop execution and wait for input, which is saved in variable TEST
select CHOICE in $LIST #let the user select one value from a list to be stored in CHOICE
getopt ab:c -a -b test test2 -c #Output Options first, then parameters: -a -b test -c -- test2
while getopts ab:c opt
do
  case $opt in 
    a) cmd
    b) cmd $OPTARG
    c) cmd
  esac
done
```

## Modifying text
```bash
nl file #show with line numbers
sort file #sort alphabetically. -n for numeric
uniq file #Remove double lines. They have to be adjacent!
cut -d ':' -f1-3 #print columns 1 to 3 with delimiter ':'
```
## Searching
Search after files
```bash
find /dir1 -name "*.sh" -maxdepth 3 -exec cp {} dir1/ \;#: for searching a file/folder
find . -type f #file type: file, dir, block, char, ...
find . -size +5M -size -10M #between 5 and 10 MB
find . -mtime -1 #modification time less than 1*24h 
find . -newer file #files with modification time newer than file
find . -user 1000 #Owner uid. Call 'id' or see /etc/passwd to find yours
find . -perm 0755 #permissions
```
Search within files
```bash
grep abc file #search for abc within file
grep '^[abc]' file #grep accepts simple regex
egrep 'ab|cd' -o file #egrep necessary for extended regular expressions. -o: Show only the regex match
grep -v 'abc' file # -v: invert
grep -rni --include \*.py 'word' ./ #: For searches within files. -r: recursive -n: line number -i: ignore case --include: search only within if GLOB matches
```
## Filesystem
### Partitions & Creation
A physical storage device is usually divided in partitions to create logical disks for the OS. The partition table contains the information about the partitions. On each partition, a different filesystem can be implemented.
```bash
fdisk -l #List partition tables. Also lists the physical device names
umount /dev/abc* #unmount all partitions on device abc
wipefs --all /dev/abc #remove filesystem by deleting the signature
cfdisk /dev/sda #an interactive CLI frontend to fdisk. Use it to create a partition table on a device
mkfs.vfat -n 'NAME' /dev/abc1 #create FAT filesystem on partition 1
```

## Filepaths
```bash
basename file #basename without path
dirname file #pathname without base
realpath file #absolute path. Use --relative-to=path to get path relative to other
```

## Process Handling
```shell
ps -fax #show snapshot of running processes
top -u User.Name #Show Interactive process overview
kill -TERM <pid> #send TERM (15): friendly request to terminate
kill -KILL <pid> #send SIGKILL (9): terminate immediately
kill -HUP <pid> #send SIGHUP (1): stay in memory and reinitialize configuration
kill -HUP -1 #send SIGHUP ("Hang up") signal to all processes, the "friendly" request for termination
```

### Background jobs
```bash
Ctrl-Z: Pause job
bg #Continue job in background
fg #bring job to foreground
jobs #list jobs
kill %1 # '1' is the Job ID you get by calling jobs: "[1] + Running ..."
```

## Archiving
```bash
bzip2 out.zip file #compress file. Slower, but better than zip
tar -cjvf file.tar.bz2 dir/ #pack directory as archive file. -c: create -v: verbose -f: set name of archive -j: compress with bzip2
tar -tf file.tar #look into tar
tar -xf file.tar.bz2 #unpack. Be carful: It will be unpacked to the paths you see from tar -tf!
```


## Networking
```bash
ip a #ip address, mac address
ip route show #routing table with default gateway
cat /etc/resolve.conf #file with name server. Different in Ubuntu
cat /etc/services #show port numbers of services
ping -c 2 192.168.0.1 -w 1 #send echo request. -c: repetitions, -w: timeout
traceroute www.google.de #route of the package
ss -atp #active connections
nmap <ip or domain> #show open ports
systemctl start ssh #start (or stop, reload) services
```

## Automated Execution
Use `cron`. Crontabs are stored in /var/spool/cron/crontabs/. Every standard out or error of the programs is sent to user via email.
Things to note:
* Cron uses its own environment (use `env` to see variables)
* Use absolute paths in cron scripts
* commands are executed when match: `(m && h && mon ) && (dom || dow)`
* be careful with time consuming jobs. Make sure they are not started multiple times in parallel
```bash
crontab -e #edit the cron configuration via this command and not directly.
```

## Mail
Originally, every linux system has its own mail client
```bash
mail user #send email to another user
```

## Images
```bash
jpegoptim file.jpg #lossless jpeg compression, overwrite original
jpegoptim -S20% -d dir/ file.jpg #reduce quality to 20% filesize and save in dir/
exiftool file.jpg #show metadata
exiftool -all= file.jpg #remove all metadata
```

## Backup
`rsync` is a tool which is really powerful for backups. It copies directories based on file changes, which are detected using time stamp or changes in size. It is powerful for remote connections, but requires that rsync is available on both sides.
```bash
rsync -av from/ to/ #synchronize two directories -a: all subdirectories with attributes. -v: verbose
rsync -uav user@server:dir/ local/ #uses ssh (standard) to copy from remote server
-c # use checksums instead of timestamps
```

# Examples
* pipes (`mkfifo`) are useful together with `read MSG < pipefile` 

# Shells
## Settings
* Global 
* * Login: /etc/profile
* * Bash: /etc//bash.bashrc
* User
* * Login: ~/.profile
* * Bash: ~/.bashrc
## Bash
'Bourne again shell'

## ZSH
'Z-Shell'

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