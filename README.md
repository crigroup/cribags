
# cribags
ROS bags used by the [Control Robotics Intelligence Group](http://www.ntu.edu.sg/home/cuong/) from the [Nanyang Technological University, Singapore](http://www.ntu.edu.sg/).

## Clone this repository
Go to your `git` directory and clone this repository:
```
$ cd ~/git
$ git clone https://github.com/crigroup/cribags.git -b hydro-devel
```

## Update the README
Right before pushing any changes to the repository, please run the provided python script:
```
$ cd ~/git/rosbags
$ python update_readme.py
```

## Bags Info


### 2015-12-31-11-15-32.bag

- **version**:     2.0
- **size**:        2.0 MB
- **messages**:    4302
- **duration**:    35.9 seconds

| Topic | msgs | Freq | Type |
| ----- | ---- | ---- | ---- |
| /optitrack/rigid_bodies | 4302 | 120.2 Hz | optitrack/RigidBodyArray |
