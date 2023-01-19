

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python General](#-python-general)
  - [Installation](#-installation)
  - [Virtual Environments](#-virtual-environments)
    - [Venv](#-venv)
    - [Conda](#-conda)
  - [Code Formatting](#-code-formatting)
  - [General](#-general)
    - [Loops and Conditions](#-loops-and-conditions)
    - [Boolean operators](#-boolean-operators)
    - [Functions:](#-functions-)
      - [Type hints](#-type-hints)
    - [Variable reference in Python](#-variable-reference-in-python)
    - [Datatypes](#-datatypes)
      - [Complex Numbers](#-complex-numbers)
    - [Strings](#-strings)
      - [f-Strings](#-f-strings)
      - [Regex](#-regex)
    - [Arrays](#-arrays)
    - [Lists](#-lists)
    - [List comprehensions](#-list-comprehensions)
    - [Slices](#-slices)
    - [Iterables](#-iterables)
      - [Zip](#-zip)
    - [Hashables](#-hashables)
    - [Sets](#-sets)
    - [Dictionaries](#-dictionaries)
  - [IO](#-io)
    - [File paths](#-file-paths)
      - [Glob](#-glob)
      - [Temporary Files](#-temporary-files)
      - [Shell](#-shell)
    - [CLI Arguments](#-cli-arguments)
  - [Exceptions](#-exceptions)
  - [Object Orientation](#-object-orientation)
    - [Decorators](#-decorators)
    - [Get/Set](#-getset)
    - [Operator overloading](#-operator-overloading)
  - [Datetime module](#-datetime-module)
    - [Creation](#-creation)
    - [Operations](#-operations)
  - [time Module](#-time-module)
  - [Serialization](#-serialization)
    - [JSON](#-json)
    - [Pickle](#-pickle)
- [Numpy](#-numpy)
    - [Numpy I/O](#-numpy-io)
    - [Numpy Arrays](#-numpy-arrays)
    - [Indexing](#-indexing)
    - [Basic Slicing](#basic-slicing)
    - [Numpy sortieren](#-numpy-sortieren)
  - [Numpy Array Transformations](#-numpy-array-transformations)
    - [Broadcasting](#-broadcasting)
      - [Numpy Array reshape](#-numpy-array-reshape)
    - [stack/extend/combine/transpose numpy arrays](#-stackextendcombinetranspose-numpy-arrays)
    - [combine multidimensional arrays](#-combine-multidimensional-arrays)
    - [masked arrays](#-masked-arrays)
  - [Numpy Datentypen](#-numpy-datentypen)
  - [Numpy Funktionen](#-numpy-funktionen)
  - [Statistics](#-statistics)
  - [Fourier Transformations](#-fourier-transformations)
- [Scipy](#-scipy)
  - [Statistics](#-statistics-1)
    - [Distribution functions](#-distribution-functions)
  - [Interpolation](#-interpolation)
    - [Onedimensional](#-onedimensional)
    - [Multidimensional](#-multidimensional)
- [Pyplot/Matplotlib](#-pyplotmatplotlib)
    - [Create plot](#-create-plot)
    - [Axes and Ticks](#-axes-and-ticks)
    - [Beschriftung mit Latex](#-beschriftung-mit-latex)
    - [Legende](#-legende)
    - [Dates](#-dates)
    - [Lines and colors](#-lines-and-colors)
      - [Specifiying colors](#-specifiying-colors)
      - [Linestyle cycle](#-linestyle-cycle)
    - [colorbar](#-colorbar)
      - [Create colorbar](#-create-colorbar)
      - [Colorbar limits and scale](#-colorbar-limits-and-scale)
      - [Color cycle setzen](#-color-cycle-setzen)
    - [Modify colormaps](#-modify-colormaps)
    - [Zweite Axe rechts:](#-zweite-axe-rechts)
    - [Lines and Shapes](#-lines-and-shapes)
    - [Saving figures](#-saving-figures)
    - [Backend](#-backend)
    - [Arange subplots](#-arange-subplots)
    - [Text and annotations](#-text-and-annotations)
    - [Plot types](#-plot-types)
      - [Lines, points and bars](#-lines-points-and-bars)
      - [Histograms](#-histograms)
      - [Images (2D Verteilung) plotten](#-images-2d-verteilung-plotten)
    - [Animationen](#-animationen)
    - [Interaction](#-interaction)
  - [Subprocess](#-subprocess)
- [Pandas](#-pandas)
    - [Create Data Frame](#-create-data-frame)
    - [read from file](#-read-from-file)
    - [Acces elements](#-acces-elements)
    - [get columns](#-get-columns)
    - [Categories in one column](#-categories-in-one-column)
    - [iterration over rows](#-iterration-over-rows)
    - [Groupby](#-groupby)
- [Geopandas](#-geopandas)
  - [Maps (Contextily)](#-maps-contextily)
    - [Plot geopandas](#-plot-geopandas)
    - [Details](#-details)
- [MetPy](#-metpy)
- [NETCDF](#-netcdf)
- [Xarray](#-xarray)
  - [Creating data](#-creating-data)
  - [Reading & Writing](#-reading--writing)
  - [Inspecting data](#-inspecting-data)
  - [Selecting data](#-selecting-data)
  - [Asignments](#-asignments)
  - [Coordinates](#-coordinates)
  - [combining/extending data](#-combiningextending-data)
  - [Modifying data](#-modifying-data)
  - [Computation](#-computation)
  - [Time Series](#-time-series)
  - [Broadcasting](#-broadcasting-1)
  - [apply_ufunc](#-apply_ufunc)
  - [Plotting data](#-plotting-data)
  - [HVPlot](#-hvplot)
  - [Dask](#-dask)
- [Image processing](#-image-processing)
  - [Convolution](#-convolution)
- [IPython Jupyter](#-ipython-jupyter)
  - [Magic commands](#-magic-commands)
- [Creating your own modules](#-creating-your-own-modules)
  - [Module Structure](#-module-structure)
  - [Special files](#-special-files)
    - [Init](#-init)
    - [Requirements.txt](#-requirementstxt)
    - [Setup.cfg & Setup.py](#-setupcfg--setuppy)
    - [pyproject.toml](#-pyprojecttoml)
    - [pre-commit](#-pre-commit)
  - [Resources](#-resources)
  - [How to write proper docstrings for functions/classes:](#-how-to-write-proper-docstrings-for-functionsclasses)
- [Unittests](#-unittests)
  - [Execute tests](#-execute-tests)
- [Profiling](#-profiling)
  - [cProfile and pstats](#-cprofile-and-pstats)

<!-- /code_chunk_output -->


# Python General

## Installation

```bash
`sudo apt install python3`
Pip: `sudo apt install python3-Pip`
install package with pip: use `--user` flag if you have problems
python3 -m pip install package #install packages. Use package==1.0.1 to install a specific version
pip uninstall package #remove package
pip3 list #list installed packages
pip3 freeze > requirements.txt #list installed and version, in the form for requirements.txt
python3 -m pip install --upgrade pip #Upgrade pip. Here, it is necessary to call pip via `python3 -m`, since this loads the module into memory before execution. This is necessary, since pip will be uninstalled first and then the new version is installed.
```

## Virtual Environments
### Venv
venv ships with python
```bash
mkdir MyEnv; cd MyEnv #make a folder for the environment. Can be in your package folder, but does usually not belong to the project (put in .gitignore)
python3 -m venv env #create virtual environment
source bin/activate #activate virtual environment
pip3 install package # install packages. Do not use sudo! Use pip install -r requirements.txt to install version specifically for your package.
pip freeze > requirements.txt #Export current environment
deactivate #Deactivate virtual environment
```
### Conda
```bash
conda init #Initialize conda in the beginnind. Will create a .conda folder in your home directory
conda create --name py35 python=3.5 #Create virtual environment
conda env create -f environment.yml #Create from file
conda env update -f environment.yml --prune #update environment based on yml file, removing packages not in yml anymore
conda env list #List virtual environments
conda activate MyEnv #activate environment
conda env remove --name MyEnv #remove environment
conda rename -n old_name -d new_name #rename. Workaround, which internally clones environment and downloads all packages again.
conda list #List all packages and versions in environment
conda env export --from-history #List only explicitly installed packages
conda install NAME #Install package
conda update NAME #Update package
```
A conda environment can be configured in a .yml file. For an existing environment, this file can be created with:
`conda env export --name MyEnv --from-history`
```yml
name: my-env
channels:
  - conda-forge
  - anaconda
  - defaults
dependencies:
  - python=3.8
  - pip
```
In a conda environment, the PYTHONPATH variable is not respected. One way to activate local packages is to put a file like MyPackages.pth unter `.conda/envs/NAME/lib/python3.10/site-packages`. In it, just list the components of PYTHONPATH, separated by newline.
```txt
/full/path/to/packagecollection1
/full/path/to/packagecollection2
```

## Code Formatting
Typically, you would use a linter or linter package like `flake8` (pip install flake8), which formats your code according to certain style guides. Project specific settings should usually be placed in the `setup.cfg` file.
```python
[flake8]
ignore =
    E402 # module level import not at top of file
    E501 # line too long. VSCode will read setup.cfg automatically.
```


## General
Beendet ein Python Program 
```python
import sys
sys.exit()
```
### Loops and Conditions
```python
if condition: #if conditions
  code
elif condition:
  code
else:
  code
a=0 if condition else a=1 #ternary operator
```
```python
for i in iterable:#for loop
  code
while condition:#while loop. There is no do-while loop in python
  code
```

### Boolean operators
```python
if a < b < c: #python supports chained comparison operators. This is equal to (a < b) and ( c < d)
```

### Functions: 
often use "args" and "kwargs" (=keyword arguments) to pass additional arguments to new function.
Syntax: *args or **kwargs This is part of a more general behaviour: * unpacks an array or list so its elements can be function arguments, ** does the same with a dictionary (creating named arguments)
#### Type hints
https://realpython.com/python-type-checking/
They have no effect during runtime, but help understanding the code and are often used by linters to detect errors and deliver better suggestions.
```python
def myfunc(a: str, b : int = 5) -> str:
import typing as tp
def myfunc(a : tp.Union[str, int]) -> str: #Specify multiple possible input types. From Python
```

### Variable reference in Python
in general, every object has an id (similar to pointer in C)
Function arguments are in general by reference, i.e. inside the function, we are dealing with a new reference for the original object
Generally, expressions are evaluated from the right
Expressions like a=a+10 (a can be numpy array!): Create a new, deep copy and assign its reference to a

### Datatypes
```python
int(x) #convert to integer
chr(97) #convert to character 'a'
str(97) #convert to string "97"
```

#### Complex Numbers
```python
z=3 + 2j #define complex number
complex(3,2) #alternative via factory function
z.real # Real part
z.imag #Imaginary part
abs(z) #Amplitude
cmath.phase(z) #Phase
```

### Strings
```python
test="Hallo"+"du" #Combination
8*'hey' #Repetition
if 'll' in 'Hallo' #Test for substrings (no need for regex here)
"Hallo".startswith("Ha") #check for prefix (similar: endswith)
```
Split and combine arrays
```python
",".join(arr) #print array elements with the given separator (if necessary: use `[str(i) for i in arr] first`)
string.split(",")#split string into array of strings with the given separator
```
Modify
```python
string.strip("\n")#remove at beginning or end
string.replace('a','b')
string.lower()# turn to lowercase
```
Format specifiers: These are deprecated, better to use f=Strings!
```python
"%d %f %s"%(1, 0.314,"hallo")#the % operator applied to strings will insert the values from the tuple into the format string.
```
#### f-Strings
https://realpython.com/python-f-strings/
A way to 'insert' python code into strings. Currently the recommended way to format strings (python 3.6 or newer).
```python
f"Hello {name}"#Allow to directly evaluate python expressions within {}
f"This is {object!r}"#By default, __str__ of an object is used, but with '!r' we can switch to __repr__
f"{number:.3f}"#You can use format specifiers in f strings
```
#### Regex
https://realpython.com/regex-python/
```python
import re
re.findall('ABC', 'ABCD')#Return match
match=re.search('([0-9]*)',string) #search for all matches. Use () to capture groups. Return None if no match is found, so you can use it like:
if re.search... :
match.groups()#Tuple with all groups. () needs to be defined!
match.group(1)#Select a group. Index is one-based!

```


### Arrays
returns the position as well as the value of the array
```python
for index, values in enumerate(array, start)
```
`numpy.ndenumerate:`
Extremely useful for looping over multidimensional arrays! Gives index as tuple.
if index should be single value: `enumerate(array.flatten())`

Converts scalars to array and leaves everything else untouched=>Usefull for functions to handle scalars as well arrays
```python
np.atleast_1d(arrays)
```
convert to 2d by "adding one pair of brackets": array2d=[array1d] or array2d=\[[scalar]]
```python
np.atleast_2d(array)
```

### Lists
Arrays, which can contain different data types and can be extended dynamically
```python
list=[]
list.append("Hello")
list.append(liste2)#list of lists
a=[1]+[2,3]#List concatenation
b=[1]*3#=[1]+[1]+[1]
if a: #a returns false is len(a)=0 (list is empty). The same holds for most collections like dict, tuple, ...
a.pop() #return and remove last element from list. With pop(), you can use a list as a stack. Use pop(0) to remove front or any other index (simple queue)
```
### List comprehensions
```python
arr=[expr(i) for i in indices]
arr=[expr(i) for i in indices if condition(i)]
arr=[expr(i) if condition(i) else expression2(i) for i in indices]
```

### Slices
```python
sl=slice(1,2,3)#Creates a slice object, which can be used to slice strings or lists
sl.start#slice objects have members start, step and stop
```

### Iterables
Closely related to list comprehensions are generator expressions. They create iterables which do not get evaluated immediately. Iterables are objects which support the __next__() method, which returns the next iteration state.
```python
iterable=(obj.evalute() for obj in objlist)
```
Generators can be created with the `yield` operator. It is similar to `return`, but keeps the function state in memory and continues execution when the next element is requested.
```python
def com(l, k):
  """Example: Generates an iterator over all possible k-size subsets of l"""
    if k==0:
        yield []
    elif k>=len(l):
        yield l
    else:
        for com_without in com(l[1:], k):
            yield com_without
        for com_without in com(l[1:],k-1):
            yield [l[0]]+com_without
```
There are a lot of useful functions, which work with iterables.
#### Zip
```python
zip_iter=zip(a,b,c)#zip takes multiple iterables and aggregates the first, second,... elements each in a tuple. It returns an iterator.
transposed=list(map(list, zip(*l))) #With zip, you can "transpose" a list of lists
list1, list2=zip(*sorted(zip(list1, list2)))#Sort multiple lists according to the first one
for i,j in zip(l1,l2) #iterate over multiple lists in parallel. With .items(), this works for dicts as well.
from itertools import zip_longest
zip_longest(a,b,c, fillvalue=" ")#usually, zip stops after the shortest iterable reaches its end. Zip_longest will continue and insert fill values instead.
```

### Hashables
An object is hashable if it has a hash value which never changes during its lifetime (it needs a `__hash__()` method), and can be compared to other objects (it needs an `__eq__()` or `__cmp__()` method). Hashable objects which compare equal must have the same hash value. (from the Python glossary)
### Sets
Unordered collections, where each element appears only once. Pretty much the same thing as you know from mathematics! Elements must be immutable
https://realpython.com/python-sets/
```python
a=set(['foo', 'foo', 'bar']) #Create from iterable of immutables. Result: a={'foo', 'bar'}
a={'foo','bar','baz'} #Alternative definition
a | b #Union: elements in a or b
a & b #Intersection: elements in a and b
a - b #Difference: elements in a and not in b
a <=b #a is subset of b
a < b #a is real subset of b
a == b #elements in a and b are equal
a |=b #Update a to be a | b. Works with & and - as well
```

### Dictionaries
Unordered storage vor key-values pairs.
```python
example={"key": value, "key2": value2}
example["key2"]#Access elements by key
d=dict(zip(keys, values))#use dict to create a dictionary from a list of key-value tupples (zip creates such a list from key and value lists)
list(d.keys())#get keys as a list. Similar: d.values()
for k,v in d.items(): #items() provides a view on the dict keys and values, which is useful for iterations
dict1 | dict2 #Merge two dicts to have the union. In case of conflict, values from dict2 replace values of dict1
dict1 |= dict2#update a dictionary in place with the values from another one (replace keys or create if not existing). TODO: requires Python >3.9
d.get('key',default)#return default if key not existent
d.pop('key', default)#return & remove key if existing and return default otherwise
func(**kwargs):
  key=kwargs.pop('key', default)#Very useful for function argument defaults
```

## IO
### File paths
Old: the os module. For python 3.5+, use the object-oriented pathlib module!
```python
import os.path
os.path.join(str1, str2) #join to one filepath
os.path.basename(path)#basename if a file, empty for directory. might not work with Windows
os.path.abspath(path)#get the absolute filepath
os.path.dirname(path)#directory name
os.path.splitext(filename)#tuple with Path+Name and Extension
os.path.isfile(filename)#check for type or existence
```

How to use Pathlib from the standard library:
```python
from pathlib import Path
Path("a/b/c.txt") #create from string
p=Path.cwd() #current working directory
p / "a" / "file.txt" #you can use the '/' operator to join path objects (and strings)
p.mkdir(parents=True, exist_ok=True) #Make directories
p.resolve() #Get the absolute path
p.parent #get the parent path (as path object).
p.name #get the filename
p.suffix #get the file extension as string
p.stem #get the final path component without the suffix as string
p.with_suffix('.jpg') #replace file extension. Use '' to remove file extension.
p.glob('*.py') #get list of paths matching glob in the given directory
str(p) #the "traditional" string representation of a path
```
For opening file streams:
```python
with open('file', 'w') as f:#w: writing, r: reading, a: append
  f.readline(size=-1)#Read line or at most size char.
  f.readlines()#Read all remaining lines and give a list
  for line in f:#f is an iterable over the lines
  f.write(str)#write string
  f.writelines(seq)#NO line endings are added
```
#### Glob
Unix style pathname expansion
```python
import glob
glob.glob('*.py') #return list with all python files in current directory
```
#### Temporary Files
use `tempfile` from the standard library
```python
f, name=tempfile.mkstemp(".nc", "Gauss", "Directory")#Create a temporary file and return file handle and name
```
#### Shell
```python
import os
os.environ["HOME"] #Access environment variables
expanded=os.path.expandvars(string) #expand environment variables in a string
``` 
### CLI Arguments
```python
import sys
sys.argv[1]#Command line arguments. argv[0] contains program name. 
```
`argparse` is a useful package in the standard library to parse command line arguments
```python
import argparse
par=argparse.ArgumentParser(description="What this script does")
par.add_argument('-f', type=str, help="filepath")#Add command line arguments
par.add_argument('-f','--filename', type=str, help="filepath")#you can specify a short and long name
par.add_argument('infile', nargs='?', default="abc")#consume zero or one argument (like Latex '?'!). Take default if zero arguments are present.
par.add_argument('-i', type=int, default=1)
par.add_argument('-s',action='store_true')#Boolean flag
args=par.parse_args()
args.filename#Access argument values
```
## Exceptions
Rasising Exceptions
```python
raise Exception("Message")
assert(1==2)#Assertions raise an AssertionError
```

Try statement
```python
try:
  somecode()
except KeyError: #multiple exceptions: except (KeyError, ValueError, ...):
  someOtherCode #Can use 'pass' to jump out of this section
else:
  code #if no exception was thrown
finally:
  code #Always execute this code. Usually, you can also write it directly after without finally
```
Never do this: `try ... except: pass`! Catching all exceptions, regardless of the type, makes debugging almost impossible!

Custom Exceptions
```python
class MyError(Exception): #Derived from Exception class
    def __init__(self, value): 
        self.value = value 
    def __str__(self): 
        return(repr(self.value)) 
```



## Object Orientation
General syntax:
```python
class Test(object):#Derived from 'object'
  def __init__(self, var1, var2):#Konstruktor
    self._var1=var1
    self._var2=var2
    self.__dict__.update(kwargs) #shortcut to set all keyword arguments as class attributes
    super().__init__()#If derived from another class, we can access parent methods through super()
  
  @classmethod
  def from_string(cls, string):#The recommended way to create different Constructors are multiple classmethods
    v1,v2=parse(string)
    return cls(v1,v2)

  def method(self, var):
    dosomething
  def _method2(self, var):#Private method
    dosomething
    return something  
  def __str__(self):#This method is invoked by 'repr(obj)' and returns a string representation for the object
    return repr(self.var1)
```
Comparing objects:
https://realpython.com/python-is-identity-vs-equality/
```python
mo=MyObject()
type(mo)==MyObject#Check the exact type
isinstance(mo, MyObject)
isinstance(mo, Parent)#Is instance is also true for the parent type
mo1==mo2#This checks whether the objects are equal according to their __eq__ implementation (for example they have the same content). Similarly, you can overload __ne__, __le__, __lt__, __ge__, __gt__ for the other comparison operators.
mo1 is mo2#Whether mo1 and mo2 really point the the same instance in memory
```

Object introspection
Get information about an object and its members.
```python
dir(obj) #list attributes and methods
import inspect #module to get detailed information about objects
inspect.getmembers(obj) #list members
```
### Decorators
https://realpython.com/primer-on-python-decorators/
Decorators: define two functions a:int->int, F:func->func. Now, you can do `a=F(a)` to get a new function a passed through F. Usually, F is a wrapper that does some pre and post processing. Shorthand for this is `@F`. Useful applications: Debugging: Print function arguments! Timers, Register function in dict, ...
```python
import functools
def F(func):
  @functools.wraps(func) #this line ensures that the wrapped function returns the original .__name__ attribute
  def wrapper(*args, **kwargs):
    #do something before
    val=func(*args, **kwargs)
    #do something after
    return val
  return wrapper
@F
def a(var):
  ...
```

### Get/Set
```python
class OurClass:
    def __init__(self, a):
        self.var = a
    @property
    def var(self):
        return self.__var
    @var.setter
    def var(self, val):
        if val < 0:
            self.__var = 0
        else:
            self.__var = val
```

### Operator overloading
https://realpython.com/operator-function-overloading/#making-your-objects-capable-of-being-added-using
Implement by use of special methods like `__add__`, `__mul__`,... By convenction, add and similar should return a new instance of the class!
```python

```

## Datetime module
Datum und Zeit
Übersicht: https://www.programiz.com/python-programming/datetime
### Creation
```python
from datetime import datetime
from dateutil.parser import parse
t=datetime(2021,4,3) #specify year, month, day, hour, ...
time = datetime.strptime("8.21.2017 15:00:00","%m.%d.%Y %H:%M:%S") #date parsed from string
"%m.%d.%y %H:%M:%S.%f"#falls mit Milliseconds
time.strftime("%H:%M") #String from date
datetime.date.today() #get current date
```

### Operations
```python
from datetime import timedelta
(a-b).total_seconds() #Difference in seconds
t=t+timedelta(hours=7) #Add times
t2=t.replace(hour=8,month=8) #Create new datetime from existing
```



## time Module

```python
import time
time.sleep(5.5)#5.5 seconds pause
```
## Serialization
Idea: convert python objects to byte streams, which you can send or store. There are three modules in the python standard library for this:
* `marshal`: Do not use this one. Mainly for the python interpreter.
* `pickle`: Serialize to binary, supports many types
* `json`: Save as human-readable ascii file, only limited types.

### JSON
Supports:   int, long, float, str, tuple, list, dict, True, False, None
```python
import json
with open('file.json' 'r') as f:
  data=json.load(f) #read object from json
with open('file.json', 'w') as f:
  json.dump(data,f, indent=4) #dump data to file
```
Here you find an example including strings, ints, float, lists and dictionaries:
```json
{
 "manufacturer": "Superrad",
 "wheels": 2,
 "users": ["Jim", "Tina"],
 "location": {"lat": 52.3, "lon": 9.8}
} 
```

### Pickle
```python
import pickle
with open("file",'wb') as f:
  pickle.dump(obj, f)#write object to file
  pickle.load(f)#read object from file
```



# Numpy
### Numpy I/O
```python
np.save("folder/file",array)#save as binary numpy object
array=np.load("folder/file.npy")#load binary object
array=np.genfromtxt("file")#load from asciifile
A=np.genfromtxt('file_name',skip_header = N,max_rows =1)#read only specific line/range
```

### Numpy Arrays
```python
a=np.zeros(100)
b=np.ones((10,20))#2d Array
b.shape#Tuple (10,20)
b.size#Number of elements: 200
b.ndim#NUmber of dimensions: 2
```

### Indexing
Boolsche Indizes: auswählen eines bestimmten Teilarrays
<,>,== geht direkt, für Verknüpfung (Oder, Und) mehrerer Ausdrücke:
```python
b=np.logical_and(t<deltat, t>=0)
```
Elementwise boolean operations: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.logic.html
```python
np.logical_and(a,b)#perform logical and elementwise
```
###Basic Slicing
```python
array[start:stop:step]#if start/stop<0, replace by start/stop+n with n the dimension of the axis
```


### Numpy sortieren
argsort: Liefert array mit den Indizes in der sortierten Reihenfolge => einsetzen liefert sortiertes Array
```python
np.unique(a, return_counts=False)#Find unique elements or count elements
ind=np.argsort(a)
print(a[ind])#sortiert
def multiargsort(array):#for multidimensional arrays, we can flatten them first
    flat=array.flatten()
    ind=flat.argsort()
    return np.unravel_index(ind,array.shape)#unravel_index does the stride arithmetic to convert linear to multidimensional indices
np.searchsorted(a,v)#a must be sorted. Find the places where the elements of v must be inserted. Use it e.g. to find the nearest/closest values to v in a.
def nearest(a,v):
    assert(np.all(np.diff(a)>=0))#check sorted
    _am=convolve(a,[0.5,0.5],mode='valid')#from scipy.signal import convolve
    return a[np.searchsorted(_am, v)]
```


Numpy Elemente finden: np.where gibt array zurück mit allen reihenindizes in einem array und allen columnindizes in zweitem.Bsp:
```python
a=[1,1,1,2,2,3]
indexarray=np.where(a==1)#gibt array: (array([0, 1, 2]),)=> indexarray[0] ist also [0,1,2] für die vorkommen von "1" in a
np.amax(array)#maximum of array
np.argmax(array)#index of maximum
```

## Numpy Array Transformations
### Broadcasting
https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
Whenever you are doing arithmetic with arrays, it is on an element-by-element basis. However, what happens if the arrays do not have the same shape? In this case, the dimensions are compared, starting from the last dimension. If their lengths are not the same, one of them has to be length one. This one will be repeated before applying the arithmetic.
See the example:
```python
A      (4d array):  8 x 1 x 6 x 1
B      (3d array):      7 x 1 x 5
Result (4d array):  8 x 7 x 6 x 5
#This does not work:
A      (2d array):      2 x 1
B      (3d array):  8 x 4 x 3 # second from last dimensions mismatched
```
#### Numpy Array reshape
Imagine the old array to be flattened first: First, the last dimension is counted up (0,1,2,3...), then the second last is raised +1 and the last counted up again and so on.
Secondly, the resulting 1d array is filled into the new one by the same principle: the first (50) elements of the 1D array are put in the last dimension (0-50), then the second last dimension (0-400) is raised +1 and the next (50) elements are put into the last dimension (0-50) again, and so on.
```python
new=old.reshape((3,400,50))
```

### stack/extend/combine/transpose numpy arrays
```python
np.column_stack((arr1, arr2, arr3))#combine 1D arrays to 2D
np.row_stack((arr1, arr2, arr3))
np.tile(arr,(3,1))#can also be used to repeat an array. Introduces new dimensions as neccessary. E.g., this will repeat a 1D array 3 times in a second dimension (and additionally 1 time in the existing dimension)
np.repeat(arr1[:, :, np.newaxis], n_repeat, axis=2)#Alternative to repeat an array
arr.transpose(1,0,2)#switch the order of axes. Similar to arr.T in two dimensions
xgrid, ygrid=np.meshgrid(x,y,indexing='ij')#make e.g. two 2D grids of two 1D arrays. With ij, every column of xgrid equals x, every row of ygrid equals y. This is the "matrix interpretation".
array=np.roll(array, shift=(1,2), axis=(0,1))#Make a cyclic shift of an array
```
### combine multidimensional arrays
```python
np.concatenate((arr1, arr2), axis=1)#must have same dimensions except on the concatenation axis
```
### masked arrays
numpy support masked arrays with `numpy.ma` module. These are useful in combination with e.g. some plots
```python
arr_mask = np.ma.masked_where(mask, arr)
ax.imshow(arr_mask, cmap=mymap)#use mymap.set_bad('b') to set the masked values to blue!
```
## Numpy Datentypen
```python
arr2=arr1.astype(int)#Array conversion
```

## Numpy Funktionen
```python
np.mean(Array, Axis=0)#Numpy
np.histogram2d(x,y,weights=z, bins=10)#1 or 2d histogram in numpy. See also binned_statistics in scipy
np.arctan2(y,x)/np.pi*180#Gives the angle of a point (in radians!) x,y including information about the quadrant (be aware: arctan2(y,x), NOT x,y!)
#x=1, y=1: 45°, x=-1, y=1: 135°, x=-1, y=-1: -135°, x=1, y=-1: -45° (upper half (y>0) positive angles, lower half negative angles)
#Easy transformation 0 to 360: (360+angle)%360
np.interp(x_new, x_old, y_old)#perform linear interpolation of the old values at the adjacent old points. x_old must be increasing if not specified further!
np.trapz(y, x)#integral over y (sampling points located at x)
```

## Statistics
```python
np.random.rand(*arr.shape)#produce random numbers between 0 and 1 in an array with the given dimensions
np.random.normal(0,1,(2,2))#produce normal distributed values in an array with the given shape
np.random.multivariate_normal(a,b)#produce a set of numbers (vector), such that these variables in the limit of many observations have the given covariance matrix b (around the mean vector a).
```

## Fourier Transformations
```python
sig_f=np.fft.fft(sig)#Simple discrete Fourier transform
sig2d_f=np.fft.fft2(sig2d)#For 2d arrays (images)
```
Sig_f contains the amplitudes corresponding to the frequencies given from `np.fft.fftfreq(N, d=1.0)`, with `N=len(sig)`. The general format is [k0, k1, ..., kN/2, k(-N/2), ... k(-1)], and the values are just kn=n/(N*d). Therefore, to get the real frequencies k we usually want in e^(ikx), we have to set d=dx/(2 * pi), with dx the spacing of the real space points in `sig`.


# Scipy
## Statistics
```python
from scipy import stats
stats.binned_statistic_2d(x, y, values, 'mean', bins=[binx,biny])#Extended version of histogram2d in numpy. Also allows to take the mean and more over all weights.
```
### Distribution functions
stats contains a lot of statistical distribution functions like gaussian, lognormal or poisson. You can easily create samples, plot the function and more
```python
from scipy.stats import norm, lognorm
norm # Gaussian distribution
lognorm #lognormal distribution
norm.pdf(values, loc, scale) #evaluate gaussian at values: mean:loc  standard dev:scale
norm.cdf(values, loc, scale) #cumulative distr. function
norm.ppf(values, loc, scale) #Percent point function (inverse of cdf)
samples=norm.rvs(size=100) #Get gaussian samples
```

## Interpolation
### Onedimensional
```python
from scipy.interplate import interp1d
f=interp1d(x,y,kind='cubic') #linear or cubic (spline) interplation
ynew=f(xnew) #returns a callable object
```
### Multidimensional
https://stackoverflow.com/questions/37872171/how-can-i-perform-two-dimensional-interpolation-using-scipy
* Rbf: My recommendation for irregular points. Gives a reusable object after fitting to the input data.
```python
from scipy.interpolate import Rbf
rbfi = Rbf(x, y, z, values)  #input coordinates and values as arrays 
di = rbfi(xi, yi, zi)   # interpolated values
```
* griddata: 

# Pyplot/Matplotlib
https://matplotlib.org/faq/usage_faq.html#usage
Basic structure: A Figure object is the empty window which contains the plots.
In the figure is a certain number of Axes objects, the actual "plots".
Each Axes object can have for example two or three Axis-objects, the actual "axes of the plots". Axes!=Axis!!!

### Create plot
```python
fig,ax=plt.subplots()
fig2, ax2=plt.subplots(nrows=2, ncols=2)#ax2: either 1D or 2D array => use atleast2d().T if necessary
fig.suptitle('This is a somewhat long figure title', fontsize=16)
```


### Axes and Ticks
```python
ax.set_ylim(1e-7,5e1)#Limits
ax.invert_yaxis()#Invert axis
ax.set_xticks([1,2,3], minor=False)#Ticks setzen. ax.get_xticks() liefert ticks
ax.set_xticklabels(["A12", "B12", "C12"], rotation=90, minor=False)#use [] to turn off labels
ax.tick_params(labelsize=16)
ax.yaxis.tick_right()#Ticks rechts setzen
a.xaxis.tick_top()#Ticks oben setzen
a.xaxis.set_label_position('top')#Label open setzen
ax.get_yaxis().set_visible(False)#hide ticks/axis
ax.set(ylabel="ratio", title="Titel")#Beschriftung
ax.grid(True, which='major')#Gitter. Positions according to xticks major/minor
ax.set_yscale("log")#set axis to logscale (also linear, symlog, ...)
#Tick formatters
ax.set_major_formatter("{x} km") # strings can be used as formatter
import matplotlib.ticker as ticker #Define a custom formatter
def myfmt(x, pos): #x: value, pos: position
  return x.to_string()
ax.set_major_formatter(ticker.FuncFormatter(fmt))
```
### Beschriftung mit Latex
```python
plt.rc('text', usetex=True) #always necessary?
ax1.set_xlabel(r'Irradiance [$\frac{mW}{m^{2}nm}]$', fontsize=18)
ax.plot(x,y, label=r'$\phi={0}\pi$'.format(i))#use variable in latex label
ax.yaxis.set_label_position("right")#which side
ax.yaxis.set_label_coords(-0.1, 0.5)#exakte position
```
### Legende
```python
legend = ax.legend(loc='lower right', shadow=True, fontsize='medium', ncol=2, title='Some lines')#Legende
lines = []#Legende nur mit Linestyle
lines.append(ax.plot([],[], c="black", linestyle ="-", linewidth=1.2)[0])
lines.append(ax.plot([],[], c="black", linestyle ="--", linewidth=1.6)[0])
legend = ax.legend(lines, [l.get_label() for l in lines])
ax.add_artist(legend)
```
Multiple legends in one axes object
```python
leg1=ax.legend()
leg2=ax.legend()
ax.add_artist(leg1)
ax.add_artist(leg2)
```
### Dates
```python
import matplotlib.dates as dates
ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))#Specify (major) label format. Use usual datetime formats like %b (Jan), %Y (2021), %m (1),...
ax.xaxis.set_major_locator(dates.MinuteLocator(interval=2))#Plotting intervals. Similar: MonthLocator
```

You can specify limits & Co in datetimes now.
```python
ax.set_xlim(datetime.datetime.strptime("8.21.2017 15:00","%m.%d.%Y %H:%M:%S"),datetime.datetime.strptime("8.21.2017 16:00","%m.%d.%Y %H:%M:%S")) #Important: you have to specify date and time, if the data contains both!
```

### Lines and colors
#### Specifiying colors
https://matplotlib.org/stable/tutorials/colors/colors.html
```python
color="C0" #The default colors in the cycle can be set with C0, C1, ...
```
#### Linestyle cycle
```python
from itertools import cycle
lines = ["-","--","-.",":"]
linecycler = cycle(lines)
ax.plot(x,y, linestyle=next(linecycler))
```


### colorbar

#### Create colorbar
They always live in their own axes object!
All maps: https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
```python
cbar=fig.colorbar(im, ax=ax, orientation='vertical')#In this case, the colorbar space is 'stolen' automatically from ax! Otherwise, use 'cax=ax'
#Manual way: If there are multiple axes and we want to assign a colorbar to one, we can create a small axes next to the axes with the image:
cbar.set_label("Label")
cbar.ax.tick_params(labelsize=10)
cbar=fig.colorbar(format=formatter(), ticks=[0,1,2]) #custom tick labels. See Axes and Ticks for information on formatters
from mpl_toolkits.axes_grid1 import make_axes_locatable
def add_colorbar(fig, ax, image, **kwargs):
  divider = make_axes_locatable(ax)#If there are multiple axes 0,1,2,3...
  cax = divider.append_axes('right', size='5%', pad=0.05)
  return fig.colorbar(image, cax=cax, **kwargs)
```
#### Colorbar limits and scale
https://matplotlib.org/users/colormapnorms.html
```python
import matplotlib.colors as colors
ax.matshow(Mat, norm=colors.SymLogNorm(linthresh=0.003, linscale=1.0, vmin=-2.0, vmax=2.0))#log scale with symmetric area around 0. linthresh: the value, where the linear range starts. linscale: if 1.0, the linear range has the width of one order of magnitude on the colorbar.
cmap=im.get_cmap() #get cmap for a specific image/contour/...
cmap.set_under('green') #set outlier color. Also: set_over()
im.set_cmap(cmap) #set cmap
```
Make a categorial colorbar with custom categories
```python
cmap=plt.cm.get_cmap('binary', 2), vmin=-0.5, vmax=1.5)
# This function formatter will replace integers with target names
corelabels={0:'no core', 1:'core'}
formatter = plt.FuncFormatter(lambda val, loc: corelabels[val])
cbar=add_colorbar(fig, ax[0,1], im,ticks=[0,1], format=formatter)
```

#### Color cycle setzen
```python
cm = plt.get_cmap('gist_rainbow')#Cmaps: https://matplotlib.org/examples/color/colormaps_reference.html
ax.set_prop_cycle(plt.cycler('color', [cm(1.*i/15) for i in range(15)]))
```
### Modify colormaps
```python
from matplotlib.colors import ListedColormap
cmap=ListedColormap(["orange", "green","black"]) #Use mpl colorlabels
cmap=ListedColormap(np.arange(40).reshape((10,4))) #Use a numpy array specifying rgba colors (shape [N,4])
```

If you want a cutout of an existing colormap:
```python
from matplotlib.colors import LinearSegmentedColormap
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = LinearSegmentedColormap.from_list('trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval), cmap(np.linspace(minval, maxval, n)))
    return new_cmap
cmap = plt.get_cmap('jet')
new_cmap = truncate_colormap(cmap, 0.2, 0.8)
```

### Zweite Axe rechts:
```python
ax2=ax.twinx()#twiny() for axis on top
```

### Lines and Shapes
```python
ax.axvline(x=20)#axhline(y=20) create a vertical or horizontalline
ax.axvspan(1,2,alpha=0.5, color='r') #Highlight an area. Similar: axhspan
circle1 = plt.Circle((1000, 1000), 30, color='r', fill=True)
ax.add_artist(circle1)
```

### Saving figures
```python
plt.rcParams["savefig.directory"] =os.path.dirname(os.path.abspath(__file__))#need to "import os"
plt.rcParams["savefig.format"]="pdf"
fig.savefig("Plot1.pdf", bbox_inches='tight', format='png')#save plot. bbox_inches is very useful to remove white area around (and even add area if some labels are not visible otherwise)
```
### Backend
```python
matplotlib.use("Agg")#specify backend, before importing pyplot! Important if Display variable is not set. Alternative: TkAgg
matplotlib.get_backend()#get backend
print(matplotlib.matplotlib_fname()) #find matplotlibrc
```


### Arange subplots
```python
fig, ax=plt.subplots(2,2, figsize=(4,3))#Easiest way
fig.subplots_adjust(hspace=0.1,wspace=0.1)#Adjust height and width spacing in units of mean axis length

import matplotlib.gridspec as gridspec
fig = plt.figure(figsize=(4,3))
grid = plt.GridSpec(4, 3, hspace=0.4, wspace=0.2)#Define grid and specify over how many cells axes spread
ax1 = fig.add_subplot(grid[:-1,:])
#another possibility
gs = fig.add_gridspec(4, 2, width_ratios=[1, 1], height_ratios=[1, 10,10, 10])
ax2 = fig.add_subplot(gs[-1, :])
```

### Text and annotations
Generally, font sizes can be given absolute in pt or relative to `font.size` from the rc parames. Relative measures are: `xx-small, x-small,small, medium, large, x-large, xx-large, larger, or smaller`
```python
ax1.text(1,2,"Hallo", rotation=45,fontsize='large')#Annotation, Text
ax1.annotate("Hallo", xy=(0.5,0.5), xytext=(0.6,0.6), xycoords='axes fraction')#more functions than simple text, e.g. make arrows and give coordinates in different formats
```

### Plot types
#### Lines, points and bars
```python
ax.plot(x,y,'.-', linewidth=0.4,label="label")
ax.scatter(x,y,c=z, alpha=0.5, marker='.', markersize=4)#scatter plot. alpha sets transparency of points, which is useful to visualize the density as well. useful markers: 'o', '.', ',', 'x'
ax.errorbar(x,y,xerr, yerr)#like ax.plot, but with errorbars to show standard deviation
ax.fill_between(x,y-yerr, y+yerr)#draw the error as shaded region between two curves
ax.bar(xarr,height=yarr, width=1.5)#Barplot with vertical bars (columnplot). For horizontal, use barh and exchange height and width
```
#### Histograms
```python
n, bins, _ =ax2.hist(distance,bins=100, weights=values, range=(-60,60), density=True, cumulative=False)#histogramm. If density=True, the y axis values are in units of %/xaxis, i.e. np.sum(n[-1]*np.diff(bins))=1.0. (n[-1] in the case of multiple categories and stacked=True, for a plot with one category it is just n*np.diff) Cumulative allows for cumulative histograms
im=ax2.hist2d(x,y,bins=100, weights=values, range=(-60,60), cmin=1)[3]#histogramm 2d, object for colorbar is the fourth returned object. Cmin: All values below are set to nan.
```

#### Images (2D Verteilung) plotten
Imshow is usually the fastest solution. It is for data on a regular grid. Use 'extent' to set the axes coordinates if they should be something else than pixels. Things become tricky together with 'aspect', which is like a scaling factor height=aspect*width. By default, aspect=1, i.e. the PIXELS are kept squares IN AXES COORDINATES. E.g. if your xaxis is 1000 (m) and your y axis 1 (m), the image will appear extremly elongated. In this case, set aspect to 1000 and the yaxis will be stretched, such that the RESULTING IMAGE looks like a square.
```python
from matplotlib.colors import LogNorm#falls mit LogNorm
im=ax.imshow(b, cmap='gray', interpolation='none', norm=LogNorm(), extent=(0,1,0,1))#b: 2D Array mit Pixelwerten. Use "extent" to give the image a coordinate measure other than just pixels.
```
```python
contour=ax.contour(x,y,z, colors='k')#Contour plot: Draw height lines ('isobares')
ax.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize='medium')#write height values to lines

ax.contourf(x,y,z, cmap='Greys')#Draw a filled contour plot, i.e. with areas rather than lines.
ax.pcolormesh(x,y,c)#plot 2d with non-regular grid. x,y: 1D arr with length one greater than c. C: 2darr, rows are plotted as y, columns are x
```


### Animationen
Animation Artist:
```python
import matplotlib.animation as animation
fig, ax=plt.subplots()
ims=[]
for i in range(1,200):
    title = plt.text(0.5,1.01,i, ha="center",va="bottom", transform=ax.transAxes)
    im=ax.imshow(image[i], cmap="Greys_r")#pcolormesh o.ä. works as well
    ims.append([im,title])
ani = animation.ArtistAnimation(fig, ims, interval=30, blit=True, repeat_delay=40)
ani.save('SimpleBox.mp4')
plt.show()
```
Animation Function:
```python
from matplotlib.animation import FuncAnimation
def create_1d_animation(fig, ax, x, values, interval):
    #format [frame, position]
    line, = ax.plot([], [], lw=1)
    def animate(i):
        a = x[i]
        b = values[i]
        line.set_data(a, b)
        return line,
    print(x.shape[0])
    anim = FuncAnimation(fig, animate, frames=x.shape[0], interval=interval, blit=True)
    return anim
```

### Interaction
Matplotlib provides an API to allow users to interact with figures via key presses and mouse clicks. A good introduction can be found [here](https://matplotlib.org/stable/users/event_handling.html).
```python
ax.figure.canvas.mpl_connect("button_press_event", on_press) #connect a function to an event via figure.canvas (accessible via an ax object, if you want).
def on_press(event): #The function must take an event as argument
  if event.button==1: #button_press_event is a MouseEvent, which contains the mouse button clicked in the button property
  event.xdata #Key and Mouse Event have additional properties like xadata and ydata, the location in data coordinates, where the event happened
  event.inaxes #over which axes the event happened
  event.x #pixel coordinates of the canvas
  event.canvas.draw() #After you changed something, redraw the canvas to make changes visible
```

## Subprocess
Library to execute commands on commandline (bash)
```python
import subprocess as sp
sp.call("echo test", shell=True)#Simple execution of string
```

# Pandas
### Create Data Frame
```python
test=[[4,5,6],[1,2,3]]
testdf=pd.DataFrame(test,columns=['A','B','C'])
```
### read from file
```python
data=pd.read_csv("FileName")
```

### Acces elements
```python
df.loc['A','B']#if you use column/row names
df.iloc[1:2,3:4]#if you use indices
df[(s < -1) | (s > 0.5)] #boolean indexing
```
important: iloc chooses based on the POSITION, loc is based on the LABEL! Can be confusing because, e.g. for rows, integers can be labels as well.
### get columns
```python
datadp.columns
```

### Categories in one column
```python
np.unique(testdf.A)
```

### iterration over rows
```python
for index, line in df.iterrows():
    print(line)
```
### Groupby
combine rows which have a common feature into subgroups
(https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html)
```python
datgroup=data.groupby("Label")
```
if groupby by two labels: multindices occur: https://www.datacamp.com/community/tutorials/pandas-multi-index
* acces
```python
datgroup.get_group["A"]
```
* iterate over groups
```python
for name, group in enumerate(datgroup):
    print(group)
```

# Geopandas
Library on top of pandas and shapely, which allows to plot maps. Basic idea: A pandas dataframe with a special column "geometry", which contains shapely objects (Points, LineStrings or Polygons), which can represent cities, streets or countries.

## Maps (Contextily)
However, if you want to plot data on a map, you need more than geopandas, since geopandas is basically just shapely with coordinate transformations. Maps of the earth usually consist of tiles, which are provided by different providers like e.g. OSM. To download such tiles and add them to a matplotlib figure, `contextily` is made.
Documentation: https://contextily.readthedocs.io/en/stable/index.html
Generally, contextily works in Spheric Mercator projection (EPSG:3857), so you need to convert all your coordinates first! (Sometimes, lon/lat is also accepted)

### Plot geopandas
```python
import contextily as ctx
gdf=gdf.to_crs(epsg=3857) #Convert your geopandas dataframe to the projection used by contextily 
ax=gdf.plot()
ctx.add_basemap(ax,zoom=6) #Add basemap to axes. Use the axes you get back from geopandasdf.plot()
```

### Details
```python
ctx.howmany(w, s, e, n, 6, ll=False) #How many tiles will be downloaded at zoom level 6. If ll, bounding box is given in lon/lat
sources=[i for i in dir(ctx.tile_providers) if i[0]!='_'] #list all providers included in ctx
srcurl=getattr(ctx.sources, sources[2]) #select a provider
img, ext=ctx.bounds2img(w, s, e, n, 6, url=srcurl, ll=False)#If you want the map as an array image
plt.imshow(img, extent=ext)
```

# MetPy
```python
from metpy.calc import relative_humidity_from_specific_humidity
from metpy.units import units
relative_humidity=relative_humidity_from_specific_humidity(da.pressure*units.Pa,da.temperature*units.degK,da.humidity).metpy.convert_units('percent') #metpy can operate on xarray DataArrays. It provides the .metpy accessor.
```
# NETCDF
Idea: A NETCDF File consits of variables. Each variable can implement a certain number of dimensions (like time, lat, lon).
Dimensions are essentially also variables itself ("coordinate variables")

```python
import netCDF4
ncf = netCDF4.Dataset("Example.nc", 'r')
print(ncf)#print overview of whole dataset
print(ncf.groups)#print groups if available
print(ncf.dimensions)#print avalabledimensions
print(ncf.dimensions.keys())#get dimension names
print(ncf.variables.keys())#get variable names
pmom=ncf.variables["pmom"]#get one variable
print(pmom)#get overview
print(pmom.dimensions)#one variable does not necessarly have to implement all dimensions!
print(pmom.shape)#get shape of the data
print(pmom.units)#get units
print(pmom[1,:,0,1])#data can be accessed like numpy arrays
ncf.close()#close stream after use
```
# Xarray
https://xarray.pydata.org/en/stable/index.html
Generalization of pandas to work with higher dimensional data, basically a front-end for the netcdf format. Basic idea: The fundamental element is the DataArray. It describes values of one variable, which implements certain dimensions. A dimension can be seen as one axis in the higherdimensional space the variable exists in. Each dimension usually has a list of coordinates, these are labels which specify certain positions on the axis (think of the axis 'ticks'). Technically, dimensions are just DataArrays itself.
Multiple DataArrays can be contained in a Dataset. Not every array in a Dataset needs to implement all dimensions. Datasets are usefull because you can perform some operations on many DataArrays at once, e.g. slicing along one dimension, which will slice every DataArray which implements this dimension.

## Creating data
```python
import xarray as xr
#Datasets
ds=xr.Dataset({'name':DataArray})#create Dataset
ds.temp#select a Data variable
ds['temp']=ds.temp.astype(float)#convert a variable or dimension to another type. You have to use the [.] notation for assignments
ds=ds.squeeze(drop=False)#Fix/Drop all dimensions with length one
da.drop([d for d in list(data.coords.keys()) if d not in data.dims])#Drop all non-dimensional coordinates
#DataArrays
da=xr.DataArray(nparray, coords=[('x',xarr), ('y', yarr)])#Create a DataArray from numpy
da2=da1.copy(data=arr)#create a DataArray with new values based on an existing DataArray
da.name='radiance'#DataArrays can have names to identify them in Datasets
da.attrs['long_name']='lorem ipsum'#DataArrays can store attributes
da.attrs['units']='km'#long_name and units is used by the .plot() routine
```
## Reading & Writing
```python
ds=xr.open_dataset("filename.nc")#open Dataset
ds.to_netcdf("filename.nc")#save Dataset
```
Open a single dataset from multiple files. To get this to work, ensure a few things:
* Indexes of the coordinates should not overlap. E.g., make sure you don`t have daily files with hours [0,...,24]
* Small differences (typos) in the attributes of variables can prevent the merge. Use combine_attrs here.
* by default, after the merge with combine_by_coords, all variables will include all coordinates. To prevent this, use data_vars='minimal'
```python
ds=xr.open_mfdataset('filename.nc', combine_attrs='override', preprocess=myfunc, data_vars='minimal') 
```
## Inspecting data
```python
#DataArrays:
da.dims#The dimension names of the data
list(da.coords.keys())#The names of the coordinates (also non-active ones which are squeezed)
da.sizes #dictionary: coordname:size
#Datasets:
list(ds.data_vars)#The names of the Data variables in the set
list(ds.variables)#Everything: names of the variables AND coordinates (also squeezed ones)
npt.assert_equal(sorted(list(ds.data_vars)), ['a', 'b'])#Check the formatting
```

## Selecting data
https://xarray.pydata.org/en/stable/indexing.html
```python
da[...,2]#based on coordinate index and dimension index
da.loc[...,'z']#based on coordinate label and dimension index
ds[["var1","var2"]]#select variables in a dataset.
ds=ds.isel(temp=0, drop=False, missing_dims='raise')#selection based on index along the dimension. Alternatively, you can provide: {'temp':0} as indexer.
ds=ds.sel(temp=34.3) #Selection based on coordinate of the dimension.
ds.sel(temp=30, method='nearest', tolerance=5)#Nearest neighbour lookup to find a value close to 30
da.sel(x=da.x[da.x<-0.1])#Boolean indexing works only positional with []!
da.drop_sel(x=...)#like sel, but return everything except the selected part
```
## Asignments
This is something a little counterintuitive in xarray: You can never assign values to isel() or sel()! Instead, it is possible with loc[] or xr.where(cond, returnTrue, returnFalse)
```python
da.loc[db.coords]=db#Assign values of db to a subset of da
```

## Coordinates
Each dimension can have a coordinate array assigned. Imagine them as the tick labels of the dimension axis. Additionally, you can assign further coordinates to the dimension, which are then non-coordinate arrays! E.g., this is useful if you want to reference every "tick" on an dimension axis by two labels like weekday and monthday.
Be aware: Dimensions have names. You see them in () when printing. Coordinates can have the same names as the dimension they label (e.g. 'space') or different names (e.g. 'weekday' for dimension 'time'). In the latter case, you must of course tell xarray that 'weekday' belongs to the dimension 'time'.
```python
locs = ['A','B','C']
weekdays = ['Mon', 'Tue', 'Wed', 'Thurs']
foo = xr.DataArray(np.random.rand(4, 3), coords={'weekday':('time', weekdays), 'space':locs}, dims=['time', 'space'])#DataArray with two dimensions with coordinates
foo.coords['month'] = ('time', [6, 7, 8,9])#another coordinate set for dimension time
foo.assign_coords(time=[1,2,3,4])#another way to assign coords. You can also provide a dict directly here
foo=foo.swap_dims({'time':'monthday'})#Now 'monthday' is the new "main" label for the dimension time
da.get_axis_num('y')#useful when using numpy with da.values
da.reindex(x=[1,1,2,3], method='nearest')#return data of da, but with new coordinates
```

## combining/extending data
```python
new=xr.concat([old1, old2], dim='time')
data.expand_dims({'newdim':[1,2,3]})
a2, b2=xr.broadcast(a,b)#Xarray support broadcasting by dimension names. I.e., if a has dimension 'x' and b has dimensions 'x' and 'y', a is extended to have 'x' and 'y' as well, irrespective of the order (this is different to numpy, where broadcasting is done positional). For computation like a*b, this works automatically.
data1=data1.combine_first(data2)#extend data1 by the values of data2 (introducing nans if empty areas are created), but keep the values of data1 if there are already some present.
xr.combine_nested([[a1, a2], [a3, a4]], concat_dim=['x', 'y'])#Combine with position of subsets encoded in list of lists
```

## Modifying data
```python
dist.where(condition,other=na, drop=False)#return where cond is true and fill in 'other' where it is false (default na). If drop, coordinates with only false are dropped.
ds.coarsen(photons=4).mean()#calculate mean over blocks of 4 along photons
ds.drop_vars('a')#remove a variable
ds.drop_dims('time')#remove a dimension and all related variables
da.rename({'old':'new'})#Rename a var or coord in a DataArray
da.transpose('y', 'z',..., 'x')#Reorder dimensions. Use ellipsis if further dimensions are present.
da.sortby('time')#Also sortby(['time', 'lat'])
da.dropna(dim='time', how='any')#Drop the label if any (alternative: all) value is nan
ds.fillna({"a":2})#fill missing values. For datasets, use a dict to fill variables individually
da.stack(z=('x', 'y'))#create a single multiindex from multiple existing indices
```

## Computation
```python
ds.mean(dim='time')#calculate mean/sum/...
ds.groupby("time.dayofyear").mean()#mean over the same days of multiple years
ds.groupby_bins('height', bins=[0,10,23], labels=[0,10]).mean() #aggregate using custom bins along an axis.
da.rolling(x=3, center=True, min_periods=2).mean()#rolling mean/std/median/...
```
## Time Series
For the time axis, there exists a lot of special functionality
```python
ds.sel(time="2022-05-28", time2=slice("2022-05-28", "2022-05-30")) #selection based on strings
ds.isel(time=(ds.time.dt.dayofyear==100)) #Selection based on a datetime property
da.resample(time='24H', base=6, label='right', loffset='1H').mean()#Special for temporal data. Take a 24h mean, starting at 06:00 every day and assign every resulting value the time of the right side + 1H of the 24H interval.
da.resample(time="10min").interpolate() #Upsample time data
```

## Broadcasting
Like numpy, xarray has a set of broadcasting rules. The difference to numpy is that xarray includes dimension and coordinate information. This allows you to calculate many thing in a very short and elegant manner.
```python
#Matrix Multiplication: C_ik=A_ij*B_jk -> A and B need one common dimension j (second for A, first for B)
C=(A*B).sum("j")
```

## apply_ufunc
https://xarray.pydata.org/en/stable/examples/apply_ufunc_vectorize_1d.html#apply_ufunc
Idea: Apply a function which works for numpy arrays to xarray. Super useful, because it cares about all the fiddling with dimensions, coordinates. Example: You have a function which takes scalar or 1D data and want to apply it for all dimensions in a dataarray and return the result as a new dataarray.
```python
interped = xr.apply_ufunc(
  interp1d_np,  # first your function
  air,  # now arguments in the order expected by 'interp1_np'
  air.lat,  # as above
  newlat,  # as above
  input_core_dims=[["lat"], ["lat"], ["new_lat"]],  # list with one entry per arg
  output_core_dims=[["new_lat"]],  # returned data has one dimension
  exclude_dims=set(("lat",)),  # dimensions allowed to change size. Must be a set! Regard the comma!
  vectorize=True,  # loop over non-core dims
)
result=xr.apply_ufunc(self.retrieval, measurement, measurement.theta,input_core_dims=[['theta'], ['theta']], output_core_dims=[['retresult']], exclude_dims=set(('theta',)), vectorize=True) #Another similar example
```

## Plotting data
```python
da.plot(x='a', ax=ax1) #1D. Data is automatically plotted in the 'open' dimension y. 'ax' allows to specify a matplotlib axes object.
da.plot(x='a', hue='b') #2D
da.plot(x='a', hue='b', col='c', col_wrap=2) #3D with multiple subplots
da.plot(x='a', hue='b', col='c', row='d') #4D
da.plot.pcolormesh(x='a', y='b',cmap='jet') #pcolormesh is the default for 2D
#Imshow is a faster alternative to pcolormesh. Allows 3D Data to be interpreted as rgb
aspect=float(rgb.x.max()/rgb.y.max())
ax=da.plot.imshow(size=10, aspect=aspect,x='x', y='y', rgb='rgb', interpolation='antialiased')
fig=ax.get_figure()
```

## HVPlot
Hvplot provides a way to create interactive plots, which are based on bokeh or plotly instead of matplotlib. This works for xarray as well as other common packages (pandas, etc)
```python
import hvplot.xarray
da.hvplot() #Create a standard hv plot based (line, image, hist, based on the dimensions)
da.hvplot.image(groupby="time") #Create an image with an interactive slider for the third dimension 'time'
da.hvplot.rgb(x='x', y='y', bands='rgb', rasterize=True) #rgb image
```

## Dask
Allows for parallel processing of big arrays in a chunked manner.

Nomenclature:
* Scheduler: Distributes work to the different workers
* Workers: Are available to execute work. Each worker can create multiple threads.

If you plan to call dask from a file with the standard interpreter, most of the code should be in `__main__`. Every worker will read the file when created, but only the main run should execute the heart of the code
```python
import Mylib
def func1: pass #This stuff will be available to all workers
if __name__=="__main__": #Main code here
  from dask.distributed import Client
  client=Client(n_workers=4, threads_per_worker=4, memory_limit='20GB') #It is convenient to set up a client.
  print(client) #This will allow you to monitor the scheduler progress via a dashboard in your browser
```
Issues

I found quite some issues when using dask.
Without the generation of a client, things seem to work just fine, but you can`t limit the resources used on the server.

When generating a client in vscode interactive:
* With processes=False, I usually get a lock error somewhere in the computation
* without arguments, the client is always restarting the workers. This seems to be an unresolved issue with vscode interactive.

In a python script:
* Creation of a client has to be included in the main file (see above)
* All execution code has to be included in the main file (see above)
* the HDF5_USE_FILE_LOCKING=FALSE variable has to be exported
* I usually get an error at the end of the computation, when shutting down the workers

In a juypter ipynb:
* Everything works, even in vscode


# Image processing
## Convolution
```python
from scipy import signal as sig
AcM=sig.convolve2d(A,M, mode='full', boundary='fill', fillvalue=0)
```
boundary: How boundary conditions are treated: fill missing values on the rim with a value, use periodic boundary conditions ('wrap') or mirror the values directly at the rim to the outside ('symm')
mode: Size of the resulting array, 'full', "valid", or "same"

# IPython Jupyter
Allows interactive python programming using jupyter notebooks
```bash
pip install jupyter
```
## Magic commands
To trigger additional features
```python
%prun command #performance profile the following python command
%cd #change the current working directory of the kernel
%matplotlib inline #trigger interactive matplotlib plots
%load_ext autoreload #trigger autoloading packages
%autoreload 1 #only autoload packages imported with '%aimport package'. 2: autoreload all, except '%aimport -package'
%aimport package.module #import with autoloading. It seems like '%aimport package' will not autoload submodules
```


# Creating your own modules
https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
All about paths and importing from other directories:
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html

Configure paths:
* option1: define PYTHONPATH variable in .bashrc (problem: might be system dependent, dotfiles are synchronized via github)
for intellisense: set in settings json: "python.autoComplete.extraPaths": ["Path/To/ModuleFolder"]
* option2: set a link in one of the default locations (import sys, print(sys.path))
e.g. in /usr/lib/python3/dist-packages
intellisense should work automatically
* option3: If you need a selfmade module only for some project and do not want to add it to the path permanently, you can import it in a specific code by:
```python
import sys
sys.path.append("path/to/new_project/")
import module
```
## Module Structure
Typical directory structure
```text
new_project
├── mypackage
│   ├── __init__.py         # make it a package
│   └── antigravity.py
└── test
    ├── __init__.py         # also make test a package
    └── test_antigravity.py
```
How to use this package from another python script:
```python
import mypackage# import the functions provided in __init__.py
from mypackage import antigravity# import the antigravity module
from mypackage.antigravity import my_object# or an object inside the antigravity module
```
import from parent directory
```python
def load_src(name, fpath):
    import os, imp
    p = fpath if os.path.isabs(fpath) \
        else os.path.join(os.path.dirname(__file__), fpath)
    return imp.load_source(name, p)
load_src("Tools", "/example/example/Tools.py")#absolute or relative path possible!
import Tools
```
Reload a module in the REPL
```python
import importlib
importlib.reload(module)
```

## Special files
### Init
In `packagename/__init__.py`, you would typically write which methods and objects the module exports to the user. By default, if the user imports everything with `from mypackage import *`, all functions not beginning with an underscore are imported. This can be changed by setting the `__all__` variable.
```python
from .antigravity import function1#Typically on bigger projects, you have the API functions sorted in seperate files
__version__="1.0"
__all__=(
# Functions
  "function1", 
#Constants
  "__version__",
)
```

### Requirements.txt

### Setup.cfg & Setup.py
Located at the top level of your module, `setup.cfg` is read by various python modules and contains setup e.g. for code formatting. `setup.py` is a python script next to `setup.cfg`, usually calling `setup` from the `setuptools` package. Nowadays, for smaller projects a `pyproject.toml` file might be prefered.

### pyproject.toml
Dependencies can be installed via `pip install .` if a pyproject.toml file is present in the folder.
To include optional dependencies, call `pip install ".[dev]"`
```toml
[build-system]
requires      = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "realpython-reader"
version = "1.0.0"
description = "Read the latest Real Python tutorials"
readme = "README.md"
authors = [{ name = "Real Python", email = "info@realpython.com" }]
license = { file = "LICENSE" }
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
keywords = ["feed", "reader", "tutorial"]
dependencies = [
    "feedparser >= 5.2.0",
    "html2text",
    'tomli; python_version < "3.11"',
]
requires-python = ">=3.9"

[project.optional-dependencies]
dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]

[project.urls]
Homepage = "https://github.com/realpython/reader"

[project.scripts]
realpython = "reader.__main__:main"
```

### pre-commit
`.pre-commit-config.yaml` contains the configurations for the `pre-commit` module. Pre-commit help you to automatically set up git hooks, which are executed before every commit to format or test your code. Pre-commit automatically downloads the specified modules from github and executes them, if they follow certain criteria (e.g. python modules must define an entry point). Pre-commit is itself a python module, but could theoretically be used with any programming language.
```bash
cd your_package
touch requirements_dev.txt #write 'pre-commit' in the development requirements.
pip install -r requirements_dev.txt
pre-commit install #install the hooks in .git/hooks/pre-commit. Now, they are executed on every commit.
pre-commit run --all-files #if you setup pre-commit in an existing module, you may run it on all files.
```
.pre-commit-config.yaml:
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
  - repo: https://github.com/PyCQA/isort
    rev: 5.8.0
    hooks:
      - id: isort
  - repo: https://gitlab.com/pycqa/flake8
    rev: 3.9.2
    hooks:
      - id: flake8
```
## Resources
Sometimes, modules need to contain non-python files called "resources". To use them from inside the code, do not use filepaths directly.
```python
from importlib import resources
  traversable=resources.files("module_name") #Module as object or string. Creates a 'traversable' object. Needs python >=3.9
  with resources.as_file(traversable) as f: #Use as_file to get a context manager which provides a pathlib.Path
    print(f/"data" / "my_resource.txt")
```

## How to write proper docstrings for functions/classes:
```python
https://www.python.org/dev/peps/pep-0257/
def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
```
# Unittests
https://realpython.com/python-testing/

General folder structure
```txt
tests/
|
└── unit/
|   ├── __init__.py
|   └── test_sum.py
|
└── integration/
    |
    ├── fixtures/
    |   ├── test_basic.json
    |   └── test_complex.json
    |
    ├── __init__.py
    └── test_integration.py
```
```python
import unittest as ut
class SomeTests(ut.TestCase):
  def setUp(self):
    #come code if necessary
  def test_something(self):#Must start with test_
    #testing with asserts
```
## Execute tests
Best to use the command line interface. Take the example from 
[the importing modules section](#module-structure)
```bash
cd new_project
python3 -m unittest discover #All tests in test directory. use -t testdir if not named test.
python3 -m unittest test.test_antigravity #one specific test (python notation). Remember to have an __init__.py in your test and probably subfolders present.
```
```Makefile
unittest:
	python3 -m unittest discover -s test/unit
.PHONY:unittest
```
unittest introduces a few improved assertions:
```python
with self.assertRaises(SomeException): MyFunc(arguments)#Test for exception
```


# Profiling
## cProfile and pstats
In the standard library, there is `cProfile` as a profiler and `pstats` to analyze the results in the command line
```python
python3 -m cProfile -o output.prof Program.py #Run Program.py and save analytics in output.prof
python3 -m pstats output.prof #start interactive session to browse output.prof
pstats% help #Show help
pstats% strip #Strip leading paths in report
pstats% sort cumtime #sort according to cumulative time
pstats% stats 10 #print the first 10 statistics
```
