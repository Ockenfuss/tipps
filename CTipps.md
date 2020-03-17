#Tipps concerning C


###Pointer
```C
double *a;//Initialize a pointer:
double b=0.0
&b//How to get the pointer from the variable:
```
#####NULL
NULL is a special pointer that points nowhere. It cannot be dereferenced. Check for null pointer via: `if(ptr) printf("Pointer is null!");`

###Create arrays
```C
bool boolArray[5] = {true , false , true , false , true}; //only with #include <stdbool.h>
int array[5];//Without defining values
double *distance= (double *)calloc(L, sizeof(double));//dynamic, but should be avoided usually
int *array = (int *) malloc(size * sizeof(int));//allocate memory without cleaning
free(distance); free(array);//important!!!
```

###Structures
####Define
```C
typedef struct person{
    int a;
    int b;
}person;
```
####Access members
```C
person paul;
paul.a=5;
person* philipp;
philipp->a=4//equals (*paul).a=5, i.e. we follow the pointer
```

##IO
Output
```C
#include <stdio.h>
printf("Hello\n");
fprintf(stdout,"Numbers: %d %d\n",1,2);
```
Input
```C
#include <stdio.h>
char c=getchar();//Read one char from stdin. If no character is present, wait until the user specified one or more char and presses ENTER. (if multiple char are typed in, the following calls to getchar() will first return these before waiting again!)
char string[10];
gets(string); //Read until newline from stdin. Buffer overflow possible!
fgets(string, 10, stdin);//Read until newline, but maximal 10 char (including \n and \0)
```

##Strings

###Format specifier: 
https://codeforwin.org/2015/05/list-of-all-format-specifiers-in-c-programming.html
```C
%i//integer
%zu//size_t
%e//scientific notation
%f//float
%g//use e or f (what's shorter)
%p//pointer
```
###String functions
```C
strcpy(dest, source);//copy source into destination. !Strings must be long enough!
strlen(str)//return length of string as integer
```


String zerteilen: Use `strtok`. Important: modifies string, so create a copy if necessary! No new memory is allocated, just replaces all delimiters by `\0` and sets the returned pointer to the beginning of a section.
```C
char delimiter[] = ",;";
char *ptr;
token = strtok(string, delimiter);//Initialize: get pointer to first section
token=strtok(NULL, delimiter);//next call: Use NULL to get the next section
if(token==NULL)//If no more sections, NULL is returned
//the end of each section is marked with /0 (End of string)
for (token = strtok(input, delim); token != NULL; token = strtok(NULL, delim))//Short combination
}
```


## Compile
### Header files
Declare every function and type in a separate header file


### gcc flags
* -iquote abc: set "abc" at the beginning of the list of quote directories, i.e. direcotries which are searched for #include "file"
* -g: debug mode, important if you want to use gdb
* -Wall: Warn all. Enable a lot of warnings.

### Debugging
gdb: Debugger for Linux

### Profiling
perf: profiler for linux
Eventually, you need to set the kernel parameter: `sudo sysctl -w kernel/perf_event_paranoid=0`
`perf record --call-graph dwarf ./Main`
hotspot: GUI to analyze perf output (alternatively, use `perf report`): `hotspot perf.data`