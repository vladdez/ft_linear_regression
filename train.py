from tools import LR
import sys


def main():
    learningRate = 0.5
    epochs = 500

    milages, prices = LR.get_data(sys.argv[1])
    #print(milages)
    LR.GD(milages, prices, learningRate, epochs)
    


if __name__ == '__main__':
    main()
