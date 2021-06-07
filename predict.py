from tools import LiRe
import os


if __name__ == '__main__':
    LR = LiRe()
    milage = ""
    while (not milage.isnumeric() or milage == ""):
        milage = input("Enter a mileage: ")
        if (not milage.isnumeric()):
            print('Wrong input, please write a number')
    milage = int(milage)
    if os.path.exists('thetas.csv'):
        with open('thetas.csv', 'r') as file:
            data = list(map(float, file.read().split(" ")))
        price = LR.EstimatePrice(milage, data[0], data[1])
    else:
        print('Model is not trained yet. Please, train it.')
        price = LR.EstimatePrice(milage, 0, 0)
    print("Price: {:.2f}".format(price))

