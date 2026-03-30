*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://testautomationpractice.blogspot.com
*** Test Cases ***
Handling alerts(simple)
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2

    Click Button    //button[@onclick="myFunctionAlert()"]
    Handle Alert
    ${text}  Get Text    xpath=//p[@id="demo"]
    Log To Console    ${text}

    Sleep    5
    Close Browser
Confirmation
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2

    Click Button    xpath=//button[@onclick="myFunctionConfirm()"]


    Handle Alert  #action=DISMISS      #for cancelling
    Page Should Contain    OK!
    ${text}  Get Text    xpath=//p[@id="demo"]
    Log To Console    ${text}

    Sleep    5
    Close Browser

prompt
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2

    Click Button    xpath=//button[@onclick="myFunctionPrompt()"]

    Input Text Into Alert    AbABjjk    #action=DISMISS
    Page Should Contain    AbABjjk
    ${text}  Get Text    xpath=//p[@id="demo"]
    Log To Console  ${text}

    Sleep    2
    Close Browser