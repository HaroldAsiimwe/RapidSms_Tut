from rapidsms.contrib.handlers import KeywordHandler

help_text = {
	'aaa': 'Help for aaa is...',
	'bbb': 'Help for bbb is ...',
	'ccc': 'Help for ccc is ...',
	}

class HelpHandler(KeywordHandler):
	"""docstring for HelpHandler"""

	keyword  = "help"
	
	def help(self):
		self.respond("Allowed commands are AAA, BBB, and CCC. Send HELP <command> for more help on a specific command.")

   	def handle(self, text):
   		"""Invoked if someone sends `HELP <any text>`"""
   		text = text.strip().lower()
   		if text == 'aaa':
   			self.respond(help_text['aaa'])
   		elif text == 'bbb':
   			self.respond(help_text['bbb'])
   		elif text == 'ccc':
   			self.respond(help_text['ccc'])
   		else:
   			self.help()