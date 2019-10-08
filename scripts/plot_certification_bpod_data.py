import ibllib.plots.pprint as pprint
import numpy as np
import matplotlib.pyplot as plt
import ibllib.io.raw_data_loaders as raw

spath = r'C:\iblrig_data\Subjects\_iblrig_calibration\2019-10-08\002'
fpath = spath + r'\raw_behavior_data\_iblrig_.taskData.raw.json'
data = raw.load_data(spath)
data = {'Bpod start timestamp': 0.334712, 'Trial start timestamp': 0.334712, 'Trial end timestamp': 119.658717, 'States timestamps': {'trial_start': [(0, 0.0001)], 'listen': [(0.0001, 111.54180000000001)]}, 'Events timestamps': {'Tup': [0.0001], 'BNC1High': [7.8509, 7.9339, 8.3339, 9.9504, 11.567, 11.9669, 12.0668, 14.1333, 14.1661, 14.2665, 14.6667, 16.2998, 17.8829, 18.2829, 18.3827, 19.4159, 22.4322, 25.448700000000002, 28.465, 31.4812, 34.5144, 37.5306, 40.5305, 42.6129, 42.7135, 43.113600000000005, 44.7132, 46.3299, 46.7299, 46.8296, 46.9132, 48.929, 49.029500000000006, 49.4296, 51.0461, 52.645900000000005, 53.0458, 53.1458, 54.195800000000006, 55.212, 55.245000000000005, 55.3457, 55.745400000000004, 57.362, 58.9619, 59.361900000000006, 59.461800000000004, 60.5118, 63.511500000000005, 66.4945, 69.4941, 72.4939, 72.5432, 72.6606, 73.04390000000001, 74.6769, 76.2602, 76.6769, 76.7765, 78.8264, 78.8592, 78.9598, 79.3598, 80.9925, 82.5926, 82.9929, 83.0926, 84.1256, 87.1421, 90.1419, 93.17500000000001, 96.19120000000001, 99.2077, 102.22370000000001, 105.2406, 107.3229, 107.42360000000001, 107.8236, 109.44000000000001, 111.0398, 111.4398, 111.5224], 'BNC1Low': [7.8695, 8.0699, 8.8698, 11.0196, 11.8359, 12.036200000000001, 12.085700000000001, 14.1521, 14.2025, 14.402600000000001, 15.2192, 17.3522, 18.1519, 18.352, 18.4017, 21.451900000000002, 24.4682, 27.4846, 30.5008, 33.534, 36.533500000000004, 39.549800000000005, 42.5996, 42.6495, 42.8495, 43.649300000000004, 45.7992, 46.5991, 46.7991, 46.848800000000004, 48.9155, 48.965500000000006, 49.165600000000005, 49.9656, 52.1152, 52.915, 53.115100000000005, 53.1646, 55.182300000000005, 55.2312, 55.281600000000005, 55.4816, 56.2815, 58.431400000000004, 59.2312, 59.431200000000004, 59.4808, 62.514100000000006, 65.4972, 68.49680000000001, 71.49640000000001, 72.52980000000001, 72.5798, 72.7797, 73.5963, 75.7461, 76.5459, 76.7461, 76.7955, 78.84530000000001, 78.89580000000001, 79.0958, 79.8956, 82.062, 82.8619, 83.06190000000001, 83.11160000000001, 86.16170000000001, 89.178, 92.1945, 95.2107, 98.227, 101.2433, 104.25970000000001, 107.3096, 107.35940000000001, 107.5596, 108.3592, 110.5091, 111.30900000000001, 111.509, 111.54180000000001]}}
ev = data['Events timestamps']
high = ev['BNC1High']
low = ev['BNC1Low']
bla = []
bla.extend(high)
bla.extend(low)
bla = sorted(bla)
plt.plot(bla, np.ones(len(bla)), '|')
plt.plot(high, np.ones(len(high)) + 0.01, '|')
plt.plot(low, np.ones(len(low)) - 0.01, '|')
plt.show()