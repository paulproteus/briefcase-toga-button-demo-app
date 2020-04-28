"""
My first application
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW



class HelloWorld(toga.App):

    def startup(self):
        """
        Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        print('Hello from HelloWorld.startup()')
        main_box = toga.Box(style=None)
        class Refreshable:
            refresh = lambda *args, **kwargs: None
        main_box._root = Refreshable  # Hack: Avoiding layout
        button = toga.Button(
            "Say Hello!",
            on_press=self.say_hello,
            style=Pack(padding=5),
        )
        main_box.add(button)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, _ignored_widget):
        print("Hello, world! from Android Toga app")

def main():
    # XXX Hack
    class HasDunderPackage:
        __package__ = 'helloworld'
    import sys
    sys.modules['__main__'] = HasDunderPackage
    ## XXX End hack
    return HelloWorld()
