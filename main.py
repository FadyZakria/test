from kivy.app import App
from kivy.uix.image import Image

class MyImageApp(App):
    def build(self):
        return Image(source='image.jpg')  # استبدل 'image.jpg' باسم صورتك

if __name__ == '__main__':
    MyImageApp().run()
