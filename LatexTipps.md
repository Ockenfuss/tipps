# Latex
Tipps and code snippets to format texts in Latex

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Latex](#latex)
- [Tikz](#tikz)
- [Science](#science)
  - [Units](#units)
- [Math](#math)
  - [Aligning](#aligning)
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


# Tikz
Extremly comprehensive package to create all kinds of graphics.

# Science
## Units
Recommended to use the si package. It allows you to adapt the format afterwards, e.g. to fulfill the requirements of a journal.
```latex
\usepackage{siunitx}
\SI{100}{\per\cubic\centi\metre}
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