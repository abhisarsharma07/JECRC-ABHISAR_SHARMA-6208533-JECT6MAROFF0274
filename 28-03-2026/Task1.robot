*** Settings ***
Documentation  Handling Colors Dropdown
Library  SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handling Colors
    [Documentation]     chrome Navigating to url
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Scroll Element Into View    xpath=//label[text()="Sorted List:"]
    Page Should Contain List    id=colors
    ${options}=  Get List Items    id=colors
    Log To Console    ${options}
    Select From List By Label    id=colors  Blue  Yellow


    ${select_option}=   Get Selected List Label    id=colors
    Log To Console    ${select_option}
    Sleep    2s
    Close Browser

    