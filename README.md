# Fixed Size Face Detection System 

![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue.svg)
![OpenCV Version](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-important.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen.svg)


A real-time Face Detection application built using Python and OpenCV. The application layout automatically centers on your desktop screen and allows you to dynamically import any video format via a built-in file explorer dialog.

---

## Features 

- **Dynamic Video Import:** Integrated with `tkinter` file dialog to easily select and browse video files from your computer.
- **Auto-Centering Window:** Dynamically calculates your monitor's resolution and positions the OpenCV window perfectly in the center of the screen (adjusting automatically for the OS taskbar and title bars).
- **Enhanced Visuals:** Real-time face tracking using Haar Cascade with highly visible, bold bounding boxes.
- **Responsive Windowing:** Uses standard 720p scaling so high-resolution videos (like 1080p or 4K) fit nicely inside the fixed frame.

---

## Prerequisites 

Before running the project, make sure you have Python installed and the required dependencies.

### Dependencies

Install the required OpenCV package via pip:

```bash
pip install opencv-python
```

> **Note:** `tkinter`, `sys`, and `os` come built-in with standard Python installations.

---

## How to Run 🏃‍♂️

1. Clone or download this repository.
2. Open your terminal or command prompt inside the project folder.
3. Run the Python script:

```bash
python main.py
```

> Replace `main.py` with the actual name of your script file if it's different.

---

## How It Works 

1. **File Selection:** Upon launching, a File Explorer window will pop up prompting you to choose a video file (`.mp4`, `.avi`, `.mkv`, etc.).
2. **Screen Calibration:** The app checks your screen size using Tkinter and launches the video preview box exactly in the middle.
3. **Face Detection:** The app utilizes OpenCV's pre-trained `haarcascade_frontalface_default.xml` to convert frames to grayscale and scan for faces.
4. **Controls:** Press the `q` key on your keyboard at any time to exit the video playback cleanly.

---

## License 

This project is open-source and available under the [MIT License](LICENSE).