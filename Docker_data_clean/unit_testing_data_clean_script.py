import unittest
from Docker_data_clean.data_clean_script import *
import random


class TestDataCleaning(unittest.TestCase):

    def setUp(self):
        # NS: Create a test dataframe with some checkout dates, return dates and ANSWER col. 
        self.raw_data = pd.DataFrame({
            "Book checkout": pd.to_datetime(['2023-01-01', '2023-01-15', '2023-03-10']),
            "Book Returned": pd.to_datetime(['2023-01-10', '2023-02-20', '2023-03-25']),
            "answer": [9, 36, 15]
        })
   
        
    def test_daysOnLoan(self):
        # NS: Test if daysOnLoan function calculates the correct number of days by comparing to a known ANSWER column..
        
        def test(pos):
            self.assertEqual(test_data.loc[pos, "DaysOnLoan"], test_data.loc[pos, "answer"], 'Days on loan for this record should be: ' + str(test_data.loc[pos, "answer"]))
            
            # # Alternative way using entire column comparison, not quite working as there is a coimpriasion error
            # self.assertEqual(test_data["DaysOnLoan"], test_data["answer"])

        test_data = self.raw_data.copy()
        daysOnLoan(test_data, "Book Returned", "Book checkout", "DaysOnLoan")

        
        for i in range(len(test_data)-1):
            test(i)
            print("Tested record:", i)

if __name__ == '__main__':
    unittest.main()