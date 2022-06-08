## PySimpleCurses
### What is it?

PySimpleCurses is a python module that allows you to make terminal user interfaces.

---

```diff
-=[ WARNING: THIS MODULE WILL ONLY WORK ON WINDOWS ]=-
```

### Examples
#### Bare Bones
```py
from PySimpleCurses import *

# Initalize the window
window = Window()

# Make the main loop
while 1:
     window.update()
```

#### Making your first "Hello, World!" program
```py
# Add the widget "Label"
window.add(Label(1, 1, "Hello, World!"))
```

#### Adding buttons
```py
# Add the widget "Button"
window.add(Button(1, 1, "This is a button!"))
```

#### Getting user input
There are two ways of getting user input
1. Use the function `getinput()`, the function `getinput()` will return a class called inputData and that class has 4 attributes you can use the following:
     1. X (Mouse X value)
     2. Y (Mouse Y value)
     3. MB (Mouse Button)
     4. Key (Key the user pressed)
2. Use the widget "Entry"

### Documentation
---
#### Widgets

- Button
- Entry
- Label
- Rect
- SubWindow
- TextBox

#### How to implement each widget

#### Button Widget:

Optional Arguments:
- ONCLICK (This is the function that the widget will run when it is clicked. DEFAULT=None)

Positional Arguments:
- X (X value of the widget)
- Y (Y value of the widget)
- TEXT (This is the text the widget will show)

```py
window.add(Button(X, Y, TEXT, ONCLICK))
```

#### Entry Widget:

Positional Arguments:
- X (X value of the widget)
- Y (Y value of the widget)
- TEXT (This is the text the widget will show)

Optional Arguments:
- PLACEHOLDER (This is what will show when the widget isn't seleceted. DEFAULT="")

```py
window.add(Entry(X, Y, DEFAULT_TEXT, PLACEHOLDER))
```

#### Label Widget:

Positional Arguments:
- X (X value of the widget)
- Y (Y value of the widget)
- TEXT (This is the text that will show)

```py
window.add(Label(X, Y, TEXT))
```

#### Rect Widget:

Optional Arguments:
- FILL_COLOR (This sets the color of the Rect (rectangle). DEFAULT=(255, 255, 255))

Positional Arguments:
- X (X value of the widget)
- Y (Y value of the widget)
- WIDTH (WIDTH of the Rect (rectangle))
- HEIGHT (HEIGHT of the Rect (rectangle))

```py
window.add(Rect(X, Y, WIDTH, HEIGHT, FILL_COLOR))
```

#### SubWindow Widget:

Positional Arguments:
- X (X value of the widget)
- Y (Y value of the widget)
- WIDTH (WIDTH of the SubWindow)
- HEIGHT (HEIGHT of the SubWindow)
- TITLE (This is the title of SubWindow)

```py
window.add(SubWindow(X, Y, WIDTH, HEIGHT, TITLE))
```

#### TextBox Widget:

Optional Arguments:
- TEXT (This is the default text it will show. DEFAULT="")
- PLACEHOLDER (This is what will show when the widget isnt seleceted. DEFAULT="")

Positional Arguments:
- X (X value of the widget)
- Y (Y value of the widget)
- WIDTH (WIDTH of the TextBox)
- HEIGHT (HEIGHT of the TextBox)

```py
window.add(TextBox(X, Y, WIDTH, HEIGHT, TEXT, PLACEHOLDER))
```
