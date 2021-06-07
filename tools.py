import csv
import sys
import os
import math
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from matplotlib.widgets import Slider

class LiRe():
    def __init__(self):
        self.th0 = 0.0
        self.th1 = 0.0
        self.milages = []
        self.prices = []
        self.milages_n = []
        self.prices_n = []
        self.p_mean = 0
        self.p_std = 0
        self.evolution = [[0.0, 0.0]]

    def get_data(self):
        try:
            with open('data.csv', 'r') as file:
                if os.stat('data.csv').st_size != 0:
                    data = csv.DictReader(file, delimiter=',')
                    for row in data:
                        self.milages.append(float(row['km']))
                        self.prices.append(float(row['price']))
                else:
                    exit()
        except:
            print("You need nonempty and correct data.csv in your working directory")
            exit()


    def EstimatePrice(self, milage, th0, th1):
        return th0 + th1 * milage

    def GD(self, l_rate, epochs):
        # normalization of parameters
        m_mean = np.mean(self.milages)
        m_std = np.std(self.milages)
        self.p_mean = np.mean(self.prices)
        self.p_std = np.std(self.prices)
        self.milages_n = (self.milages - m_mean) / m_std
        self.prices_n = (self.prices - self.p_mean) / self.p_std
        length = len(self.prices)
        for i in range(0, epochs - 1):
            tmp0 = 0.0
            tmp1 = 0.0
            # mean squared error
            for milage, price in zip(self.milages_n, self.prices_n):
                h = LiRe.EstimatePrice(self, milage, self.th0, self.th1)
                error = h - price
                tmp0 += error
                tmp1 += error * milage
            self.th0 -= l_rate * (tmp0 / length)
            self.th1 -= l_rate * (tmp1 / length)
            if i % 10 == 0:
                a, b = LiRe.denormalization(self)
                self.evolution.append([a + b *100, a + b * 250000])
        self.th0, self.th1 = LiRe.denormalization(self)
        data = np.column_stack([self.th0, self.th1])
        print("{:.2f}, {:.2f}".format(self.th0, self.th1))
        np.savetxt('thetas.csv', data, fmt=['%f', '%f'])

    def denormalization(self):
        # denormalization of thetas through normalized h and x
        newprice0 = LiRe.EstimatePrice(self, self.milages_n[0], self.th0, self.th1) * self.p_std + self.p_mean
        newprice1 = LiRe.EstimatePrice(self, self.milages_n[1], self.th0, self.th1) * self.p_std + self.p_mean
        # theta1 was counted by formula of tangent of angle
        th1 = (newprice0 - newprice1) / (self.milages[0] - self.milages[1])
        th0 = newprice0 - th1 * self.milages[0]
        return th0, th1

    def lr_plot(self):
        fig, ax = plt.subplots()
        ax.scatter(self.milages, self.prices)
        fig.set_figwidth(8)  # ширина и
        fig.set_figheight(8)  # высота "Figure"
        plt.title('Predicted prices based on milages')
        plt.xlabel('Milages')
        plt.ylabel('Price')

        x1, y1 = [min(self.milages), max(self.milages)], \
                 [self.th0 + self.th1 * min(self.milages),
                  self.th0 + self.th1 * max(self.milages)]
        plt.plot(x1, y1, marker='o')
        plt.show()

    def evolution_plot(self):
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.scatter(self.milages, self.prices)
        fig.set_figwidth(8)  # ширина и
        fig.set_figheight(8)  # высота "Figure"
        plt.title('Evolutution of regression line during training')
        plt.xlabel('Milages')
        plt.ylabel('Price')
        ax_slider = plt.axes([0.15, 0.01, 0.71, 0.03])
        slider = Slider(ax_slider, 'Epoch', 0, len(self.evolution) - 1, valinit=0)
        #print(self.evolution)

        def update(val):
            line.set_data([0, 240000], self.evolution[int(val)])
            print(self.evolution[int(val)])
            plt.draw()
        slider.on_changed(update)
        line, = ax.plot([0, 240000], self.evolution[0], lw=2)
        #print(self.evolution)
        plt.show()

    def Goodness_of_Fit(self):
        h = 0.0
        SSres = 0.0
        x2 = 0.0
        for milage, price in zip(self.milages, self.prices):
            expected = LiRe.EstimatePrice(self, milage, self.th0, self.th1)
            SSres += (price - self.th0) ** 2
            h += (price - expected) ** 2
            x2 += h / expected
        mse = h / len(self.milages)
        rmse = sqrt(mse)
        r2 = 1 - mse/SSres
        print('Goodness of Fit: MSE = {:.2f}, RMSE = {:.2f}, r2 = {:.2f}, x2 = {:.2f}'.format(mse, rmse, r2, x2))



