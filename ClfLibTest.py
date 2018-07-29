import unittest
import random
import ClfLib
from ClfType import ClfType


class ClfLibTest(unittest.TestCase):

    def test_should_prepare_right_amount_of_clfs(self):
        # given
        number_of_clfs = random.randint(1, 10000)
        # when
        clfs = ClfLib.prepare_clfs(ClfType.LINEAR, number_of_clfs)
        # then
        self.assertEqual(number_of_clfs, len(clfs))
