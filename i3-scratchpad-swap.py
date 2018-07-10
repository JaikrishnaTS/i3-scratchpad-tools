#!/usr/bin/env python3

import bisect
import i3ipc
import sys

i3 = i3ipc.Connection()
tree = i3.get_tree()
focused = tree.find_focused()
cur_con_is_sp = False

move_left = (len(sys.argv) > 1) and (sys.argv[1] == 'left')

p = focused
while p.type != 'workspace':
    if p.floating and (p.scratchpad_state != 'none'):
        cur_con_is_sp = True
        break
    p = p.parent

if not cur_con_is_sp:
    print('I am not a scratchpad')
    sys.exit(0)

i3.command('scratchpad show')

sp_nodes = sorted(tree.scratchpad().floating_nodes, key=lambda x:x.id)
if len(sp_nodes) == 0:  # happens when the only scratchpad is focused. Just hide
    sys.exit(0)

pos = bisect.bisect_left([x.id for x in sp_nodes], focused.id)
if move_left:
    pos -= 1
pos %= len(sp_nodes)

sp_nodes[pos].nodes[0].command('focus')
