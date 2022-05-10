# USRL Colormaps

This repository contains a collection of colormaps that are useful when generating figures for
presentations or papers by the Uppsala Social Robotics Lab. Available colormaps:

## Installation

```
pip install usrl-colormaps
```


## Usage

```python
import matplotlib.pyplot as plt
import usrl-colormaps  # colormaps are registered automatically

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
ax.bar(langs,students)
plt.show()

```
