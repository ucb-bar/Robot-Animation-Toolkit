
import numpy as np
import matplotlib.pyplot as plt

data = np.load("data.npy")

print(data.shape)


# plot 3d trajectory
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# color according to z value
z = data[:, 3]
c = z / z.max()
ax.scatter(data[:, 1], data[:, 2], data[:, 3], c=c)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

# set scale
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(0, 2)

plt.show()


