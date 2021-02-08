import unittest
import concat

class TestAvg(unittest.TestCase):
    def test_avg(self):

        a = "2, 4, -2, 3, 5";
        b = 0;
        self.assertEqual(concat.concat(a, b), a + " " + b);

    def test_avg1(self):

        a = "Hugh"
        b = "MacWilliams"
        self.assertEqual(concat.concat(a, b), a + " " + b);

    def test_avg2(self):

        a = "asd"
        b = 2;
        self.assertEqual(concat.concat(a, b), a + " " + b);




if __name__ == '__main__':
    unittest.main(verbosity=3);
