"""
A small and simple converter to translate hour angle to degrees (and otherwise)
:author: Fenja Kollasch
:date: 06/13/2017
"""
import sys


def convert_hourangle(angle):
    s = angle.split('h')
    deg = float(s[0]) * 15
    s = s[1].split('m')
    deg += float(s[0])/4
    s = s[1].split('s')
    deg += float(s[0])/240

    return deg


def convert_deg(deg):
    hour = deg - (deg % 15) * 15
    s = deg - hour
    minute = s - (deg % 0.25) * 0.25
    s = s - minute
    return "{0}h{1}m{2}s".format(hour, minute, s)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: 'Hourangle: <value>' or 'Degree: <value>', respectively.")
        print("First one")
    else:
        try:
            if sys.argv[1] == "Hourangle:":
                print("Degree: {0}".format(convert_hourangle(sys.argv[2])))
            elif sys.argv[1] == "Degree:":
                print("Hourangle: {0}".format(convert_deg(sys.argv[2])))
            else:
                print("Usage: 'Hourangle: <value>' or 'Degree: <value>', respectively.")
                print("Second one")
        except Exception:
            print("Seems like your String is not formatted right.")
            print("it should look like: 00h00m00.0000s")