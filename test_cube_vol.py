import unittest
import cube_vol
import math


class TestCube(unittest.TestCase):
    def test_cube_vol(self):


        inputs = [2, 4, -2, "asd", math.sqrt(3)];

        for x in range(len(inputs)):
            self.assertEqual(cube_vol.cube_vol(inputs[x]), inputs[x]**3);



if __name__ == '__main__':
    unittest.main(verbosity=3);
