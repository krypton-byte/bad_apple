from colorama import Cursor
from os import get_terminal_size
import cv2
import sys


translate = [
    ' ',
    '.',
    '-',
    '/',
    '!',
    '+',
    '*',
    '%',
    '$',
    '&',
    '#',
    '@',
]


def patternResCustom(x, y, res):
    """
    AutoScale
    """
    if x == y:
        return [res, res]
    elif x > y:
        return [res, int(y/(x/res))]
    elif x < y:
        return [int(x/(y/res)), res]


def toAscii():
    camera = cv2.VideoCapture("x.mp4")
    while True:
        ret, frame = camera.read()
        x_term, y_term = get_terminal_size()
        frame2 = cv2.cvtColor(
            cv2.resize(
                frame,
                (x_term, y_term)
            ),
            cv2.COLOR_BGR2GRAY
        )
        sys.stdout.write(
            Cursor.POS(1, 1) +
            ''.join(
                [''.join(
                    [translate[int(c/25.5)] for c in w]) for w in frame2]))
        sys.stdout.flush()
        if cv2.waitKey(7) & 0xFF == ord("q"):
            break


toAscii()
