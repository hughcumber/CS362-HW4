import unittest
import avg
import math
from numpy import mean

class TestAvg(unittest.TestCase):
    def test_avg(self):

        inputs = [2, 4, -2, 3, 5];
        self.assertEqual(avg.avg(inputs), mean(inputs));

    def test_avg1(self):

        inputs = [];
        self.assertEqual(avg.avg(inputs), mean(inputs));

    def test_avg2(self):

        inputs = ["asd", "1234"];
        self.assertEqual(avg.avg(inputs), mean(inputs));




if __name__ == '__main__':
    unittest.main(verbosity=3);
