import sublime
import sublime_plugin


class LitterLogCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view()
        print 'hi'
        print view.name()
