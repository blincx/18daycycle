import unittest
from datetime import datetime, timedelta
from confirm18 import simple_loop_method, simple_subtraction_method, clean_today, date_string_from_obj, datetime_obj_from_string



"""TESTDATA
February 12th - March 19th
37 days - should end up on 1st day
"""

# dateformat : %Y-%m-%d


class TestSimpleLoopMethod(unittest.TestCase):
    """
    Test the simple loop method
    """
    def test_simple_loop_method(self):
        # Feb 12 - March 19th - 37 days - should end up on 1st day
        feb122020 = datetime_obj_from_string("2020-02-12")
        mar192020 = datetime_obj_from_string("2020-03-19")
        print("studying diff days")
        diff01 = (mar192020 - feb122020).days
        print(f"{diff01} days difference")
        print("yet if you count from calendar, it is 37 days.")
        print("This was the cause of the original error")
        cycle_test = simple_loop_method(feb122020,mar192020)
        self.assertEqual(cycle_test[1],1,"simple_loop_method not working")
        
        # Jan 1st - March 1st - end up on 7th day
        jan012020 = datetime_obj_from_string("2020-01-01")
        mar012020 = datetime_obj_from_string("2020-03-01") 
        cycle_test02 = simple_loop_method(jan012020,mar012020)
        self.assertEqual(cycle_test02[1],7,"simple_loop_method not working")

        # Jan1st - Jan1st - end up on 1st day
        cycle_test03 = simple_loop_method(jan012020,jan012020)
        self.assertEqual(cycle_test03[1],1,"simple_loop_method not working")



    def test_simple_subtraction_method(self):
        # Feb 12 - March 19th - 37 days - should end up on 1st day
        feb122020 = datetime_obj_from_string("2020-02-12")
        mar192020 = datetime_obj_from_string("2020-03-19")
        cycle_test = simple_subtraction_method(feb122020,mar192020)
        self.assertEqual(cycle_test,1,"simple_subtraction_method not working")
        
        # Jan 1st - March 1st - end up on 7th day
        jan012020 = datetime_obj_from_string("2020-01-01")
        mar012020 = datetime_obj_from_string("2020-03-01") 
        cycle_test02 = simple_subtraction_method(jan012020,mar012020)
        self.assertEqual(cycle_test02,7,"simple_subtraction_method not working")

        # Jan1st - Jan1st - end up on 1st day
        cycle_test03 = simple_subtraction_method(jan012020,jan012020)
        self.assertEqual(cycle_test03,1,"simple_subtraction_method not working")

    

    # def test ten_forward

if __name__ == '__main__':
    unittest.main()
