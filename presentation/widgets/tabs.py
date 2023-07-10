from kivymd.uix.tab import MDTabsBase
from kivy.properties import  StringProperty
from kivymd.uix.floatlayout import MDFloatLayout

from kivy.lang import Builder


Builder.load_string('''
#:import effect kivy.uix.effectwidget.EffectWidget
#:import HorizontalBlurEffect kivy.uix.effectwidget.HorizontalBlurEffect
#:import VerticalBlurEffect kivy.uix.effectwidget.VerticalBlurEffect
#:import TooltipMDLabel presentation.widgets.mdTooltipIconButton.mdtooltipiconbutton.TooltipMDLabel

<Tab>:
    MDBoxLayout:
        orientation: 'vertical'
        md_bg_color: 0, 0.56, 0.33, 0.15

        ScrollView:

            MDGridLayout:
                cols: 4
                padding: [dp(10)]
                spacing: dp(10)

                MDCard:
                    radius: [dp(15)]
                    size_hint_y: .5
                    MDFloatLayout:
                        EffectWidget:
                            radius: [dp(15)]
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                            effects: (HorizontalBlurEffect(size=10), VerticalBlurEffect(size=10),)
                            FitImage:
                                radius: [dp(15)]
                                source: 'assets/abstract.jpg'

                        MDLabel:
                            text: "2004-08-19"
                            color: "white"
                            bold: True
                            pos_hint: {'center_x': 0.55, 'center_y': 0.85}
                        
                        MDIconButton:
                            rounded_button: True
                            md_bg_color: 1, 1, 1, 0.7
                            pos_hint: {'center_x': 0.9, 'center_y': 0.85}
                            icon: "heart"
                            theme_text_color: "Custom"
                            text_color: 0, 0.56, 0.33, 1
                            icon_size: "18sp"
                        
                        MDLabel:
                            text: "Loi N° 2004-017"
                            color: "white"
                            bold: True
                            halign: "center"
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

                        TooltipMDLabel:
                            text: "Autorisant la ratification de la Convention des Nations Unies  contre la Corruption par Madagascar"
                            text_color: "white"
                            bold: True
                            halign: "center"
                            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
                            theme_text_color: "Custom"
                            font_size: "13.5sp"
                            markup: True
                            ellipsis_options: {'color':'white'}
                            max_lines: 2
                            tooltip_text: "Autorisant la ratification de la Convention des Nations Unies  contre la Corruption par Madagascar"

''')


class Tab(MDFloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
    content_text = StringProperty()


    
