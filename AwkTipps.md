# Tips for the AWK programming language
https://www.tutorialspoint.com/awk/index.htm
Some program examples: https://www.gnu.org/software/gawk/manual/html_node/Miscellaneous-Programs.html#Miscellaneous-Programs
### Usage

```bash
gawk 'PATTERN {COMMANDS}' File.dat#from command line
gawk -f Code.awk File.dat#from code file
```
AWK scripts consist of blocks, where each block contains some commands within `{}`brackets.
There can be multiple commands in one block, separated by ';'
Each block usually contains a condition before the brackets, which determines whether the block is executed. The whole script is applied to each line in a file.

There are two special blocks `BEGIN {...}` and `END {...}`, which are executed only once before respectively after the main program (useful for e.g. variable declaration or creation of a file without input).


### Command line arguments
```bash
gawk -F ',' -f Code.awk File.dat#specify the column separator, default is ' '
gawk -i inplace file.txt#Inplace editing: Redirect the output to a temporary file and overwrite the original file with the temporary file after execution
```



### Columns
`$0` represents the whole line, `$1`, `$2`,... are the single columns. If possible, the strings are directly converted to real numbers!
Columns can also be accessed by variables via `$i`

### Loops and conditions
```bash
gawk '{for(i=0; i<10; i++) print i}'
gawk '{if (condition){actions}}'
gawk '{while (condition) {actions}}'
```
### Logical Operators
```bash
{ if( $2>50 && $3>50 ) print $1 }#Logical And
{ if( $2<50 || $3<50 || $4<50 ) print $1 }#Logical Or
```

### Printing
```bash
print $1, $2#print line. Without ',', the values are not separated!
printf $1 "a" #print without newline
```

### Build in functions
```bash
'length($0)>18'#pattern matching all lines with more than 18 characters
'match($0, "Ha..o")'#give the position where the given regex matches the given string (whole line here)
'match($0, "Ha..o",a); print a[0]'#in this case, a is an array where the 0th position contains the part of $0 that matches the regex
gawk '{sub("[0-3]","y",$0); print $0}'#Replace first regex match, 'gsub' replaces all
'tolower($0)'#make characters lowercase
'system("echo $(ls)")'#call bash commands from awk
'exit'#end program
```

###Build in variables
* FS: the current file separator
* NF: Number of fields(=columns) in the current record (=line)
* FNR: Number of the current line in the current file
* NR: Number or the current line

###Regex
`$0~/REGEX/`: true if $0 does match the regex. `!~` means "does not match". Regex can also be combined using logical operators: `a~/REGEX1/ && b!~/REGEX2/{do...}`

##Examples
* Remove empty lines: `gawk 'NF>0`
* Invert lines: `gawk '{a[i++]=$0}END{for(j=i-1; j>=0;j--) print a[j]}'`
* Find file extension: Here, we use subexpressions in regex to get the extension in a[2].  `echo 'abc.def' | gawk '{match($0, "(^.*)\\.(.*$)", a); print a[2]}'`
* Inverse sum (over blocks separated by "x"): `gawk '!/x/{a[count++]=$0} /x/{print $0; sum=0; for(j=count-1; j>=0; j--){ sum+=a[j]; b[j]=sum} for(j=0; j<count; j++) print a[j] " " b[j]; count=0}'`
* Combine lines
```bash
BEGIN{count=0}
{
    a[count++]=$0
    if (count==2){for (i in a) printf a[i] ";"; count=0; printf "\n"}
}
```