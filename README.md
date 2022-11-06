**To run**

Create, set up new virtual environment
```
python -m venv myvenv #create environment
```

- Install external modules 
1. [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html): enables image processing and webcam access
2. [mediapipe](https://google.github.io/mediapipe/solutions/solutions.html): enables pose estimation model
3. [pyautogui](https://pyautogui.readthedocs.io/en/latest/): allows python script to access and controll keyboard
```
pip install opencv-python
pip install mediapipe
pip install pyautogui
```

- Make sure tikinter is downloaded from cmu_112_graphics.py on the [CMU 15-112 website](https://www.cs.cmu.edu/~112/notes/notes-graphics.html#installingModules).
```
import sys
print(f"sudo '{sys.executable}' -m pip install pillow")
print(f"sudo '{sys.executable}' -m pip install requests")
```

- Run run.py
```
python3 run.py
```


