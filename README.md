# gradecalculatorpy

This python package can primarily calculate grades for a course along with the capabilities to allow user customize their own course information with self-defined course componenet names, update grades for different course components, and even understand how well the Final exam has to be to pass the course or achieve a certain level of grade in this course.

## Functions

This package contains the following functions:

- `construct_course`: <br>Allow user to input course components' information (component name and coresponding weight) one by one.<br>Course component names accept any user self-defined course component name(s).<br>Save the course information as a .csv file to the specified file path.

- `update_grades`: <br>By loading a certain saved course information .csv file, allow user to update course component grade(s) <br> Then save the updated course information as a new .csv file to the specified file path.
- 
- `predict_final`: <br>Before the Final exam (for the secnario only the Final grade is missing), based on the provided other course component information, calculate how well the Final exam has to be in order to pass the course or achieve a certain level of grade in this course.
- 
- `calculate_grade`: <br>When all course components are presented, calculate the course overall grade based on information provided.

## Suitability within Python Ecosystem

This course grade calculator is unique as it provide an interactive way for user to input the course component information and update information as needed. With the `predict_final` function available, user can understand how well the Final exam has to be in order to pass the course or achieve a certain level of grade in this course, then adjust their Final review plan based on our calculation, to meet user's course expectation.

The package `predict_final` function does not take any users' previous study or course information into account to calculatoin of the desired Final performance, only based on the current course component information inputted/updated. 

There are othe course grade calculators in the Python ecosystem. Some of the examples can be found [here](https://pypi.org/project/grade/) and [here](https://pypi.org/project/grade-tracker/). While other packages focus on autograding without user interaction and they do not provide similar functions like `predict_final` function in this package.

## Installation

```bash
$ pip install gradecalculatorpy
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`gradecalculatorpy` was created by Chen Lin, Edward Yukun Zhang, Shirley Zhang. It is licensed under the terms of the MIT license.

## Credits

`gradecalculatorpy` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
