from Dataset import Dataset
from Opts import Opts
from ClfType import ClfType
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
    iter = 1
    for clf, X, y in zip(clfs, dataset.training_sets_X, dataset.training_sets_y):
        print(iter)
        clf.fit(X, y)
        trained_clfs.append(clf)
        iter += 1
    return trained_clfs
