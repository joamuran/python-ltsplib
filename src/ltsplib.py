#!/usr/bin/env python

import sys
import glob
import os
import string
import time

class LtspInfo:
	'''
	Info class for values
	'''
	LTSP_CHROOT_PATH="/opt/ltsp/"
	LTSP_IMAGES_PATH="/opt/ltsp/images/"
	LTSP_LAST_TIME="time.time"
	


class LtspException(Exception):
	'''
	Custom exception class
	'''
	def __init__(self, message, Errors):
		# Call the base class constructor with the parameters it needs
		Exception.__init__(self, message)

		# Now for your custom code...
		self.Errors = Errors


class LtspDic:
	'''
	Class to manage LTSP Dictionaries
	'''
	
	def __init__(self):
		'''
		Simple init method, that initializes a new Dictionary
		'''
		self.dic_images={}
		self.dic_images["images"]=[]


	def get_img_str(self, img_id):
		'''
		Get image string path 
		'''
		
		if os.path.exists(LtspInfo.LTSP_IMAGES_PATH+"/"+img_id+".img"):
			return str(LtspInfo.LTSP_IMAGES_PATH+"/"+img_id+".img")
		else:
			return None
	
	def get_squashfs_str(self,img_id):
		'''
		Get squashfs string path
		'''
		if os.path.exists(LtspInfo.LTSP_CHROOT_PATH+"/"+img_id+"/"):
			return str(LtspInfo.LTSP_CHROOT_PATH+"/"+img_id+"/")
		else:
			return None
	
	def get_modification_time(self,img_id):
		'''
		Get the last modification time
		'''
		if os.path.exists(LtspInfo.LTSP_CHROOT_PATH+"/"+img_id+"/"+LtspInfo.LTSP_LAST_TIME):
			last_time = open(LtspInfo.LTSP_CHROOT_PATH+"/"+img_id+"/"+LtspInfo.LTSP_LAST_TIME,'r').read()
			return last_time
		else:
			return None


	def get_ltsp_dic_desktop(self):
		'''
		Get the dic entry for desktops
		'''
		self.dic_images["images"].append(
			{
			"id":"desktop",
			"name": "LliureX Desktop",
			"desc": "LliureX Desktop Description",
			"img": "lliurex-escriptori.png",
			"image_file" : self.get_img_str("desktop"),
			"squashfs_dir": self.get_squashfs_str("desktop"),
			"installed":self.get_modification_time("desktop"),
			"lliurex_version":None,
			"errorcode":None,
			"errormsg":None
			}
		)
		
	

	
	def get_ltsp_dic(self):
		'''
		Returns a simple dictionary with LTSP images information
		'''
		# Dic images
		# self.dic_images={}

		self.dic_images={}
		self.dic_images["images"] = []
		
		# Append desktop
		self.get_ltsp_dic_desktop()
		
		return self.dic_images
	
	#def get_ltsp_dic


class LtspTest:
	'''
	Class LtspTest : Simple Tests suite for Ltsp image system
	'''
	
	dic_images = {}
	dic_images["images"] =[]
	
	def __init__(self):
		'''
		Simple init method
		'''
		pass
	

	def test_chroot(self, chroot_dir):
		'''
		test_chroot test if the given directory is a real chroot or 
		besides, it seems like a chroot.
		'''
		if os.path.isdir(chroot_dir):
			return True
		else:
			return False

	#def test_chroot(self, chroot_dir)
	
	def test_error_101(self,ltsp_id):
		'''
		Test if img is created under the correct path of ltsp
		'''
		try:
			print("Testing the world")
		except Exception as e:
			raise LtspException(e)
		
		
	#def test_error_101
	
	def test_all(self,ltsp_id):
		
		# For method in test_error_* execute it!
		for f in range(200):
			for item in dir(self):
				if "test_error_"+str(f) == item:
					try:
						getattr(self,item)(ltsp_id)
					except LtspException as e:
						print str(e)
				
	#def test_all
		
	
	
#class LtspTest

