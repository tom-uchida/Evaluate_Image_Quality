import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

from matplotlib import cycler
colors = cycler('color', ['#EE6666', '#3388BB', '#9988DD', '#EECC55', '#88BB44', '#FFBBBB'])
plt.rc('axes', facecolor='#E6E6E6', edgecolor='none', axisbelow=True, grid=False, prop_cycle=colors)
plt.rc('grid', color='w', linestyle='solid')
plt.rc('patch', edgecolor='#E6E6E6')
plt.rc('lines', linewidth=2)

# Check arguments
import sys
args = sys.argv
if len(args) != 2:
    print("\nUSAGE   : $ python graph_NMSE.py [csv_file_path]")
    sys.exit()


# Read csv file
csv = pd.read_csv(args[1], header=None)

# Convert to numpy
LR_NMSE = csv.values
LR   = LR_NMSE[0:16,0]
NMSE = LR_NMSE[0:16,1]

# Create figure
# plt.plot(LR, NMSE, color='black')
c = plt.scatter(LR, NMSE, color='black')

plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["mathtext.rm"] = "Times New Roman"
plt.rcParams["font.size"] = 14
plt.xlabel('$L$', fontsize=14)
plt.ylabel('NMSE', fontsize=14) # Gray scale

plt.xticks([1, 50, 100, 150], fontsize=14)
# plt.yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=14)
plt.yticks([0, 0.05, 0.1, 0.15, 0.2], fontsize=14)

plt.grid()
plt.legend(fontsize=12)

plt.show()