from libqtile import widget
# ------ Clock ---------------
clock = widget.Clock(
    format='%a %d/%m/%y %I:%M %p',
)

# ------------- Net ----------------
net = widget.Net(
    interface="wlan0",
)

# ----------------- Group -----------
group_box = widget.GroupBox(
    font="JetBrainsMono NF",
    fontsize=30,
    active="#7c4dff",
    boderwidth=1,
    highlight_method='block',
    this_current_screen_border="#ffffff",
    rounded=False,
    this_screen_border="#ffffff",
    disable_drag=True
)

