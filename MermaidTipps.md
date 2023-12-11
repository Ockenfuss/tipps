
[TOC]

Check out the [live editor](https://mermaid.live/)
# General
```mermaid
%% Comment. Must be in separate line
```
# Flow Chart
```mermaid
%% Either TD (top-down) or LR (left-right)
flowchart TD
    A[Christmas] -->|Get money| B(Go shopping)
    B --> C{Let me think}
    C -->|One| D["Line1
                    Line 2
                    Line 3"]
    C -->|Two| E["`Markdown inside: **bold**`"]
    C -->|Three| F[fa:fa-car Car]
```