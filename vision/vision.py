#!/usr/bin/python3

from cv2 import numpy, putText, FONT_HERSHEY_SIMPLEX, LINE_AA
from sys import argv

if len(argv) < 3:
  print("Usage: ./vision.py [flag_file] [ouput_file]")
  exit(0)

ffile = ''
ofile = ''

try:
  ffile = argv[1]
  ofile = argv[2]
except Exception as e:
  print(e)
  exit(0)

# Adjust the size to contain your flag
img = numpy.zeros((512, 512, 3), numpy.uint8)

with open(ffile, 'r') as flag:

    flag = flag.read().strip()

    putText(img, flag, (0, 200),
               FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2, LINE_AA)

    img.dump(ofile)
