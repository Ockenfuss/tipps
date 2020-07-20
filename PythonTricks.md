# Python Tricks


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Python Tricks](#python-tricks)
  - [Python General](#python-general)
    - [Installation](#installation)
    - [General](#general)
      - [Functions:](#functions)
        - [Type hints](#type-hints)
      - [Variable reference in Python](#variable-reference-in-python)
      - [Datatypes](#datatypes)
      - [Strings](#strings)
        - [f-Strings](#f-strings)
        - [Regex](#regex)
      - [Arrays](#arrays)
      - [Lists](#lists)
      - [List comprehensions](#list-comprehensions)
      - [Iterables](#iterables)
      - [Sets](#sets)
      - [Dictionaries](#dictionaries)
      - [File paths/IO](#file-pathsio)
    - [Exceptions](#exceptions)
    - [Object Orientation](#object-orientation)
      - [Decorators](#decorators)
      - [Get/Set](#getset)
      - [Operator overloading](#operator-overloading)
    - [Datetime module](#datetime-module)
      - [Datum aus String](#datum-aus-string)
      - [String aus Datum:](#string-aus-datum)
      - [Differenz in Sekunden:](#differenz-in-sekunden)
      - [Zeiten addieren:](#zeiten-addieren)
      - [Zeiten Plotten](#zeiten-plotten)
    - [time Module](#time-module)
  - [Numpy](#numpy)
      - [Numpy I/O](#numpy-io)
      - [Numpy Arrays](#numpy-arrays)
      - [Indexing](#indexing)
      - [Basic Slicing](#basic-slicing)
      - [Numpy sortieren](#numpy-sortieren)
    - [Numpy array transformations](#numpy-array-transformations)
      - [Broadcasting](#broadcasting)
        - [Numpy Array reshape](#numpy-array-reshape)
      - [stack/extend/combine/transpose numpy arrays](#stackextendcombinetranspose-numpy-arrays)
      - [combine multidimensional arrays](#combine-multidimensional-arrays)
      - [masked arrays](#masked-arrays)
    - [Numpy Datentypen](#numpy-datentypen)
    - [Numpy Funktionen](#numpy-funktionen)
    - [Statistics](#statistics)
    - [Fourier Transformations](#fourier-transformations)
  - [Scipy](#scipy)
    - [Statistics](#statistics-1)
      - [Distribution functions](#distribution-functions)
  - [Pyplot/Matplotlib](#pyplotmatplotlib)
      - [create plot](#create-plot)
      - [Axen und Ticks](#axen-und-ticks)
      - [Beschriftung mit Latex](#beschriftung-mit-latex)
      - [Legende](#legende)
      - [linestyle cycle](#linestyle-cycle)
      - [colorbar](#colorbar)
        - [Create colorbar](#create-colorbar)
        - [Colorbar limits and scale](#colorbar-limits-and-scale)
        - [Color cycle setzen](#color-cycle-setzen)
      - [Modify colormaps](#modify-colormaps)
      - [Zweite Axe rechts:](#zweite-axe-rechts)
      - [Figuren](#figuren)
        - [Kreis plotten](#kreis-plotten)
      - [Save File Location default and default extension (pdf)](#save-file-location-default-and-default-extension-pdf)
      - [Backend](#backend)
      - [Arange subplots](#arange-subplots)
      - [Text and annotations](#text-and-annotations)
      - [Plot types](#plot-types)
        - [Lines, points and bars](#lines-points-and-bars)
        - [Histograms](#histograms)
        - [Images (2D Verteilung) plotten](#images-2d-verteilung-plotten)
      - [Animationen](#animationen)
  - [Subprocess](#subprocess)
  - [Pandas](#pandas)
      - [Create Data Frame](#create-data-frame)
      - [read from file](#read-from-file)
      - [acces element](#acces-element)
      - [boolean indexing](#boolean-indexing)
      - [get columns](#get-columns)
      - [Categories in one column](#categories-in-one-column)
      - [iterration over rows](#iterration-over-rows)
      - [Groupby](#groupby)
  - [Geopandas](#geopandas)
    - [Maps (Contextily)](#maps-contextily)
      - [Plot geopandas](#plot-geopandas)
      - [Details](#details)
  - [NETCDF](#netcdf)
  - [Xarray](#xarray)
    - [Inspecting data](#inspecting-data)
    - [Selecting data](#selecting-data)
    - [Asignments](#asignments)
    - [Coordinates](#coordinates)
    - [combining/extending data](#combiningextending-data)
    - [Modifying data](#modifying-data)
    - [apply_ufunc](#apply_ufunc)
    - [Plotting data](#plotting-data)
  - [Image processing](#image-processing)
      - [Convolution](#convolution)
  - [CLI Arguments](#cli-arguments)
  - [Create your own modules](#create-your-own-modules)
      - [Module Structure](#module-structure)
      - [How to write proper docstrings for functions/classes:](#how-to-write-proper-docstrings-for-functionsclasses)
  - [Unittests](#unittests)
    - [Execute tests](#execute-tests)

<!-- /code_chunk_output -->


## Python General

### Installation

`sudo apt install python3`
Pip: `sudo apt install python3-Pip`
install package with pip: use `--user` flag if you have problems
also possible: install with `python3 -m pip install`
list packages (python3 -m) `pip list`
upgrade pip: 

### General

beendet ein Python Program 
<!-- Stop Interrupt -->
```python
import sys
sys.exit()
```

#### Functions: 
often use "args" and "kwargs" (=keyword arguments) to pass additional arguments to new function.
Syntax: *args or **kwargs This is part of a more general behaviour: * unpacks an array or list so its elements can be function arguments, ** does the same with a dictionary (creating named arguments)
##### Type hints
https://realpython.com/python-type-checking/
They have no effect during runtime, but help understanding the code and are often used by linters to detect errors and deliver better suggestions.
```python
def myfunc(a : int, b : str) -> str:
  ...
```

#### Variable reference in Python
in general, every object has an id (similar to pointer in C)
Function arguments are in general by reference, i.e. inside the function, we are dealing with a new reference for the original object
Generally, expressions are evaluated from the right
Expressions like a=a+10 (a can be numpy array!): Create a new, deep copy and assign its reference to a

#### Datatypes
convert to integer
`int(x)`

#### Strings
```python
test="Hallo"+"du" #Combination
8*'hey' #Repetition
if 'ocken' in 'ockenfuss' #Test for substrings (no need for regex here)

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
```
Format specifiers: These are deprecated, better to use f=Strings!
```python
print("%d %f %s"%(1, 0.314,"hallo"))#Write a percent sign and then the tuple with the values
```
##### f-Strings
https://realpython.com/python-f-strings/
A way to 'insert' python code into strings. Currently the recommended way to format strings (python 3.6 or newer).
```python
name="Paul"
print(f"Hallo{name}")
print(f"This is {object!r}")#By default, __str__ of an object is used, but with '!r' we can switch to __repr__
```
##### Regex
https://realpython.com/regex-python/
```python
import re
re.findall('ABC', 'ABCD')#Return match
match=re.search('([0-9]*)',string) #search for all matches. Use () to capture groups. Return None if no match is found, so you can use it like:
if re.search... :
match.groups()#Tuple with all groups. () needs to be defined!
match.group(1)#Select a group. Index is one-based!

```


#### Arrays
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

#### Lists
Like Arrays, but can (1) contain different data types and (2) be extended dynamically
```python
liste=[]
liste.append("Hallo")
liste.append(liste2)#list of lists
a=[1]+[2,3]#List concatenation
b=[1]*3#=[1]+[1]+[1]
if a: #a returns false is len(a)=0 (list is empty). The same holds for most collections like dict, tuple, ...
sl=slice(1,2,3)#Creates a slice object, which can be used to slice strings or lists
sl.start#slice objects have members start, step and stop
```
#### List comprehensions
```python
arr=[expr(i) for i in indices]
arr=[expr(i) for i in indices if condition(i)]
arr=[expr(i) if condition(i) else expression2(i) for i in indices]
```
#### Iterables
Closely related to list comprehensions are generator expressions. They create iterables which do not get evaluated immediately. Iterables are objects which support the __next__() method, which returns the next iteration state.
```python
iterable=(obj.evalute() for obj in objlist)
```
Iterables can be created with the `yield` operator. It is similar to `return`, but keeps the function state in memory and continues execution when the next element is requested.
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
There are a lot of useful function, which work with iterables.
```python
list1, list2=zip(*sorted(zip(list1, list2)))#Sort multiple lists according to the first one
```
#### Sets
Unordered collections, where each element appears only once. Pretty much the same thing as you know from mathematics! Elements must be immutable
https://realpython.com/python-sets/
```python
a=set(['foo', 'foo', 'bar']) #Create from iterable of immutables. Result: a={'foo', 'bar'}
a | b #Union: elements in a or b
a & b #Interection: elements in a and b
a - b #Difference: elements in a and not in b
a <=b #a is subset of b
a < b #a is real subset of b
a |=b #Update a to be a | b. Works with & and - as well
```

#### Dictionaries
Unordered storage vor key-values pairs.
```python
example={"key": value, "key2": value2}
print(example["key2"])#Access elements by key
d=dict(zip(keys, values))#use dict to create a dictionary from a list of key-value tupples (zip creates such a list from key and value lists)
list(d.keys())#get keys as list
dict1.update(dict2)#update a dictionary with the values from another one (replace keys or create if not existing)
d.pop('key', default)#return & remove key if existing and return default otherwise
func(**kwargs):
  key=kwargs.pop('key', default)#Very useful for function argument defaults
```

#### File paths/IO
```python
import sys
sys.argv[1]#Command line arguments. argv[0] contains program name. 
import os.path
os.path.join()
os.path.basename(path)#basename if a file, empty for directory. might not work with Windows
os.path.abspath(path)#get the absolute filepath
os.path.dirname(path)#directory name
os.path.splitext(filename)#tuple with Path+Name and Extension
os.path.isfile(filename)#check for type or existence
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
### Exceptions
Rasising Exceptions
```python
raise Exception("Message")
assert(1==2)#Assertions raise an AssertionError
```

Try statement
```python
try:
  somecode()
except KeyError:
  someOtherCode #Can use 'pass' to jump out of this section
else:
  code #if no exception was thrown
finally:
  code #Always execute this code. Usually, you can also write it directly after without finally
```

Custom Exceptions
```python
class MyError(Exception): #Derived from Exception class
    def __init__(self, value): 
        self.value = value 
    def __str__(self): 
        return(repr(self.value)) 
```



### Object Orientation
General syntax:
```python
class test(object):#Derived from 'object'
  def __init__(self, var1, var2):#Konstruktor
    self._var1=var1
    self._var2=var2
    super().__init__()#If derived from another class, we can access parent methods through super()
  
  @classmethod
  def formString(cls, string):#The recommended way to create different Constructors are multiple classmethods
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
mo1==mo2#This checks whether the objects are equal according to their __eq__ implemntation (for example they have the same content)
mo1 is mo2#Whether mo1 and mo2 relly point the the same instance in memory
```
#### Decorators
https://realpython.com/primer-on-python-decorators/
Decorators: define two functions a:int->int, F:func->func. Now, you can do `a=F(a)` to get a new function a passed through F. Usually, F is a wrapper that does some pre and post processing. Shorthand for this is `@F`. Useful applications: Debugging: Print function arguments! Timers, Register function in dict, ...
```python
def F(func):
  def wrapper(*args, **kwargs):
    #do something before
    val=func(*args, **kwargs)
    #do something after
    return val
@F
def a(var):
  ...
```

#### Get/Set
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

#### Operator overloading
https://realpython.com/operator-function-overloading/#making-your-objects-capable-of-being-added-using
Implement by use of special methods like `__add__`, `__mul__`,... By convenction, add and similar should return a new instance of the class!
```python

```

### Datetime module
Datum und Zeit
Übersicht: https://www.programiz.com/python-programming/datetime
Vergleiche: PlotSeries.py
```python
import datetime
from dateutil.parser import parse
```
#### Datum aus String 
```python
strptime()
time = np.array([datetime.datetime.strptime(TimeString[i],"%m.%d.%y %H:%M:%S") for i in range(len(TimeString))])
"%m.%d.%y %H:%M:%S.%f"#falls mit Milliseconds
```
####String aus Datum:
```python
s=time.strftime("%H:%M")
```

####Differenz in Sekunden: 
(a-b).total_seconds()
```python
t=np.array([(time[i]-time[i+1]).total_seconds() for i in range(len(time))])
```

####Zeiten addieren:
```python
time=time+timedelta(hours=7)
```

#### Zeiten Plotten 
"time" muss dabei wieder ein Array aus datetime-Objekten sein.
Vergleiche: PlotJPLResults.py
```python
import matplotlib.dates as dates
ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
```


Wichtig: Wenn Daten außer einer Uhrzeit auch ein Datum enthalten, muss dieses in den Limits auch angegeben werden.

```python
ax.set_xlim(datetime.datetime.strptime("8.21.2017 15:00","%m.%d.%y %H:%M:%S"),datetime.datetime.strptime("8.21.2017 16:00","%m.%d.%y %H:%M:%S"))
```

Abstände der Labels (hier 2 Minuten)
```python
ax.xaxis.set_major_locator(dates.MinuteLocator(interval=2))
plt.plot(time,d)
```






### time Module

```python
import time
time.sleep(5.5)#5.5 seconds pause
```











## Numpy
#### Numpy I/O
```python
np.save("folder/file",array)#save as binary numpy object
array=np.load("folder/file.npy")#load binary object
array=np.genfromtxt("file")#load from asciifile
A=np.genfromtxt('file_name',skip_header = N,max_rows =1)#read only specific line/range
```

#### Numpy Arrays
```python
a=np.zeros(100)
b=np.ones((10,20))#2d Array
b.shape#Tuple (10,20)
b.size#Number of elements: 200
b.ndim#NUmber of dimensions: 2
```
make e.g. two 2D grids of two 1D arrays. With ij, every column of xgrid equals x, every row of ygrid equals y. This is the "matrix interpretation".
```python
xgrid, ygrid=np.meshgrid(x,y,indexing='ij')
```

#### Indexing
Boolsche Indizes: auswählen eines bestimmten Teilarrays
<,>,== geht direkt, für Verknüpfung (Oder, Und) mehrerer Ausdrücke:
```python
b=np.logical_and(t<deltat, t>=0)
```
Elementwise boolean operations: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.logic.html
```python
np.logical_and(a,b)#perform logical and elementwise
```
####Basic Slicing
```python
array[start:stop:step]#if start/stop<0, replace by start/stop+n with n the dimension of the axis
```


#### Numpy sortieren
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

### Numpy array transformations
#### Broadcasting
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
##### Numpy Array reshape
Imagine the old array to be flattened first: First, the last dimension is counted up (0,1,2,3...), then the second last is raised +1 and the last counted up again and so on.
Secondly, the resulting 1d array is filled into the new one by the same principle: the first (50) elements of the 1D array are put in the last dimension (0-50), then the second last dimension (0-400) is raised +1 and the next (50) elements are put into the last dimension (0-50) again, and so on.
```python
new=old.reshape((3,400,50))
```

#### stack/extend/combine/transpose numpy arrays
```python
np.column_stack((arr1, arr2, arr3))#combine 1D arrays to 2D
np.row_stack((arr1, arr2, arr3))
np.repeat(arr1[:, :, np.newaxis], n_repeat, axis=2)#repeat a given array into a new direction
arr.transpose(1,0,2)#switch the order of axes. Similar to arr.T in two dimensions
```
#### combine multidimensional arrays
```python
np.concatenate((arr1, arr2), axis=1)#must have same dimensions except on the concatenation axis
```
#### masked arrays
numpy support masked arrays with `numpy.ma` module. These are useful in combination with e.g. some plots
```python
arr_mask = np.ma.masked_where(mask, arr)
ax.imshow(arr_mask, cmap=mymap)#use mymap.set_bad('b') to set the masked values to blue!
```
### Numpy Datentypen
```python
arr2=arr1.astype(int)#Array conversion
```

### Numpy Funktionen
```python
np.mean(Array, Axis=0)#Numpy
np.histogram2d(x,y,weights=z, bins=10)#1 or 2d histogram in numpy. See also binned_statistics in scipy
np.arctan2(y,x)/np.pi*180#Gives the angle of a point (in radians!) x,y including information about the quadrant (be aware: arctan2(y,x), NOT x,y!)
#x=1, y=1: 45°, x=-1, y=1: 135°, x=-1, y=-1: -135°, x=1, y=-1: -45° (upper half (y>0) positive angles, lower half negative angles)
#Easy transformation 0 to 360: (360+angle)%360
np.interp(x_new, x_old, y_old)#perform linear interpolation of the old values at the adjacent old points. x_old must be increasing if not specified further!
np.trapz(y, x)#integral over y (sampling points located at x)
```

### Statistics
```python
np.random.rand(*arr.shape)#produce random numbers between 0 and 1 in an array with the given dimensions
np.random.normal(0,1,(2,2))#produce normal distributed values in an array with the given shape
np.random.multivariate_normal(a,b)#produce a set of numbers (vector), such that these variables in the limit of many observations have the given covariance matrix b (around the mean vector a).
```

### Fourier Transformations
```python
sig_f=np.fft.fft(sig)#Simple discrete Fourier transform
sig2d_f=np.fft.fft2(sig2d)#For 2d arrays (images)
```
Sig_f contains the amplitudes corresponding to the frequencies given from `np.fft.fftfreq(N, d=1.0)`, with `N=len(sig)`. The general format is [k0, k1, ..., kN/2, k(-N/2), ... k(-1)], and the values are just kn=n/(N*d). Therefore, to get the real frequencies k we usually want in e^(ikx), we have to set d=dx/(2 * pi), with dx the spacing of the real space points in `sig`.


## Scipy
### Statistics
```python
from scipy import stats
stats.binned_statistic_2d(x, y, values, 'mean', bins=[binx,biny])#Extended version of histogram2d in numpy. Also allows to take the mean and more over all weights.
```
#### Distribution functions
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

## Pyplot/Matplotlib
https://matplotlib.org/faq/usage_faq.html#usage
Basic structure: A Figure object is the empty window which contains the plots.
In the figure is a certain number of Axes objects, the actual "plots".
Each Axes object can have for example two or three Axis-objects, the actual "axes of the plots". Axes!=Axis!!!

####create plot
```python
fig,ax=plt.subplots()
fig2, ax2=plt.subplots(nrows=2, ncols=2)#ax2: either 1D or 2D array => use atleast2d().T if necessary
fig.suptitle('This is a somewhat long figure title', fontsize=16)
```


#### Axen und Ticks
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

ax2.set(ylabel="ratio", title="Titel")#Beschriftung
ax.grid(True, which='major')#Gitter. Positions according to xticks major/minor
ax.set_yscale("log")#set axis to logscale (also linear, symlog, ...)
```
#### Beschriftung mit Latex
```python
plt.rc('text', usetex=True) #always necessary?
ax1.set_xlabel(r'Irradiance [$\frac{mW}{m^{2}nm}]$', fontsize=18)
ax.plot(x,y, label=r'$\phi={0}\pi$'.format(i))#use variable in latex label
ax.yaxis.set_label_position("right")#which side
ax.yaxis.set_label_coords(-0.1, 0.5)#exakte position
```
#### Legende
```python
legend2 = ax2.legend(loc='lower right', shadow=True, fontsize='medium', ncol=2, title='Some lines')#Legende
dummy_lines = []#Legende nur mit Linestyle
dummy_lines.append(ax.plot([],[], c="black", linestyle ="-", linewidth=1.2)[0])
dummy_lines.append(ax.plot([],[], c="black", linestyle ="--", linewidth=1.6)[0])
legend = ax.legend(dummy_lines, ["Measurements", "Simulation"])
ax.add_artist(legend2)
```
Multiple legends in one axes object
```python
leg1=ax.legend()
leg2=ax.legend()
ax.add_artist(leg1)
ax.add_artist(leg2)
```

#### linestyle cycle
```python
from itertools import cycle
lines = ["-","--","-.",":"]
linecycler = cycle(lines)
ax.plot(x,y, linestyle=next(linecycler))
```


#### colorbar

##### Create colorbar
They always live in their own axes object!
All maps: https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html
```python
cbar=fig.colorbar(im, ax=ax, orientation='vertical')#In this case, the colorbar space is 'stolen' automatically from ax! Otherwise, use 'cax=ax'
#Manual way: If there are multiple axes and we want to assign a colorbar to one, we can create a small axes next to the axes with the image:
cbar.set_label("Label")
cbar.ax.tick_params(labelsize=10)
from mpl_toolkits.axes_grid1 import make_axes_locatable
def add_colorbar(fig, ax, image, **kwargs):
  divider = make_axes_locatable(ax)#If there are multiple axes 0,1,2,3...
  cax = divider.append_axes('right', size='5%', pad=0.05)
  return fig.colorbar(image, cax=cax, **kwargs)
```
##### Colorbar limits and scale
https://matplotlib.org/users/colormapnorms.html
```python
import matplotlib.colors as colors
ax.matshow(Mat, norm=colors.SymLogNorm(linthresh=0.003, linscale=1.0, vmin=-2.0, vmax=2.0))#log scale with symmetric area around 0. linthresh: the value, where the linear range starts. linscale: if 1.0, the linear range has the width of one order of magnitude on the colorbar.
```
Make a categorial colorbar with custom categories
```python
cmap=plt.cm.get_cmap('binary', 2), vmin=-0.5, vmax=1.5)
# This function formatter will replace integers with target names
corelabels={0:'no core', 1:'core'}
formatter = plt.FuncFormatter(lambda val, loc: corelabels[val])
cbar=add_colorbar(fig, ax[0,1], im,ticks=[0,1], format=formatter)
```

##### Color cycle setzen
```python
cm = plt.get_cmap('gist_rainbow')#Cmaps: https://matplotlib.org/examples/color/colormaps_reference.html
ax.set_prop_cycle(plt.cycler('color', [cm(1.*i/15) for i in range(15)]))
```
#### Modify colormaps
If you want to present the same information, but in an different style, vmin and vmax are not sufficient. You need to create you own colormap, e.g. as a cutout of a predefined colormap.
```python
import matplotlib.colors as colors
def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap
cmap = plt.get_cmap('jet')
new_cmap = truncate_colormap(cmap, 0.2, 0.8)
```

#### Zweite Axe rechts:
```python
ax2=ax.twinx()#twiny() for axis on top
```

#### Figuren
```python
ax.axvline(x=20)#axhline(y=20)
```
##### Kreis plotten
```python
circle1 = plt.Circle((1000, 1000), 30, color='r', fill=True)
ax.add_artist(circle1)
```

#### Save File Location default and default extension (pdf)
```python
plt.rcParams["savefig.directory"] =os.path.dirname(os.path.abspath(__file__))#need to "import os"
plt.rcParams["savefig.format"]="pdf"
fig.savefig("Plot1.pdf")#save plot
```
#### Backend
```python
matplotlib.use("Agg")#specify backend, before importing pyplot! Important if Display variable is not set. Alternative: TkAgg
matplotlib.get_backend()#get backend
print(matplotlib.matplotlib_fname()) #find matplotlibrc
```


#### Arange subplots
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

#### Text and annotations
Generally, font sizes can be given absolute in pt or relative to `font.size` from the rc parames. Relative measures are: `xx-small, x-small,small, medium, large, x-large, xx-large, larger, or smaller`
```python
ax1.text(1,2,"Hallo", rotation=45,fontsize='large')#Annotation, Text
ax1.annotate("Hallo", xy=(0.5,0.5), xytext=(0.6,0.6), xycoords='axes fraction')#more functions than simple text, e.g. make arrows and give coordinates in different formats
```

#### Plot types
##### Lines, points and bars
```python
ax.plot(x,y,'.-', linewidth=0.4,label="label")
ax.scatter(x,y,alpha=0.5, marker='.')#scatter plot. alpha sets transparency of points, which is useful to visualize the density as well. useful markers: 'o', '.', ',', 'x'
ax.errorbar(x,y,xerr, yerr)#like ax.plot, but with errorbars to show standard deviation
ax.fill_between(x,y-yerr, y+yerr)#draw the error as shaded region between two curves
ax.bar(xarr,height=yarr, width=1.5)#Barplot with vertical bars (columnplot). For horizontal, use barh and exchange height and width
```
##### Histograms
```python
n, bins, _ =ax2.hist(distance,bins=100, weights=values, range=(-60,60), density=True, cumulative=False)#histogramm. If density=True, the y axis values are in units of %/xaxis, i.e. np.sum(n[-1]*np.diff(bins))=1.0. (n[-1] in the case of multiple categories and stacked=True, for a plot with one category it is just n*np.diff) Cumulative allows for cumulative histograms
im=ax2.hist2d(x,y,bins=100, weights=values, range=(-60,60), cmin=1)[3]#histogramm 2d, object for colorbar is the fourth returned object. Cmin: All values below are set to nan.
```

##### Images (2D Verteilung) plotten
Imshow is usually the fastest solution. It is for data on a regular grid. Use 'extent' to set the axes coordinates if they should be something else than pixels. Things become tricky together with 'aspect', which is like a scaling factor height=aspect*width. By default, aspect=1, i.e. the PIXELS are kept squares IN AXES COORDINATES. E.g. if your xaxis is 1000 (m) and your y axis 1 (m), the image will appear extremly elongated. In this case, set aspect to 1000 and the yaxis will be stretched, such that the RESULTING IMAGE looks like a square.
```python
from matplotlib.colors import LogNorm#falls mit LogNorm
im=ax.imshow(b, cmap='gray', interpolation='none', norm=LogNorm(), extent=(0,1,0,1))#b: 2D Array mit Pixelwerten. Use "extent" to give the image a coordinate measure other than just pixels.
im.cmap.set_under('k',1.) 
```
```python
contour=ax.contour(x,y,z, colors='k')#Contour plot: Draw height lines ('isobares')
ax.clabel(contour, colors = 'k', fmt = '%2.1f', fontsize='medium')#write height values to lines

ax.contourf(x,y,z, cmap='Greys')#Draw a filled contour plot, i.e. with areas rather than lines.
ax.pcolormesh(x,y,c)#plot 2d with non-regular grid. x,y: 1D arr with length one greater than c. C: 2darr, rows are plotted as y, columns are x
```


#### Animationen
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

## Subprocess
Library to execute commands on commandline (bash)
```python
import subprocess as sp
sp.call("echo test", shell=True)#Simple execution of string
```

## Pandas
My personal style guide: Stick to numpy arrays. If necessary (for comfort), make up columnnames like A=0, B=1 so you can call array[4,A].

#### Create Data Frame
```python
test=[[4,5,6],[1,2,3]]
testdf=pd.DataFrame(test,columns=['A','B','C'])
```
#### read from file
```python
data=pd.read_csv("FileName")
```

#### acces element
both work with boolean indexing
```python
data.loc['A','B']#if you use column/row names
data.iloc[1:2,3:4]#if you use indices
```
important: iloc chooses based on the POSITION, loc is based on the LABEL! Can be confusing because, e.g. for rows, integers can be labels as well.

#### boolean indexing
```python
 s[(s < -1) | (s > 0.5)]
```

#### get columns
```python
datadp.columns
```

#### Categories in one column
```python
np.unique(testdf.A)
```

#### iterration over rows
```python
for index, line in df.iterrows():
    print(line)
```
#### Groupby
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

## Geopandas
Library on top of pandas and shapely, which allows to plot maps. Basic idea: A pandas dataframe with a special column "geometry", which contains shapely objects (Points, LineStrings or Polygons), which can represent cities, streets or countries.
```python

```

### Maps (Contextily)
However, if you want to plot data on a map, you need more than geopandas, since geopandas is basically just shapely with coordinate transformations. Maps of the earth usually consist of tiles, which are provided by different providers like e.g. OSM. To download such tiles and add them to a matplotlib figure, `contextily` is made.
Documentation: https://contextily.readthedocs.io/en/stable/index.html
Generally, contextily works in Spheric Mercator projection (EPSG:3857), so you need to convert all your coordinates first! (Sometimes, lon/lat is also accepted)

#### Plot geopandas
```python
import contextily as ctx
gdf=gdf.to_crs(epsg=3857) #Convert your geopandas dataframe to the projection used by contextily 
ax=gdf.plot()
ctx.add_basemap(ax,zoom=6) #Add basemap to axes. Use the axes you get back from geopandasdf.plot()
```

#### Details
```python
ctx.howmany(w, s, e, n, 6, ll=False) #How many tiles will be downloaded at zoom level 6. If ll, bounding box is given in lon/lat
sources=[i for i in dir(ctx.tile_providers) if i[0]!='_'] #list all providers included in ctx
srcurl=getattr(ctx.sources, sources[2]) #select a provider
img, ext=ctx.bounds2img(w, s, e, n, 6, url=srcurl, ll=False)#If you want the map as an array image
plt.imshow(img, extent=ext)
```
## NETCDF
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
## Xarray
https://xarray.pydata.org/en/stable/index.html
Generalization of pandas to work with higher dimensional data, basically a front-end for the netcdf format. Basic idea: The fundamental element is the DataArray. It describes values of one variable, which implements certain dimensions. A dimension can be seen as one axis in the higherdimensional space the variable exists in. Each dimension usually has a list of coordinates, these are labels which specify certain positions on the axis (think of the axis 'ticks'). Technically, dimensions are just DataArrays itself.
Multiple DataArrays can be contained in a Dataset. Not every array in a Dataset needs to implement all dimensions. Datasets are usefull because you can perform some operations on many DataArrays at once, e.g. slicing along one dimension, which will slice every DataArray which implements this dimension.

```python
import xarray as xr
#Datasets
ds=xr.open_dataset("filename")#open Dataset
ds=xr.Dataset({'name':DataArray})#create Dataset
ds.to_netcdf("filename")#save Dataset
ds.temp#select a Data variable
ds['temp']=ds.temp.astype(float)#convert a variable or dimension to another type. You have to use the [.] notation for assignments
ds=ds.squeeze(drop=False)#Fix/Drop all dimensions with length one
da.drop([d for d in list(data.coords.keys()) if d not in data.dims])#Drop all non-dimensional coordinates
#DataArrays
da=xr.DataArray(nparray, coords=[('x',xarr), ('y', yarr)])#Create a DataArray from numpy
da.name='radiance'#DataArrays can have names to identify them in Datasets
da.attrs['long_name']='lorem ipsum'#DataArrays can store attributes
da.attrs['units']='km'#long_name and units is used by the .plot() routine
```
### Inspecting data
```python
#DataArrays:
da.dims#The dimension names of the data
list(da.coords.keys())#The names of the coordinates (also non-active ones which are squeezed)
#Datasets:
list(ds.data_vars)#The names of the Data variables in the set
list(ds.variables)#Everything: names of the variables AND coordinates (also squeezed ones)
npt.assert_equal(sorted(list(ds.data_vars)), ['a', 'b'])#Check the formatting
```

### Selecting data
https://xarray.pydata.org/en/stable/indexing.html
```python
da[...,2]#based on coordinate index and dimension index
da.loc[...,'z']#based on coordinate label and dimension index
ds=ds.isel(temp=0)#selection based on index along the dimension
ds=ds.sel(temp=34.3)#34,3°C. Selection based on coordinate of the dimension
ds.sel(temp=30, method='nearest', tolerance=5)#Nearest neighbour lookup to find a value close to 30!
da.sel(x=da.x[da.x<-0.1])#Boolean indexing works only positional with []!
da.drop_sel(x=...)#like sel, but return everything except the selected part
```
### Asignments
This is something a little counterintuitive in xarray: You can never assign values to isel() or sel()! Instead, it is possible with loc[] or xr.where(cond, returnTrue, returnFalse)
```python
da.loc[db.coords]=db#Assign values of db to a subset of da
```

### Coordinates
Each dimension can have a coordinate array assigned. Imagine them as the tick labels of the dimension axis. Additionally, you can assign furhter coordinates to the dimension, which are then non-coordinate arrays! E.g., this is useful if you want to reference every "tick" on an dimension axis by two labels like weekday and monthday.
Be aware: Dimensions have names. You see them in () when printing. Coordinates can have the same names as the dimension they label (e.g. 'space') or different names (e.g. 'weekday' for dimension 'time'). In the latter case, you must of course tell xarray that 'weekday' belongs to the dimension 'time'.
```python
locs = ['A','B','C']
weekdays = ['Mon', 'Tue', 'Wed', 'Thurs']
foo = xr.DataArray(np.random.rand(4, 3), coords={'weekday':('time', weekdays), 'space':locs}, dims=['time', 'space'])#DataArray with two dimensions with coordinates
foo.coords['month'] = ('time', [6, 7, 8,9])#another coordinate set for dimension time
foo=foo.swap_dims({'time':'monthday'})#Now 'monthday' is the new "main" label for the dimension time
da.get_axis_num('y')#useful when using numpy with da.values
da.reindex(x=[1,1,2,3], method='nearest')#return data of da, but with new coordinates
```

### combining/extending data
```python
new=xr.concat([old1, old2], dim='time')
data.expand_dims({'newdim':[1,2,3]})
a2, b2=xr.broadcast(a,b)#Xarray support broadcasting by dimension names. I.e., if a has dimension 'x' and b has dimensions 'x' and 'y', a is extended to have 'x' and 'y' as well, irrespective of the order (this is different to numpy, where broadcasting is done positional). For computation like a*b, this works automatically.
data1=data1.combine_first(data2)#extend data1 by the values of data2 (introducing nans if empty areas are created), but keep the values of data1 if there are already some present.
xr.combine_nested([[a1, a2], [a3, a4]], concat_dim=['x', 'y'])#Combine with position of subsets encoded in list of lists
```

### Modifying data
```python
ds.mean(dim='time')#calculate mean/sum/...
dist.where(condition,other=na, drop=False)#return where cond is true and fill in 'other' where it is false (default na). If drop, coordinates with only false are dropped.
ds.coarsen(photons=4).mean()#calculate mean over blocks of 4 along photons
ds.drop_vars('a')#remove a variable
ds.drop_dims('time')#remove a dimension and all related variables
da.rename({'old':'new'})#Rename a var or coord in a DataArray
da.transpose('y', 'z',..., 'x')#Reorder dimensions. Use ellipsis if further dimensions are present.
da.sortby('time')#Also sortby(['time', 'lat'])
da.dropna(dim='time', how='any')#Drop the label if any (alternative: all) value is nan
da.stack(z=('x', 'y'))#create a single multiindex from multiple existing indices
```

### apply_ufunc
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

### Plotting data
```python
da.plot(x='a') #1D. Data is automatically plotted in the 'open' dimension y
da.plot(x='a', hue='b') #2D
da.plot(x='a', hue='b', col='c', col_wrap=2) #3D with multiple subplots
da.plot(x='a', hue='b', col='c', row='d') #4D
```


## Image processing
####Convolution
```python
from scipy import signal as sig
AcM=sig.convolve2d(A,M, mode='full', boundary='fill', fillvalue=0)
```
boundary: How boundary conditions are treated: fill missing values on the rim with a value, use periodic boundary conditions ('wrap') or mirror the values directly at the rim to the outside ('symm')
mode: Size of the resulting array, 'full', "valid", or "same"

## CLI Arguments
`argparse` is a useful package to parse command line arguments
```python
import argparse
par=argparse.ArgumentParser()
par.add_argument('flight', type=str)#Add command line arguments
par.add_argument('mode', type=int)
par.add_argument('-s',action='store_true')#Boolean flag
args=par.parse_args()
number=args.mode#Access argument values
```

## Create your own modules
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
#### Module Structure
Typical directory structure
```text
new_project
├── packagename
│   ├── __init__.py         # make it a package
│   └── antigravity.py
└── test
    ├── __init__.py         # also make test a package
    └── test_antigravity.py
```
```python
import packagename# import the functions provided in __init__.py
from packagename import antigravity# import the antigravity module
from antigravity.antigravity import my_object# or an object inside the antigravity module
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


#### How to write proper docstrings for functions/classes:
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
## Unittests
https://realpython.com/python-testing/
```python
import unittest as ut
class SomeTests(ut.TestCase):
  def setUp(self):
    #come code if necessary
  def test_something(self):#Must start with test_
    #testing with asserts
```
### Execute tests
Best to use the command line interface. Take the example from 
[the importing modules section](#module-structure)
```bash
cd new_project
python3 -m unittest discover #All tests in test directory. use -t testdir if not named test.
python3 -m unittest test.test_antigravity #one specific test (python notation)
```
unittest introduces a few improved assertions:
```python
with self.assertRaises(SomeException): MyFunc(arguments)#Test for exception
```
