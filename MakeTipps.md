# Tipps for creation of Makefiles


### Internal macros
* `$<`: Name of first prerequisite
* `$*`: The "stem" where a rule matches, i.e. for dir/a.foo.b and rule a.%.b, $*=dir/foo
* `$@`: Target file to be created
* `$^`: Name of all prerequisites


###Filters and wildcards
*Filter all prerequisites for extension ".o": `$(filter %.o, $^)`




