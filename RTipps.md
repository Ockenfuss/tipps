Tipps zum Umgang mit R
https://www.rstudio.com/resources/cheatsheets/ #Cheatsheets
http://adv-r.had.co.nz/ #Advanced topics like memory management, functional programming, etc. 


<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [General](#general)
  - [Datatypes](#datatypes)
    - [Lists](#lists)
    - [Tables](#tables)
    - [Vectors](#vectors)
    - [Matrix](#matrix)
  - [Finden&Vergleichen](#findenvergleichen)
  - [Sortieren](#sortieren)
  - [Nützliche Funktionen](#nützliche-funktionen)
  - [Curve Fits](#curve-fits)
  - [Apply](#apply)
  - [Data Frames](#data-frames)
- [Colnames (Analog: Rownames) setzen/lesen:](#colnames-analog-rownames-setzenlesen)
- [Strings nicht zu Faktoren konvertieren:](#strings-nicht-zu-faktoren-konvertieren)
- [Joining](#joining)
  - [Strings](#strings)
  - [Boolean](#boolean)
- [Operators: single (& or |) perform vectorized comparison, double (&& or ||) compare only first elements of vectors](#operators-single-or-perform-vectorized-comparison-double-or-compare-only-first-elements-of-vectors)
  - [In- and Output](#in-and-output)
    - [Input](#input)
    - [Output](#output)
- [colored text output: https://github.com/r-lib/crayon](#colored-text-output-httpsgithubcomr-libcrayon)
  - [Working with Files](#working-with-files)
  - [Tidy Package](#tidy-package)
  - [Statistik](#statistik)
  - [GGPlot2](#ggplot2)
  - [Lineplots](#lineplots)
  - [Barplots](#barplots)
  - [Arrange multiple plots](#arrange-multiple-plots)
  - [General language behaviour](#general-language-behaviour)
- [Environment](#environment)
  - [Installation](#installation)
  - [Packages](#packages)
  - [R Documentation](#r-documentation)

<!-- /code_chunk_output -->

# General
## Datatypes
```R
class(c(1,2,3)) #Typbestimmung
```
Faktoren: Bestimmte häufig gebrauchte Merkmale (z.B. male/female). Achtung: !=Strings!!
Faktor zu String konvertieren:
v=factor(c("l", "n", "n", "i", "l"), levels = c("n", "l", "i"))
levels(v)[v[1]]#Idee: levels gibt faktoren als strings zurück, suche daraus richtigen aus
mapvalues(x, from=c("a", "b"), to=c("A","B"))#library(plyr): ändert Faktornamen=> praktisch um in data frames zusätzliche 1:1 Beziehungen zu speichern, z.B. Ortsname und eindeutige zugehörige Abkürzung

Ausgabeformat von Zahlen als Strings
options(OutDec= ".")

### Lists
Leere Liste:
list()

names(list)#Namen in List 
list[c("a", "b")]#gibt Liste mit einelementigen Sublisten mit den Werten von "a" und "b"
unlist(list[c("a","b")])#Vektor mit den Elementen aus "a" und "b" in "list" (i.A.: "unlist" löst alle Sublisten auf und fügt den Inhalt anschließend zu einem Vektor zusammen)

### Tables
t=table(c(0.7,0.8,0.8,0.9))#Erstellt Tabelle mit Häufigkeiten (eig. named vector)
t[[2]]#=2 da 0.8 zweimal
names(t)

### Vectors
Leerer Vektor:
v=vector()
Add elements:
v=c(v,1:10)
konstanter wert 1
rep(1,10000)
Equally spaced points
seq(1,10)#optional: increment by=0.5 or number of points length.out=20 | Includes start and endpoint
seq_along(c(1,55,2,60,9,4))#gives [1,2,3,4,5,6] vektor of all indices, useful for for-loops

### Matrix
matrix("test", nrow=3, ncol=3)

Daten: werden von 1970 aus gemessen
Zahl zu Datum:
as.Date(1234, origin="1970-01-01")
String zu Datum
as.Date("05/27/84","%m/%d/%y") #https://www.r-bloggers.com/date-formats-in-r/ Übersicht formatter
Datum zu String
format(myDate, "%a %b %d")
Abstand in Tagen
as.numeric(as.Date(date1, "%m/%d/%y")-as.Date(origin,"%m/%d/%y"))
## Finden&Vergleichen
Element in Vektor/List/...
match(x, vektor)#returns position of first occurence
x %in% vektor #true or false alternativ: is.element(x,vektor)
which.min(vec)#Index of Minimum

duplicated(vektor)#logical vector with TRUE if element is duplicated
unique(vektor)#vector with doubled rows removed
## Sortieren
Order: gibt die reihenfolge der indizes des originalvektors, damit dieser sortiert wäre
order(v)=>v[order(v)] sortiert v!
dat[order(dat$v),]#sortiers data frame rows anhand von column "v"

## Nützliche Funktionen
Differenzvektor: Länge n-1, berechnet differenz benachbarter Elemente v[i]-v[i-1]
diff(v)
Integral über diskrete Funktionswerte y an den Stellen x
pracma::trapz(x,y)
lsf.str("package:dplyr") #list all functions in package

check if variable is of certain value (NULL or NaN or Inf/-Inf)
is.null(x) is.finite(x), is.infinite(x), is.nan(x)
rev(vec)#revert order of vector
## Curve Fits
least square fit:
model=nls(ET~a*sin(b*day+c)+d, data=Data, start=list(a=0.5, b=0.02, c=-200, d=0.5))
coef(model)


## Apply
apply(variable, margin, function)#margin: 1 by row, 2 by column, 1:2 for each element in variable
do.call(what, args)#Problem: Funktion, Argumente als Liste vorhanden=>what: function or string with function name args: List of arguments, names of List elements gives the names of the function arguments

##Data Frames
#Colnames (Analog: Rownames) setzen/lesen:
colnames(Dataframe)=c("Hallo", "zweitens")
make.names(names, unique=FALSE)#Erzeugt syntaktisch korrekte namen (keine Zahl am Anfang, eindeutig,...)
#Strings nicht zu Faktoren konvertieren:
data.frame(A=c("Hallo", "zweitens"), stringsAsFactors=FALSE)


# Joining
merge(): http://www.datasciencemadesimple.com/join-in-r-merge-in-r/ 
Idee: Vereine zwei Dataframes anhand einer gemeinsamen Spalte, z.B. "time": Reihen, welche in dieser Spalte gleiche, eindeutige Werte haben, werden im vereinten Dataframe in eine Reihe gesetzt.
Sofern Werte doppelt vorkommen, werden im neuen Dataframe alle möglichen Kombinationen gelistet
Optionen: all=TRUE: keine Information geht verloren, Zellen,  die im neuen Dataframe nicht definiert sind, werden mit NA gefüllt
all.x=TRUE oder all.y=TRUE: nur die "Zeiten" aus dem ersten (x) bzw. zweiten (y) DataFrame werden im neuen gelistet
Keine Optionen (alle False): "Inner join", nur Reihen mit Werten, welche in der by-Spalte in beiden DataFrames vorkommen, werden im neuen DataFrame gelistet.
merge(x=d1, y=d2, by="Time", all=TRUE)#by kann auch mehrere columns beinhalten!

Einfaches verbinden der Spalten (müssen gleiche Anzahl an Reihen haben!)/ Verbinden der Reihen (müssen gleiche Variablennamen haben!)
cbind(d1,d2)
rbind(d1,d2)
## Strings
Regex: Replacement mit sub(), gsub() (letzteres ersetzt alle vorkommen)
sub(pattern, replacement, text)
grep(pattern, x)#return all indizes in x where pattern matched the string
str_extract(text,pattern)#library(stringr): return the part of the text, which matched the pattern 
=> pattern=paste(patternlist, collapse="|")# when multiple patterns are to be matched
## Boolean
#Operators: single (& or |) perform vectorized comparison, double (&& or ||) compare only first elements of vectors
## In- and Output
### Input
read.table(file, sep=",", dec=".", stringsAsFactor=FALSE, comment.char="")#Beachte: leere Zellen (",,") werden sowohl als "" als auch als NA dargestellt, je nach Formatierung der Spalte
### Output
writeLines(text, con = stdout(), sep = "\n", useBytes = FALSE)#con: z.B. String mit Filename
write.table(x=data.frame or matrix, file="", append=FALSE, sep=" ", dec=".", row.names = TRUE, col.names = TRUE)
write.csv(x=data.frame, file="...", )
#colored text output: https://github.com/r-lib/crayon
## Working with Files
basename(path)
dirname(path)
list.files(path=".", pattern="abc")#pattern: regex pattern
## Tidy Package
https://garrettgman.github.io/tidying/
Prinzip: In Tabelle ist Information durch die Position eines Wertes codiert: x und y Position geben Auskunft über Beobachtung (Reihe) und Variable (Spalte), zu der der Wert gehört.
       country year  cases population
 1 Afghanistan 1999    745   19987071
 2 Afghanistan 2000   2666   20595360
 3      Brazil 1999  37737  172006362
 4      Brazil 2000  80488  174504898
 5       China 1999 212258 1272915272
 6       China 2000 213766 1280428583

Tabellen im Format Key-Value Pairs schreiben die Information über die y-Position in eine eigene Spalte. Insofern kann die Anzahl an Spalten reduziert werden, die Gesamtzahl an Zellen erhöht sich jedoch, da die Information, welche vorher in der Position codiert war, jetzt explizit in eigene Zellen geschrieben wird.
       country year        key      value
1  Afghanistan 1999      cases        745
2  Afghanistan 1999 population   19987071
3  Afghanistan 2000      cases       2666
4  Afghanistan 2000 population   20595360
5       Brazil 1999      cases      37737
6       Brazil 1999 population  172006362
7       Brazil 2000      cases      80488
8       Brazil 2000 population  174504898
9        China 1999      cases     212258
10       China 1999 population 1272915272
11       China 2000      cases     213766
12       China 2000 population 1280428583

Von Format 1 zu 2:
gather(dataFrame, key, value, columns)#key: Name der Key Spalte (zB. "key") Value: Name der Value Spalte; columns: Spalten, die kombiniert werden sollen (zB. 3:4)

Von Format 2 zu 1:
spread(dataFrame, key, value)#Erzeugt für jeden Faktor in Spalte key eine eigene Spalte und schreibt dort den jeweiligen Wert von value. Eventuell entstehende leere Zellen werden mit dem Argument von "fill=" gefüllt (Default: NA)

Data frame mit allen Kombinationen aus zwei oder mehr Vektoren
expand.grid(v1,v2,v3,v4)


## Statistik
```R
sd(vec) #Standard deviation
mean(vec) #Mean
```
## GGPlot2
https://tutorials.iq.harvard.edu/R/Rgraphics/Rgraphics.html

Rotate labels (and adjust position)
p1+theme(axis.text.x = element_text(angle = 90, hjust = 1))
Add labels
p1+xlab("Label")
p1+ggtitle("SettlemeyerA")
p1+scale_colour_manual(values=c("#999999", "#E69F00", "red" ), name="ActTrans", breaks=c("X1", "X2","X3"),labels=c("1.0", "0.8","Sinusodial variations"))
p1+labs(color = "Depth[cm]")#Colorbar caption
Set view (Axis limits)
p1+coord_cartesian(xlim=c(0,100), ylim=c(0,100))
Invert Axis
p1+scale_y_reverse(lim=c(10,0))

Plot Dates#library(scales)
scale_x_date(date_breaks = "1 month", labels=date_format("%b-%Y"), limits = as.Date(c('2011-01-01','2013-01-01')))


## Lineplots
geom_line(aes(y=moisture, colour=Material, linetype=Types))
geom_vline(xintercept=123, color="green", linetype="longdash")#create vertical line, horizontal: ...hline



## Barplots
Balance: Drei Spalten: Name, Flow, Direction, wobei Direction nur In/Out (jeweils einmal für jeden Namen)
p1=ggplot(Balance, aes(x=Name,y=Flow, fill=Direction))
p1=p1+geom_bar(stat="identity", position=position_dodge())
dodge: Bewirkt, dass Balken für jede richtung nicht übereinander, sondern nebeneinander stehen (Vergleich von in/out möglich)
Identity: Explizite Angabe des y-werts jedes Balkens. Default: nur x-Wert wird angegeben (zB Name)=>Balken zeigen Häufigkeit jedes Faktors (jedes möglichen Namens)

## Arrange multiple plots
grid.arrange(grobs=list(p1,p2,p3), top="Caption")#library(gridExtra), Aufruf evtl mit do.call("grid.arrange", Plotlist)

## General language behaviour
By reference or value: R in general: Always by value




# Environment
## Installation
```bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
sudo add-apt-repository 'deb https://cloud.r-project.org/bin/linux/ubuntu focal-cran40/'
sudo apt install r-base-dev
```

## Packages
Basic installation of packages via install.packages(). Some packages might require external tools. If an error occurs, read the message and install them with apt install.
```R
install.packages('packagename')
```

To create your own package: https://tinyheero.github.io/jekyll/update/2015/07/26/making-your-first-R-package.html
Installation: Best to write a short install script
```R
# install.packages("devtools") #If these packages are not already installed
# install.packages("roxygen2")
RootDir="Path/to/package/dir/packagename"
setwd(file.path(RootDir))
devtools::document()
devtools::install()
lsf.str("package:packagename")
```
## R Documentation
roxygen: #Way to create documentation automatically

Basic documentation of functions:
```R
#' HeaderLine
#' @param param1: Description
#' @param param2: Description
#' @return Description
#' @export
func=function(param1, param2)
```

Create pdf Manual for packages: type in console ("R" stands short for R.exe executable)
R CMD Rd2pdf mypackagename #command is based on Latex, so "pdflatex" must be available in PATH


