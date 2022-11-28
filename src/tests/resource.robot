*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${REFERENCES URL}  http://${SERVER}/viitteet
${ADD URL}  http://${SERVER}/lisaa_viite

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Home Page Should Be Open
    Title Should Be  Ohtuminiprojekti

Go To Home Page
    Go To  ${HOME URL}