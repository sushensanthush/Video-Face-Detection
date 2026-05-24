import cv2
import sys
import os
import tkinter as tk
from tkinter import filedialog

def get_video_path():
    root = tk.Tk()
    root.withdraw() 
    
    print("Please select a video file...")

    file_path = filedialog.askopenfilename(
        title="Select a Video File",
        filetypes=[("Video Files", "*.mp4 *.avi *.mkv *.mov"), ("All Files", "*.*")]
    )
    return file_path

def main():
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(cascade_path)

    if face_cascade.empty():
        print(f"Error: Could not load cascade classifier from {cascade_path}")
        sys.exit(1)

    video_path = get_video_path()

    if not video_path:
        print("No file selected. Exiting...")
        sys.exit(0)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video file: {video_path}")
        sys.exit(1)

    window_name = 'Fixed Size Face Detection'
    
    win_width = 1280
    win_height = 720
    
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(window_name, win_width, win_height)
    
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    
 
    x_pos = int((screen_width / 2) - (win_width / 2))
    

    y_pos = int((screen_height / 2) - (win_height / 2)) - 45
    
   
    if y_pos < 0: 
        y_pos = 0
        
    cv2.moveWindow(window_name, x_pos, y_pos)
  
  
    print(f"Playing: {os.path.basename(video_path)} in a centered window.")

    while True:
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            print("Window closed by user.")
            break

        ret, frame = cap.read()

        if not ret:
            print("End of video file reached.")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray_frame,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)

        cv2.imshow(window_name, frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("'q' key pressed. Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Video stream closed cleanly.")

if __name__ == "__main__":
    main()