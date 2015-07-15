#!/usr/bin/env python
#Test
import sys
from time import sleep
from subprocess import Popen

class Runner:
    POLL_INTERVAL = 60
    FRAME_FILE = "frame.jpg"
    STREAM_COMMAND = "ffmpeg \
        -f video4linux2 -r 30 -i /dev/video0 -s 320x240 \
        -f mpeg1video -r 30 -b:v 100k %s \
        -vf fps=1/%i -f image2 -update 1 -y %s"

    def __init__(self, url):
        self.url = url
        self.stream_process = None

    def run(self):
        while True:
            if not self.is_streaming():
                self.start_stream()

            sleep(self.POLL_INTERVAL)

    def start_stream(self):
        cmd = self.STREAM_COMMAND % (self.url, self.POLL_INTERVAL, self.FRAME_FILE)
        print("Starting stream...")
        print("Command: %s" % cmd)
        self.stream_process = Popen(cmd, shell=True)

    def is_streaming(self):
        return self.stream_process != None and not self.stream_process.poll()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Usage: %s server_url' % sys.argv[0])

    Runner(sys.argv[1]).run()

