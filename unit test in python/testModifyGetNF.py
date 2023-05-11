import unittest

# import our function
from ourModifyFunction import GetNameFamily



# Test Class
class TestMyfunction(unittest.TestCase):
    def test_name_fmily(self):                                           #  unit test -----> 1
        FunctionOutput =  GetNameFamily('Xirano' , 'taj')                # Call our function for check
        self.assertEqual(FunctionOutput, 'Xirano taj' )                  # check output of function

    def test_name_fmily_middle(self):                                    # unit test -----> 2
        FunctionOutput =  GetNameFamily('Xirano' ,'Senior', 'taj')       # Call our function for check
        self.assertEqual(FunctionOutput, 'Xirano taj Senior' )           # check output of function



# run this modual
if __name__ == "__main__":
    unittest.main()
