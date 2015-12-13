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

class MagicNumber {

	"""
		Integers with specific values
	"""
	
	def __init__(self):
		self.node_activation_cnt = 4
		self.node_size = 4  
		self.displayed_input_sample_size = 6
		self.max_history = 32
		self.repetition_count = 2
		self.max_stars = 1000
		self.max_graph_height = 100000
		self.max_substitutions = 10000
		self.max_recursion_depth = 765 
		self.max_recursion_count = 2048
		self.max_trace_length = 2048
		self.max_loops = 10000
		self.estimated_brain_size = 5000
		self.max_natural_number_digits = 10000
		self.brain_print_size = 100 
