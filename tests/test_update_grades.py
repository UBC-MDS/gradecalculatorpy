from gradecalculatorpy.update_grades import update_assignment_grade
import pandas as pd


def test_update_grades_correctly():
    '''Test that updates the grade of component 'Midterm 2' in dummycourse.csv and checks if it was updated correctly'''
    
    # set values
    input_file_path = 'tests/dummycourse.csv'
    component = 'Midterm 2'
    expected = 92.3 

    # call function 
    update_assignment_grade(input_file_path, component, expected)

    # compare output with expected grade
    df = pd.read_csv(input_file_path, index_col=0)
    assert df.query('Components == @component')['Grades (%)'].to_list()[0] == expected, "Course component not updated correctly!"

     
def test_only_one_changed():
    '''Test that ensures only the one row that was specified was changed'''
    
    # set values 
    input_file_path = 'tests/dummycourse.csv'
    component = 'Assignment 3'
    updated_grade = 97 

    # get original grades list 
    df = pd.read_csv(input_file_path, index_col=0)
    og_grades_list = list(df['Grades (%)'])

    # update csv and get new list
    update_assignment_grade(input_file_path, component, updated_grade)
    df2 = pd.read_csv(input_file_path, index_col=0)
    df2_grades_list = list(df2['Grades (%)'])

    # get index of component 
    comp_index = df.query('Components == @component').index[0]

    # update original grades list with expected grade 
    og_grades_list[comp_index] = updated_grade 

    # compare the two lists 
    assert df2_grades_list == og_grades_list, 'Grade (%) column not correct!'
    
    
def test_df_shape():
    '''Test that ensures the shape of the dataframe is still the same after updating''' 
    
    # set values
    input_file_path = 'tests/dummycourse.csv'
    component = 'Final Exam'
    updated_grade = 99
    
    # read original dataframe size 
    df = pd.read_csv(input_file_path, index_col=0)

    # call function 
    update_assignment_grade(input_file_path, component, updated_grade)
    df2 = pd.read_csv(input_file_path, index_col=0)

    # compare new dataframe size 
    assert df.shape == df.shape, 'Updated dataframe has wrong size'