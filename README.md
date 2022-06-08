# PySimpleCurses
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
