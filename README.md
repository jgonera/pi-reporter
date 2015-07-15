# pi-reporter

Magical commands:

    avconv -f video4linux2 -r 30 -i /dev/video0 -s 320x240 -f mpeg1video -r 30 -b 400k http://airfoodstream-server/test/320/240 -f image2 -r 1 -update 1 out.jpg
    avconv -f video4linux2 -r 30 -i /dev/video0 -s 320x240 -f mpeg1video -r 30 -b 400k http://10.1.157.9:8082/test/320/240 -f image2 -vf select='not(mod(n\,100))' -update 1 out.jpg
