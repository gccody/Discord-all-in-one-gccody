import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
kivy.require('1.0.7')

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<UpdatingScreen>:
    BoxLayout:
        Label:
            text: 'Checking for updates...'

<SettingsScreen>:
    
""")

# Declare both screens
class UpdatingScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestApp(App):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        def changeTitle(string: str) -> str:
          self.title = string
        sm.add_widget(UpdatingScreen(name='update'), on_enter=changeTitle('Updating...'))
        sm.add_widget(SettingsScreen(name='settings'), on_enter=changeTitle(''))

        return sm
    

if __name__ == '__main__':
    TestApp().run()