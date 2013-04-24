#!/usr/bin/env python

import sys
import glob
import os
import string


class LtspException(Exception):
	'''
	Custom exception class
	'''
	def __init__(self, message):
		self.message = message


class LtspTest:
	
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
	
	def test_error_101(self):
		print("Testing the world")
		
	#def test_error_101
	
	def test_all(self,ltsp_id):
		
		# For method in test_error_* execute it!
		for f in range(200):
			for item in dir(self):
				if "test_error_"+str(f) == item:
					try:
						getattr(self,item)(ltsp_id)
					except Exception as e:
						print str(e)
				
	#def test_all
		
	
	
#class LtspTest

