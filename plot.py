import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
fig = plt.figure()

ax1 = fig.add_subplot(311)
import numpy as np
data = np.genfromtxt('output.csv', delimiter=',', skip_header=10,
                     skip_footer=10, names=['x', 'y'])
ax1.plot(data['x'], data['y'], color='r', label='tracking', marker='o')

#ax1.set_title("Ball trajectory")
ax1.invert_yaxis()
ax1.set_xlabel('pixel in x')
ax1.set_ylabel('pixel in y')


leg = ax1.legend()

plt.show()