*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
Home Page Exists
    Home Page Should Be Open

Add References Page Exists
    Go To Add References Page
    Add References Page Should Be Open