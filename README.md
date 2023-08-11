# Stori-QA-Automation-Challenge

## 🏗️ Project Structure <a name="project-structure"></a>

The project is organized into the following key components:
- `pages`: Screens organized as separate class files.
- `step_defs`: Step definition files for each test
- `reports`: Contains the reports that are generated after every execution.

## 📁 Folder Structure <a name="folder-structure"></a>

    .
    ├── reports                        # Reports files
    │   └── reports.html               # Automated tests report on HTML format
    │   └── report.xml                 # Automated tests report on XML format
    ├── tests                          # Automated tests
    │   ├── step_defs                  # Step definition modules for each test case
    │   └── conftest.py                # Shared configuration and functions for tests
    ├── pytest.ini                     # Command line options
    └── README.md

**Setup Process**

1 - In order to install the project properly, make sure to install all the dependencies by running the following command in the terminal:

    pip install -r requirements.txt 


**EXECUTION**

You can execute all the tests cases by running the following command :

    pytest

If you want to execute one test case you can do it by executing the following command:

    pytest test_name.py

**Also, all tests were parameterized to support execution in different browsers, Examples below:**

    pytest --browser chrome test_name.py *default* 

    pytest --browser firefox test_name.py 

    pytest --browser edge test_name.py


**Notes** : After the execution, pytest will generate two reports, one on HTML format and other on XML with the tests results.

**Thanks!**

**Nicolás Pavoni**

 