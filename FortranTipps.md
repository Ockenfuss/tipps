# Tipps for Fortran


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Tipps for Fortran](#tipps-for-fortran)
  - [General Language](#general-language)
    - [Loops](#loops)

<!-- /code_chunk_output -->

## General Language
### Loops
Do Loop:
```fortran
C set v to start, check if it is smaller than limit, otherwise execute code until statement with label 100, add increment and repeat
DO 100 v=start,limit,increment
    <code>
100 CONTINUE
```

### Strings
```fortran
C substring from 1 to 10. Both numbers are inclusive, i.e. the result contains 10 characters.
v(1:10)
```