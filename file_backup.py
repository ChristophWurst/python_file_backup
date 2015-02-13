#!/usr/bin/python

import time
import datetime
import json
import sys
import os
import os.path
import shutil
import tkMessageBox
import Tkinter

ts = time.time()
time = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')

jsonFile = open(os.path.join(os.path.dirname(__file__), 'files.json'))
data = json.load(jsonFile)

root = Tkinter.Tk()
root.withdraw()

try:
	for src, dest in data.items():
		destDir = dest + os.path.sep + time
		if os.path.isdir(src):
			#directory
			shutil.copytree(src, destDir)
		else:
			#file
			if not os.path.exists(destDir):
				os.makedirs(destDir)
			shutil.copy(src, destDir)
except Exception as e:
	tkMessageBox.showwarning('File Backup', 'Backup failed (' + str(e) + ')')
	sys.exit(1)

root = Tkinter.Tk()
root.withdraw()
tkMessageBox.showinfo('File Backup', 'Backup finished')
