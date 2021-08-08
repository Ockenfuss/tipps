# Tips for the AWK programming language
https://www.tutorialspoint.com/awk/index.htm
Some program examples: https://www.gnu.org/software/gawk/manual/html_node/Miscellaneous-Programs.html#Miscellaneous-Programs

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

  - [Usage](#usage)
  - [Command line arguments](#command-line-arguments)
  - [Columns](#columns)
  - [Variables](#variables)
    - [Arrays](#arrays)
  - [Loops and conditions](#loops-and-conditions)
  - [Logical Operators](#logical-operators)
  - [Printing](#printing)
  - [Build in functions](#build-in-functions)
  - [Build in variables](#build-in-variables)
  - [Regex](#regex)
- [Examples](#examples)

<!-- /code_chunk_output -->

### Usage

```bash
gawk 'PATTERN {COMMANDS}' File.dat#from command line
gawk -f Code.awk File.dat#from code file
```
AWK scripts consist of blocks, where each block contains some commands within `{}`brackets.
There can be multiple commands in one block, separated by ';'
Each block usually contains a condition before the brackets, which determines whether the block is executed. The whole script is applied to each line in a file.

There are two special blocks `BEGIN {...}` and `END {...}`, which are executed only once before respectively after the main program (useful for e.g. variable declaration or creation of a file without input).

```bash
gawk -f code.awk file1.dat file2.dat ... #process multiple files
```
It is possible to process multiple files, in which case awk treats them like a single concatenated file. You can use NR==FNR to check whether you are in the first file. gawk implements the `ENDFILE{...}` block which is executed after each file is processed.


### Command line arguments
```bash
gawk -F ',' -f Code.awk File.dat#specify the column separator, default is ' '
gawk -i inplace file.txt#Inplace editing: Redirect the output to a temporary file and overwrite the original file with the temporary file after execution
```



### Columns
`$0` represents the whole line, `$1`, `$2`,... are the single columns. If possible, the strings are directly converted to real numbers!
Columns can also be accessed by variables via `$i`
### Variables
```bash
```
#### Arrays
```bash
a[0]=1 #Create Array. In awk, all arrays are associative, i.e. indexed by string values (compare dictionaries in python).
a[i,j]=1 #The content of i and j will be concatenated a single string that forms the key for this element.
```
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
print $1,$2 #print line. Without ',', the values are not separated. The output separator can be specified with the built in variable OFS.
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

### Build in variables
* FS: the current file separator
* NF: Number of fields(=columns) in the current record (=line)
* FNR: Number of the current line in the current file
* NR: Number or the current line

### Regex
See man gawk, Regular Expressions.
`$0~/REGEX/`: true if $0 does match the regex. `!~` means "does not match". Regex can also be combined using logical operators: `a~/REGEX1/ && b!~/REGEX2/{do...}`
```bash
match($0,".*_[[:digit:]]{6}(..)_(..)\\.txt",a); This example will match files with a date appendix like 'File_20201216_14.txt'. It contains a character class '[[:digit:]]', a repetition of a command '{6}', regex groups '(..)' (which can be accessed by a[0] and a[1]) and a dereference of a regex special character '\\.'
```

## Examples
* Remove empty lines: `gawk 'NF>0`
* Remove double lines: `gawk "!a[$0]++"`
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