from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import keys, mod

groups = [Group(i) for i in [
    "", "", "", "", "", "", "", "", "",
]]

for i, group in enumerate(groups):
    key = str(i + 1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], key, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], key, lazy.window.togroup(group.name),),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])
