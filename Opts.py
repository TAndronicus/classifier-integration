from ClfType import ClfType
from WeightType import WeightType


class Opts:
    """Class carrying integration options

    """

    def __init__(self,
                 type_of_clf: ClfType,
                 number_of_subspaces: int,
                 weight_type: WeightType,
                 number_of_selected_clfs: int,
                 ):
        self.type_of_clf = type_of_clf
        self.number_of_subspaces = number_of_subspaces
        self.weight_type = weight_type
        self.number_of_selected_clfs = number_of_selected_clfs
