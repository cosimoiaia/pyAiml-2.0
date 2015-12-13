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

import time

class Timer:
	def __init__(self):
		self.startTimeMillis = self.__currentTimeMillis()

	def _currentTimeMillis():
		return int(round(time.time() * 1000))

	def start(self):
		self.startTimeMillis = self._currentTimeMillis()

	def elapsedTimeMillis(self):
		return self._currentTimeMillis() - self.startTimeMillis+1

	def elapsedRestartMs(self):
		ret = self._currentTimeMillis() - self.startTimeMillis+1
		this.start()
		return ret

	def elapsedTimeSecs(self):
		return self.elapsedTimeMillis() / 1000

	def elapsedTimeMins(self):
		return self.elapsedTimeMillis() / 60
