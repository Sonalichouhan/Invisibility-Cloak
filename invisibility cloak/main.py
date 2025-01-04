import cv2
import numpy as np
import time

def create_bg(cap,num_frames=30):
    print("capturing bg , move away")
    background=[]
    for i in range(num_frames):
        ret,frame=cap.read()
        if ret:
            background.append(frame)
        else:
            break
        time.sleep(0.1)
    if background:
        return np.median(background,axis=0).astype(np.uint8)
    else:
        raise ValueError("could not capture bg")

def create_mask(frame,lower_color,upper_color):
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,lower_color,upper_color)
    mask=cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    mask=cv2.morphologyEx(mask, cv2.MORPH_DILATE,np.ones((3,3),np.uint8),iterations=1)
    return mask

def applycloakeffect(frame,mask,background):
    mask_inv=cv2.bitwise_not(mask)
    fg=cv2.bitwise_and(frame,frame,mask=mask_inv)
    bg=cv2.bitwise_and(background,background,mask=mask)
    return cv2.add(fg,bg)

def main():
    print("openCV version: ", cv2.__version__)

    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("error")
        return
    
    try:
        background=create_bg(cap)
    except ValueError as e:
        print(e)
        cap.release()
        return
    
    lower_blue = np.array([85, 0, 150])
    upper_blue = np.array([114, 86, 255])

    print("starting main loop press q to quit")
    while True:
        ret,frame=cap.read()
        if not ret:
            print("error couldnt read frame")
            time.sleep(1)
            continue

        mask=create_mask(frame,lower_blue,upper_blue)
        result= applycloakeffect(frame,mask, background)

        cv2.imshow('invisible cloak',result)
        if cv2.waitKey(1)&0xff==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()


