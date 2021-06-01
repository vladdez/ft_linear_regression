import csv
import sys

class LR:
    def get_data(arg):

        milages = []
        prices = []
        print(arg)
        with open(arg, 'r') as file:
            data = csv.DictReader(file, delimiter = ',')
            for row in data:
                milages.append(row['km'])
                prices.append(row['price'])
        return milages, prices
    
    def EstimatePrice(milage, th0, th1)
        price = th0 + th1*milage
        return price

    def GD(milages, prices, learningRate, iterations):
        th0 = 0.0
        th1 = 0.0
        length = len(prices)
        for i in range(0, iterations-1):
            tmp0 = 0
            tmp1 = 0
            for milage, price in zip(milage, prices)
                tmp0 += (EstimatePrice(milage, th0, th1) - price)
                tmp1 += learningRate * (EstimatePrice(milage, th0, th1) - price) * milage
            th0 = learningRate * (tmp0 / length)
            th1 = learningRate * (tmp1 / length)
            
            