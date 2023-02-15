import cv2
import numpy as np

## create blank image bitwise operations 
blank =np.zeros((400,400), dtype="uint8")
rectangle = cv2.rectangle(blank.copy(), (50,50),(250,250),255,-1)
rectangle2 = cv2.rectangle(blank.copy(), (150,150),(200,200),255,-1)
rec=cv2.bitwise_xor(rectangle,rectangle2)
cv2.imshow("rec",rec)


## essential functions
def rescale(frame,scale=1.5):
    return cv2.resize(frame,(int(frame.shape[1]*scale),int(frame.shape[0]*scale)),cv2.INTER_AREA)

def gray(frame):
    return cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

def hsv(frame): # other color spaces are lab rgb etc.
    return cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


def blur(frame):
    return cv2.GaussianBlur(frame,(3,3),cv2.BORDER_DEFAULT)

def edge(frame):
    return cv2.Canny(frame,0,150)

def dilate(frame):
    return cv2.dilate(frame,(3,3)) # erode can be also using

def crop(frame):
    return frame[:,50*5:-50*5]

def thresh(frame):
    thresh,threshold=cv2.threshold(frame,100,250,cv2.THRESH_BINARY)
    return threshold

def main():
    ## read image 
    cat=cv2.imread("C:/Users/fzlfrkkms/Desktop/quantum/python_ex/Resources/Photos/cat.jpg")
    cat=gray(cat)
    cat=thresh(cat)
    cv2.imshow("threshold", cat)
    blank =np.zeros((cat.shape[0],cat.shape[1]), dtype="uint8")
    rectangle = cv2.rectangle(blank.copy(), (170,170),(550,550),255,-1)   
    ll=cv2.bitwise_and(cat,cat,mask=rectangle)
    cv2.imshow("cat",ll )
    cv2.waitKey(0) # otherwise img window close immediately
    ## video capture
    video=cv2.VideoCapture('./Resources/Videos/dog.mp4')

    while True:
        isTrue, frame = video.read()
        frame=rescale(frame)
        frame=gray(frame)
        frame=blur(frame)
        frame=edge(frame)
        frame=dilate(frame)
        frame=crop(frame)
        cv2.imshow("Dog", frame)
        
        if cv2.waitKey(20) & 0xFF== ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__==main():
    main()
