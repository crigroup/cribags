#!/usr/bin/env python
import os, yaml
import rospy, rosbag
from pprint import pprint

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
    baginfo = []
    for line in str(bag).splitlines():
      found = False
      for field in delfields:
        if field in line:
          found = True
          break
      for field in boldfields:
        if field in line:
          line = line.replace(field, '**'+field[:-1]+'**:')
      if not found:
        baginfo.append(line)
    # Append bag info
    with open(readme, 'a+') as f:
      f.write('\n\n### %s' % filename)
      for line in baginfo:
        if '**' in line:
          f.write('\n- %s' % line)
        else:
          f.write('\n\n %s' % line)
