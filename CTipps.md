#Tipps concerning C


###Pointer
#Initialize a pointer:
double *a;
#How to get the pointer from the variable:
double b=0.0
&b


#Create arrays
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
struct person{
    int a;
    int b;
};
```
####Access members
```C
struct person paul;
paul.a=5;
```

####Pointers to struct
```C
struct person *paul;
paul->a=5;//equals (*paul).a=5, i.e. we follow the pointer
```



//Format specifier: https://codeforwin.org/2015/05/list-of-all-format-specifiers-in-c-programming.html
%i: integer
%e: scientific notation
%f: float
%g: use e or f (what's shorter)



#####Complile#####



###gcc flags
-iquote abc: set "abc" at the beginning of the list of quote directories, i.e. direcotries which are searched for #include "file"
-g #debug mode, important if you want to use gdb


#######Debugging
gdb: Debugger for Linux