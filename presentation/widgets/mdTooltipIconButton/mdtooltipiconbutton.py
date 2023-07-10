from kivymd.uix.label import MDLabel
from kivymd.uix.tooltip import MDTooltip
from kivymd.uix.button import MDIconButton


class TooltipMDIconButton(MDIconButton, MDTooltip):
    pass

class TooltipMDLabel(MDLabel, MDTooltip):
    pass