from gradecalculatorpy.predict_final import predict_final
import pandas as pd
import math

def test_predict_final():
    """ Create units test for the predict_final function."""
    
    # Set values
    input_file_all = '/tests/dsci524_grades_all.csv'
    input_file_miss = '/tests/dsci524_grades_miss.csv'
    input_file_miss_two = '/tests/dsci524_grades_miss_two.csv'
    goal = 80.0
    
    # Call the target fucntion and check if all assignment weight sum up to 100%
    error_msg1 = "Your total assignment weights are not summing up to 100%! Please update all your assignments."
    assert predict_final(input_file_all, goal) != error_msg1
    
    # Call the target fucntion and check if final score (in the last row) is NA
    error_msg2 = "Your final assignment score is already updated. Please directly use calculate_grade()."
    assert predict_final(input_file_all, goal) == error_msg2
    assert predict_final(input_file_miss, goal) != error_msg2
    
    # Call the target fucntion and check if there if more than one NA value in the 'Grades (%)' column
    error_msg3 = "Please update all your assignment scores except the final."
    assert predict_final(input_file_miss_two, goal) == error_msg3
    assert predict_final(input_file_miss, goal) != error_msg3
    
    # Check the values calculated for the target fucntion
    assert predict_final(input_file_miss, goal) == 79.0
    