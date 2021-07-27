#!/bin/bash

cd /home/d_keti/parking_streaming
HERE=$(dirname $(realpath $0))
echo $HERE
source /home/d_keti/parking_streaming/parking/bin/activate

nohup python main.py &
