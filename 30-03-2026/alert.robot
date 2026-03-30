*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Handling alerts(simple)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2

    Click Button    xpath=//button[@onclick="jsAlert()"]
    Handle Alert

    Sleep    5
    Close Browser

Confirmation
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2

    Click Button    xpath=//button[@onclick="jsConfirm()"]

    Handle Alert  action=DISMISS      #for cancelling

    Sleep    5
    Close Browser

prompt
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2

    Click Button    xpath=//button[@onclick="jsPrompt()"]

    Input Text Into Alert    AbAB    action=DISMISS

    Sleep    2
    Close Browser