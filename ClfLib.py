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
    if opts.weight_type in [WeightType.SCORE, WeightType.HALFSCORE]:
        for clf, X_val, y_val in zip(clfs, dataset.validation_sets_X, dataset.validation_sets_y):
            scores.append(clf.score(X_val, y_val))
    if opts.weight_type == WeightType.SCORE:
        weights = scores
    elif opts.weight_type == WeightType.HALFSCORE:
        weights[:] = [2 * (i - .5) for i in scores]
    return weights


def select(clfs: [], weights: [], opts: Opts):
    selected_clfs, selected_weights = [], []
    tups = []
    for clf, weight in zip(clfs, weights):
        tups.append((weight, clf))
    tups.sort(key = lambda pair: pair[0])
    for i in range(1, opts.number_of_selected_clfs + 1):
        selected_clfs.append(tups[-i][1])
        selected_weights.append(tups[-i][0])
    return selected_clfs, selected_weights
