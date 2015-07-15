#!/usr/bin/env python
#Test
import sys
from time import sleep
from subprocess import Popen

class Runner:
    POLL_INTERVAL = 5
    FRAME_FILE = "frame.jpg"
    STREAM_COMMAND = "avconv \
        -f video4linux2 -i /dev/video0 -s 320x240 -r 30 \
        -f mpeg1video -r 30 -b 400k %s"

    def __init__(self, url):
        self.url = url
        self.stream_process = None

    def run(self):
        while True:
            if not self.is_streaming():
                self.start_stream()

            sleep(self.POLL_INTERVAL)

    def start_stream(self):
        cmd = self.STREAM_COMMAND % (self.url)
        print("Starting stream...")
        print("Command: %s" % cmd)
        self.stream_process = Popen(cmd, shell=True)

    def is_streaming(self):
        return self.stream_process != None and not self.stream_process.poll()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Usage: %s server_url' % sys.argv[0])

    Runner(sys.argv[1]).run()

