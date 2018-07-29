from ClfType import ClfType
from Opts import Opts
from ReadLib import read_2018_07_02
from ClfLib import train

opts = Opts(ClfType.LINEAR, 5)
dataset = read_2018_07_02()
clfs = train(dataset, opts)
for clf in clfs:
    print(clf.coef_)
