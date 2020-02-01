import cv2
import  sys
if __name__=='__main__':
    if len(sys.argv)>1:
        img=cv2.imread(sys.argv[1],cv2.IMREAD_GRAYSCALE)
        print(img)
        # b=img[:, :, 0]
        # g=img[:, :, 1]
        # r=img[:, :, 2]
        # cv2.imshow('img', img)
        # cv2.imshow('B',b)
        # cv2.imshow('G', g)
        # cv2.imshow('R', r)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
    else:
        print('can not open the image')