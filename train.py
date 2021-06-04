from tools import LR
import sys


def main():
    learningRate = 0.5
    iterations = 500

    milages, prices = LR.get_data(sys.argv[1])
    LR.GD(milages, prices, learningRate, iterations)
    print(milages)


if __name__ == '__main__':
    main()
