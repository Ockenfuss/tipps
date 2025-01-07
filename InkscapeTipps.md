# Tipps for Inkscape

# General
- `Space`: Selector Tool (top in the toolbar). Allows to move, rotate, scale and skew objects. Click once for move, scale and click the selection a second time to switch to rotate, skew. `Strg` limits the operations to horizontal/vertical

# Drawing
To draw straight lines or Bezier curves, select the corresponding tool (shortcut B). Pressing `Strg` limits your lines to horizontal/vertical/diagonal!

# Snapping
Clicking the magnet symbol in the upper right, you can activate snapping of objects.

# Color
Click on colors at the bottom to set Fill, `Shift+Click` to set stroke color.
## Pipette
Select an object, then hit `D` to toggle pipette. `Click` or `Shift-Click` to apply the color under cursor to object.

## Filling
I think, filling with the bucket tool is not what you sould usually do in Inkscape. The bucket tool just creates an additional fill object. Instead, e.g., you can try to break apart (`Path->Break Apart`) a path to get the contour and set the fill color of the contour.

# Groups
To enter a group:
* Double click
* Right click: Enter group
* Select and `Ctrl+Enter`
# Layers
Seem to be similar to groups, except they appear only in the layer view, with less effect when you click on your drawing (?)

To leave a group:
* Double click outside
* Right click: Go to parent
* Select: `Ctrl+Back`

# Object operations

# Copy
There are multiple ways to create copies of objects: `Ctrl+C` copies to clipboard, `Ctrl+D` directly inserts the duplicate into the same position.
`Alt+D` created a linked copy ('clone'), which shares properties with the original.
`Ctrl+V` inserts the object.
## Copy style
When you copy and object, then select a new one and press `Ctrl+Shift+V`, only the style of the object in the clipboard is applied to the new one

## Clip
Useful to crop an image. Select two objects (like image and a shape on top) and select Object->Clip to keep only the overlapping area.

## Arange
Use the arange tool to create e.g. equally spaced lines or rotational symmetry


# Tools
## Text
Click to write text or drag to define an area where you can write (with linewrap).