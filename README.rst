i3-scratchpad-dmenu
###################

i3ipc program to list scratchpad containers with dmenu and focus the selection.

Install
=======

* Install i3ipc python module: ``pip3 install --user i3ipc``

* Copy the executable to ``~/.local/bin/``

* Suggested keybindings

  .. code:: bash

    # focus any scratchpad window
    bindsym $mod+t exec ~/.local/bin/i3-scratchpad-dmenu.py


i3-scratchpad-swap
##################

i3ipc program to swap among scratchpad containers while having them active. 

While i3 provides sufficient support to cycle through scratchpad windows with 
``scratchpad show`` while a scratchpad is active, it is required to press the
same keybinding twice to get to the next scratchpad. Also, there is no support
to swap back to the previous scratchpad. This program attemps to solve those
issues using the i3-ipc interface.

Install
=======

* Install i3ipc python module: ``pip3 install --user i3ipc``

* Copy the executable to ``~/.local/bin/``

* Suggested keybindings

  .. code:: bash

    # move window to scratchpad
    bindsym $mod+Shift+m move scratchpad

    # show the scratchpad
    bindsym $mod+m scratchpad show

    # move/swap among scratchpads while focused
    bindsym $mod+n exec ~/.local/bin/i3-scratchpad-swap.py left
    bindsym $mod+comma exec ~/.local/bin/i3-scratchpad-swap.py right

Use the keybindings to move previous/next through scratchpad windows while one
of them is focused. The program will work only when a scratchpad is focused.

