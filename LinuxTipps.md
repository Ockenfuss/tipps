# Tipps for daily Linux work
Also includes a lot of useful snippets when working with the command line

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Tipps for daily Linux work](#tipps-for-daily-linux-work)
- [Linux General](#linux-general)
  - [Linux Installation](#linux-installation)
  - [Kernel](#kernel)
  - [Permissions in Linux](#permissions-in-linux)
  - [User Handling](#user-handling)
  - [Files](#files)
    - [Types](#types)
    - [Filesystems](#filesystems)
    - [Typical directories](#typical-directories)
  - [Links](#links)
  - [Installing Software](#installing-software)
  - [Boot process](#boot-process)
  - [Packages](#packages)
  - [SVN](#svn)
  - [PDF](#pdf)
  - [ssh](#ssh)
    - [Portforwarding](#portforwarding)
    - [sshfs](#sshfs)
    - [scp](#scp)
    - [rsync](#rsync)
    - [unison](#unison)
  - [Desktop](#desktop)
    - [Icons](#icons)
  - [Everyday commands](#everyday-commands)
  - [Appearance](#appearance)
    - [Fonts](#fonts)
- [Printing](#printing)
- [Network](#network)
  - [VPN](#vpn)
    - [Cisco Anyconnect](#cisco-anyconnect)
  - [SAMBA/CIFS](#sambacifs)
  - [NTP Timeserver](#ntp-timeserver)
- [Encryption](#encryption)
  - [gpg2](#gpg2)
  - [LUKS](#luks)
- [External Devices](#external-devices)
  - [Udev](#udev)
  - [Bluetooth](#bluetooth)
- [Useful Tools](#useful-tools)
  - [Webmin](#webmin)
- [Zsh Configuration](#zsh-configuration)
  - [Change colors of command prompt:](#change-colors-of-command-prompt)

<!-- /code_chunk_output -->

bash in general: there are various types of shells: login, interactive, non-interactive
if a bash script is executed, this is usually done in a non-interactive shell. Therefore, custom commands from the .bashrc or .zshrc are not available there!

# Linux General
## Linux Installation
You can create a bootable linux on a stick or CD.
- Download an iso image e.g. from Ubuntu
- If 'startup disk creator' is not installed, use: `sudo apt install usb-creator-gtk`
- On ubuntu, use 'startup disk creator' to turn a stick into a boot medium
## Kernel
* What is a kernel? C't Articles: https://www.heise.de/select/ct/2019/16/softlinks/yzpg?wt_mc=pred.red.ct.ct162019.174.softlink.softlink
```bash
#Change kernel parameters at runtime
cd /proc/sys #Here, kernel parameters are stored
sysctl -a#list all parameters with value
sysctl -w parameter=value #make a non-persistent change (reset by reboot)
#persistent changes can be made by modifying the .conf files in /etc/sysctl.d/
```
* What are all the top level files in linux for: https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard

## Permissions in Linux
https://www.guru99.com/file-permissions.html
Syntax:
-rwxr-xr-x#file Type | rwx: User permissions|r-x: Group permissions| r-x: World permissions (all others)
* for files: r: read, w: write, x: execute
* for directories: r: list files within, w: create/delete files within, x: change into


## User Handling
Important files: /etc/passwd, /etc/shadow
/etc/group #all groups

## Files
'Everything is a file'
### Types
* -: regular file
* b: block oriented device: HDD's, USB, partitions,...
* c: character oriented device: serial ports
* l: link, symbolic or hard
* p: pipe

### Filesystems
Linux:
* ext4: today standard on linux
* btrfs: binary tree fs
* zfs

Windows:
* FAT, FAT32: traditional, old. FAT32 often on USB sticks
* ntfs: more modern, linux usage possible.

Network based:
* nfs: network file system, unix/linux
* cifs: common internet file system (invented by microsoft). smb is the corresponding protocoll

### Typical directories
Some first level directories:
* /bin: binaries
* /dev: device files
* /etc: configurations
* /mnt: manual mounts
* /media: mounts like usb sticks, sd cards
* /var: logs, spools
* /sbin: superuser binaries
* /lib: drivers
* /tmp: Temporary files. Typically get deleted after every reboot or 10 days

Some deeper level directories:
* /var/tmp: Temporary files. Last typically 30 days and don`t get deleted after reboot

## Links
```bash
ln source destination #create hard link: pointer to the same physical memory area. 
ln -s Source Destination #create symbolic link: pointer to the original path. Invalid if original is removed.
readlink [-f]#get destination of existing link
```

## Installing Software
Flatpak
Alternative to 'snap' from Canonical. Compared to package managment with apt, flatpak puts everything in one special directory and should enable applications to run on any distribution
```bash
flatpak install --user --from URL #Install. --user does not require sudo
flatpak list #list installed
sudo flatpak update #Update all
sudo flatpak update PACKAGE #Update package
```


## Boot process
When booting usig UEFI, each operating system (-> dual boot) needs an entry in the Efi boot table.
```bash
efibootmgr #list boot table
```
Reinstalling grub usually creates an EFI entry. You can do this from a live system, if you are not able to boot your main system anymore. In this case, you need to mount the EFI partition and the root partition of your system. Usually, the EFI partition is at the beginning of the disk and around 250MB in size.
```bash
mount /dev/nvme0n1p1 /efi_mount #mount efi partition in the live system
mount /dev/nvme0n1p7 /linux_home_mount #mount your normal root in the live system
grub-install --efi-directory /efi_mount --boot-directory /linux_home_mount/boot/grub #if on a live system
```

A broken boot setup can also be fixed using boot-repair. I think, this also attempts to reinstall grub, but be careful which grub is actually reinstalled if on a live system!
```bash
sudo add-apt-repository ppa:yannubuntu/boot-repair && sudo apt update
sudo apt install -y boot-repair && boot-repair
```

two different boot processes are common today: systemV and systemd

SystemV:Starts scripts sequentially. In /etc/rc#.d/ collection of links to scripts. If `S...`: call this command with `start` option

systemd: Event based booting consisting of units. Use `systemctl` command to handle them.
```bash
systemctl list-units #list all units
systemctl status apache2 #status of service
systemclt start service #start (or stop) a service
journalctl -f #command to see systemd log
```


## Packages
Use a package manager. There are debian based distributions (Debian, Ubuntu,...) and rpm based (Suse).
```bash
dpkg -L nmap #package manager, but cannot handle dependencies. Better: apt. -L cmd: show all files created when installing
dpkg -i dir/package #install package directly from file
man apt #Good overview without details!
vi /etc/apt/sources.list #urls of package repositories
apt search package #search in repository
sudo apt install package #Install package
sudo apt update; sudo apt upgrade #update list and upgrade all packages
apt show package #Show package information (version, description, etc.)
apt list --installed #Show all installed packages
apt remove package #deinstall program
apt autoremove #remove unnecessary, automatically installed packages
apt purge #remove everything, even configuration files
apt -f install #force install of packages which are flagged as missing (e.g. dependencies from an attempt to install with dpkg before)
```
Manually: put them into or create a link in e.g. /usr/bin/local. Meanwhile, many projects provide an AppImage which runs on most linux systems without installation. I collect them e.g. in ~/Software and create a link to a folder within the $PATH.


## SVN
```bash
svn co https://svn.physik.uni-muenchen.de/repos/libRadtran/trunk libRadtran #Checkout repository
svn up #Update repository
svn diff --summarize #show changed files
svn revert -R src/#Revert all changes in src/ (recursive, be aware that changes can be lost!)
```

## PDF
```bash
pdfcrop in.pdf out.pdf #Crop all white space around the content in a pdf
pdftk pdf1.pdf pdf2.pdf cat output out.pdf #combine pdfs. Alternative: 'pdfunite'
pdftk in.pdf cat 1-3 output out.pdf #Extract pages from pdf
qpdf --encrypt pwd_user pwd_owner 256 -- A.pdf A_encrypt.pdf #Encrypt a pdf with 256 bit
qpdf -decrypt pdffile_protected.pdf pdffile_notprotected.pdf #Remove read only e.g. to make annotations to the pdf
```
## ssh
Usual directory: `~/.ssh`. There, you find your private key (`id_rsa`, keep it safe!) and your public key (`id_rsa.pub`). To use it for automatic login on a server, the public key must be added in the servers `.ssh/authorized_keys` file. Therefore, you need to provide another method of authentification to the server, like a password or send an email to the admin, whatever. The usual way is to use ssh-copy-id, which automatically copies your public key in the servers authorized_keys list (using e.g. password authentification). Now, the server trusts everyone who can prove to have the private key to the public one in known_hosts (Imagine the server encrypting a test message and sending it to the client. If the client can decrypt the message and send it back (encrypted with e.g. the servers public key, of course), the client can be trusted). 
```bash
ssh-keygen -t ed25519 -f ~/.ssh/key_for_xy -C "Comment(Email address)" #Generate a key public private key pair
ssh-copy-id -i id_rsa.pub My.Loginname@some.server.de #Add public key to server authorized_keys
ssh -X User@ServerAddress #Now log in to server (use -X to enable X11 forwarding)
```
Config file for ssh. Use it for configuration, abbreviation of long names, etc.
```shell
Host MyNickname
  HostName ServerAddress
  User MyLoginNameOnTheServer
  IdentityFile ~/.ssh/xy_ed25519.pub
  # If there is a login/jump server in between, use this command
  ProxyJump user@jumpserver
	ProxyCommand ssh -X -q -W %h:%p jumpserver #Old, now use 'ProxyJump'
  #Multiplexing: Open multiple ssh connections over a single TCP connection
	controlmaster auto
	ControlPath  ~/.ssh/sockets/%r@%h-%p #For this, you need a directory 'sockets' in .ssh, where the sockets are located in format name@host-port
	ControlPersist  600


```
Control Master: Allows you to use one tcp connection for multiple ssh sessions. Has the advantage that you need to login only once!
```shell
Host MyNickname #Use "Host *" if you want it always
  controlmaster auto #enable it
  ControlPath  ~/.ssh/sockets/%r@%h-%p #files with the sockets will be created here. Can be any folder, e.g. in \tmp\... Create .ssh/sockets manually if not existent
  ControlPersist  600 #if you log out on the master session, the connections remains this many seconds open in background if other subsession are still connected. This allows a re-login without a blocked terminal, if you accidentally logged out.
```
### Portforwarding
```bash
ssh -L2002:111.111.111.111:443 user@222.222.222.222 #build a secure connection via unsecure network, if ssh server is running on remote host. 2002:local port to be forwarded. 111...: remote server address 443:remote server port 
```

### sshfs
```bash
sshfs -o reconnect,ServerAliveInterval=16,ServerAliveCountMax=3 #Options to reconnect and avoid stuck processes
sshfs -o idmap=user -o uid=$(id -u) -o gid=$(id -g) My.Loginname@some.server.de:/folder/on/server ~/Work #Usermapping: Map Ownership from remote user to current user
fusermount -uz ~/Mounts/Remote #Unmount directory "Remote"
killall -9 sshfs #If stuck :)
```
### scp
```bash
scp Path/fileTocopy user@university_computer:File/path/#Copy files via ssh from one computer to other
```
### rsync
```bash
rsync -a -v --exclude=".*" SimulationGit My.Loginname@server.de:
Ergebnisse zurückholen: rsync -a -v My.Loginname@UniversityLogin.de:SimulationGit/NamederErgebnisse.results . 
```
### unison
progam to synchronize directories via ssh. `apt install unison-all-gtk` for graphical program.


## Desktop

To start programs from the launcher, they need a corresponding .desktop file. Personal files can be located in `~/.local/share/applications`. 
```txt
[Desktop Entry]
Version = 1.5
Type =		Application
Name =		Linphone
GenericName =	Telephony client
Comment =	A libre SIP client
Icon =linphone-logo.png
Categories =	Office;Telephony;
MimeType =	x-scheme-handler/sip-linphone;x-scheme-handler/sip;x-scheme-handler/sips-linphone;x-scheme-handler/sips;x-scheme-handler/tel;x-scheme-handler/callto;
OnlyShowIn =	GNOME;XFCE;

Terminal =	false
Exec =		linphone %F
StartupNotify =	true
```
### Icons
Icons can be located in `~/.local/share/icons` (personal) or `/usr/share/pixmaps` (system).

## Everyday commands
Rename
```bash
rename -n#show how files would be renamed. Overview: https://www.computerhope.com/unix/rename.htm
rename -n 's/Expr1/Expr2/' files#Replace all Expr1 in the given filenames with Expr2
```
Zip
```bash
unzip file.zip -d DestinationFolder
```
Diskusage
`du -h --max-depth=1 #-h: Human readable`

```bash
time -o time.txt -f "%e" command #measure runtime of command in seconds ("%e" specifier) and write it to file time.txt
wc # counts words (-w), lines (-l) or characters (-m)
```
.zshrc
`source ~/.zshrc #reload configurations`

## Appearance
### Fonts
Fonts are located in `/usr/share/fonts` or `~/.local/share/fonts`. You can just add fonts to this locations.
```bash
fc-cache -f -v #rebuild font cache
fc-list #list installed fonts
```
# Printing
All options: https://www.cups.org/doc/options.html
Usually, printing is handled by CUPS (common unix printing system). It is preinstalled on all Ubuntu distributions. It has a client/server structure and can handle many printers and also provide them in network. Usually, you have a local cups server running which handles the printers for your local system. It can be reached in browser via 'http://localhost:631/'
```bash
lpstat -p #show printers (from local cups server)
lspstat -h "cups.mycompany.de:631/version=1.1" #specify a remote cups server
CUPS_SERVER=server:port evince document.pdf #Specify an alternative cups server for a given process 
lp -d Printer_Name dokument.pdf #print pdf
lpq -a #all jobs of current computer
lprm -P Druckername Job-ID
```
Add a printer from a server according to https://superuser.com/questions/98520/print-over-remote-cups-server-but-just-show-a-subset-of-the-printers:
```bash
lpadmin -p newprinter -v ipp://cups.mycompany.de:631/printers/printername
cupsenaple newprinter
cupsaccept newprinter
```

To specify a cups server in general, you can edit the config file
```bash
cd /etc/cups/
touch client.conf #Create if not existent
vim client.conf #Add line: ServerName cups.mycompany.de
sudo systemctl restart cups
```

# Network
## VPN
### Cisco Anyconnect
In order to add a profile, go to folder /opt/cisco/anyconnect/profile and add
```xml
<?xml version="1.0" encoding="UTF-8"?>

<AnyConnectProfile xmlns="http://schemas.xmlsoap.org/encoding/">
<ServerList>
     <HostEntry>
          <User>your username</User>
          <HostName>your hostname</HostName>
          <HostAddress>you host url</HostAddress>
     </HostEntry>
</ServerList>
</AnyConnectProfile>
```

## SAMBA/CIFS
```bash
sudo mount -t cifs -o user=username,uid=1000,gid=1000,password=abc //smb.server.de/projects/folder ~/Work #necessary to install 'sudo apt install cifs-utils'. Use an 'unc path' to specify the server but replace '\' with '/' for unix. Use password option only for e.g. fstab, normally you will get a dialog. Uid and gid important if fileattributes are not transmitted from server.
-o rw #mount read/write
-o noperm #do not perform permission checks. Can help if you have problems with permission denied when writing.
sudo umount Work #Unmount samba share
sudo umount -a -t cifs -l #Lazy Unmount all CIFS mounts
```

## NTP Timeserver
```bash
sudo vim /etc/systemd/timesyncd.conf #write "NTP=IP/Servername"
timedatectl set-ntp 1 #Activate the ntp server as time source
systemctl status systemd-timesyncd.service #check that the connection is working
```
# Encryption
## gpg2
GnuPG, where pgp is 'pretty good privacy'. Use it to encrypt or decrypt files.
Working principle: The basis is the usual principle of asymmetric encryption. Like e.g. ssh, I have a public key and a private key, which is ideally additionally protected with a password. When creating, it is useful to create an additional revocation certificate. This certificate can only be created with the private key available, but afterwards it can be used to designate the key as invalid on a key server, even if the private key is lost (or compromised). Therefore, try to keep it safe as well.
```bash
gpg -c file #simply encrypt a file using a passphrase. No keys or anything involved here.
gpg2 -k #list public keys in keyring
gpg2 -full-gen-key #create key pair
gpg2 -a -o key.asc --export Name #Export public key as ascii
gpg2 --import key.asc #Import to keyring. Without --import, just print the key
gpg2 --delete-secret-key <ID> #delete public and private key
gpg2 --keyserver 'pgpkeys.eu' --search-keys 'Prename Name' #Search key in web of trust. Server list: https://www.sks-keyservers.net/status/
gpg2 --recv-keys <ID> #download key from server
gpg2 --refresh-keys [ID] #refresh key (all if no ID given)

gpg2 -e -r Name1 -r Name2 File.txt #Encrypt file for recipients Name1, Name2. Use -a to get result as ascii instead of binary.
gpg2 -d -o Output.txt File.txt.asc #Decrypt file. 
gpg2 -b -a File.txt #Make a separate signature for File.txt
gpg2 --verify File.txt.asc #Verify signature. Without second argument, it is assumed in 'File.txt'
```
Web of Trust: Problem: I have a public key, but do I know that it really belongs to the person which owns the corresponding email address and name? (i.e. that person has the private key?) I can either: a) Ask the person itself for a proof and then trust this key, or b) ask anyone else who I trust that this key is trustworthy. The latter is the idea of the web of trust. There are 5 trust levels which you can assign to keys and which determine, whether gpg will trust new keys which are signed by one of the trusted keys. Usually, use 3, only if you really trust a person use 4. 5 is only for yourself.
```bash
gpg2 --edit-key Name #Start key editing
>sign #Sign this key if you are sure that it belongs to the person with this name and email. This is useful for others, which trust you such that they can also trust this key.
>trust #Choose a level of trust associated with this key. This is useful for you, because now gpg2 trusts other keys which are signed by this key.
>expire #Change the expiration date of the key. This is always possible, therefore you can choose a short one (1-2 years)
>save #save your changes
```

## LUKS
The linux standard to encrypt partitions.
See https://wiki.ubuntuusers.de/LUKS/Partitionen_verschl%C3%BCsseln/
Unmount the partition before you start with the following commands!
Initialization of an encrypted disk:
```bash
sudo dd if=/dev/urandom bs=1M count=8 of=/dev/sda1 #Write random bytes at the start of the partition. This will corrupt any existing filesystem!
sudo cryptsetup luksFormat -c aes-xts-plain64 -s 512 -h sha512 -y /dev/sda1 # Create encrypted container
sudo cryptsetup luksOpen /dev/sda1 my_drive #will create a virtual device /dev/mapper/my_drive
sudo mkfs.ext4 -L 'FS_NAME' /dev/mapper/my_drive #create filesystem (with a name)
sudo mount /dev/mapper/my_drive /mnt_point #now you can mount the partition 
sudo cryptsetup luksAddKey /dev/sda1 lukskey.txt #Add lukskey.txt as a keyfile for this partition
```
How to open and close manually:
```bash
sudo cryptsetup luksOpen --key-file lukskey.txt /dev/sda1 my_drive
sudo mount /dev/mapper/my_drive /media/my_drive #mount
... #do your stuff
sudo umount /dev/mapper/my_drive #unmount
sudo cryptsetup luksClose /dev/mapper/my_drive #Close virt. device 
```

# External Devices
## Udev
Linux subsystem for managing device events. Really usefull to get information about a connected device and to trigger scripts based on events like connecting, removing,...
```bash
udevadm monitor #livemonitoring
udevadm info -a -n /dev/sda #get information about a device: type, serial number, name, path,...
sudo udevadm control --reload #execute this after you changed the rules
```
https://opensource.com/article/18/11/udev
Udev allows to create rules, which are matched against device attributes. Rules are comma separated lists with entries in the form "Keyword>Operator>Value". Keywords could be e.g. SUBSYSTEM, ATTRS or ACTION. Operators could be e.g. `==` for comparison with the value or `+=` for assignment.
It is important to distinguish between attributes from the parent, referenced with an additional `S` (like `ATTRS`) and the device itself (like `ATTR`). Note that if e.g. a harddrive is connected, this can be done in multiple steps: the drive, then the partitions,... Arguments from the previous step become the parents in the next step.
```bash
cd /etc/udev/rules.d #directory with custom rules
touch 80-backup.rules #create a rule file
'ATTRS{idVendor}=="03f0", ACTION=="add", SYMLINK+="safety%n"' #example for rules
'SUBSYSTEM=="block", ATTRS{idVendor}=="03f0", ACTION=="add", RUN+="/usr/local/bin/trigger.sh"'
```


## Bluetooth
Bose qc 35 verbinden: https://askubuntu.com/questions/833322/pair-bose-quietcomfort-35-with-ubuntu-over-bluetooth
in /etc/bluetooth/main.conf: "ControllerMode = bredr" setzen und danach "sudo service bluetooth restart"
=> neu im Bluetooth Menü verbinden. Anschließend kann ggf. wieder "#ControllerMode = dual" gesetzt werden (LE=Low energy) und wieder "sudo service bluetooth restart"


# Useful Tools
## Webmin
Starts a server, where you can log in and control most of your system as root.









# Zsh Configuration
source ~/.zshrc #reload zshrc
## Change colors of command prompt:
```txt
host_color="%F{green}"
username_color="%F{blue}"
path_color="%F{blue}"
PROMPT="${username_color}$USERNAME%f@${host_color}%B%m%b%f ${path_color}%B%~%b%f > "
```




