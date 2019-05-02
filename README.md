# easyTello
[![version info](https://img.shields.io/pypi/pyversions/easytello.svg)](https://pypi.org/project/easytello/)
[![liscence](https://img.shields.io/pypi/l/easytello.svg)](https://pypi.org/project/easytello/)
[![PyPI](https://img.shields.io/pypi/v/easytello.svg)](https://pypi.org/project/easytello/)

**easyTello** is a Python library created to provide users with a simple way to interface and send commands to the DJI Tello drone, as well as to simply and easily teach students how to control the drone using Python 3. All the commands outlined in the DJI Tello SDK 1.3.0.0 are present in this library.

## Installation
To install the library, simply run:
```
pip install easytello
```
or to install from cloned source:
```
$ git clone https://github.com/Virodroid/easyTello.git
$ cd easyTello
$ python setup.py install
```
**Note:** easyTello requires OpenCV-Python. If you don't have it installed, simply run:
```
pip install opencv-python
```
For more information on OpenCV-Python click [here](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html).

## Examples
Creating a drone object in Python:
```python
from easytello import tello

my_drone = tello.Tello()
```
Programming the drone to takeoff, fly in a square and then land:
```python
my_drone.takeoff()

for i in range(4):
	my_drone.forward(100)
	my_drone.cw(90)
	
my_drone.land()
```
Toggling state of video stream:
```python
# Turning on stream
my_drone.streamon()
# Turning off stream
my_drone.streamoff()
```
