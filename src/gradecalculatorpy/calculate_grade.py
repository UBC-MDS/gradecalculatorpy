import pandas as pd

def calculate_grade(input_file):
    """
    When all course components are presented, calculate the course overall grade based on information provided.
    
    Parameters
    ----------
    input_file : str
        Path to read the saved .csv file as a string.
    
    Returns
    -------
    course_grade : double
        The course overall grade once all course components present.
    
    Examples
    --------
    >>> calculate_grade('DSCI524.csv')
    """