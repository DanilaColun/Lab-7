#  Колун Дэнилэ, 373732 (Вар 2)

import random
from time import perf_counter
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import PillowWriter




#  Первая задача
def comparison():
    ar1 = []
    ar2 = []
    res = []

    for i in range(1000000):
        ar1.append(random.randint(1, 1000000))
        ar2.append(random.randint(1, 1000000))

    begin = perf_counter()

    for i in range(1000000):
        res.append(ar1[i] * ar2[i])
    try1 = perf_counter() - begin
    print("На перемножение стандартных списков ушло ", try1, "секунд.")

    ar1 = np.random.randint(0, 1000000, 1000000)
    ar2 = np.random.randint(0, 1000000, 1000000)

    try2 = perf_counter()
    res = np.multiply(ar1, ar2)
    print("На перемножение массивов NumPy ушло ", perf_counter() - try2, "секунд.")


#  Второе задание
def histogram():
    ar = np.genfromtxt('data2.csv', delimiter=',')
    ar = ar[1:]

    ph = np.array(ar[:, 0], float)
    ph = ph[~np.isnan(ph)]

    figure = plt.figure(figsize=(8, 6))
    axis = figure.add_subplot()

    axis.hist(ph, 50, (0, 14), color='lightblue', ec='blue')
    axis.grid()

    plt.title('гистограмма')
    plt.xlabel('ph')
    plt.ylabel('частота')

    plt.show()

    figure = plt.figure(figsize=(8, 6))

    axis = figure.add_subplot()
    axis.hist(ph, 50, (0, 14), color='lightgreen', ec='green', density=True)

    axis.grid()
    plt.title('нормализованная гистограмма')
    plt.xlabel('ph')
    plt.ylabel('частота')

    plt.show()

    print('среднеквадратичное отклонение: ', np.std(ph))


#  Третье задание
def plotin3d():
    np.random.seed(40)

    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)*np.cos(x)
    z = np.sin(x)*np.cos(x)

    figure = plt.figure()
    axis = figure.add_subplot(111, projection='3d')
    axis.plot(x, y, z, marker='*', c='blue')

    plt.title('график 3D')
    plt.show()


#  Доп. задание
def animation():
    figure = plt.figure()
    l, = plt.plot([], [], 'k')

    plt.xlim(-7, 7)
    plt.ylim(-2, 2)

    write = PillowWriter(fps=30)

    xc = []
    yc = []

    with write.saving(figure, "animation.gif", 100):
        for x in np.linspace(-7, 7, 100):
            xc.append(x)
            yc.append(np.sin(x))

            l.set_data(xc, yc)
            write.grab_frame()


if __name__ == '__main__':
    comparison()
    histogram()
    plotin3d()
    animation()