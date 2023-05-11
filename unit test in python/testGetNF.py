import unittest

# import our function
from ourFuction import GetNameFamily


# Test Class
class TestMyfunction(unittest.TestCase):
    def test_name_fmily(self):                                   # unit test
        FunctionOutput =  GetNameFamily('Xiorano' , 'taj')       # Call our function for check
        self.assertEqual(FunctionOutput, 'Xiorano taj' )         # check output of function


# Run this Modual
if __name__ == "__main__":
    unittest.main()

