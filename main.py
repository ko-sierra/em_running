# -*- coding: utf-8 -*-
#!/usr/bin/python
from functions import *

while 1:
    accel_x1,accel_y1,accel_z1 = get_accel_data_g()
    slope_x1,slope_y1,slope_z1 = calc_slope_for_accel_1axis(accel_x1,accel_y1,accel_z1)
    slope_x1 = math.degrees( slope_x1 )
    slope_y1 = math.degrees( slope_y1 )
    slope_z1 = math.degrees( slope_z1 )
    print '傾き[θ]',
    print 'x: %06.3f' % slope_x1,
    print 'y: %06.3f' % slope_y1,
    print 'z: %06.3f' % slope_z1,
    print       # 改行.
    sleep(0.1)