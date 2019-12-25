# Tips concerning C++
##General language

### Variables
```C++
int a;//Declaration
int a=5;//Declaration & Initialization
auto a;//The type will be deduced from the type used by initialization
```

### Loops
Range based for loops:
```C++
for(auto i:v){}//Loop over vector v elements
for(int a:{1,2,3})//Loop over 1,2,3
```

### IO
```C++
#include <iostream>
std::cout<<"Here" <<endl;//Print on stdout
#include <fstream>
std::ofstream outfile ("Test.txt");
int a,b;
cin >> a >> b;//Read two variables from stdin. Any kind of space (tab, newline) can serve as a separator.
```


###Data containers
Classical (multidimensional arrays)
```C++
int a[3]={1,2,3};
int x[3][4] = {0, 1 ,2 ,3 ,4 , 5 , 6 , 7 , 8 , 9 , 10 , 11};//Multidimensional Array. The are still handled linearly in memory (more effective)!
int x[3][4] = {{0,1,2,3}, {4,5,6,7}, {8,9,10,11}};//Alternative initialization
```


Vector: Like an array, but additional elements can be stored and memory is extended automatically. However, less memory efficient than arrays due to memory overhead for extension.
```C++
#include <vector>
std::vector<int> v = {7, 5, 16, 8};//create
v.push_back(25);//add element
```
Stack: stacked memory with last-in, first-out (LIFO) logic. Vectors already serve stack functionality.

Queue: memory with first in, first out (FIFO) logic.
```C++
#include <queue>
queue<int> myqueue; //Declare
myqueue.push(0); //Add element
myqueue.front(); //Get elemnt from front
myqueue.pop();  //Delete element from front
```

Deque: "double ended queue": Array, where elements can be inserted on both ends.
```C++
std::deque<int> d = {7, 5, 16, 8};//create
d.push_front(13);//Add element to front
d.push_back(25);//Add element to back
d.pop_back();//Remove last element
d.pop_front();//Remove first element
```
