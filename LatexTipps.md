# Latex
Tipps and code snippets to format texts in Latex

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Latex](#latex)
  - [ToDo package](#todo-package)
  - [Subfiles](#subfiles)
- [Biblatex](#biblatex)
- [Tikz](#tikz)
- [Science](#science)
  - [Units](#units)
- [Math](#math)
  - [Aligning](#aligning)
  - [Symbols](#symbols)
- [Figures](#figures)
- [Tables](#tables)
- [Glossaries](#glossaries)
- [Examples](#examples)

<!-- /code_chunk_output -->

Checkliste vor Druck:
-Hyperlinks in Farbe ausschalten! `\usepackage[hidelinks]{hyperref}`
-Seitenanordnung richig? Leerseiten? Seitenränder? `\documentclass[a4paper,10pt, twoside]{report}`


##########Geometry
show geometry:
\usepackage{layout}
\begin{document}\layout
...
## ToDo package
```latex
\usepackage{todonotes}
\todo{some text}
\missingfigure{some text}
```

## Subfiles
Very useful package when a big latex project should be splitted into different subfiles. 
```latex
% In the main document
\usepackage{subfiles}
\begin{document}
\subfile{title}
...
% In the subfiles
\documentclass[../Main.tex]{subfiles}
\begin{document}
...
```
# Biblatex
Citation commands:
```latex
\cite{PublicationKey} %Normal textual citation
\parencite{PubKey} %Cite within parentheses
```

# Tikz
Extremly comprehensive package to create all kinds of graphics.

# Science
## Units
Recommended to use the si package. It allows you to adapt the format afterwards, e.g. to fulfill the requirements of a journal.
https://www.namsu.de/Extra/pakete/Siunitx.html
```latex
\usepackage{siunitx}
\si{\km} %unit only
\num{10} %Number only
\SI{100}{\per\cubic\centi\metre}
\SI{90}{\degree} %Alternatively, use $^{\circ}$
\SIrange{1}{2}{\km} %range of values
```

# Math
## Aligning
Align multiple equations with one label
```latex
\begin{align}\label{eq:example}
        a&=b &
        c&=d &
        e&=f
\end{align}
```
Align multiple quations in one row side by side with separate labels
```latex
\begin{center}
    \begin{minipage}[b]{.45\textwidth}
    \begin{equation}
        P_{\lambda}=2f\delta (1-\mu)+(1-f)P_{\lambda}^* 
        \label{eq:wiscombe}
      \end{equation}
    \end{minipage}
    \quad
    \begin{minipage}[b]{.45\textwidth}
      \begin{equation}
        P_{\lambda}^*=\sum^{\infty}_{l=0}p_l^* P_l(\mu)
        \label{eq:wiscombe2}
      \end{equation}
    \end{minipage}
  \end{center}
```
## Symbols
Typical alterations of variable names
```latex
$\hat{\alpha}$ %Small hat over a letter
$\tilde{\alpha}$ %Small tilde over a letter
```
Mathematical symbols
```latex
\coloneqq %defined: := (in package mathtools)
\leq %less than or equal
\geq %greater than or equal
\partial %Partial derivative
\int_0^1 %integral
\sum_0^1 %sum symbol
\in %is element symbol
```

# Figures
My personal best practice: Already set the correct figsize in matplotlib so that no scaling in latex is necessary! For this, use `\showthe\textwidth` in latex and combine it with the Pytex package in my template collection.

# Tables
```latex
\begin{table}[h]
    \centering
    \begin{tabular}{ c | c | c  c }
        \hline
        Quantity&Symbol&Definition&Unit\\
        \hline
        Radiant Energy&Q&&$J$\\
        Radiant Power&$\phi_\lambda$&$\frac{dQ}{dt\cdot d\lambda}$&$Wnm^{-1}$\\
        \hline
    \end{tabular}
    \caption{some caption}
    \label{tab:mytable}
\end{table}
```

# Glossaries
Package to create an overview of acronyms and technical terms. Generally, there are two types of entries: Glossaryentries are meant to contain descriptions of technical terms and definitions, while acronyms list the long version of abbreviated names.
```latex
\usepackage[acronym]{glossaries}
\newglossaryentry{cosmo}{name=Cosmo,description={NWP model, originally developed by DWD in 1999. \glslink{COSMO}{COSMO}}}
\newacronym{COSMO}{COSMO}{Consortium for Small-scale Modeling. \gls{cosmo}}
\newacronym[longplural={diagonal matrices}]{dm}{DM}{diagonal matrix}
```
In order to use the entries in your latex document, use:
```latex
\makeglossaries
\begin{document}
\gls{cosmo}%Normal reference
\Gls{cosmo}%Capitalize first letter
\glspl{cosmo}%Term in plural form, i.e. add an 's'. Alternativly, you need to define the "longplural" and "shortplural" keys. Also \Glspl{cosmo} is possible.
\glsunset{cosmo}%Acronyms are displayed with definition when used the first time. Use this to manually mark an acronym as defined
\glsunsetall %Mark all as defined
\glsaddall %Adding all the elements to the glossary, regardless of whether they are used somewhere

\printglossaries
\end{document}
```
In order to compile a document with a glossary:
```bash
pdflatex Glossary
makeglossaries Glossary
pdflatex Glossary
```

# Examples
Full working example
```latex
\documentclass[a4paper,10pt, twoside]{report}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{geometry}
\usepackage[english]{babel}
\usepackage{amssymb}
\usepackage[pdftex]{graphicx}
\usepackage[backend=biber,style=authoryear,maxcitenames=1,giveninits=true, natbib=true]{biblatex}%
\usepackage{graphicx}
\usepackage[hidelinks]{hyperref}
\usepackage{csquotes}
\usepackage{amsmath}
\usepackage{array}
\usepackage{multirow}
\usepackage{placeins}
\usepackage{float}
\usepackage{subcaption}
\usepackage{cleveref}
\usepackage{subfiles}
\usepackage{gensymb}
\usepackage{zref}
\usepackage{pdfpages}
\usepackage{subcaption}
\usepackage{pdflscape}
\usepackage{fancyhdr}
\usepackage[toc,page]{appendix}
\addbibresource{Quellen.bib}

\begin{document}

\section*{ResearchPlan}
\subsection*{Motivation}%star removes numbering
test, test
% \bibliography{Quellen.bib}
\printbibliography[title={Bibliography},heading=bibintoc]

\end{document}
```