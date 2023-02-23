#!/bin/bash
ps aux | grep reply.py | grep -v grep | awk '{ print "kill -9", $2 }' | sh
cd /home/pi/work/morazubot_v4
source v4env/bin/activate
sleep 1
python reply.py &
