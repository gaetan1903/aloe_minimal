from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivy.properties import  StringProperty

from kivy.lang import Builder


Builder.load_string('''
<Tab>:
    MDScreen:
        md_bg_color: 0, 0.56, 0.33, 0.15
        MDLabel:
            text: root.content_text
            halign: 'center'
            pos_hint: {"center_x": .5, "center_y": .5}
''')


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    content_text = StringProperty()


    
