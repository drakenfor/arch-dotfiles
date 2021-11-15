from libqtile import bar, widget
from libqtile.config import Screen

from .widgets import clock, net, group_box

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                group_box,
                # widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                net,
                clock,
                widget.QuickExit(),
            ],
            24,
            opacity=0.8
        ),
    ),
]
