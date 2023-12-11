Label Studio: Application for data labeling

# Install
Using pip:
```bash
python3 -m venv labelstudio #best to create virtual env.
. ./labelstudio/bin/activate
pip install label-studio #install as python package
```
```bash
docker pull heartexlabs/label-studio:latest
```

# Start
start label studio using docker container
```bash
docker run -it -u $(id -u) -p 8080:8080 -v $(pwd)/data:/label-studio/data --env LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true --env LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/label-studio/files -v $(pwd)/riming_images:/label-studio/files heartexlabs/label-studio:latest label-studio
```

## Permission Issue
Folders have to be in home directory, not on the NAS! Otherwise, I get permission issues.
Label Studio is using a non-root docker container with uid 1001. Therefore, this user needs write permissions on the mounted directories.
The easiest way to achive this:
```bash
chmod 777 data
```

# Tasks and Storage
You can store the data for each task in a local folder. Set the following environment variables in your shell:
```bash
export LABEL_STUDIO_LOCAL_FILES_SERVING_ENABLED=true
export LABEL_STUDIO_LOCAL_FILES_DOCUMENT_ROOT=/home/p/Paul.Ockenfuss/LabelStudio/Oldmasks/riming_images
```

In label studio, create a cloud storage and select local. The data has to be located in a child of the given env. variable path.
If you define complex tasks involving multiple images, text, etc, you have to define them in form of .json files.
For simple tasks based on just one image/text, check "Treat every bucket object as a source file". This way, every image in the child folder will result in one labeling task.

# Labeling Tags
Simple Labels
```html
<Choices name="choice" toName="image">
<Choice value="Suspicious (check later)" hotkey='w'/>
</Choices>
```
Rectangle selection in Images
```html
<View>
  <Image name="image" value="$image"/>
  <RectangleLabels name="label" toName="image">
    <Label value="Invalid" background="red" hotkey='w' selected="true"/>
  </RectangleLabels>
</View>
```

# Export Data
Choose Json-min if you want only the results
## Image Areas
They are given in percentage. Use the following to convert to pixels:
```python
pixel_x = x / 100.0 * original_width
pixel_y = y / 100.0 * original_height
pixel_width = width / 100.0 * original_width
pixel_height = height / 100.0 * original_height
```