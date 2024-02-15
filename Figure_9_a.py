import pandas as pd
from pylab import *
import numpy as np
import matplotlib.pyplot as plt

dicts = { "Direct Load Averaging (Method 1)": [25314.95961,	63420.37799,	71030.82335],

             "Flow Weighted Average (Method 2)": [59726.43966,	63538.7656,	67351.09153],
             
             "International Joint Commission method (Method 3)": [59740.5101,	63553.73415,	67366.95819],
             
             "Regression (Method 4)": [57907.37096, 63634.47359, 69361.57621],
             
             "Regression and variance adjustment (Method 5)": [54990.12792, 63942.00921, 72893.8905],
                 
            "Regression with stratification (Method 6)": [114967.4205,	134938.287,	154909.1534]}

CARDS = pd.DataFrame(dicts)

fig = plt.figure()
fig.suptitle('Strata 1', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
ax.boxplot(CARDS[['Direct Load Averaging (Method 1)', 
                  'Flow Weighted Average (Method 2)',
                  'International Joint Commission method (Method 3)',
                  'Regression (Method 4)',
                  'Regression and variance adjustment (Method 5)', 
                  'Regression with stratification (Method 6)']],
           
                   labels = ['Method 1', 'Method 2', 'Method 3', 'Method 4', 
                             'Method 5', 'Method 6'],
                   patch_artist = True, boxprops = dict(facecolor = "lightblue"))

# ax.set_title('axes title')
ax.set_xlabel('Flux estimation methods')
ax.set_ylabel('Total nitrogen Load (kg/day)')

plt.show()

image_format = 'png' # e.g .png, .svg, etc.
image_name = 'Strata 1.png'

fig.savefig(image_name, format=image_format, dpi=1200)


