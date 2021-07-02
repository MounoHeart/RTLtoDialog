import sublime
import sublime_plugin

class RTLtoDialogCommand(sublime_plugin.EventListener):
    def on_hover(self, view, point, hover_zone):
        if hover_zone == 1:
        	sel = view.sel()
        	region1 = sel[0]
        	ch = view.substr(region1)
        	if ('\u0600' <= ch <= '\u06FF' or '\u0750' <= ch <= '\u077F' or '\u08A0' <= ch <= '\u08FF' or '\uFB50' <= ch <= '\uFDFF' or '\uFE70' <= ch <= '\uFEFF' or '\U00010E60' <= ch <= '\U00010E7F' or '\U0001EE00' <= ch <= '\U0001EEFF'):
        		sublime.message_dialog(ch)
                self.view.show_popup(ch) #Shows a popup displaying HTML content.

