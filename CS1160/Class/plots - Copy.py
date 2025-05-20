<<<<<<< HEAD
from matplotlib import pyplot as plt
import numpy as np

def main():
    x = np.arange(0.0, 10.0, 0.01)
    y = x * np.sin(2 * np.pi * x)

    plt.title("Growing Sine Wave")
    plt.xlabel("Time (years)")
    plt.ylabel("Bank Account Balance")
    plt.plot(x, y)
    plt.grid(True, color='b',linestyle='dashed')
    plt.show()

if __name__ == "__main__":
    main()
=======
from matplotlib import pyplot as plt
import numpy as np

def main():
    x = np.arange(0.0, 10.0, 0.01)
    y = x * np.sin(2 * np.pi * x)

    plt.title("Growing Sine Wave")
    plt.xlabel("Time (years)")
    plt.ylabel("Bank Account Balance")
    plt.plot(x, y)
    plt.grid(True, color='b',linestyle='dashed')
    plt.show()

if __name__ == "__main__":
    main()
>>>>>>> 0bbfd1684901d0e83ffcbb9b34c1d45876c2c81b
