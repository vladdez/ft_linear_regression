from tools import LiRe
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--learning_rate', default=0.5, type=float)
    parser.add_argument('--plot', default=0, type=float)
    parser.add_argument('--evolution', default=0, type=float)
    parser.add_argument('--gof', default=0, type=float)
    args = parser.parse_args()
    # print(args.__dict__)
    l_rate = args.__dict__['learning_rate']
    if l_rate > 1:
        l_rate = 0.5
        print('Warning! Too big learning rate. It was set to 0.5.')
    if l_rate < 0.000001:
        l_rate = 0.5
        print('Warning! Too small learning rate. It was set to 0.5.')
    epochs = 100
    LR = LiRe()
    LR.get_data()
    LR.GD(l_rate, epochs)

    if args.__dict__['gof'] == 1:
        LR.Goodness_of_Fit()
    if args.__dict__['plot'] == 1:
        LR.lr_plot()
    if args.__dict__['evolution'] == 1:
        LR.evolution_plot()


if __name__ == '__main__':
    main()
