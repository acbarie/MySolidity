#import remi.gui as gui
from remi import start, App
from remi.gui import *
import json
import subprocess

class Generator(App):
	def __init__(self, *args):
		self.lbl = {}
		self.txt = {}
		self.btn = {}
		self.dd = {}
		super(Generator, self).__init__(*args)
		
	def main(self):
		window1 = Widget()
		window1.attributes.update({"editor_baseclass":"Widget","editor_tag_type":"widget","editor_newclass":"False","editor_constructor":"()","class":"Widget","editor_varname":"window1"})
		window1.style.update({"position":"absolute","margin":"0px","overflow":"auto","top":"20px","left":"20px","width":"340.0px","height":"420.0px"})
		width = 100
		height = 25
		spacew = 110
		spaceh = 30
		
		def clbl(win, index, caption, x=0, y=0, w=1, h=1):
			leftstr = str(10+x*spacew)
			topstr = str(10+y*spaceh)
			widthstr = str(w*width)
			heightstr = str(h*height)
			lblstr = "lbl"+str(index)
			lbl1 = Label(caption)
			lbl1.style.update({"position":"absolute","margin":"0px","overflow":"auto","top":topstr+".0px","left":leftstr+".0px","width":widthstr+".0px","height":heightstr+".0px"})
			win.append(lbl1,lblstr)
			self.lbl[index] = lbl1
		
		def ctxt(win, index, sline=True, x=0, y=0, w=1, h=1):
			leftstr = str(10+x*spacew)
			topstr = str(10+y*spaceh)
			widthstr = str(w*width)
			heightstr = str(h*height)
			txtstr = "txt"+str(index)
			txt1 = TextInput(sline,'')
			txt1.style.update({"position":"absolute","margin":"1px","overflow":"auto","top":topstr+".0px","left":leftstr+".0px","width":widthstr+".0px","height":heightstr+".0px"})
			win.append(txt1,txtstr)
			self.txt[index] = txt1
		
		def cbtn(win, index, caption, cmdstr, x=0, y=0, w=1, h=1):
			leftstr = str(10+x*spacew)
			topstr = str(10+y*spaceh)
			widthstr = str(w*width)
			heightstr = str(h*height)
			btnstr = "btn"+str(index)
			btn1 = Button(caption)
			btn1.style.update({"position":"absolute","margin":"0px","overflow":"auto","top":topstr+".0px","left":leftstr+".0px","width":widthstr+".0px","height":heightstr+".0px"})
			btn1.onclick.do(cmdstr)
			win.append(btn1,btnstr)
			self.btn[index] = btn1
		
		def cdd(win, index, cmdstr, x=0,y=0, w=1, h=1):
			leftstr = str(10+x*spacew)
			topstr = str(10+y*spaceh)
			widthstr = str(w*width)
			heightstr = str(h*height)
			dd1 = DropDown()
			ddstr = "dd"+str(index)
			dd1.style.update({"position":"absolute","margin":"0px","overflow":"auto","top":topstr+".0px","left":leftstr+".0px","width":widthstr+".0px","height":heightstr+".0px"})
			dd1.onchange.do(cmdstr)
			win.append(dd1,ddstr)
			self.dd[index] = dd1
		
		clbl(window1,0,"", 0,0,1,1)
		ctxt(window1,0,True, 1,0,1,1)
		cbtn(window1,0,"Click Me", self.btn0,0,1,1,1)
		cdd(window1,0,self.dd0, 1,1,1,1)
		
		self.lbl[0].set_text("Forum name")
		self.dd[0].append("Number1")
		self.dd[0].append("Number2")
		
		self.window1 = window1
		return self.window1

	# listener function
	def btn0(self, emitter):
		self.lbl[0].set_text("Click me")
		
	def dd0(self, emitter,new_value):
		self.lbl[0].set_text(new_value)
        
# starts the web server
start(Generator)
