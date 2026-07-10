import cv2
import numpy as np
from pyzbar import pyzbar
import sys

def scan_qr():
    cap=cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return
    print("press 'q' to quit, 's' to save result")
    while True:
        ret, frame=cap.read()
        if not ret:
            break
        decoded_objects=pyzbar.decode(frame)
        for obj in decoded_objects:
            qr_data=obj.data.decode("utf-8")
            pts=obj.polygon
            if len(pts)>4:
                hull=cv2.convexHull(np.array([pt for pt in pts], dtype=np.float32))
                pts=hull
            n=len(pts)
            for i in range(n):
                cv2.line(frame, (pts[i].x, pts[i].y), (pts[(i+1) % n].x, pts[(i+1) % n].y), (0, 255, 0), 2)
                cv2.putText(frame,qr_data, (pts[0].x, pts[0].y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0),2)
                print(f"OR code:,{qr_data}")
        cv2.imshow("qr scanner",frame)
        key=cv2.waitKey(1)&0xFF
        if key==ord('q'):
            break
        elif key==ord('s')and decoded_objects:
            with open("qr_result.txt", "w")as f:
                f.write(decoded_objects[0].data.dacoded('utf-8'))
            print("saved to qr_result.txt")

    cap.release()
    cv2.destroyAllWindows()

if __name__ =="__main__":
    scan_qr()
