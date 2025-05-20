<<<<<<< HEAD
from matplotlib import pyplot as plt
import numpy as np

def main():
    x0 = np.arange(0.0, 2.0, 0.05)
    y0 = np.sin(2 * np.pi * x0)

    #x1 = np.arange(0.0, 2.0, 0.01)
    y1 = 0.5 * np.tan(4 * np.pi * x0)

    #x = np.array([0, 1, 2, 3, 4, 5])
    #y = np.array([100, 200, 50, 250, 275, -3])

    plt.style.use('Solarize_Light2')

    plt.plot(x0, y0)#, color='black', marker='o', linestyle='dashed', linewidth=3)#, label='sin(2*pi*x)')
    plt.plot(x0, y1)#, label='this is a tangent function')
    plt.legend(['sin(2*pi*x)', 'this is a tangent function'])
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    main()
=======
from matplotlib import pyplot as plt
import numpy as np

def main():
    x0 = np.arange(0.0, 2.0, 0.05)
    y0 = np.sin(2 * np.pi * x0)

    #x1 = np.arange(0.0, 2.0, 0.01)
    y1 = 0.5 * np.tan(4 * np.pi * x0)

    #x = np.array([0, 1, 2, 3, 4, 5])
    #y = np.array([100, 200, 50, 250, 275, -3])

    plt.style.use('Solarize_Light2')

    plt.plot(x0, y0)#, color='black', marker='o', linestyle='dashed', linewidth=3)#, label='sin(2*pi*x)')
    plt.plot(x0, y1)#, label='this is a tangent function')
    plt.legend(['sin(2*pi*x)', 'this is a tangent function'])
    plt.grid(True)
    
    plt.show()

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
