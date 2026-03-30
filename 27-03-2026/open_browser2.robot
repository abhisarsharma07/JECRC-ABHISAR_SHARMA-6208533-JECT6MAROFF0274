*** Settings ***
Documentation  Opening of Browser
Library  SeleniumLibrary

*** Test Cases ***
Opening Chrome headless Browser
    [Documentation]  chrome headless browser
    [Tags]  smoke
    ## Used for grouping the test cases
    ## Single space complete name
    ## double space different group names
    Open Browser  https://www.cricbuzz.com/  chrome
    Maximize Browser Window

    Log  navigated to cricbuzz
    Log To Console    navigated to crickbuzz
    Sleep    3s


#    robot -d reports -i "smoke" open_browser2.robot