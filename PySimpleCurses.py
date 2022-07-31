import os
import cursor
import win32con
import win32file
from win32console import *
from win32con	import *
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

if os.name != 'nt':
	from colorama import *
	print(Fore.RED + 'WARNING: THIS MODULE IS FOR WINDOWS ONLY!!!' + Fore.WHITE)
	exit()
os.system('')
os.system('cls')
print("\033[%d;%dH" % (0, 0))

class Window:
	def __init__(self):
		os.system('')
		self.layout = []
		self.widgets = []
		self.selidx = 0
		self.oS = os.get_terminal_size() # old Size
		self.nS = os.get_terminal_size() # new Size
		self.curwidgetidx = 0
		self.w, self.h = os.get_terminal_size()
		self.addorder = []
		self.fcolor = [255, 255, 255]
		self.bcolor = [0, 0, 0]
		self.initalize_window()
		self.draw_layout()
		cursor.hide()

	def initalize_window(self):
		self.widgets = []
		for i in range(len(self.addorder)):
			self.add(self.addorder[i], first=0)
		self.layout = []
		for y in range(self.h-1):
			self.layout.append([])
			for x in range(self.w-1):
				self.layout[y].append([' ', 255, 255, 255, 0, 0, 0, 0])
		for y in range(len(self.layout)):
			for x in range(len(self.layout[y])):
				cur = self.layout[y][x]
				print(cur[0], [cur[1], cur[2], cur[3]], [cur[4], cur[5], cur[6]], end='')
			print()
		for y in range(len(self.layout)):
			print("\033[A", end='')
		
	def constrain(self, var, min, max):
		if var < min: return min
		if var > max: return max
		return var

	def draw_layout(self):
		for y in range(self.h-1):
			for x in range(len(self.layout[y])):
				cur = self.layout[y][x]
				print(cur[0], [cur[1], cur[2], cur[3]], [cur[4], cur[5], cur[6]], end='')
			print()
		for y in range(len(self.layout)):
			print("\033[A", end='')
	
	def clear(self):
		for y in range(len(self.layout)):
			for x in range(len(self.layout[y])):
				cur = self.layout[y][x]
				print(' ', end='')
			print()
		for y in range(len(self.layout)):
			print("\033[A", end='')
	
	def add(self, widget, first=1):
		widget.place = self.curwidgetidx
		widget.selected = 0
		self.curwidgetidx += 1
		if first:
			self.addorder.append(widget)
		self.widgets.append(widget)
		widget.win = self
		try:
			widget.init()
		except:
			pass
	
	def remove(self, widget):
		try:
			self.widgets.remove(widget)
			self.addorder.remove(widget)
		except: pass

	def re_init(self):
		cursor.hide()
		self.w = self.nS.columns
		self.h = self.nS.lines
		os.system('')
		os.system('cls')
		print("\033[%d;%dH" % (0, 0))
		self.initalize_window()
	
	def remove_unused(self):
		for y in range(len(self.layout)):
			for x in range(len(self.layout[y])):
				self.layout[y][x][0] = ' '
				self.layout[y][x][1] = 0
				self.layout[y][x][2] = 0
				self.layout[y][x][3] = 0
				self.layout[y][x][4] = 0
				self.layout[y][x][5] = 0
				self.layout[y][x][6] = 0
				self.layout[y][x][7] = 0

	def update(self):
		self.remove_unused()
		if self.nS != self.oS:
			self.re_init()
		position = getinput()
		for i, widget in enumerate(self.widgets):
			widget.win = self
			widget.update(position)
		self.draw_layout()
		self.oS = self.nS
		self.nS = os.get_terminal_size()
		self.set_color([255, 255, 255], [0, 0, 0])

	def addstr(self, x, y, string):
		for i in range(len(string)):
			try:
				self.layout[y][x+i][0] = string[i]
				self.layout[y][x+i][1] = self.fcolor[0]
				self.layout[y][x+i][2] = self.fcolor[1]
				self.layout[y][x+i][3] = self.fcolor[2]
				self.layout[y][x+i][4] = self.bcolor[0]
				self.layout[y][x+i][5] = self.bcolor[1]
				self.layout[y][x+i][6] = self.bcolor[2]
				self.layout[y][x][7] = 1
			except: pass
	
	def set_color(self, fg=[255, 255, 255], bg=[0, 0, 0]):
		self.fcolor = fg
		self.bcolor = bg
	
	def reset_selected(self):
		for widget in self.widgets:
			widget.selected = 0
		for widget in self.addorder:
			widget.selected = 0

########## WIDGETS ##########

# LABEL
class Label:
	def __init__(self, x, y, text, fg=[54, 54, 54], bg=[0, 0, 0]):
		self.x = x
		self.y = y
		self.text = text
		self.selectable = 0
		self.fg = fg
		self.bg = bg

	def update(self, uData=-1):
		self.win.set_color(self.fg, self.bg)
		self.win.addstr(self.x, self.y, self.text)

# BUTTON
class Button:
	def __init__(self, x, y, text, onclick=None, fg=[100, 100, 100], bg=[0, 0, 0]):
		self.x = x
		self.y = y
		self.text = text
		self.onclick = onclick
		self.fg = fg
		self.bg = bg
		self.selectable = 1
		self.firstclick = 0

	def update(self, uData=-1):
		if uData.Y == self.y and uData.MB == 1 and uData.X >= self.x and uData.X < self.x + len(self.text):
			self.win.reset_selected()
			self.win.selidx = self.place
			self.selected = 1
			if self.onclick:
				self.onclick()
		self.win.set_color(self.fg, self.bg)
		self.win.addstr(self.x, self.y, self.text)

# ENTRY
class Entry:
	def __init__(self, x, y, name, ispassword=0):
		self.x = x
		self.y = y
		self.name = name
		self.oname = name
		self.text = ''
		self.ispassword = ispassword
		self.selectable = 1
		self.special_keys = ["ENTER", "ESCAPE", "DELETE", "INSERT", "HOME", "END", "PAGEUP", "PAGEDOWN", "LEFT", "RIGHT", "UP", "DOWN", "WIN", "CTRL", "SHIFT"]

	def update(self, uData=-1):
		if uData.Y == self.y and uData.MB == 1 and uData.X >= self.x and uData.X < self.x + len(self.name):
			self.win.reset_selected()
			self.win.selidx = self.place
			self.selected = 1
		
		if self.selected:
			if uData != -1 and uData.Key not in self.special_keys and uData.Key != None:
				if uData.Key != '\b':
					self.text += uData.Key
				else:
					if len(self.text) != 0:
						self.text = list(self.text)
						self.text[-1] = ' '
						self.text = ''.join(self.text)
						self.win.addstr(self.x+len(self.name), self.y, self.text)
						self.text = list(self.text)
						self.text.pop()
						self.text = ''.join(self.text)

			self.win.set_color([255, 255, 255], [0, 0, 0])
			self.win.addstr(self.x+len(self.name), self.y, self.text)
		else:
			self.win.set_color([54, 54, 54], [0, 0, 0])
		self.win.addstr(self.x+len(self.name), self.y, '*'*len(self.text) if self.ispassword else self.text)
		self.win.addstr(self.x, self.y, self.name)

# RECT
class Rect:
	def __init__(self, x, y, w, h, fill_color, hollow=0):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.fill_color = fill_color
		self.selectable = 0
		self.hollow = hollow
	
	def update(self, uData=-1):
		self.win.set_color(self.fill_color, self.fill_color)
		for i in range(self.h):
			for j in range(self.w):
				if self.hollow:
					try:
						if i == 0 or j == 1 or i == self.h-1 or j == 0 or j == self.w-2 or j == self.w-1:
							self.win.addstr(self.x+j, self.y+i, ' ')
					except: pass
				else:
					try:
						self.win.addstr(self.x+j, self.y+i, ' ')
					except: pass

class SubWindow:
	def __init__(self, x, y, w, h, title):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.title = title
		self.widgets = []
		self.selected = 0
		self.selectable = 1
		self.title = Label(self.x, self.y, self.title, fg=[0, 0, 0], bg=[255, 255, 255])
		self.main = Rect(self.x, self.y, self.w, self.h, [255, 255, 255], hollow=1) # Main area
		self.XBTN = Button(self.x+self.w-3, self.y+1, 'X', onclick=self.close, fg=[255, 0, 0], bg=[255, 255, 255])

	def update(self, uData=-1):
		if uData.MB == 1 and uData.Y == self.y and uData.X >= self.x and uData.X < self.x + self.w and uData.X != self.x+self.w-3:
			self.selected = 1

		if self.selected and uData.MB != 1:
			self.selected = 0

		if self.selected == 1:
			self.x = uData.X
			self.y = uData.Y
		
		self.title.x = self.x+2
		self.title.y = self.y
		self.main.x = self.x
		self.main.y = self.y
		self.XBTN.x = self.x+self.w-3
		self.XBTN.y = self.y
		for widget in self.widgets:
			widget.x = self.x+2+widget.ox
			widget.y = self.y+1+widget.oy
	
	def add(self, widget):
		widget.ox = widget.x
		widget.oy = widget.y
		widget.x += self.x+2
		widget.y += self.y+1
		self.widgets.append(widget)
		self.win.add(widget)

	def close(self):
		self.win.remove(self.title)
		self.win.remove(self.main)
		self.win.remove(self.XBTN)
		for widget in self.widgets:
			self.win.remove(widget)

	def init(self):
		self.win.remove(self.title)
		self.win.remove(self.main)
		self.win.remove(self.XBTN)
		self.win.add(self.main)
		self.win.add(self.XBTN)
		self.win.add(self.title)
