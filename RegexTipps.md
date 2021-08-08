<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [General](#general)
  - [Logical operators](#logical-operators)
  - [Occurences](#occurences)
  - [Special matches](#special-matches)
  - [Character groups](#character-groups)
  - [Subexpressions (or Groups)](#subexpressions-or-groups)
  - [Lookahead and lookbehind](#lookahead-and-lookbehind)
- [Examples](#examples)

<!-- /code_chunk_output -->


# General
Page where you can insert a regex to get an automatic explanation of its parts:
http://rick.measham.id.au/paste/explain.pl
Escape a regex char by using `\\`, e.g. match a point with `\\.`.



## Logical operators
```bash
[^a] #Exclusion
```
* logical or: `a|b`

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

## Subexpressions (or Groups)
Formed by round brackets around a part of the regex. They allow you to apply quantifiers and similar things to the entire regex within `()`. Additionally, the match within the brackets is captured so you can access it separately in your code.
```bash
(ba.)? #matches e.g. 'bad' or 'bag' if it appears zero or one time and stores the match (e.g. 'bad')
(?:ba.)? #Non-capturing group. Same as above, but the match is not stored for later use
```

## Lookahead and lookbehind
https://www.regular-expressions.info/lookaround.html
They match a part of the string, but do not consume the matched characters, but only return match or no match.
```bash
(?=u) #positive lookahead. Matches the u in quit, but does not move on to the following i, i.e. the following regex will continue from the u as well
(?!u) #negative lookahead. Success if u does not match.
(?<=u)#positive lookbehind. step back one char in the string and check for a match. Similarly to lookahead, it does not consume the current char, so in 'quit', if we are at 'i' it would match the preceeding 'u', but stay at the 'i' for the next regex part.
```
Examples
```bash
(?=[+-]?\d*)[\d+-]{5} #match any exactly 5 character integer, like 12345 or -1234 or +1234. Here, you can see the lookahead like an if statement: Match 5 numbers and signs, but only if the appear in the right order, which is checked by the lookahead
```


# Examples
* Exclude a certain word: If it occures once, we will not match: `^()`
* Test if string is an int/float number: `^[0-9]+((\.[0-9]+)|$)$`