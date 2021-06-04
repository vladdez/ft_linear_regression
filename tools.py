import csv
import sys
import math


class LR:
    def get_data(arg):
        milages = []
        prices = []
        print(arg)
        with open(arg, 'r') as file:
            data = csv.DictReader(file, delimiter=',')
            for row in data:
                milages.append(float(row['km']))
                prices.append(float(row['price']))
        return milages, prices

    def EstimatePrice(milage, th0, th1):
        h = th0 + th1 * milage
        #print (th0, "*", th1, "*", milage, '=', h)
        return h

    def GD(milages, prices, learningRate, epochs):
        th0 = 0.0
        th1 = 0.0
        h = 0.0
        length = len(prices)
        print(length)
        #for i in range(0, epochs - 1):
        for i in range(0, 10):
            tmp0 = 0.0
            tmp1 = 0.0
            # mean squared error
            for milage, price in zip(milages, prices):
                h = LR.EstimatePrice(milage, th0, th1)
                #print(tmp0, tmp1)
                error = h - price
                tmp0 += error
                tmp1 += error * milage
                #if (i == 30):
                   #print((tmp0), (tmp1), error, milage, h)
            # print(tmp0, tmp1, h, error, price)
            th0 -= learningRate * (tmp0 / length)
            th1 -= learningRate * (tmp1 / length)
            print(th0, th1)
            
