*** Settings ***
Documentation  Opening of Browser
Library  SeleniumLibrary
*** Variables ***
#scalar variables
${url}  https://testautomationpractice.blogspot.com/
#list variables
@{days}  Monday  Tuesday  Wednesay  Thursday  Friday  Saturday  Sunday
## dict variables
&{cars}  nissan=gtr  honda=civic  bmw=m5


*** Test Cases ***
Opening Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser    ${url}
    Maximize Browser Window

    Log To Console    Navigated to cricbuzz
    Click Element    xpath=//input[@value="male"]



    Close Window
    Sleep    3s