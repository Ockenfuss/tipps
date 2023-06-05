<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [General](#general)
  - [Execution](#execution)
  - [Variables](#variables)
    - [Definition](#definition)
    - [Arrays](#arrays)
    - [Parameter expansion](#parameter-expansion)
    - [Environment variables](#environment-variables)
    - [Aliases](#aliases)
  - [Program logic](#program-logic)
    - [Branching](#branching)
    - [Loops](#loops)
      - [For loops](#for-loops)
    - [Boolean operators](#boolean-operators)
      - [test or [](#test-or)
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
  - [Stream Editing](#stream-editing)
  - [Filesystem](#filesystem)
    - [Partitions & Creation](#partitions-creation)
    - [Mounting](#mounting)
    - [Formatting](#formatting)
  - [Filepaths](#filepaths)
  - [Renaming](#renaming)
  - [Process Handling](#process-handling)
    - [Background jobs](#background-jobs)
  - [Compressing and Archiving](#compressing-and-archiving)
    - [Compressing](#compressing)
    - [Archiving](#archiving)
  - [Networks](#networks)
    - [Downloading](#downloading)
  - [Automated Execution](#automated-execution)
    - [System](#system)
    - [Systemd](#systemd)
  - [Mail](#mail)
  - [Images](#images)
  - [Video](#video)
  - [Conversion](#conversion)
  - [Date and Time](#date-and-time)
  - [Backup](#backup)
  - [Slurm](#slurm)
  - [Netcdf](#netcdf)
- [Examples](#examples)
- [Shells](#shells)
  - [Settings](#settings)
  - [Bash](#bash)
  - [ZSH](#zsh)
    - [Oh my zsh](#oh-my-zsh)
- [Tmux](#tmux)

<!-- /code_chunk_output -->

# General
Shell: Program which processes text serially and interprets them as shell commands

## Execution
```bash
./Test #Execute a binary or shell script in a subhell
source ./Test.sh #Execute a script in this shell
. ./Test.sh #'.' is short for source
```
## Variables
### Definition
```bash
test=VAR1 #local variable. No spaces around =!
echo $VAR1 #read variable. This is actually a special case of parameter expansion.
echo "${VAR1}" #for security and clarity, it is better to add {} around the name
echo '$VAR1' #within '', the string is not interpreted by the shell.
c=$(($a+$b))#$((...)) provides an arithmetic environment. Inside, expressions are evaluated in c style
test=$(ls) #store function output in variable There are no spaces allowed around the "="!
test=`ls` #Alternative to $(). Note the difference between ` and '
test="$variable"variable2 #Insert the variable expression and directly add variable2
export test #export local var to global environment, which is copied to every child process (such that it is available in subshells)
unset test #undefine a variable
```
### Arrays
```bash
a=(1 2 3 4) #set array elements.
a=($VAR) #use VAR to set elements (separated by IFS) 
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

### Parameter expansion
```bash
${var:offset:length} #get part of a string variable
${var:-default} #use default here if var not set
${var:=default} #set var to default if var not set
${var:?message} #write message to stderr and exit if var is not set
${var#prefix} #remove prefix from content of var. Use ## for the longest matching pattern.
${var%suffix} #remove suffix from content of var. Use %% for the longest matching pattern.
```

### Environment variables
```bash
env #show environment variables
$? #Contains the exit status of the last command
$$ #Contains the process id of the shell
$# #number of positional parameters
$0 #contains the name of the script
PS1; PS2 #the format of the bash prompt 1 and 2 (latter e.g. for multiline constructs)
IFS=$'\n' #set independent field separator to newline. Used e.g. by for loop or in Array creation to separate fields.
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
for A in $VAR; do #Will use IFS to read entries from variable
for (( run=$STARTNUM; run<=$ENDNUM; run++ )); do #C style environment
...
done
```
### Boolean operators
They work on the exit codes of the command. E.g. `grep -sq word file && echo found` will print "found" only if grep exits successfully.
Here, we also use that they are lazy and the second part is only executed if the first was successful.
#### test or [
"test" or equivalent "[" is a program to compare numbers or check filetypes. E.g.
* ` [ -f file ] && delete ` deletes only if file exists
* !: Inversion. E.g., `[ ! -f file ]` checks for non-existence.

Test provides a list of unary operators which work on files:
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
var=$[10*20] #Math environment. Only integers, zsh supports full float! :)
var=$((10*20)) #also math environment
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
command1 | xargs -p -i -t command2 -flag1 {} -flag2 #execute command2 with each output line from command1. With -i, "{}" is replaced by the output from command1. With -p, you get asked before execution. -t: verbose (print command)
command1 | xargs -t -i sh -c "command2 {} | grep word" #you can execute more complex commands like pipes using sh -c
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
mkdir -p /path/dir/ #create directory. -p: create if not existent, including intermediate directories.
man 5 passwd #Show manpage for commands, files,... They are organized in levels, see man man.
apropos keyword #Seach manpages short descriptions
yes test #Repeat string until program ends
: #or 'true': do nothing else than returning successful execution. Like the 'pass' statement in python. Useful e.g. to apply parameter expansion but do nothing else or define a vecho commant, which is echo or ':', dependent on the verbose status.
wc -l file #Word/Line/Character count
stat file #show file status and file attributes
```

## Displaying text
```bash
echo -ne "Hello\tWorld" #-n: no new line at end. -e: Interpret escape sequences
printf "%20s%.3d %3.2f" "Hello" 10 20.1234 #C Style formatting
```
### Files
```bash
cat file #Concatenate concent of files and print to stdout. Often used to just print one file
tac file #cat inverse
head -1 file #show first lines. head -n -1 to print all but the last line
tail -20 file #Use -f to have a live view. tail -n +20 to print line 20 and following.
more file #Display sequentially.
less file #Similar to more. Interactive view.
diff file1 file2 #compare files line by line
```

## User interaction
```bash
read TEST #Stop execution and wait for input, which is saved in variable TEST
read -p "Continue? (y/n)" -i "y" CHOICE #ask the user for input with -p. Preselect y with -i
case $CHOICE in
  [yY]) cmd;;
  [nN]) cmd;;
  *) cmd;;
esac
select CHOICE in $LIST #let the user select one value from a list to be stored in CHOICE
getopt ab:c -a -b test test2 -c #Output Options first, then parameters: -a -b test -c -- test2
while getopts ab:c opt
do
  case $opt in 
    a) cmd ;;
    b) cmd $OPTARG ;;
    c) cmd
  esac
done
shift $[ $OPTIND - 1 ] #Now shift to have all non optional arguments in $1, $2, ...
```
Full example including help text and longoptions:
```bash
# Process input parameter
#   Check and canonicalise input parameter
Parameter=$(getopt --options d:hqv --longoptions date,help,quiet,verbose --name "${0##*/}" -- "$@")
if [ $? != 0 ] ; then
  echo "Try '${0##*/} --help' for for more information." >&2
  exit 1
fi
eval set -- "$Parameter"
#   Actual processing
while (( $# > 0 )) ; do
  case "$1" in
    (-d | --date )
      Date=$2
      shift 2 ;;
    (-q | --quiet )
      vecho=:
      shift 1 ;;
    (-v | --verbose )
      verbose=1
      shift 1 ;;
    ( -h | --help )
      echo "Usage: $0 [OPTIONS]"
      echo ""
      echo "The following environment variables must be set:"
      echo "MY_VARIABLE"
      echo ""
      echo "Options:"
      echo "  -d, --date    Date in the form YYYYMMDD. Default ist today."
      echo "  -q, --quiet   Suppress output."
      echo "  -v, --verbose Show all output."
      echo "  -h, --help    Show this help."
      echo ""
      echo "Examples:"
      echo "  $0 -d 20210916"
      exit ;;
    ( -- ) 
      if (( $# > 1 )) ; then
        echo "${0##*/}: invalid parameter '$2'" >&2
        echo "Try '${0##*/} --help' for for more information." >&2
        exit 1
      fi
      shift ;;
  esac
done
```

## Modifying text
```bash
nl file #show with line numbers
sort file #sort alphabetically. -n for numeric
uniq file #Remove double lines. They have to be adjacent!
cut -d ':' -f1-3 #print columns 1 to 3 with delimiter ':'
cut -c1-10 #print only first to tenth character from line. Also useful to trim/remove characters from line
```
## Searching
Search after files
```bash
find dirname -name "*.sh" #search specific files below a directory
find . -maxdepth 3 #limit search depth
find . -path "*/dir/*.jpg" #search full path
find . -type f #file type: file, dir, block, char, link ...
find . -size +5M -size -10M #between 5 and 10 MB
find . -mtime -1 #modification time less than 1*24h 
find . -newer file #files with modification time newer than file
find . -user 1000 #Owner uid. Call 'id' or see /etc/passwd to find yours
find . -perm 0755 #permissions
find . -not -name "abc" #boolean negation: invert match with 'not'
#do something with files:
find . -name 'abc*' -delete #delete matches
find . -name 'abc*' -exec cp {} dir1/ \;  #execute a command on every file
```
Search within files
```bash
grep abc file #search for abc within file
grep '^[abc]' file #grep accepts simple regex
egrep 'ab|cd' -o file #egrep necessary for extended regular expressions. -o: Show only the regex match
grep -v -l 'abc' file*.txt # -v: invert -l: print only filename of matching file
grep -L 'abc' file.txt #print only non-matching files
grep -rni --include \*.py 'word' ./ #: For searches within files. -r: recursive -n: line number -i: ignore case --include: search only within if GLOB matches
```
## Stream Editing

## Filesystem
### Partitions & Creation
A physical storage device is usually divided in partitions to create logical disks for the OS. The partition table contains the information about the partitions. On each partition, a different filesystem can be implemented.
```bash
fdisk -l #List partition tables. Also lists the physical device names
fdisk /dev/sda #start interactive mode on disk /dev/sda. E.g. 'p' will list information about the partitions on this disk.
umount /dev/abc* #unmount all partitions on device abc
wipefs --all /dev/abc #remove filesystem by deleting the signature
cfdisk /dev/sda #an interactive CLI frontend to fdisk. Use it to create a partition table on a device
mkfs.vfat -n 'NAME' /dev/abc1 #create FAT filesystem on partition 1
fsck -N /dev/sda1 #check filesystem. -N: do not execute checks, just show.
```
### Mounting
Getting information about mountpoints, paritions, filesystems
```bash
lsblk #List all storage devices in a tree-like format (Name, mountpoint,...)
blkid #Get UUID, label, type,... of all partitions
findmnt -n -o TARGET /dev/sda1 #find the mount point of a device. -o: output columns, -n: do not print header
```
```bash
sudo mount /dev/sda1 /mnt/mountpoint #mount a device file 
sudo mount -a #mount all filesystems listed in /etc/fstab
sudo umount /dev/sda1 #unmount a device, either by specifying device file or mountpoint.
udisksctl mount -b /dev/sda1 #Automount device in folder media. Works without root in Ubuntu.
udisksctl power-off /dev/sda #Power off external hard drive to safely remove it.
```

### Formatting
```bash
sudo shred -vf /dev/sda #Erase all data beyond reconstruction by overwriting with random stuff
```

## Filepaths
```bash
basename file #basename without path
dirname file #pathname without base
realpath file #absolute path. Use --relative-to=path to get path relative to other
```
## Renaming
Rename multiple files in current folder using Perl regex syntax. General pattern:
`rename OPTIONS 'REGEX' FILES` with regex in the form `s/SEARCH/REPLACE/MODIFIER`
```bash
rename -n 's/Max Mustermann/Erika Mustermann/g' * #-n: dry-run
rename 's/(\d{4})-(\d{2})-(\d{2})/$3.$2.$1/g' *.jpg #Change format of jpg from YYYY-MM-DD into DD.MM.YYYY using regex groups
rename 's/\.html$/.xhtml/' *.html #Change file extension
```

## Process Handling
```shell
ps -fax #show snapshot of running processes
pidof -q -o 1234 -x abc #Find pid of process. -x: also if abc is a shell script -o: omit the given PID (e.g. the calling program itself) -q: quiet, return only exit status true/false
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

## Compressing and Archiving
### Compressing
Save a file more efficiently
```bash
bzip2 out.zip file #compress file. Slower, but better than zip
gzip -kdv file.gz #Another program to zip files. -d: unzip/decompress -k: keep original files -v: verbose
unzip file.zip #Another tool. -l: show content of zip only without extracting
```
### Archiving
Bundle a directory structure in one file. With tar, you can compress and archive in one step
```bash
tar -cjvf file.tar.bz2 dir/ #pack directory as archive file. -c: create -v: verbose -f: set name of archive -j: compress with bzip2
tar -tf file.tar #look into tar
tar -xf file.tar.bz2 #unpack. Be carful: It will be unpacked to the paths you see from tar -tf!
```


## Networks
```bash
ip a #ip address, mac address
ip route show #routing table with default gateway
cat /etc/resolve.conf #file with name server. Different in Ubuntu
cat /etc/services #show port numbers of services
ping -c 2 192.168.0.1 -w 1 #send echo request. -c: repetitions, -w: timeout
traceroute www.google.de #route of the package
host google.com #show ip from hostname or vice versa
ss -atp #active connections
nmap <ip or domain> #show open ports
systemctl start ssh #start (or stop, reload) services
vnstat -i enp0s31f6 -h #show traffic on device. -i: specific device (default: all) -h: hourly statistic
```
### Downloading
```bash
wget -q -o logfile -O Outputname URL #download a file or webpage from the Internet. -q: quiet
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

### System
```bash
uname #print system information such as kernel version
```

### Systemd
Alternatively, you can use systemd units to execute jobs. This provides more flexibility than cron, since you can define dependencies and conditions on jobs.
```bash
cd /etc/systemd/system #place your files here
touch testunit.service #service units are most common for manually defined tasks
touch test@.service #it is possible to define templates to create unit files dynamically. Within these, you can use specifiers like %i to refer everything between @ and .service.
systemctl --no-block start SERVICEFILE #start a unit. If already running, no second process will be started. --no-block: do not wait until finished.
systemctl --user start SERVICEFILE #Alternatively, place files in /ect/systemd/user and start them with --user flag. These units are executed as the current user without root privileges.
```
Example for a simple backup service named `backup@.service`
```text
[Unit]
 Description=Backup to USB Flash Disk

[Service]
 Type=simple
 ExecStart=/path/to/backup.sh %i
```

## Mail
Originally, every linux system has its own mail client
```bash
mail -s subject -A attachment -r return_address address #send email to someone.
echo -e "~b mail@mail.de\nText\n" | mail -s subject #mail reads text from standard-in. For bcc and further commands, use so called "compose escapes" (standard character is "~", followed by the command)
```

## Images
```bash
jpegoptim file.jpg #lossless jpeg compression, overwrite original
jpegoptim -S20% -d dir/ file.jpg #reduce quality to 20% filesize and save in dir/
exiftool file.jpg #show metadata
exiftool -all= file.jpg #remove all metadata
```

## Video
For video editing, ffmpeg is the most versatile tool.
```bash
ffmpeg -i A.mp4 B.mp3 #convert video to audio only
ffmpeg -ss 00:04:32.200 -i vid.mp4 -vframes 1 -q:v 1 out.jpg #extract a single image from a video. -q:v control the quality from 1 to 31, with 1 meaning highest quality
ffmpeg -framerate 10 -start_number 4 -i IMG_%03d.jpg out.mkv #combine numbered pictures to video
ffmpeg -ss 00:01:00 -i input.mp4 -to 00:02:00 -c copy output.mp4 #trim video from 'ss' until 'ss+to' (format hh:mm:ss). Here, the result would be 2min long from 01:00 to 03:00
ffmpeg -i input.mkv -filter:v "setpts=PTS/60" output.mkv #Speed up video by factor 60. Use "-an" to remove audio
```

## Conversion
```bash
convert a.jpg b.jpg -page a4 out.pdf #convert one or multiple images into one pdf. -page: make all pages a4 instead of image format
convert -density 300 a.pdf png:filename #convert pdf to image. Use type:name if you want to specify the output type explicitly
convert -transparent white a.png a2.png #make all white in image transparent
convert -alpha remove -alpha off a.pdf a.png #opposite: avoid transparent areas when converting pdf
convert a.png -trim out.png #crop white area from border
```

## Date and Time
The different format to input a date are described [here](https://www.gnu.org/software/coreutils/manual/html_node/Date-input-formats.html#Date-input-formats).
```bash
date +"%Y-%m-%d %H:%M:%S" #Format current date and time 
date -d "2021-05-01 14:30:00" #Use the specified time instead of the current one.
date --date='10 days ago' #Relative time strings are possible
date -d "2021-05-01 1 day ago" #Date relative to a specified date
date -d "today 0" #Current day, starting at midnight
date +"%-m" #date allows several flags and a width specifier after '%', influencing the padding with zeros or similar of numeric fields.
```

## Backup
`rsync` is a tool which is really powerful for backups. It copies directories based on file changes, which are detected using time stamp or changes in size. It is powerful for remote connections, but requires that rsync is available on both sides.
```bash
rsync -av from to #copy folder 'from' to 'to', resulting in a folder to/from on the target. -a: all subdirectories with attributes. -v: verbose.
rsync -av from/ to #For the source, it makes a difference if there is a trailing slash: With slash, the content of the folder `from` is copied into `to`, but not the folder itself.
rsync from to/ #Without a trailing slash in the source, an additional folder 'to/from/' is created, i.e. not only the content, but the folder with content is copied.
rsync -uavznP user@server:dir/ local/ #uses ssh (standard) to copy from remote server. -z: Use compression to reduce amount of data. -P: keep partially transferred files to resume if connection is broken and show progress. -n: dry-run without actually copying files -u: skip files that are newer on the receiver
-c # use checksums instead of timestamps
rsync -avzR /dir1/./dir2/dir3/ dest/ #-R: this will create the directories dest/dir2 and dest/dir2/dir3.
rsync -vna --prune-empty-dirs --include "*/" --include "*ext" --exclude "*" from to #Copy all files with extension 'ext' and all folders, but omit the folders without any 'ext'-files
rsync --files-from Filename dest #read sourcefiles from file
```

## Slurm
Tool for job managment on clusters
```bash
sbatch myscript.sh #submit job
squeue -u username #list all running jobs (-u: for a specific user)
scancel jobid #kill a job
srun job.sh #run a job in your command line on the cluster
srun --pty bash #open a terminal on the cluster. Useful to check environments and stuff
```

## Netcdf
```bash
ncdump -h file.nc  #show variables, attributes and dimensions
ncatted -O -a attribute,variable,o,c,"Text" file.nc #Change attributes. Syntax: attribute,variable,mode,type,value. Mode can be a:append, o:overwrite,... type can be c:char,... Option -O: overwrite original file or -o new.nc
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
### Oh my zsh
For the zsh, there exists a framework of configurations and plugins called 'oh-my-zsh'. See [the Github page](https://github.com/ohmyzsh/ohmyzsh) for installation. This framework contains a lot of different themes. Plugins can add support for e.g. git or better vi-mode

#### History
When configuring the zsh history, you have to answer the following question: Should the history file be a true history, listing all commands in order of execution, or a more complete, but non-chronological collection of all commands ever used?
```shell
setopt extended_history       # record timestamp of command in HISTFILE
setopt hist_expire_dups_first # delete duplicates first when HISTFILE size exceeds HISTSIZE
setopt hist_ignore_all_dups       #if a command is already present in the history file, append it and remove the older one
setopt hist_find_no_dups      # even if the history file contains duplicates, show only once when using the command line history feature
setopt hist_ignore_space      # ignore commands that start with space
setopt hist_verify            # show command with history expansion to user before running it
setopt share_history          # share command history data
```

# Tmux
Terminal multiplexer. Allows to keep your session alive after remote logout.
Generally, most funcionality is available after you press your tmux leader key like <C-a>.
```shell
tmux ls #List active sessions
tmux a -t main #Attach to session main
tmux new -s SessionName #Create new session
<Leader> d #Detach from session
<Leader> : #start mode to enter commands (like in vim)
<Leader> : kill-session #close all panes and quit session
tmux source-file ~/.tmux.conf #reload tmux conf
```
Tmux is controlled via a `.tmux.conf` file.

How to set format options, e.g. for the status bar. See `man tmux`, search FORMATS
```bash
setw -g automatic-rename-format '#{?condition,optionA, optionB}' #ternary operator
setw -g automatic-rename-format '#{m:regex,#{pane_current_path}}' #return 1 if regex matches current pane path
setw -g automatic-rename-format '#{?condition,#[bg=colour40],}' #conditional styling
```