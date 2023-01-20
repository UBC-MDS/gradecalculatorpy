from gradecalculatorpy.construct_course import construct_course
import pandas as pd

def test_construct_course():
    file_path = '../src/gradecalculatorpy/dsci524.csv'

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

    # Make sure generated .csv has third column "Grades (%)" with all NANs
    assert course_df["Grades (%)"].isnull().all(), "Course component grades should all be NAN for now"

    print("All test passed!")