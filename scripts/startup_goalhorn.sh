#!/bin/bashvim
tmux new-session -d -s goal-session 'python /horn/scripts/server.py'
sleep 0.5
tmux split-window -h 'python /horn/scripts/hardware_monitor.py'
sleep 0.5
tmux split-window -v 'python /horn/scripts/software_goal.py'
exit 0

