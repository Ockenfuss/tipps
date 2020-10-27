Tipps concerning Cameras, Photos and Databases




# Cameras
## GoPro Hero 7
### Wifi
You can connect to the gopro via wifi and access the sd card via the gopro webserver.
The current password can be found in Preferences>Connections>Camera Info
Access the sd card via `http://10.5.5.9:8080/videos/DCIM/`. Use e.g. wget to download files.
```bash
wget -r -A .JPG http://10.5.5.9:8080/videos/DCIM/
```

# Collection
## Digikam
My main solution to organize photos. Open-source and powerful. Allows to assign Tags, rename files and edit metadata.