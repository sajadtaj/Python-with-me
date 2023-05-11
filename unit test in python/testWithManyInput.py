import unittest

# import our function
from ourFuction import GetNameFamily


# input for test
# try check all aspect of input
inputFun = [
            ("Ali","Ahmadi",'Ali Ahmadi')
            ,("Darab","firoozi",'Darab firoozi')
            ,("ahmad","asadi","kangarshahi",'ahmad asadi kangarshahi')
            ,("firooz"," nadery",'firooz nadery')
            ,("sara",'sara')
            ,("ali ","goodarzi",'ali goodarzi')
            ]


# Test Class
class TestMyfunction(unittest.TestCase):
    def test_name_fmily(self):         
        for i in inputFun:                                               # unit test
            with self.subTest(i=i):
                FunctionOutput =  GetNameFamily(i[0] , i[1])             # Call our function for check
                self.assertEqual(FunctionOutput, i[2] )                  # check output of function



# run this modual
if __name__ == "__main__":
    unittest.main()
