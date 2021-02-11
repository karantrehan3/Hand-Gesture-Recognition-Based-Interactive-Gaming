# Hand Gesture Recognition Based Interactive Gaming using Python

![Hand.png](https://repository-images.githubusercontent.com/320211558/8e815900-6cc9-11eb-8fe5-684a95443875?raw=true)

Wouldn’t it be fun, if you could use your hand to control the car in a game? So, here we have proposed a computer vision concept to control the game with hand gestures by mapping gestures to the W, A, S, D keyboard keys.

Tested on games like: Need for Speed, GTA 5, Blur, Spiderman.


## Video Tutorial
{% include googleDrivePlayer.html %}

The code is well documented at each step and is easy to understand and implement.


## Libraries Used
* imutils     `pip install imutils`
* numpy       `pip install numpy`
* opencv2     `pip install opencv-python`
* time 
* sklearn     `pip install scikit-learn`
* ctypes      


## Scripts
**The repository includes three main python(.py) files particularly:**
1.	`control.py` (Code to map gesture- slope and distance with the keys)
2.	`directkeys.py` (Code to interact with the keyboard keys. Reference: [Simulate Python keypresses for controlling a game](https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game%20#%20))
3.	`final.py` (Main code to take input i.e. hand gesture using background subtraction method, find end points of hand and henceforth distance and slope using convex hull)


## How to run the code?
**Steps to run the code:**
1.	Download the Scripts Directory and unzip all .py scripts in same folder. 
2.  We have used PyCharm Community Edition to run the codes. You may use other python editors which support the above libraries.
3.	Run the `final.py` file.
4.	Adjust the HSV values using the track bar, so that only your hand is visible.
5.	After that, set the Start track bar to 1. 
Hurray!! You can now use your hand to control the game. 


### Note:
1.	Please use plain white or black background for more accuracy. Also, make sure the room is well lit.
2.	You are free to modify the slope and distance values depending upon the gesture you make in `control.py`.
3.	You can map more gestures with keys. Refer to the [link](https://gist.github.com/dretax/fe37b8baf55bc30e9d63)

Hope you Like it! Thanks.
