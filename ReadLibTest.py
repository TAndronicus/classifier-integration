import unittest
import ReadLib
import numpy as np


class ReadLibTest(unittest.TestCase):

    def test_should_read_correct_data(self):
        # given
        filename = "test.xlsx"
        # when
        dataset = ReadLib.read_2018_07_02(filename = filename)
        X = np.array(dataset.training_sets_X)
        X_test = np.array(dataset.testing_sets_X)
        y = dataset.training_sets_y
        X_len = len([item for sublist in X for item in sublist])
        X_test_len = len([item for sublist in X_test for item in sublist])
        # then
        self.assertEqual(4, X_len)
        self.assertEqual(1, X_test_len)
        self.assertEqual(2, len(X[0]))
        self.assertEqual(1, y[0][0])
        self.assertEqual(0, y[0][1])
        self.assertEqual(5.5, X_test[0][0][6])
