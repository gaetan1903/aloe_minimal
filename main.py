from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager

from presentation.screens.homescreen.homescreen import HomeScreen
from presentation.screens.splashscreen.splashscreen import SplashScreen


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.font_name = 'Product Sans'
        Window.size = (1280, 744)
        Window.title = "Accès sur les Lois Environnement" 
        screen_manager = ScreenManager()
        screen_manager.add_widget(SplashScreen(name='splash'))
        screen_manager.add_widget(HomeScreen(name='home'))
        return screen_manager


MainApp().run()
