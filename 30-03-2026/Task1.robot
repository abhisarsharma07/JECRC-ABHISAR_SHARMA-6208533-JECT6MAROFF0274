*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Window Handling
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Mouse Over    xpath=//button[@id="PopUp"]
    Sleep    2s
    Click Element    xpath=//button[@id="PopUp"]

    @{windows}  Get Window Handles
    Switch Window    NEW
    @{title}    Get Window Titles
    Log To Console    ${title}[2]
    Sleep    2s
#    Page Should Contain    New Window

    Switch Window    ${windows}[0]
    Log To Console   ${title}[0]
    Sleep    2s

    Close Browser
