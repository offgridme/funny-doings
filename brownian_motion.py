import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

num_particles = 100
num_frames = 200
trail_length = 30  # number of previous positions to keep for each particle

fig, ax = plt.subplots()

# initialize particle positions
positions = np.random.uniform(-10, 10, (num_particles, 2))

# initialize history of positions
history = np.zeros((num_particles, trail_length, 2))
history[:, 0] = positions

# initialize particles and paths
particles, = ax.plot([], [], 'o', ms=6, color='lightgreen')
paths = [ax.plot([], [], 'b-', lw=1)[0] for _ in range(num_particles)]

# axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# animation update function
def update(frame, positions, history):
    # update particle positions
    positions += np.random.normal(0, 0.1, (num_particles, 2))
    
    # update history
    history[:, 1:] = history[:, :-1]  # Shift previous positions
    history[:, 0] = positions
    
    # update particle positions in the plot
    particles.set_data(positions[:, 0], positions[:, 1])
    
    # update path lines
    for i, path in enumerate(paths):
        path.set_data(history[i, :, 0], history[i, :, 1])
    
    return [particles] + paths

# create animation
ani = animation.FuncAnimation(fig, update, fargs=(positions, history), frames=num_frames, interval=50, blit=True)

# show the animation
plt.show()