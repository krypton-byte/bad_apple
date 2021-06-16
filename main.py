from PIL import Image
from os import get_terminal_size
import cv2
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
        frame_str=""
        img=Image.fromarray(frame)
        #real_size = tuple(patternResCustom(*size, max([x_term, y_term])))
        img=img.resize([x_term, y_term])
        for x in range(img.height):
            for i in range(img.width):
                jum=sum(img.getpixel((i, x)))
                frame_str+= "^" if jum > 80 else "|" if jum > 70 else "*" if jum > 50 else " "

        print(frame_str)
        #cv2.imshow("CAP", np.array(img))
        if cv2.waitKey(7) & 0xFF == ord("q"):
            break
toAscii()