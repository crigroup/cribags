#!/usr/bin/env python
import os, yaml
import rospy, rosbag
from pprint import pprint
from rosbag.bag import _human_readable_frequency, _human_readable_size

header = """
# rosbags
ROS bags used by the [Control Robotics Intelligence Group](http://www.ntu.edu.sg/home/cuong/) from the [Nanyang Technological University, Singapore](http://www.ntu.edu.sg/).

## Clone this repository
Go to your `git` directory and clone this repository:
```
$ cd ~/git
$ git clone https://github.com/crigroup/rosbags.git -b hydro-devel
```

## Update the README
Right before pushing any changes to the repository, please run the provided python script:
```
$ cd ~/git/rosbags
$ python update_readme.py
```

## Bags Info
"""

if __name__ == '__main__':
  # Write the header
  datafolder = os.path.dirname(os.path.realpath(__file__))
  readme = os.path.join(datafolder, 'README.md')
  with open(readme, 'w') as f:
    f.write(header)
  delfields = ['compression:','end:','path:','start:']
  boldfields = ['version:','duration:','size:','messages:','types:','topics:']
  spaces='&nbsp;&nbsp;&nbsp;'
  # Get the metadata from all the bagfiles
  for filename in os.listdir(datafolder):
    if not filename.endswith('.bag'):
      continue
    bag = rosbag.Bag(filename)
    baginfo = yaml.load(bag._get_yaml_info())
    # Bag details
    version = '%d.%d' % (int(bag.version / 100), bag.version % 100)
    duration = baginfo['duration']
    size = _human_readable_size(bag.size)
    msgs = baginfo['messages']
    types = '\n'.join([field['type'] for field in baginfo['types']])
    #~ 606 msgs @ 348.1 Hz : sensor_msgs/JointState
    lines = []
    for v in baginfo['topics']:
      s = '| %s | %d | %s | %s |' % (v['topic'], v['messages'], _human_readable_frequency(v['frequency']), v['type'])
      lines.append(s)
    topics = '\n'.join(lines)
    # Append bag info
    with open(readme, 'a+') as f:
      f.write('\n\n### %s' % filename)
      data="""
- **version**:     %s
- **size**:        %s
- **messages**:    %d
- **duration**:    %.1f seconds

| Topic | msgs | Freq | Type |
| ----- | ---- | ---- | ---- |
%s
""" % (version, size, msgs, duration, topics)
      f.write('\n%s' % data)
