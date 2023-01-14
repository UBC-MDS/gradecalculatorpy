import pandas as pd

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
    
    Examples
    --------
    >>> predict_final('DSCI100.csv', 90.0)
    """