Tipps concerning C

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Language](#language)
  - [Variables](#variables)
    - [Pointers](#pointers)
      - [NULL](#null)
    - [Arrays](#arrays)
      - [Fixed Length Arrays](#fixed-length-arrays)
      - [Variable Length Arrays](#variable-length-arrays)
      - [Dynamic sized Arrays](#dynamic-sized-arrays)
    - [Structures](#structures)
      - [Define](#define)
      - [Access members](#access-members)
    - [Functions](#functions)
  - [IO](#io)
    - [Files](#files)
  - [Strings](#strings)
    - [Format specifiers:](#format-specifiers)
    - [String functions](#string-functions)
  - [Time and Date](#time-and-date)
  - [Networking](#networking)
    - [Sockets](#sockets)
- [Compile](#compile)
  - [gcc](#gcc)
    - [gcc flags](#gcc-flags)
  - [Debugging](#debugging)
  - [Profiling](#profiling)
- [Structure](#structure)
  - [Header files](#header-files)

<!-- /code_chunk_output -->
#Language

## Variables


### Pointers
```C
double *a;//Initialize a pointer:
double b=0.0
&b//How to get the pointer from the variable:
```
#### NULL
NULL is a special pointer that points nowhere. It cannot be dereferenced. Check for null pointer via: `if(ptr) printf("Pointer is null!");`

### Arrays
C does not know special array types, but continuous blocks of memory can be allocated. There are different types of arrays created in this way.
#### Fixed Length Arrays
Their length is already determined at compiletime. They are freed automatically.
```C
int array[5]; //Declaration of 5 elements space.
int array[5] = {1,2,3,4,5}; //With initialization.
int array[] = {1,2,3,4,5}; //Infer the number of elements from the initialization.
```

#### Variable Length Arrays
Their length is determined at runtime, but the size cannot be changed after initialization.
They are freed automatically
```C
int array[n]; //here, n is not a compile-time constant, but can be e.g. user input.
```

#### Dynamic sized Arrays
If you do not know the array size at compile time, you need to use dynamic memory allocation.
```C
int *array = (int *) malloc(size * sizeof(int)); //allocate a fixed number of bytes in  memory without cleaning and return a pointer to it
double *array= (double *)calloc(length, sizeof(double)); //initialize with 0
free(array); //free memory after usage. 
```

### Structures
#### Define
```C
typedef struct person{
    int a;
    int b;
}person;
```
#### Access members
```C
person paul;
paul.a=5;
person* philipp;
philipp->a=4//equals (*paul).a=5, i.e. we follow the pointer
```

### Functions
In C, functions are 'pass by values', i.e. the values passed to the function (actual parameters) are copied before being used inside the function (formal parameters).
```C
void fun(){} //simple function without return
double fun(){} //returns a double
void fun(int a){} //one parameter a
void fun(int *a){}//pass an array by passing the pointer. Remember that the pointer is copied first. Nevertheless, you can call AND MODIFY the values of the array inside the function, since the referenced values are not copied.
```

## IO
Output
```C
#include <stdio.h>
printf("Hello\n");
fprintf(stdout,"Numbers: %d %d\n",1,2);
sprintf(string, "Number: %i\n", 1); //write formatted output to string.
```
Input
```C
#include <stdio.h>
char c=getchar();//Read one char from stdin. If no character is present, wait until the user specified one or more char and presses ENTER. (if multiple char are typed in, the following calls to getchar() will first return these before waiting again!)
char string[10];
gets(string); //Read until newline from stdin. Buffer overflow possible!
fgets(string, 10, stdin);//Read until newline, but maximal 10 char (including \n and \0)
```
### Files
Get file attributes
```C
#include <sys/stat.h>
struct stat attributes;
stat("datei.txt", &attributes);
attributest.st_size; //filesize in bytes
```
Open, write and close files
```C
fwrite(*char, blocksize_bytes, num_blocks, stream) //write fixed number of bytes from a string to a stream. This does not care about null-char! If you want to include it (uncommon in files, but anyway), use num_blocks=strlen(str)+1 and blocksize_bytes=1
```
Manipulate file pointers
```C
#include <stdio.h>
i=ftell(fp);//get the current position in stream
rewind(fp);//set position to the beginning of the file
```

## Strings
They are represented by character arrays. The last character must be a `\0`, which signals the end of the string. This is used by many function, e.g. `strlen`.
```C
char string[]="hello world";//the c compiler will append the \0 automatically
```
### Format specifiers: 
https://codeforwin.org/2015/05/list-of-all-format-specifiers-in-c-programming.html
```C
%i//integer
%ld//long int
%zu//size_t
%f//float
%e//float scientific notation
%g//use e or f (what's shorter)
%s//string
%p//pointer
```
### String functions
```C
#include <string.h>
strlen(str); // return length of string as integer, excluding terminating null-char.
strcpy(dest, source); //copy source into destination. !Strings must be long enough and don't overlap! (use memmove in case of overlapping strings)
strstr(haystack, needle);//find the string needle in the string haystack and return a pointer to the first occurrence (null if not found)
int i = sscanf(string, "%s %d", strptr, &double); //try to read the values in the format string from the given string and put the results in the given variables. Returns the number of successfully read variables.
```


String zerteilen: Use `strtok`. Important: modifies string, so create a copy if necessary! No new memory is allocated, just replaces all delimiters by `\0` and sets the returned pointer to the beginning of a section.
```C
char delimiter[] = ",;";
char *ptr;
token = strtok(string, delimiter); //Initialize: get pointer to first section
token=strtok(NULL, delimiter);//next call: Use NULL to get the next section
if(token==NULL){} //If no more sections, NULL is returned
//the end of each section is marked with /0 (End of string)
for (token = strtok(input, delim); token != NULL; token = strtok(NULL, delim))//Short combination
}
```
## Time and Date
```C
#include <time.h>
time_t time1; //Standard time type. Represents time in seconds since 1970.
time1=time(NULL); //set to current time.
struct tm *time2=localtime(&time1); //convert to struct with tm_sec, tm_min, tm_hour,...
char *timestamp=ctime(&time1); //convert time_t to string representation.
char *timestamp=asctime(time2); //convert struct tm to string representation.
```
## Networking
### Sockets
* Socket=IP address and port
```C
#include <socket.h>
int Socket=socket(AF_INET, SOCK_STREAM, 0); //AF_INET: Use Internet (TCP/IP), SOCK_STEAM: two way stream (TCP), 0: standard protocoll for this socket type

```

# Compile

## gcc
### gcc flags
* -iquote abc: set "abc" at the beginning of the list of quote directories, i.e. direcotries which are searched for #include "file"
* -g: debug mode, important if you want to use gdb
* -Wall: Warn all. Enable a lot of warnings.

## Debugging
gdb: Debugger for Linux

## Profiling
perf: profiler for linux
Eventually, you need to set the kernel parameter: `sudo sysctl -w kernel/perf_event_paranoid=0`
`perf record --call-graph dwarf ./Main`
hotspot: GUI to analyze perf output (alternatively, use `perf report`): `hotspot perf.data`

# Structure
To execute a C program, you always need a main() function:
```C
int main(){} //the most simple form without command line arguments
int main(int argc, char **argv){
//argc will contain the number of command line arguments
//argv is the array containing the arguments. argv[0] will contain the name of the compiled program.
}
```
## Header files
Declare every function and type in a separate header file