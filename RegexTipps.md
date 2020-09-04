<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [General](#general)
  - [Logical operators](#logical-operators)
  - [Occurences](#occurences)
  - [Special matches](#special-matches)
  - [Character groups](#character-groups)
  - [Subexpressions](#subexpressions)
- [Examples](#examples)

<!-- /code_chunk_output -->


# General
Escape a regex char by using `\\`, e.g. match a point with `\\.`.



## Logical operators
```bash
[^a] #Exclusion
```
* Or: `a|b`

## Occurences
Of the preceding character
* Zero or one: `?`
* Zero or more: `*`
* One or more: `+`
Example: `.*` matches every char zero or more times.

## Special matches
* `^`: Line start
* `$`: Line end

## Character groups
Formed by `[abc]`
```bash
. #Matches every char except \n
[ae] #matches a and e
[0-9] #matches a single digit between 0 and 9
\d #all digits
\w #word characters
\l or \u #all lower- or uppercase characters
[:blank:] #space and tab
```

## Subexpressions
Formed by round brackets around a part of the regex.

# Examples
* Exclude a certain word: If it occures once, we will not match: `^()`
* Test if string is an int/float number: `^[0-9]+((\.[0-9]+)|$)$`