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
	'''
	Default chroot path
	'''
	
	LTSP_IMAGES_PATH="/opt/ltsp/images/"
	'''
	Default images path
	'''
	
	LTSP_LAST_TIME="time.time"
	'''
	Default last time modification token
	'''
	
	

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
	#get_img_str
	
	def get_squashfs_str(self,img_id):
		'''
		Get squashfs string path
		'''
		if os.path.exists(LtspInfo.LTSP_CHROOT_PATH+"/"+img_id+"/"):
			return str(LtspInfo.LTSP_CHROOT_PATH+"/"+img_id+"/")
		else:
			return None
	# get_squashfs_str
	
	def get_modification_time(self,img_id):
		'''
		Get the last modification time
		'''
		if os.path.exists(LtspInfo.LTSP_CHROOT_PATH+"/"+img_id+"/"+LtspInfo.LTSP_LAST_TIME):
			last_time = open(LtspInfo.LTSP_CHROOT_PATH+"/"+img_id+"/"+LtspInfo.LTSP_LAST_TIME,'r').read()
			return last_time
		else:
			return None
	# get_modification_time

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
	# get_ltsp_dic_desktop(self):
		
	def get_ltsp_dic_client(self):
		'''
		Get the dic entry for clients
		'''
		self.dic_images["images"].append(
			{
			"id":"client",
			"name": "LliureX Client",
			"desc": "LliureX Client Description",
			"img": "lliurex-client.png",
			"image_file" : self.get_img_str("client"),
			"squashfs_dir": self.get_squashfs_str("client"),
			"installed":self.get_modification_time("client"),
			"lliurex_version":None,
			"errorcode":None,
			"errormsg":None
			}
		)
	# get_ltsp_dic_client
	
	def get_ltsp_dic_music(self):
		'''
		Get the dic entry for music
		'''
		self.dic_images["images"].append(
			{
			"id":"music",
			"name": "LliureX Music",
			"desc": "LliureX Music Description",
			"img": "lliurex-music.png",
			"image_file" : self.get_img_str("music"),
			"squashfs_dir": self.get_squashfs_str("music"),
			"installed":self.get_modification_time("music"),
			"lliurex_version":None,
			"errorcode":None,
			"errormsg":None
			}
		)
	# get_ltsp_dic_music

	def get_ltsp_dic_pime(self):
		'''
		Get the dic entry for Pime
		'''
		self.dic_images["images"].append(
			{
			"id":"pime",
			"name": "LliureX Pime",
			"desc": "LliureX Pime Description",
			"img": "lliurex-pime.png",
			"image_file" : self.get_img_str("pime"),
			"squashfs_dir": self.get_squashfs_str("pime"),
			"installed":self.get_modification_time("pime"),
			"lliurex_version":None,
			"errorcode":None,
			"errormsg":None
			}
		)
	# get_ltsp_dic_pime
	
	def get_ltsp_dic_infantil(self):
		'''
		Get the dic entry for infantil
		'''
		self.dic_images["images"].append(
			{
			"id":"infantil",
			"name": "LliureX Infantil",
			"desc": "LliureX Infantil Description",
			"img": "lliurex-infantil.png",
			"image_file" : self.get_img_str("infantil"),
			"squashfs_dir": self.get_squashfs_str("infantil"),
			"installed":self.get_modification_time("infantil"),
			"lliurex_version":None,
			"errorcode":None,
			"errormsg":None
			}
		)
	# get_ltsp_dic_infantil
	
	def get_ltsp_dic(self):
		'''
		Returns a simple dictionary with LTSP images information
		'''
		# Dic images
		# self.dic_images={}

		self.dic_images={}
		self.dic_images["images"] = []
		
		# Append flavours
		self.get_ltsp_dic_desktop()
		self.get_ltsp_dic_client()
		self.get_ltsp_dic_infantil()
		self.get_ltsp_dic_music()
		self.get_ltsp_dic_pime()
		
		# Return the dictionary
		return self.dic_images
	# get_ltsp_dic


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
	# __init__

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

