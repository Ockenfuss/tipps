
# General

## Elements
```html
<p>Content</p>  <!--Content is placed inside tags -->
<p attribute="value">Content </p> <!-- Elements can have attributes-->
<p disabled>Content </p> <!-- Boolean attribute-->
```

## General Structure
```html
<!DOCTYPE html> #for historical reasons
<html lang="en-US"> #root element
  <head> #Contains Settings and stuff
    <meta charset="utf-8" /> #General metadata. UTF-8 it always advisable
    <title>My test page</title> #This it NOT the page title, but the metadata title
  </head>
  <body> #Content
    <p>This is my page</p>
  </body>
</html>
```

## Basic Elements
```html
<a href="https://www.mozilla.org/"> Link Text </a> #URL Link: Use the href attribute of the anchor element
<a href="../dir1/index.html"> Link Text </a> #Alternatively, you can use normal unix paths to create relative links to other files
```