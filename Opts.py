from ClfType import ClfType


class Opts:
    """Class carrying integration options

    """

    def __init__(self,
                 type_of_clf: ClfType,
                 number_of_subspaces: int,
                 ):
        self.type_of_clf = type_of_clf
        self.number_of_subspaces = number_of_subspaces
