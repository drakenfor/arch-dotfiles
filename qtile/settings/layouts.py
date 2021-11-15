from libqtile import layout
from libqtile.config import Match

layout_conf = {
    'border_focus': '#7c4dff',
    'border_width': 1,
    'margin': 1
}

layouts = [
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    layout.Bsp(**layout_conf, fair=False),
    layout.Columns(**layout_conf, insert_position=1),
    # layout.Matrix(columns=2, **layout_conf),
    # layout.MonadTall(**layout_conf),
    # layout.MonadWide(**layout_conf),
    # layout.RatioTile(**layout_conf),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
    # layout.Max(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),
        Match(wm_class='makebranch'),
        Match(wm_class='maketag'),
        Match(wm_class='ssh-askpass'),
        Match(title='branchdialog'),
        Match(title='pinentry'),
    ],
    border_focus="#7c4dff'",
)
