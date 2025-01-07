# Installation
The easiest way is probably the AppImage (https://www.libreoffice.org/download/appimage/). I use the 'Basic Still' Version.
However, it seems (Jan. 2025) that the AppImage is not the most recent version (7.x, most recent are 24.x versions).
Therefore, I switched to the .deb package again.
- Download from webpage
- Untar
- Install all files in DEBS directory: `sudo dpkg -i *.deb`
## Uninstall
Libreoffice often comes preinstalled on Ubuntu, but the version in the standard ppa is often outdated. To uninstall, simply call:
```bash
sudo apt remove --purge 'libreoffice*'
sudo apt autoremove
```
# Selection
* Select object behind other object: Alt+Click (Shift+Alt+Click to cycle reverse)

# Moving
* Arrow: Move
* Alt-Arrow: Move one pixel

# Scaling
* Shift+Drag: Keep ratio constant