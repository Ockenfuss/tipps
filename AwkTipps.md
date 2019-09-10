#Tips for the AWK programming language
https://www.tutorialspoint.com/awk/index.htm
Some program examples: https://www.gnu.org/software/gawk/manual/html_node/Miscellaneous-Programs.html#Miscellaneous-Programs
###Usage

```bash
gawk 'PATTERN {COMMANDS}' File.dat#from command line
gawk -f Code.awk File.dat#from code file
```
There can be multiple commands in one block, separated by ';'

###Command line arguments
```bash
gawk -F ',' -f Code.awk File.dat#specify the column separator, default is ' '
```



###Columns
`$0` represents the whole line, `$1`, `$2`,... are the single columns. If possible, the strings are directly converted to real numbers!
Columns can also be accessed by variables via `$i`

###Loops and conditions
```bash
gawk '{for(i=0; i<10; i++) print i}'
gawk '{if (condition){actions}}'
```

###Build in functions
```bash
'length($0)>18'#pattern matching all lines with more than 18 characters
'match($0, "Ha..o")'#give the position where the given regex matches the given string (whole line here)
gawk '{sub("[0-3]","y",$0); print $0}'#Replace first regex match, 'gsub' replaces all
'tolower($0)'#make characters lowercase
```

###Build in variables
* FS: the current file separator
* NF: Number of fields(=columns) in the current record (=line)
* FNR: Number of the current line in the current file

###Regex
`$0~/REGEX/`: true if $0 does match the regex. `!~` means "does not match".

#Examples
* Invert lines: `gawk '{a[i++]=$0}END{for(j=i-1; j>=0;j--) print a[j]}'`

* Inverse sum (over blocks separated by "x"): `gawk '!/x/{a[count++]=$0} /x/{print $0; sum=0; for(j=count-1; j>=0; j--){ sum+=a[j]; b[j]=sum} for(j=0; j<count; j++) print a[j] " " b[j]; count=0}'`
* Combine lines
```bash
BEGIN{count=0}
{
    a[count++]=$0
    if (count==2){for (i in a) printf a[i] ";"; count=0; printf "\n"}
}
```