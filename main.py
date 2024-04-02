from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    md_bg_color: self.theme_cls.backgroundColor
    MDLabel:
        text: "Тест пройден"
		halign: "center"
    	theme_text_color: "Custom"
    	text_color: "red"
        halign: "center"
'''
class TestApp(MDApp):
	def build(self):
		return Builder.load_string(KV)

if __name__ == "__main__":
	TestApp().run()
