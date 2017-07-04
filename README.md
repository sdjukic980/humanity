# humanity
Test Automation Task for Humanity

This project goal is to demonstrate test automation for humanity.com scheduling system

It is based on Python 3.5, using Selenium, pytest and unittest2 modules
In order to install dependant libraries, in cmd window navigate to the project folder and run
"pip install -r requirements.txt"

As of now, it only supports Chrome browser (chromedriver.exe Selenium driver for Python is also included in this repository), 
but it is meant to be modular, and other drivers can be added easily.

Chrome Version 59 or newer is required.

In order to be able to run tests, in file Framework/basictestcase.py change the line :
        self.driver = webdriver.Chrome("C:\\humanity\\chromedriver.exe")
with propper path of the chromedriver.exe file.

To run tests, from cmd window, navigate to the project folder and run:
"py.test --html=report.html" 
which will run the test suite and generate the html report


