#!/usr/bin/python

import sys, os

if sys.version_info < (3,):
	def tobyte(x): return chr(x)
else:
	def tobyte(x): return bytes([x])

gamma = float(sys.argv[1])

for i in range(256):
	value = int(((float(i) / 255)**gamma) * 255)
	os.write(sys.stdout.fileno(), tobyte(value))
