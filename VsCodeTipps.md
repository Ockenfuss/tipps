# Alle Arten von Notizen zu vscode

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Alle Arten von Notizen zu vscode](#alle-arten-von-notizen-zu-vscode)
- [Allgemeine Einstelllungen](#allgemeine-einstelllungen)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Debugging](#debugging)
- [Special variables for files](#special-variables-for-files)
- [Language specific configurations](#language-specific-configurations)
  - [Latex](#latex)
  - [Python](#python)
- [Plugins](#plugins)
  - [VIM](#vim)

<!-- /code_chunk_output -->



# Allgemeine Einstelllungen
Datei->Einstelllungen->Einstelllungen
-Links: Große Liste aller Default Einstelllungen
=>Klick auf Kopieren: Kopiert den ausgewählten Block in entweder: Benutzereinstellungen (gelten immer) oder Arbeitseinstellungen (gelten im gewählten Verzeichnis) => Überschreiben Standardeinstellungen
Ort: werden damit automatisch im settings.json file im Ordner .vscode gespeichert (Editieren auch hier direkt möglich)

# Keyboard Shortcuts
einfach: File-preferences-keyboard Shortcuts
allgemein: keybindings.json (link über obiges menü)

ctrl+J: wechsel zwischen panel (terminal) und editor (eintrag in .json file. Alternativ: Wechsel mit automatischem öffnen und schließen: einfach an "Toggle Panel" binden)
ctrl+W in Terminal: Close it (self defined)


# Debugging
tasks.json: File which defines how to compile the open editor file, e.g. gcc with -g and all further arguments for C.

launch.json: File with recipe how to debug the program, after compiling with a task in tasks.json, e.g. use gdb for C debugging.

# Special variables for files
* ${workspaceFolder} - the path of the folder opened in VS Code
* ${workspaceFolderBasename} - the name of the folder opened in VS Code without any slashes (/)
* ${file} - the current opened file
* ${relativeFile} - the current opened file relative to workspaceFolder
* ${relativeFileDirname} - the current opened file's dirname relative to workspaceFolder
* ${fileBasename} - the current opened file's basename
* ${fileBasenameNoExtension} - the current opened file's basename with no file extension
* ${fileDirname} - the current opened file's dirname
* ${fileExtname} - the current opened file's extension
* ${cwd} - the task runner's current working directory on startup
* ${lineNumber} - the current selected line number in the active file
* ${selectedText} - the current selected text in the active file
* ${execPath} - the path to the running VS Code executable
* ${defaultBuildTask} - the name of the default build task



Logpoints: Advanced break points, which can e.g. depend on a condition
In watch window:
Show pointer as array: "*pointer@3"

# Language specific configurations

## Latex
Strg+Alt+B: Wählt automatisch das erste "Recipe" aus. die hier gelisteten Tools werden nacheinander ausgeführt
Tools: Kurzformen für commandozeilenbefehle mit Argumenten
Speicherort: in Standard- und Benutzereinstellungen
https://pmateusz.github.io/latex/2017/03/29/vs-code-latex-editor.html
in "tasks.json":
{
 "version": "0.1.0",
 "isShellCommand": true,
 "suppressTaskName": true,
 "showOutput": "always",
 "tasks": [{
         "taskName": "Build PDF",
         "command": "pdflatex",
         "isBuildCommand": true,
         "args": [
             "-interaction=nonstopmode",
             "-file-line-error",
             "report.tex"
         ]}, {
         "taskName": "Build BibTex",
         "command": "bibtex",
         "isTestCommand": true,
         "args": ["report.aux"]
         }]
}

Latex subfile package:
-Option: "Use sub file" to specify which file should be used for the autobuild (main file or the currently open editor subfile)
-Option: "do not prompt" to specify whether you want to be asked each time
## Python
Formatting code: independently of vscode, install autopep8: python3 -m pip install autopep8
Pytonpath: You can place a file `.env` in your workspace folder, which contains environment variables. Those are used by the Python extension e.g. to find packages. This is also the way to set the path for jupyter kernels, e.g. when working remotely
```txt
PYTHONPATH=/path/to/additional/modules
```


# Plugins
## VIM
### Remapping
You can remap key combinations either using vim keybindings provided by the extension or general vscode keyboard shortcuts (very flexible, but only recommended if keybindings not work).
```json
"vim.normalModeKeyBindingsNonRecursive":[
    {
        "before": ["Y"],
        "after": ["y","$"]
    },
    {
        "before": ["<S-Space>"],
        "after": ["i"]
    },
    {
        "before": ["<leader>","e"],
        "commands": [
                        "editor.action.smartSelect.expand",
                        "jupyter.execSelectionInteractive", //Ideally, set smartSelect.selectSubwords to False for this
                        "extension.vim_escape"
                    ]
    }
],
```


























