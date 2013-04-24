#!/usr/bin/env python

import sys
import glob
import os
import string


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
			return {'status': True, 'msg':'[N4dChroot] Directory existent'}
		else:
			return {'status': False, 'msg':'[N4dChroot] Directory not existent'}

	#def test_chroot(self, chroot_dir)
	
#class LtspTest

