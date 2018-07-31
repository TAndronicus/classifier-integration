from ClfType import ClfType
from WeightType import WeightType
from Opts import Opts
from ReadLib import read_2018_07_02
from ClfLib import train, validate, select

opts = Opts(ClfType.LINEAR, 5, WeightType.SCORE, 5)  # Step 0
dataset = read_2018_07_02()  # Step 1, 2
clfs = train(dataset, opts)  # Step 3
weights = validate(clfs, dataset, opts)  # Step4
selected_clfs, selected_weights = select(clfs, weights, opts)
for w in selected_weights:
    print(w)