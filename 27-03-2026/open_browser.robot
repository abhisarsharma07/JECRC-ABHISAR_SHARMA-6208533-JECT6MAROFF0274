## four sections settings, variables, test cases, keywords
## Use two Spaces and Tabs , we dont use single space much
*** Settings ***  # it is one of the section
## It have import files / Resource
## It is an Description in Documentation Keyword
Documentation  Opening Of Browsers
Library  SeleniumLibrary
*** Variables ***
## Declare all variables we are going to use
*** Test Cases ***
## Here we write test scripts
## This become one test case
Opening Chrome Browser
    [Documentation]  Chrome browser naigating to  https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  chrome
     ## It takes Two arguments 1.Crickbuzz link and 2.Browser... Name
     Maximize Browser Window

     Log    navigated to cricbuzz
     Log To Console    navigated to cricbuzz
     Sleep    5s
     ## You can also write 5 minutes 30s
#     Close Window
#     Close Browser
#     Close All Browsers
Opening Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser    https://www.cricbuzz.com/  edge
    Maximize Browser Window

    Log To Console    Navigated to cricbuzz
    Close Window
    Sleep    3s
    
Opening Firefox Browser
    [Documentation]  Firefox browser navigating to https://www.cricbuzz.com/
    Open Browser    https://www.cricbuzz.com/  firefox
    Maximize Browser Window

    Log To Console    Navigated to cricbuzz
#    Close Window
    Sleep    3s
    Close All Browsers
Opening Chrome headless Browser
    [Documentation]  Chrome browser naigating to  https://www.cricbuzz.com/
    Open Browser  https://www.cricbuzz.com/  headlesschrome
     ## It takes Two arguments 1.Crickbuzz link and 2.Browser... Name
     Maximize Browser Window

     Log    navigated to cricbuzz
     Log To Console    navigated to cricbuzz
     Sleep    5s
     ## You can also write 5 minutes 30s
#     Close Window
     Close Browser
#     Close All Browsers


*** Keywords ***
## User defined Keywords are written in this section



