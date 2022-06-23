import win32con
import win32file
from win32console import *
from win32con     import *
import os
from ctypes import (windll, byref, Structure, c_char, c_short, c_uint32, c_ushort, WinError)
os.system('')
STDOUT = -11
STDERR = -12

handles = {STDOUT: windll.kernel32.GetStdHandle(STDOUT), STDERR: windll.kernel32.GetStdHandle(STDERR)}
SHORT = c_short
WORD = c_ushort
DWORD = c_uint32
TCHAR = c_char

class COORD(Structure):
     _fields_ = [('X', SHORT), ('Y', SHORT)]

class  SMALL_RECT(Structure):
     _fields_ = [("Left", SHORT), ("Top", SHORT), ("Right", SHORT), ("Bottom", SHORT)]

class CONSOLE_SCREEN_BUFFER_INFO(Structure):
     _fields_ = [("dwSize", COORD), ("dwCursorPosition", COORD), ("wAttributes", WORD), ("srWindow", SMALL_RECT), ("dwMaximumWindowSize", COORD)]
     def __str__(self):return '(%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d)' % (self.dwSize.Y, self.dwSize.X, self.dwCursorPosition.Y, self.dwCursorPosition.X, self.wAttributes, self.srWindow.Top, self.srWindow.Left, self.srWindow.Bottom, self.srWindow.Right, self.dwMaximumWindowSize.Y, self.dwMaximumWindowSize.X)

def GetConsoleScreenBufferInfo(stream_id=STDOUT):
     handle = handles[stream_id]
     csbi = CONSOLE_SCREEN_BUFFER_INFO()
     success = windll.kernel32.GetConsoleScreenBufferInfo(handle, byref(csbi))
     if not success:
          raise WinError()
     return csbi

def cpos():
     csbi = GetConsoleScreenBufferInfo()
     return '({},{})'.format(csbi.dwCursorPosition.X, csbi.dwCursorPosition.Y)

class Test:
     def __init__(self, X=999, Y=999, MB=0, KEY=None, NB=0):
          self.X   = X
          self.Y   = Y
          self.MB  = MB
          self.Key = KEY
          self.NB  = 0

pos = PyCOORDType(X=0, Y=0)

def process_key(key):
     if key == VK_ESCAPE:
          return "ESCAPE"
     elif key == VK_RETURN:
          return "ENTER"
     elif key == VK_BACK:
          return "BACKSPACE"
     elif key == VK_TAB:
          return "TAB"
     elif key == VK_SHIFT:
          return "SHIFT"
     elif key == VK_CONTROL:
          return "CTRL"
     elif key == VK_MENU:
          return "ALT"
     elif key == VK_PAUSE:
          return "PAUSE"
     elif key == VK_CAPITAL:
          return "CAPS"
     elif key == VK_SPACE:
          return "SPACE"
     elif key == VK_PRIOR:
          return "PGUP"
     elif key == VK_NEXT:
          return "PGDN"
     elif key == VK_END:
          return "END"
     elif key == VK_HOME:
          return "HOME"
     elif key == VK_LEFT:
          return "LEFT"
     elif key == VK_UP:
          return "UP"
     elif key == VK_RIGHT:
          return "RIGHT"
     elif key == VK_DOWN:
          return "DOWN"
     elif key == VK_INSERT:
          return "INSERT"
     elif key == VK_DELETE:
          return "DELETE"
     elif key == VK_LWIN:
          return "WIN"
     elif key == VK_RWIN:
          return "WIN"
     elif key == VK_APPS:
          return "MENU"
     elif key == VK_F1:
          return "F1"
     elif key == VK_F2:
          return "F2"
     elif key == VK_F3:
          return "F3"
     elif key == VK_F4:
          return "F4"
     elif key == VK_F5:
          return "F5"
     elif key == VK_F6:
          return "F6"
     elif key == VK_F7:
          return "F7"
     elif key == VK_F8:
          return "F8"
     elif key == VK_F9:
          return "F9"
     elif key == VK_F10:
          return "F10"
     elif key == VK_F11:
          return "F11"
     elif key == VK_F12:
          return "F12"
     elif key == VK_NUMLOCK:
          return "NUMLOCK"
          

def getinput():
     global pos
     conin=PyConsoleScreenBufferType( win32file.CreateFile( "CONIN$", win32con.GENERIC_READ|win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, None, win32con.OPEN_EXISTING, 0, 0))
     conin.SetConsoleMode(ENABLE_WINDOW_INPUT | ENABLE_MOUSE_INPUT)
     if conin.GetNumberOfConsoleInputEvents() == 0:
          return Test()
     input_records=conin.ReadConsoleInput(10)
     for input_record in input_records:
          if input_record.EventType == KEY_EVENT and input_record.KeyDown:
               if input_record.Char=='\0':
                    final_key = process_key(input_record.VirtualKeyCode)
                    return Test(KEY=final_key)
               if input_record.KeyDown:
                    return Test(KEY=input_record.Char)
          if input_record.EventType==MOUSE_EVENT:
               pos=input_record.MousePosition
               if input_record.EventFlags == 0:
                    return Test(X=pos.X, Y=pos.Y-1, MB=input_record.ButtonState, NB=1)
               else:
                    return Test(MB=input_record.ButtonState, X=pos.X, Y=pos.Y-1, NB=0)
     return Test()

a = print
def print(text='', fg_color=[255, 255, 255], bg_color=[0, 0, 0], end='\n'):
    r, g, b = fg_color
    result = f'\033[38;2;{r};{g};{b}m{text}'
    r, g, b = bg_color
    result = f'\033[48;2;{r};{g};{b}m{result}\033[0m'
    a(result, end=end)