class Dataset:
    """Class with sets to train, validate and test classifiers

    """

    def __init__(self,
                 training_sets_X: [],
                 training_sets_y: [],
                 validation_sets_X: [],
                 validation_sets_y: [],
                 testing_sets_X: [],
                 testing_sets_y: []):
        self.training_sets_X = training_sets_X
        self.training_sets_y = training_sets_y
        self.validation_sets_X = validation_sets_X
        self.validation_sets_y = validation_sets_y
        self.testing_sets_X = testing_sets_X
        self.testing_sets_y = testing_sets_y
