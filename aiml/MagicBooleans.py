#        pyAiml-2.0 Python portring for AIML 2.0 implementation
#        Contact: cosimo.iaia@gmail.com
#
#       This library is free software you can redistribute it and/or
#        modify it under the terms of the GNU Library General Public
#        License as published by the Free Software Foundation either
#        version 2 of the License, or (at your option) any later version.
#
#        This library is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#        Library General Public License for more details.
#
#        You should have received a copy of the GNU Library General Public
#        License along with this library if not, write to the
#        Free Software Foundation, Inc., 51 Franklin St, Fifth Floor,
#        Boston, MA  02110-1301, USA.
#
#


#
# Global boolean values that control various actions
# 



class MagicBooleans:

	def __init__(self):
		self.trace_mode = True
		enable_external_sets = True
		enable_external_maps  = True
		jp_tokenize = True
		fix_excel_csv = True
		enable_network_connection = True
		cache_sraix = True
		qa_test_mode  = True
		make_verbs_sets_maps  = True

	def trace(self, traceString):
		if(self.trace_mode):
			print (traceString)
