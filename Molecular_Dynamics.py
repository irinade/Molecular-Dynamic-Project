import matplotlib.pyplot as plt

m = 5
k = 4
n_steps = 100
dt = 0.1


def force_pot_energy(pos):
    F = -k * pos
    Epot = 0.5 * k * pos**2
    return(F, Epot)


def kinetic_energy(v):
    Ecin = 0.5 * m * v**2
    return(Ecin)


def step_forward(pos, v, F):
    v = v + 0.5 * dt * F / m
    pos = pos + v * dt
    F, Epot = force_pot_energy(pos)
    v = v + 0.5 * dt * F / m
    Ecin = kinetic_energy(v)
    return(pos, v, F, Ecin, Epot)


def output(t, pos, Ecin, Epot):
    traj_t.append(t)
    traj_pos.append(pos)
    traj_Ecin.append(Ecin)
    traj_Epot.append(Epot)
    Em = Epot + Ecin
    traj_Em.append(Em)
    return()


traj_t = []
traj_pos = []
traj_Ecin = []
traj_Epot = []
traj_Em = []

pos = 7
v = 8
F, Epot = force_pot_energy(pos)


for i in range(n_steps):
    t = i * dt
    pos, v, F, Ecin, Epot = step_forward(pos, v, F)
    output(t, pos, Ecin, Epot)


x = [i for i in range(n_steps)]

plt.plot(x, traj_pos)
plt.xlabel('x : time')
plt.ylabel('y : Position')
plt.title('Fonction : Position over time')
plt.show()

plt.plot(x, traj_Em, label="Mechanical energy")
plt.plot(x, traj_Epot, label="Potential enegy")
plt.plot(x, traj_Ecin, label="Kinetic energy")
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=2, mode="expand", borderaxespad=0.)
plt.subplots_adjust(top=0.8)
plt.xlabel('x : time')
plt.ylabel('y : Energy')
plt.title('Fonction : Energy over time', y=1.15)
plt.show()
