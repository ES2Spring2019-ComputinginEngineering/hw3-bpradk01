# NAME: Ben Pradko
# Bubble Level
# I worked with Alycia Wong on this project


import microbit
import math

while True:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()

    def calc_tilt_x(x, z):
        Theta_X = math.atan2(x, z)
        X = Theta_X * 180 / math.pi
        # microbit.display.scroll(X_deg)
        return (X)

    def calc_tilt_y(y, z):
        Theta_Y = math.atan2(y, z)
        Y = Theta_Y * 180 / math.pi
        # microbit.display.scroll(Y_deg)
        return (Y)

    Y_deg = calc_tilt_y(y, z)
    X_deg = calc_tilt_x(x, z)

    #microbit.sleep(1000)
    print(calc_tilt_x(x, z))
    print(calc_tilt_y(y, z))

    def X_location(deg):
        if (deg == 180) or (deg == 0):
            X = 2
        elif (deg < 180) and (deg >= 135):
            X = 3
        elif (deg < 135) and (deg > 0):
            X = 4
        elif (deg > -180) and (deg <= -135):
            X = 1
        elif (deg > -135) and (deg < 0):
            X = 0
        return X

    def Y_location(deg):
        if (deg == 180) or (deg == 0):
            Y = 2
        elif (deg < 180) and (deg >= 135):
            Y = 3
        elif (deg < 135) and (deg > 0):
            Y = 4
        elif (deg > -180) and (deg <= -135):
            Y = 1
        elif (deg > -135) and (deg < 0):
            Y = 0
        return Y

    microbit.display.set_pixel(X_location(X_deg), Y_location(Y_deg), 9)
    microbit.sleep(100)
    microbit.display.clear()

