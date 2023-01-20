from construct_course import construct_course

def test_construct_course():
    construct_course.construct_course('dsci524', '../src/gradecalculatorpy')
    # Make sure generated .csv file has 3 columns

    # Make sure generated .csv has first column as "Components"

    # Make sure generated .csv has second column as "Weights (%)"

    # Make sure generated .csv has third column as "Grades (%)"

    # Make sure generated .csv has second column "Weights (%)" add up to 100%

    # Make sure generated .csv has third column "Grades (%)" with all NANs

    
