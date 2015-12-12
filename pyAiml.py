#!/usr/bin/env python

from aiml import *


class pyAiml():


	def sraixCache(self, filename, chat)
		import os, logging, readline, sys
		try:
			fd = open(filename, 'r')
	                cont = True
	                while cont:
	                        strLine=fd.readline()
				print 'Human: '+strLine
	                        strLine=strLine.strip()
	                        if not strLine == '': 
	                                response = chat.multisentenceRespond(strLine)
					print ('Robot: '+response)
	
	        except:
			return 0;


	
