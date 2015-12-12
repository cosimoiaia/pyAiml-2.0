#!/usr/bin/env python

from aiml import *


if __name__ == '__main__':
	import os, logging, readline, sys
	chat = Chat()
	try:
                cont = True
                while cont:
                        strLine=raw_input('Human: ')
                        strLine=strLine.strip()
                        if not strLine == '': 
                                response = chat.multisentenceRespond(strLine)
				print ('Robot: '+response)

        except KeyboardInterrupt:
		sys.exit(0);

