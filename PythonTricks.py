Install:
sudo apt install python3
Pip: sudo apt install python3-Pip   
import numpy as np



#Verschiedenste Tricks im Umgang mit Python
################################Allgemein#################################
sys.exit()#beendet ein Python Program #Stop #Interrupt

#Datentypen
int(x)#convert to integer

#################################Arrays###################################
for index, values in enumerate(array, start)#returns the position as well as the value of the array
#numpy.ndenumerate: Extremely useful for looping over multidimensional arrays! Gives index as tuple.
#if index should be single value: enumerate(array.flatten())

np.atleast_1d(arrays)#Converts scalars to array and leaves everything else untouched=>Usefull for functions to handle scalars as well arrays
np.atleast_2d(array)#convert to 2d by "adding one pair of brackets": array2d=[array1d] or array2d=[[scalar]]

##################################Lists###############################
#Like Arrays, but can (1) contain different data types and (2) be extended dynamically
liste=[]
liste.append("Hallo")
liste.append(liste2)#list of lists
############################Dateipfade########################paths#file
import os.path

############################Datetime module##############################
#Datum und Zeit
#Vergleiche: PlotSeries.py
import datetime
from dateutil.parser import parse
#Datum aus String: strptime()
time = np.array([datetime.datetime.strptime(TimeString[i],"%m.%d.%y %H:%M:%S") for i in range(len(TimeString))])
"%m.%d.%y %H:%M:%S.%f"#falls mit Milliseconds
#String aus Datum: strftime()
s=time.strftime("%H:%M")
#Differenz in Sekunden: (a-b).total_seconds()
t=np.array([(time[i]-time[i+1]).total_seconds() for i in range(len(time))])
#Zeiten addieren:
time=time+timedelta(hours=7)

#Zeiten Plotten: "time" muss dabei wieder ein Array aus datetime-Objekten sein.
#Vergleiche: PlotJPLResults.py
import matplotlib.dates as dates
ax.xaxis.set_major_formatter(dates.DateFormatter('%H:%M'))
#Wichtig: Wenn Daten außer einer Uhrzeit auch ein Datum enthalten, muss dieses in den Limits auch angegeben werden.
ax.set_xlim(datetime.datetime.strptime("8.21.2017 15:00","%m.%d.%y %H:%M:%S"),datetime.datetime.strptime("8.21.2017 16:00","%m.%d.%y %H:%M:%S"))
#Abstände der Labels (hier 2 Minuten)
ax.xaxis.set_major_locator(dates.MinuteLocator(interval=2))


plt.plot(time,d)




############time Module######
import time
#Pause
time.sleep(5.5)#5.5 seconds pause




##########################################Numpy##########################################################
#Numpy Arrays erstellen
np.zeros(100)
np.ones(100)
xgrid, ygrid=np.meshgrid(x,y)#make e.g. two 2D grids of two 1D arrays

#Boolsche Indizes: auswählen eines bestimmten Teilarrays
#<,>,== geht direct, für Verknüpfung (Oder, Und) mehrerer Ausdrücke:
b=np.logical_and(t<deltat, t>=0)
print(t[b])
#Elementwise boolean operations: https://docs.scipy.org/doc/numpy-1.13.0/reference/routines.logic.html
np.logical_and(a,b)#perform logical and elementwise


#Numpy sortieren
#argsort: Liefert array mit den Indizes in der sortierten Reihenfolge => einsetzen liefert sortiertes Array
ind=np.argsort(a)
print(a[ind])#sortiert


#Numpy Elemente finden: np.where gibt array zurück mit allen reihenindizes in einem array und allen columnindizes in zweitem.Bsp:
a=[1,1,1,2,2,3]
indexarray=np.where(a==1)#gibt array: (array([0, 1, 2]),)=> indexarray[0] ist also [0,1,2] für die vorkommen von "1" in a

#Numpy Array reshape
#Imagine the old array to be flattened first: First, the last dimension is counted up (0,1,2,3...), then the second last is raised +1 and the last counted up again and so on.
#Secondly, the resulting 1d array is filled into the new one by the same principle: the first (50) elements of the 1D array are put in the last dimension (0-50), then the second last dimension (0-400) is raised +1 and the next (50) elements are put into the last dimension (0-50) again, and so on.
new=old.reshape((3,400,50))

#combine numpy arrays
np.column_stack((arr1, arr2, arr3))#combine 1D arrays to 2D
np.row_stack((arr1, arr2, arr3))

#Numpy Datentypen
arr2=arr1.astype(int)#Array conversion

#Numpy Funktionen
np.mean(Array, Axis=0)#Numpy

np.arctan2(y,x)#Gives the angle of a point x,y including information about the quadrant (be aware: arctan2(y,x), NOT x,y!)
#x=1, y=1: 45°, x=-1, y=1: 135°, x=-1, y=-1: -135°, x=1, y=-1: -45° (upper half (y>0) positive angles, lower half negative angles)
############################################Pyplot/Matplotlib###############################################################################################
#https://matplotlib.org/faq/usage_faq.html#usage
#Basic structure: A Figure object is the empty window which contains the plots.
#In the figure is a certain number of Axes objects, the actual "plots".
#Each Axes object can have for example two or three Axis-objects, the actual "axes of the plots". Axes!=Axis!!!

###create plot
fig,ax=plt.subplots()

###Axen und Ticks
ax.set_ylim(1e-7,5e1)#Limits
ax.set_xticks([1,2,3])#Ticks setzen. ax.get_xticks() liefert ticks
ax.tick_params(labelsize=16)

ax2.set(ylabel="ratio", title="Titel")#Beschriftung
ax.grid(True, which='major')#Gitter
###Beschriftung mit Latex
plt.rc('text', usetex=True)
ax1.set_xlabel(r'Irradiance [$\frac{mW}{m^{2}nm}]$', fontsize=18)
ax.plot(x,y, label=r'$\phi={0}\pi$'.format(i))#use variable in latex label

###Legende
legend2 = ax2.legend(loc='lower right', shadow=True, fontsize='medium')#Legende
dummy_lines = []#Legende nur mit Linestyle
dummy_lines.append(ax2.plot([],[], c="black", linestyle ="-", linewidth=1.2)[0])
dummy_lines.append(ax2.plot([],[], c="black", linestyle ="--", linewidth=1.6)[0])
legend2 = ax2.legend([dummy_lines[i] for i in [0,1]], ["Measurements", "Simulation"], loc="upper left")
ax2.add_artist(legend2)

#Color cycle setzen
cm = plt.get_cmap('gist_rainbow')
ax.set_prop_cycle(plt.cycler('color', [cm(1.*i/15) for i in range(15)]))
#linestyle cycle
from itertools import cycle
lines = ["-","--","-.",":"]
linecycler = cycle(lines)
ax.plot(x,y, linestyle=next(linecycler))

###colorbar: They always live in their own axes object!
cbar=fig.colorbar(im)#If there are multiple axes and we want to assign a colorbar to one, we can create a small axes next to the axes with the image:
cbar.set_label("Label")
cbar.ax.tick_params(labelsize=10)
from mpl_toolkits.axes_grid1 import make_axes_locatable
divider = make_axes_locatable(ax[0])#If there are multiple axes 0,1,2,3...
cax = divider.append_axes('right', size='5%', pad=0.05)
fig.colorbar(contour, cax=cax)

###Zweite Axe rechts:
ax2=ax.twinx()#twiny() for axis on top

###Figuren
ax.axvline(x=20)#axhline(y=20)
#Kreis plotten
circle1 = plt.Circle((1000, 1000), 30, color='r', fill=True)
ax.add_artist(circle1)

###Save File Location default and default extension (pdf)
plt.rcParams["savefig.directory"] =os.path.dirname(os.path.abspath(__file__))#need to "import os"
plt.rcParams["savefig.format"]="pdf"

###Size of plots
fig = plt.figure(figsize=(4,3))#Define grid and specify over how many cells axes spread
grid = plt.GridSpec(4, 3, hspace=0.4, wspace=0.2)
ax1 = fig.add_subplot(grid[:-1,:])
ax2 = fig.add_subplot(grid[-1, :])

###############Plot types#############
ax2.hist(distance,bins=100, weights=values, range=(-60,60))#histogramm
ax1.text(1,2,"Hallo", rotation=45)#Annotation, Text

###############Images (2D Verteilung) plotten#################
from matplotlib.colors import LogNorm#falls mit LogNorm
im=ax.imshow(b, cmap='gray', interpolation='none', norm=LogNorm())#b: 2D Array mit Pixelwerten
im.cmap.set_under('k',1.) 


#######################Animationen########################
import matplotlib.animation as animation
fig, ax=plt.subplots(2,2)
ims=[]
for i in range(1,200):
    im=ax[0,1].imshow(image[i], cmap="Greys_r")
    ims.append([im])
ani = animation.ArtistAnimation(fig, ims, interval=30, blit=True, repeat_delay=40)
ani.save('SimpleBox.mp4')
plt.show()


#############################Image processing#####################################
#Convolution
from scipy import signal as sig
AcM=sig.convolve2d(A,M, mode='full', boundary='fill', fillvalue=0)
#boundary: How boundary conditions are treated: fill missing values on the rim with a value, use periodic boundary conditions ('wrap') or mirror the values directly at the rim to the outside ('symm')
#mode: Size of the resulting array, 'full', "valid", or "same"


############################################Create your own modules#################################
#https://www.digitalocean.com/community/tutorials/how-to-write-modules-in-python-3
#All about paths and importing from other directories
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
