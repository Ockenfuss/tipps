#Tipps concerning C


###Pointer
```C
double *a;//Initialize a pointer:
double b=0.0
&b//How to get the pointer from the variable:
```

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

##Strings

###Format specifier: 
https://codeforwin.org/2015/05/list-of-all-format-specifiers-in-c-programming.html
```C
%i//integer
%e//scientific notation
%f//float
%g//use e or f (what's shorter)
```
###String functions
```C
strcpy(dest, source);//copy source into destination. !Strings must be long enough!
strlen(str)//return length of string as integer
```


String zerteilen: Use `strtok`. Important: modifies string, so create a copy first!!
```C
char delimiter[] = ",;";
char *ptr;
ptr = strtok(string, delimiter);//Initialize: get pointer to first section
ptr=strtok(NULL, delimiter);//next call: Use NULL to get the next section
if(ptr==NULL)//If no more sections, NULL is returned
//the end of each section is marked with /0 (End of string)
for (token = strtok(input, delim); token != NULL; token = strtok(NULL, delim))//Short combination
}
```


##Compile
###Header files
Declare every function and type in a separate header file


###gcc flags
-iquote abc: set "abc" at the beginning of the list of quote directories, i.e. direcotries which are searched for #include "file"
-g #debug mode, important if you want to use gdb


###Debugging
gdb: Debugger for Linux