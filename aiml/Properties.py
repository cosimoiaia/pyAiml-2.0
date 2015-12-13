#        pyAiml-2.0 Python portring for AIML 2.0 implementation
#        Contact: cosimo.iaia@gmail.com
#
#       This library is free software; you can redistribute it and/or
#        modify it under the terms of the GNU Library General Public
#        License as published by the Free Software Foundation; either
#        version 2 of the License, or (at your option) any later version.
#
#        This library is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#        Library General Public License for more details.
#
#        You should have received a copy of the GNU Library General Public
#        License along with this library; if not, write to the
#        Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
#        Boston, MA  02110-1301, USA.
#
#

class Properties

	def __init__(self):
		self.hsh = dict()

	def get(key):
		value = ''
		if self.hsh.has_key(key):
			value = self.hsh[key]
		else 
			value = MagicStrings.default_property
		
		return value

	def getPropertiesFromInputStream(self, fd):
		cnt = 0
		try:
			for l in fd.readlines():
				if l.find(':'):
					buff = l.split(':')
					self.hsh[buff[0]] =  buff[1]
					cnt = cnt+1;
		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
		
		return cnt

	def getProperties(self, filename):
		try:
			fd = open(filename, 'r')

			return self.getPropertiesFromInputStream(fd)

		except IOError as e:
			print "I/O error({0}): {1}".format(e.errno, e.strerror)
		except:
			print "Unexpected error:", sys.exc_info()[0]
			raise
