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

def MagicString:
	""" 
		Global values for many strings
	"""
	def __init__(self):
		self.program_name_version = "pyAiml-2.0 beta -- Python portring for AIML 2.0 implementation"
                self.comment = "Added repetition detection."
                self.aimlif_split_char = ","
                self.default_bot = "alice2"
                self.default_language = "EN"
                self.aimlif_split_char_name = "\\#Comma"
                self.aimlif_file_suffix = ".csv"
                self.ab_sample_file = "sample.txt"
                self.text_comment_mark = ";;"
                self.pannous_api_key = "guest"
                self.pannous_login = "test-user"
                self.sraix_failed = "SRAIXFAILED"
                self.repetition_detected = "REPETITIONDETECTED"
                self.sraix_no_hint = "nohint"
                self.sraix_event_hint = "event"
                self.sraix_pic_hint = "pic"
                self.sraix_shopping_hint = "shopping"
                self.unknown_aiml_file = "unknown_aiml_file.aiml"
                self.deleted_aiml_file = "deleted.aiml"
                self.learnf_aiml_file = "learnf.aiml"
                self.null_aiml_file = "null.aiml"
                self.inappropriate_aiml_file = "inappropriate.aiml"
                self.profanity_aiml_file = "profanity.aiml"
                self.insult_aiml_file = "insults.aiml"
                self.reductions_update_aiml_file = "reductions_update.aiml"
                self.predicates_aiml_file = "client_profile.aiml"
                self.update_aiml_file = "update.aiml"
                self.personality_aiml_file = "personality.aiml"
                self.sraix_aiml_file = "sraix.aiml"
                self.oob_aiml_file = "oob.aiml"
                self.unfinished_aiml_file = "unfinished.aiml"
                self.inappropriate_filter = "FILTER INAPPROPRIATE"
                self.profanity_filter = "FILTER PROFANITY"
                self.insult_filter = "FILTER INSULT"
                self.deleted_template = "deleted"
                self.unfinished_template = "unfinished"
                self.bad_javascript = "JSFAILED"
                self.js_enabled = "true"
                self.unknown_history_item = "unknown"
                self.default_bot_response = "I have no answer for that."
                self.error_bot_response = "Something is wrong with my brain."
                self.schedule_error = "I'm unable to schedule that event."
                self.system_failed = "Failed to execute system command."
                self.default_get = "unknown"
                self.default_property = "unknown"
		self.root_path = "~/pyAiml"
	
		def setRootPath(self, newRootPath):
			self.root_path = newRootPath
	
