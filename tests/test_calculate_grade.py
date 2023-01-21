from gradecalculatorpy.calculate_grade import calculate_grade
import pandas as pd
import math

def test_calculate_grade():
    file_path = 'tests/dsci524_grades_all.csv'
    # file_path = 'dsci524_grades_format.csv'
    # file_path = 'dsci524_grades_miss.csv'

    course_df = pd.read_csv(file_path, index_col=0)
    columns = course_df.columns

    # Make sure generated .csv file has 3 columns
    assert len(columns) == 3, "Course information table column number is not 3"

    # Make sure generated .csv has first column as "Components"
    assert columns[0] == "Components", "Course information table first column is not 'Components'"

    # Make sure generated .csv has second column as "Weights (%)"
    assert columns[1] == "Weights (%)", "Course information table second column is not 'Weights (%)'"

    # Make sure generated .csv has third column as "Grades (%)"
    assert columns[2] == "Grades (%)", "Course information table third column is not 'Grades (%)'"

    # Make sure generated .csv has second column "Weights (%)" add up to 100%
    assert sum(course_df["Weights (%)"]) == 100, "Course component weights not adding up to 100%"

    for i, row in course_df.iterrows():
        comp = row['Components']
        grade = row['Grades (%)'] 
        # Make sure generated .csv has third column "Grades (%)" with all non-Nan values (no missing values)
        assert not math.isnan(grade), "Course component grades have missing values for " + comp

        # Make sure generated .csv has third column "Grades (%)" with all values with 2 decimals
        assert len(str(grade).rsplit('.')[-1]) == 2, "Course component grades should be with 2 decimals for " + comp

    print("All test passed!")