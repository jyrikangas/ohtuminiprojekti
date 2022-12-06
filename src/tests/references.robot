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

References Page Exists
    Go to References Page
    References Page Should Be Open

Click References Link
    Click Link  Viitteet
    References Page Should Be Open

Click Add Link
    Click Link  Uusi
    Add References Page Should Be Open

Click Remove Reference
    Go To References Page
    Click Link  Poista viite
    References Page Should Be Open

Add References
    Go To Add References Page
    Set Author  J.R.R Tolkien
    Set Title  The Hobbit
    Set Year  2011
    Set Publisher  Harpercollins
    Submit Credentials
    References Page Should Be Open

*** Keywords ***

Submit Credentials
    Click Button  Lisää

Set Author
    [Arguments]  ${author}
    Input Text  author  ${author}

Set Title
    [Arguments]  ${title}
    Input Text  title  ${title}

Set Year
    [Arguments]  ${year}
    Input Text  year  ${year}

Set Publisher
    [Arguments]  ${publisher}
    Input Text  publisher  ${publisher}