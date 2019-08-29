#import os
##import math
##import sys

##import numpy as np
##import cv2

##import _config as cf
#import _filesys as fs
#import _functions as fn

#class file_info:

#	def __init__(self, fullpath, workingfolder):

#		filename_arr = fullpath.split(os.sep)
				 
#		self.rootfolder = workingfolder
#		self.fullfilename = fullpath
#		self.filename = filename_arr[-1]
#		self.extension = fs.file_ext(fullpath); 
#		self.folder = os.sep.join(filename_arr[:-1])
#		self.excludefilereorg = fn.exclude_in_file_reorg(self.fullfilename)

#		self.isatroot = self.rootfolder == self.folder;

#		if self.isatroot: 
#			return
		
#		parent_arr = fullpath.replace(workingfolder, "").split(os.sep)
		
#		if len(parent_arr) < 2: return

#		self.parentfoldername = [s for s in parent_arr if len(s) > 0][0]
		
#		workingfolderArr = [s for s in workingfolder.split(os.sep) if len(s) > 0]
#		workingfolderArr.append(self.parentfoldername)

#		self.parentfolderpath = os.sep.join(workingfolderArr)

