import pandas as pd
import os
import math

def predict_final(input_file, goal):
    """
    Calculate what grade the student needs to have for the final assignment in order to reach the goal for overall grade
    and return the scores needed for the final assignment.
    
    Parameters
    ----------
    input_file : str
        Path to read the saved .csv file as a string.
    goal : double
        The goal for your overall grade for this course.
    
    Returns
    -------
    final_score_needed : double
        The scores needed for the final assignment. 
        Otherwise return warning message.
    
    Examples
    --------
    >>> predict_final('/DSCI100.csv', 90.0)
    """
    # Set up input path
    cwd = os.getcwd()
    path = cwd + input_file
    course_info = pd.read_csv(path, index_col=0)
    
    # Check if all assignment weight sum up to 100%
    if course_info['Weights (%)'].sum() != 100:
        error_msg = "Your total assignment weights are not summing up to 100%! Please update all your assignments."
        final_score_needed = error_msg
        return final_score_needed
    
    


    

    
  