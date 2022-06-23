## PySimpleCurses
### What is it?

PySimpleCurses is a python module that allows you to make terminal user interfaces.

---

```diff
-=[ WARNING: THIS MODULE WILL ONLY WORK ON WINDOWS ]=-
```

### Examples
#### Bare Bones

!!! Please note all of the arguments are **CASE SENSITIVE** !!!

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
     1. x (Mouse x value)
     2. y (Mouse y value)
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
- onclick (This is the function that the widget will run when it is clicked. DEFAULT=None)

Positional Arguments:
- x (x value of the widget)
- x (y value of the widget)
- name (This is the name the widget will show)

```py
window.add(Button(x, y, name, onclick))
```

#### Entry Widget:

Positional Arguments:
- x (x value of the widget)
- y (y value of the widget)
- text (This is the text the widget will show)

Optional Arguments:
- placeholder (This is what will show when the widget isn't seleceted. DEFAULT="")

```py
window.add(Entry(x, y, DEFAULT_TEXT, placeholder))
```

#### Label Widget:

Positional Arguments:
- x (x value of the widget)
- y (y value of the widget)
- text (This is the text that will show)

```py
window.add(Label(x, y, text))
```

#### Rect Widget:

Optional Arguments:
- FILL_COLOR (This sets the color of the Rect (rectangle). DEFAULT=(255, 255, 255))

Positional Arguments:
- x (x value of the widget)
- y (y value of the widget)
- width (width of the Rect (rectangle))
- height (height of the Rect (rectangle))

```py
window.add(Rect(x, y, width, height, FILL_COLOR))
```

#### SubWindow Widget:

Positional Arguments:
- x (x value of the widget)
- y (y value of the widget)
- width (width of the SubWindow)
- height (height of the SubWindow)
- title (This is the title of SubWindow)

```py
window.add(SubWindow(x, y, width, height, title))
```

#### TextBox Widget:

Optional Arguments:
- text (This is the default text it will show. DEFAULT="")
- placeholder (This is what will show when the widget isnt seleceted. DEFAULT="")

Positional Arguments:
- x (x value of the widget)
- y (y value of the widget)
- width (width of the TextBox)
- height (height of the TextBox)

```py
window.add(TextBox(x, y, width, height, text, placeholder))
```