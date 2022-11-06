!/usr/bin/env bash




echo "Finished setting up the virtual environment!"

pip install opencv-python
pip install mediapipe
pip install pyautogui

echo "Finished downloading packages! Now running!"


python3 main_cv.py 
python3 main.py 
