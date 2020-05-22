# Latex
Tipps and code snippets to format texts in Latex

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Latex](#latex)
  - [ToDo package](#todo-package)
  - [Subfiles](#subfiles)
- [Tikz](#tikz)
- [Science](#science)
  - [Units](#units)
- [Math](#math)
  - [Aligning](#aligning)
  - [Symbols](#symbols)
- [Figures](#figures)
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

# Tikz
Extremly comprehensive package to create all kinds of graphics.

# Science
## Units
Recommended to use the si package. It allows you to adapt the format afterwards, e.g. to fulfill the requirements of a journal.
https://www.namsu.de/Extra/pakete/Siunitx.html
```latex
\usepackage{siunitx}
\si{\km} %unit only
\SI{100}{\per\cubic\centi\metre}
\SI{90}{\degree} %Alternatively, use $^{\circ}$
```

# Math
## Aligning
Align multiple quations in one row side by side with labels
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

# Figures
My personal best practice: Already set the correct figsize in matplotlib so that no scaling in latex is necessary! For this, use `\showthe\textwidth` in latex and combine it with the Pytex package in my template collection.

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