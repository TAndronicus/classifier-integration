from Dataset import Dataset
from Opts import Opts
from ClfType import ClfType
from WeightType import WeightType
from sklearn.svm import LinearSVC
from sklearn.neighbors import NearestCentroid


def train(dataset: Dataset, opts: Opts):
    clfs = prepare_clfs(opts.type_of_clf, len(dataset.training_sets_X))
    trained_clfs = train_clfs(clfs, dataset)
    return trained_clfs


def prepare_clfs(type_of_clf: ClfType, number_of_clfs: int):
    clfs = []
    if ClfType.LINEAR == type_of_clf:
        for _ in range(number_of_clfs):
            clfs.append(LinearSVC(max_iter = 1e6, tol = 1e-10, C = 100))
    elif ClfType.MEAN == type_of_clf:
        for _ in range(number_of_clfs):
            clfs.append(NearestCentroid())
    return clfs


def train_clfs(clfs: [], dataset: Dataset):
    trained_clfs = []
    for clf, X, y in zip(clfs, dataset.training_sets_X, dataset.training_sets_y):
        clf.fit(X, y)
        trained_clfs.append(clf)
    return trained_clfs

def validate(clfs: [], dataset: Dataset, opts: Opts):
    scores, weights = [], []
    if opts.weight_type in [WeightType.SCORE]:
        for clf, X_val, y_val in zip(clfs, dataset.validation_sets_X, dataset.validation_sets_y):
            scores.append(clf.score(X_val, y_val))
    if opts.weight_type == WeightType.SCORE:
        weights = scores
    return weights