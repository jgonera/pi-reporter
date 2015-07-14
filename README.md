# pi-reporter

Magical command:

    avconv -f video4linux2 -i /dev/video0 -s 320x240 -r 30 -b 400k -f mpeg1video http://airfoodstream-server/test/320/240 -f image2 -an -update 1 out.jpg
