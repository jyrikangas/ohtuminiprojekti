*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To References Page


*** Test Cases *** 
Can Sort By Year
    Select Sort By Year Ascending
    Submit Sort
    References Should Be Sorted By Year Ascending

Can Sort By Added Date
    Select Sort By Added Date Descending
    Submit Sort
    References Should Be Sorted By Added Date Descending

***Keywords***

Submit Sort
    Click Button  järjestä

References Should Be Sorted By Year Ascending
    Location Should Contain  ?sort=year_asc

Select Sort By Year Ascending
    Select From List By Value  name:sort  year_asc

Select Sort By Added Date Descending
    Select From List By Value  name:sort  added_desc

References Should Be Sorted By Added Date Descending
    Location Should Contain  ?sort=added_desc
