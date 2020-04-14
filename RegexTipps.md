## General
Escape a regex char by using `\\`, e.g. match a point with `\\.`.



### Logical operators
* Exclusion: `[^abc]`
* Or: `a|b`

### Occurences
Of the preceding character
* Zero or one: `?`
* Zero or more: `*`
* One or more: `+`
Example: `.*` matches every char zero or more times.

### Special matches
* `^`: Line start
* `$`: Line end

### Character groups
Formed by `[abc]`
```bash
. #Matches every char except \n
[ae]#matches a and e
[0-9]#matches a single digit between 0 and 9
\d#all digits
\w#word characters
\l or \u#all lower- or uppercase characters
```

### Subexpressions
Formed by round brackets around a part of the regex.

###Examples
* Exclude a certain word: If it occures once, we will not match: `^()