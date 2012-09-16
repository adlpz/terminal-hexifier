#!/usr/bin/env python2

# auth: github.com/adlpz

import string
import plistlib
import sys

def convert(data):
    if data[102] == "F":
        cs = data[103:data.index('\x00', 103)]
    elif data[102] == "O":
        cs = data[105:data.index('\x00', 105)]
    else:
        return None
    return "#" + "".join(map(lambda h: "0"*(2-len(hex(h)[2:]))+hex(h)[2:], map(lambda x: int(float(x)*255), cs.split(' '))))

def main():
    try:
        f = "".join(filter(lambda c: c in string.printable, open(sys.argv[1]).read()))
        pl = plistlib.readPlistFromString(f)
    except Exception, e:
        print "Error:",e
        print "Usage: convert.py prefs.terminal"
        return

    colors = [
        "ANSIBlackColor",
        "ANSIRedColor",
        "ANSIGreenColor",
        "ANSIYellowColor",
        "ANSIBlueColor",
        "ANSIMagentaColor",
        "ANSICyanColor",
        "ANSIWhiteColor",
        "ANSIBrightBlack",
        "ANSIBrightRedColor",
        "ANSIBrightGreenColor",
        "ANSIBrightYellowColor",
        "ANSIBrightBlueColor",
        "ANSIBrightMagentaColor",
        "ANSIBrightCyanColor",
        "ANSIBrightWhiteColor",
        ]
    for i in range(len(colors)):
        try:
            c = convert(pl[colors[i]].data)
            if c:
                print "URxvt*color" + str(i) + ":\t" + c
        except KeyError:
            pass


main()

