import cv2
import datetime

cap=cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,500)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,500)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        #txt='Width: '+str(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+'  Height: '+str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        txt=str(datetime.datetime.now())
        frame=cv2.putText(frame,txt,(50,50),font,1,(255,255,255),2,cv2.LINE_AA)
        
        out.write(frame)
        ##gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)
        
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break


    else:
        break



cap.release()
cv2.destroyAllWindows()
out.release()