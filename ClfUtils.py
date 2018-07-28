def initialize_list_of_lists(number_of_elements: int = 1):
    """Creates list of independent lists
    :param number_of_elements: int
    :return: []
    """
    return [[] for _ in range(number_of_elements)]
