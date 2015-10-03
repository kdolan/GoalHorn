#!/bin/bash
#sh /horns/scripts/setuo_gpio.sh
tmux new -d -s goal-session 'sudo python /horns/scripts/goalbutton.py'
exit 0
