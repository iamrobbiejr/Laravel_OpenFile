import sublime
import sublime_plugin
import os
import re

class LaravelOpenFileCommand(sublime_plugin.WindowCommand):

	search_expressions = (r"return +view\('%s",)

	def search(self, view, text):
		word = view.substr(view.word(text))
		line = view.substr(view.line(text))

		search_result = any(re.search(e % word, line) for e in self.search_expressions)
		if search_result:
			self.get_view(view, text)

	def get_view(self, view, text):
		controllerspcpath = 'app'+os.path.sep+'Http'+os.path.sep+'Controllers'+os.path.sep 
		laravel_base_path = view.file_name().split(controllerspcpath)
		word = view.substr(view.word(text))
		blade_path = os.path.sep.join(word.split('.'))
		blade_full_path = laravel_base_path[0]+'resources'+os.path.sep+'views'+os.path.sep+blade_path+'.blade.php'
		buffer = self.window.open_file(blade_full_path)


	def run(self):
		view = self.window.active_view()
		sel = view.sel()
		for text in sel:
			self.search(view, text)
