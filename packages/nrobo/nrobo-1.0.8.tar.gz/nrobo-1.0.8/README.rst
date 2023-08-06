.. Project Description
.. Project Log

.. Logo

.. image:: https://www.namasteydigitalindia.com/connect/wp-content/uploads/2023/01/nRobo-Logo.png
    :alt: nRobo image not found!
    :height: 200
    :width: 400
    :align: center

=======================================
nRoBo (An Automated Testing Framework )
=======================================
For Web Developers, QAs and Testers
-----------------------------------

.. Project Status

--------------
Project Status
--------------
**Active**

.. Pre-requisites

Pre-requisites
--------------

Following pre-requisites needs to be installed in order to run `nRoBo` framework.

1. `Install Java 8  or higher <https://www.java.com/en/download/manual.jsp>`_
    - Run the following command to check if java is installed
    - `java --version`
2. `Install allure command line tool_ <https://docs.qameta.io/allure/#_installing_a_commandline>`_
    - Run the following command to check if allure cli is installed
    - `allure --version`

.. Installation

------------
Installation
------------


1. Install **virtualenv** package
    - `pip3 install virtualenv`
2. Create virtual environment - venv
    - `virtualenv venv`
3. Activate virtual environment
    - source venv/bin/activate
4. Install `numpy` package
    - `pip3 install numpy`
5. Install `nrobo`
    - pip3 install nrobo==1.0.8
6. Install framework
    - nrobo -i
7. Run tests (Typical)
    - nrobo -a google -l http://google.com -u panchdev -p Passw0rd -n 4 -r 0 -b chrome -t allure

.. Command Line Switches

---------------------
Command Line Switches
---------------------

**Usage**

`nrobo -a <app-name> -l <app-url> -u <username> -p <password> [-n <N>] [-r <N>] [-b <browser>] [-t allure]`

-a <app-name>          [Mandatory] Name of the Application Under Test (AUT). nRobo then uses it as test report title.
-l <app-url>           [Mandatory] Url of the AUT. nRobo runs the tests on this url.
-u <username>          [Mandatory] Username for log in into AUT.
-p <password>          [Mandatory] Password for log in into AUT.
-n <number>            [Optional] nRobo will run <number> of tests in parallel if <number> is greater than 0.
                       Or it will run test in sequence one after another if -n switch is missing.
-r <number>            [Optional] nRobo will rerun failed tests for <number> of times
                       Or it will rerun failed tests atleast 1 times if -r switch is missing.
-b <browser>           [Optional] nRobo will run the test on the <browser>.
                       Or it will run the test in the chrome browser by default if -b switch is missing.
                       Following is a list of possible <browser> options:
                       [chrome, safari, edge, ie, firefox, opera]
                       Make sure that the browser is installed already on your system where the tests are going to run.
-t <report-type>       [Optional] nRobo has capability to generate two types of reports; one is, pytest-html-report, and another is next generation, allure report.
                       Following are the possible options for <report-type>:
                       [html, allure]
                       If missing, nRobo will generate only simple-html report under test-output directory.
                       If specified "allure", it will also generate allure report under allure-test directory.
-k <key>               [Optional] nRobo will run only those tests which includes the <key> in their names.
                       For example; cosider there are three tests as mentioned below:
                       [test_cal_add, test_cal_sub, test_exercise_one]
                       And if tests run with *-k cal* then nRobo will only run tests with key, cal,
                       Hence, it will run the following tests only: test_cal_add, test_cal_sub and will skip the test, test_exercise_one.
-m <marker>            [Optional] nRobo will run the tests that are marked with the marker <marker>.
                       Following are the possible valid markers:

                       ::

                        sanity, regression, ui, api and nogui

                        Example of test methods annonated with markers;

                        @pytest.mark.regression
                        def test_cal_add():
                            # test code line 1
                            # test code line 2

                        @pytest.mark.sanity
                        def test_cal_sub():
                            # test code line 1
                            # test code line 2
                            ...

                        @pytest.mark.ui
                        def test_ui_check():
                            # test code line 1
                            # test code line 2


Example:

`nrobo -a google -l http://google.com -u panchdev -p Passw0rd -n 4 -r 0 -b chrome -t allure`


.. Video Tutorials

------
Videos
------

.. image:: https://www.namasteydigitalindia.com/connect/wp-content/uploads/2023/01/nRobo-Logo.png
    :alt: nRobo image not found!
    :height: 200
    :width: 400
    :target: https://youtu.be/rNBWA6jxV1s

.. Features

--------
Features
--------

1. Rich Browser Support
    - Chrome
    - Edge
    - Safari
    - Firefox
    - Opera
    - IE
2. Rich Platform Support
3. SeleniumWebdriver Wrapper Methods
4. Loaded with Standard TestBase class
5. Loaded with Standard Test Setup & Tear Down methods
6. Support for Test Parallelization (Inherited from pytest)
7. Support for Test Parameterization (Inherited from pytest)
8. Support for screenshot capture (Inherited from pytest)
9. Support for capturing test steps in reports (Python Standard Logging)
10. Next Generation Test Reports (Backed by Allure Reports and pytest-html-reports)
11. Support for cool tweaks in the standard reports (nRobo framework)
12. Command line Support to trigger tests (nRobo framework)
13. Easy Setup (nRobo framework)
14. Well Defined Directory Structure (nRobo framework)
15. Support for distributing tests accross multiple remote machines **In Progress** (pytest)
16. Support grouping of tests. Supported groups are sanity, ui, regression, nogui, api at present. (pytest)


.. Tools and Libraries

-----------------
Tools & Libraries
-----------------

1. Next Generation **Test Automation Framework** for **Python**
    1. `Pytest <https://docs.pytest.org/en/7.2.x/contents.html>`_
    2. pytest plugins
        1. pytest plugin that provides access to test session metadata
            - `pytest-metadata <https://pypi.org/project/pytest-metadata/>`_
        2. The pytest-xdist plugin extends pytest with new test execution modes, the most used being distributing tests across multiple CPUs to speed up test execution.
            - `pytest-xdist <https://pypi.org/project/pytest-xdist/>`_
        3. Run tests in isolated forked subprocesses
            - `pytest-forked <https://pypi.org/project/pytest-forked/>`_
        4. pytest plugin to re-run tests to eliminate flaky failures
            - `pytest-rerunfailures <https://pypi.org/project/pytest-rerunfailures/>`_
        5. Virtual Python Environment builder
            - `virtualenv <https://pypi.org/project/virtualenv/>`_
        6. YAML parser and emitter for Python
            - `PyYAML <https://pypi.org/project/PyYAML/>`_
        7. library with cross-python path, ini-parsing, io, code, log facilities
            - `py <https://pypi.org/project/py/>`_
2. Browser Automation Tool (Open Source)
    - `Selenium Webdriver 4 <https://www.selenium.dev/documentation/webdriver/getting_started/upgrade_to_selenium_4/>`_
3. **Auto Webdriver Manager**
    - `Webdriver Manager <https://pypi.org/project/webdriver-manager/>`_
4. Next Generation **Test Report Framework**
    - `Allure Framework <https://docs.qameta.io/allure/>`_
5. Simple HTML Test Report Plugin
    - `pytest-html <https://pypi.org/project/pytest-html/>`_