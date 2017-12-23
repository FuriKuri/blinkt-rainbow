#!/usr/bin/env python

import colorsys
import time

import blinkt

class GracefulKiller:
  kill_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.kill_now = True

spacing = 360.0 / 16.0
hue = 0

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

killer = GracefulKiller()

while True:
  hue = int(time.time() * 100) % 360
  for x in range(blinkt.NUM_PIXELS):
      offset = x * spacing
      h = ((hue + offset) % 360) / 360.0
      r, g, b = [int(c*255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
      blinkt.set_pixel(x, r, g, b)

  blinkt.show()
  time.sleep(0.001)
  if killer.kill_now:
    blinkt.clear()
    break