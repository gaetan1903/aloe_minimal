from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.clock import Clock

Builder.load_file('presentation/screens/splashscreen/splashscreen.kv')

class SplashScreen(Screen):
    def on_enter(self):
        Clock.schedule_interval(self.update_progress, 1)

    def update_progress(self, dt):
        progress_bar = self.manager.get_screen('splash').ids.progress_bar
        progress_bar.value += 20

        if progress_bar.value >= 100:
            self.manager.current = 'home'