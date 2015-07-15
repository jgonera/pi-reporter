#!/usr/bin/env python
from time import sleep
from subprocess import Popen

class Runner:
    POLL_INTERVAL = 5
    FRAME_FILE = "frame.jpg"
    STREAM_COMMAND = "avconv \
        -f video4linux2 -i /dev/video0 -s 320x240 -r 30 \
        -f mpeg1video -b 400k %s \
        -f image2 -r 1/%i -an -update 1 %s"

    def __init__(self, url):
        self.url = url
        self.stream_process = None

    def run():
        while True:
            if !self.is_streaming():
                self.start_stream()

            sleep(POLL_INTERVAL)

    def start_stream():
        cmd = STREAM_COMMAND % (self.url, POLL_INTERVAL, FRAME_FILE)
        print("Starting stream...")
        print("Command: %s" % cmd)
        self.stream_process = Popen(cmd, shell=True)

    def is_streaming():
        return self.stream_process != None and !self.stream_process.poll()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit('Usage: %s server_url' % sys.argv[0])

    Runner(sys.argv[1]).run()

