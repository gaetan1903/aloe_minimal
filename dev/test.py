from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.select import MDSelect
from kivymd.uix.textfield import MDTextField


class DemoApp(MDApp):
    def build(self):
        return Builder.load_string(
            """
BoxLayout:
    orientation: 'vertical'
    MDTextField:
        id: txt_field
        text: 'Select a choice'
        size_hint: 1, 0.8
        dropdown_list: dd_list
    MDSelect:
        id: dd_list
        items: ['Choice 1', 'Choice 2', 'Choice 3']
        selected_item: 'Choice 1'
        on_select:
            txt_field.text = self.text
    """
        )


if __name__ == '__main__':
    DemoApp().run()