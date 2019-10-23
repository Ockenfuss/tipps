



###Logical operators
* Exclusion: `[^abc]`
* Or: `a|b`

###Occurences
Of the preceding character
* Zero or one: `?`
* Zero or more: `*`
* One or more: `+`


###Character groups
Formed by `[abc]`
```bash
[ae]#matches a and e
[0-9]#matches a single digit between 0 and 9
\d#all digits
\w#word characters
\l or \u#all lower- or uppercase characters
```


###Examples
* Exclude a certain word: If it occures once, we will not match: `^()