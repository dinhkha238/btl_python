import cv2

IMAGE_BG = "R.jpg"
IMAGE_FG = "xam.jpg"
OUT_NAME = "blending.jpg"

BLEND_X = 0.1
BLEND_Y = 0.05
BLEND_OPAQUE = 0.5



def blend(bg, fg, x, y, opaque=1.0, gamma=0):
    """
        bg: background (color image)
        fg: foreground (color image)
        x, y: top-left point of foreground image (percentage)
    """
    h, w = bg.shape[:2]
    x_abs, y_abs = int(x*w*2), int(y*h*2)
    
    fg_h, fg_w = fg.shape[:2]
    patch = bg[y_abs:y_abs+fg_h, x_abs:x_abs+fg_w, :]
    
    blended = cv2.addWeighted(src1=patch, alpha=1-opaque, src2=fg, beta=opaque, gamma=gamma)
    result = bg.copy()
    result[y_abs:y_abs+fg_h, x_abs:x_abs+fg_w, :] = blended
    return result

def main(bg_path, fg_path):
    img_bg = cv2.imread(bg_path)
    img_fg = cv2.imread(fg_path)
    result = blend(bg=img_bg, fg=img_fg, x=BLEND_X, y=BLEND_Y, opaque=BLEND_OPAQUE)
    cv2.imshow(OUT_NAME, result)
    print("\x1b[1;%dm" % (31) + "Saved image @ %s" % OUT_NAME + "\x1b[0m")
    pass


if __name__ == "__main__":
    main(bg_path=IMAGE_BG, fg_path=IMAGE_FG)
    print('-------')
    print('* Follow me @ ' + "\x1b[1;%dm" % (34) + ' https://www.facebook.com/kyznano/' + "\x1b[0m")
    print('* Minh fanpage @ ' + "\x1b[1;%dm" % (34) + ' https://www.facebook.com/minhng.info/' + "\x1b[0m")    
    print('* Join GVGroup @ ' + "\x1b[1;%dm" % (34) + 'https://www.facebook.com/groups/ip.gvgroup/' + "\x1b[0m")    
    print('* Thank you ^^~')
cv2.waitKey(0)
