***Settings***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To References Page

*** Test Cases *** 
Add References With Tag
    Go To Add References Page
    Set Author  J.R.R Tolkien
    Set Title  The Hobbit
    Set Year  2011
    Set Publisher  Harpercollins
    Set Tag  Fiction
    Set ID  Lotr
    Submit Data
    References Page Should Be Open
    Page Should Contain  Viite lisätty onnistuneesti

Add References Without Tag
    Go To Add References Page
    Set Author  Robert Martin
    Set Title  Clean Code: A Handbook of Agile Software Craftsmanship 
    Set Year  2008
    Set Publisher  Prentice Hall
    Set ID  CleanCode
    Submit Data
    References Page Should Be Open
    Page Should Contain  Viite lisätty onnistuneesti

Show References With All Tags
    Select All Tags
    Page Should Contain  The Hobbit
    Page Should Contain  Clean Code: A Handbook of Agile Software Craftsmanship
Show References With Tag Fiction
    Select Tag Fiction
    Page Should Contain  The Hobbit
    Page Should Not Contain  Clean Code: A Handbook of Agile Software Craftsmanship

***Keywords***

Select All Tags
    Select From List By Value  name:tag  all
    Click Button  näytä vain viitteet joilla on tämä tagi

Select Tag Fiction
    Select From List By Value  name:tag  Fiction
    Click Button  näytä vain viitteet joilla on tämä tagi

Submit Data
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

Set Tag
    [Arguments]  ${tag}
    Input Text  tag  ${tag}

Set ID
    [Arguments]  ${refname}
    Input Text  refname  ${refname}