# Tipps for creation of Makefiles
Manual: https://www.gnu.org/software/make/manual/html_node/index.html#Top
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Tipps for creation of Makefiles](#tipps-for-creation-of-makefiles)
  - [General](#general)
    - [Variables](#variables)
    - [Internal macros](#internal-macros)
    - [Filters and wildcards](#filters-and-wildcards)
    - [Multiline](#multiline)
    - [Phony](#phony)
  - [Deprecated stuff](#deprecated-stuff)
    - [Suffix rules](#suffix-rules)

<!-- /code_chunk_output -->

## General
The general structure is:
```makefile
target:prerequisites
    recipe
```
### Variables
```makefile
UV=abc
$(UV)#Use variable
```

### Internal macros
* `$<`: Name of first prerequisite
* `$*`: The "stem" where a rule matches, i.e. for dir/a.foo.b and rule a.%.b, $*=dir/foo
* `$@`: Target file to be created
* `$^`: Name of all prerequisites


### Filters and wildcards
*Filter all prerequisites for extension ".o": `$(filter %.o, $^)`

### Multiline
Make spawn a new subshell for each new line. Therefore, you cannot use multiline commands in the usual way, e.g. for an if-condition. Instead, you need to write them like
```makefile
check:
    if [ condition ]; then \
        command; \
    fi
```

### Phony
Phony targets are targets, whose name is not really the name of a file.
```make
.PHONY: clean
clean:
        rm *.o temp
```

## Deprecated stuff
### Suffix rules
They are deprecated and nowadays expressed by the general pattern rules. Nevertheless, you encounter them in some old makefiles sometimes.
```makefile
.c.o:
    rule #make .o files from .c files. As pattern rule, write '%.o : %.c'
```





