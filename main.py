from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):
    def search_image(self):
        # Get user query from TextInput
        query = self.manager.current_screen.ids.user_query.text
        # Get wikipedia page and the link for the first image
        page = wikipedia.page(query)
        image_link = page.images[0]
        # Download the image
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        req = requests.get(image_link, headers=headers)
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        # Set the image in the Image widget
        self.manager.current_screen.ids.img.source = imagepath


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    # Override the build class
    def build(self):
        return RootWidget()


MainApp().run()
