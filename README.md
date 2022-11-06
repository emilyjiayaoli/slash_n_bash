**Set Up and Run Instructions (computer vision control enabled)**

Create, set up new virtual environment
```
python -m venv myvenv #create environment
```

- Install external modules 
1. [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html): enables image processing and webcam access
2. [mediapipe](https://google.github.io/mediapipe/solutions/solutions.html): enables pose estimation model
3. [pyautogui](https://pyautogui.readthedocs.io/en/latest/): allows python script to access and controll keyboard
4. [pygame](https://www.pygame.org/docs/ref/mixer.html)
```
pip install opencv-python
pip install mediapipe
pip install pyautogui
pip install pygame
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

**Set Up and Run Instructions (computer vision control disabled)**

```
pip install pygame
```
- Make sure tikinter is downloaded from cmu_112_graphics.py on the [CMU 15-112 website](https://www.cs.cmu.edu/~112/notes/notes-graphics.html#installingModules).
```
import sys
print(f"sudo '{sys.executable}' -m pip install pillow")
print(f"sudo '{sys.executable}' -m pip install requests")
```

**Citations**
Open source graphics:
[Player slash](https://pixabay.com/sound-effects/sword-and-shealt-27397/)
[Block hit](https://pixabay.com/sound-effects/swordbattle2-56044/)
[Game start sound](https://pixabay.com/sound-effects/medieval-bell-d3-90290/)
[Down](https://pixabay.com/sound-effects/swordraw-89023/)
Music:
[Background music](https://xdeviruchi.itch.io/8-bit-fantasy-adventure-music-pack/download/eyJleHBpcmVzIjoxNjY3NzA3NDQzLCJpZCI6OTc1Mzg1fQ%3d%3d.zhEQyz1dlhGEl4rhKlun9jrlJEA%3d)


