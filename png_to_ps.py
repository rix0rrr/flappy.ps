#!/usr/bin/env python
import sys

from PIL import Image


def main():
  im = Image.open(sys.argv[1])
  name = sys.argv[2]

  w, h = im.size
  pixels = im.load()

  print '/%s_w %d def' % (name, w)
  print '/%s_h %d def' % (name, h)
  print '/%s {' % name
  print 'gsave'
  print '1 -1 scale'  # right side up
  print '%d %d translate' % (-w/2, -h/2)  # middle point in center
  for y in xrange(h):
    for x in range(w):
      r, g, b, a = pixels[x, y]
      if a:
        print '%.2f %.2f %.2f setrgbcolor' % (r/255., g/255., b/255.)
        print '%d %d 1 1 rectfill' % (x, y)

  print 'grestore'
  print '} def'


if __name__ == '__main__':
  main()
