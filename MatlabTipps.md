Tipps for Matlab

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Language](#language)
  - [Arrays](#arrays)
    - [Cell Arrays](#cell-arrays)
  - [Control](#control)
    - [Loops](#loops)
  - [Strings](#strings)
  - [Functions](#functions)
    - [Use](#use)
    - [Declare](#declare)
    - [Optional arguments](#optional-arguments)
  - [I/O](#io)
  - [Dates](#dates)
- [Plotting](#plotting)

<!-- /code_chunk_output -->

# Language

## Arrays
```matlab
a=[1,2,3;4,5,6] % All matlab variables are multidimensional arrays. Separate matrix columns by ',' and rows by ';'. This works for objects in general
b=[a;a]
a(start:step:stop,1) % indices are one based! You can use slices in the form start:stop or start:step:stop
numel(a) % total number of elements in a
size(a) % dimension lengths of a
ndims(a) % number of dimensions of a
length(a) % length of longest dimension in a
```
### Cell Arrays
Consist of cells which are accessed by numbers and can contain different data types. They can be multidimensional, but must be rectangular.
```matlab
{'a', 1; 2, 'bc'} % 2x2 cell array
empty = cell(1,2,3) %empty 1x2x3 cell array
c(1,1:3) % get or set a subcell array with round brackets
c{2,3}   % access the contents with curly brackets
[v1, v2, v3] = c{1,1:3} % you cannot write a curly slice to a single list, because it contains different data types (but expansion works)x
```

## Control
### Loops
```matlab
for i = 1:10
    code
end
while a<10
    code
end
```

## Strings
```matlab
a="abc" % use ""
strlenghth(a) % lenght of string
a='abc' % character array. common before strings were introduced. 
```

## Functions
### Use
```matlab
a(b,c) % call function with two arguments
[a,b]=c $ function c returns two arguments, which are expanded into a and b.
```
### Declare
```matlab
function a=name(b) % function 'name' with input b and return value a
    a=2*b
end
sqr = @(x) x.^2 % 'anonymous' function. Compare to python lambda expr.
nargin % contains the number of provided arguments inside a function.
```
### Optional arguments 
```matlab

```

## I/O
Printing
```matlab
disp(A) %Display variables value
```
## Dates
```matlab
now % Current date as serial date number (fractional number of days since reference) call 'datetime(now, 'ConvertFrom', 'datenum')' to get datetime object
[datenum(2010,1,1):datenum(2010,2,28)] % Convert datetime to serial date number
```
# Plotting
```matlab
plot(x,y,'g:*') % plot a line plot with a green, dotted, star-marked line
hold on % plot the next plot into the same figure
```