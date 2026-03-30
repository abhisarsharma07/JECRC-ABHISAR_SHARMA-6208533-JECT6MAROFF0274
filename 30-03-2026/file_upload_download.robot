*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem
*** Variables ***
${url}      https://the-internet.herokuapp.com/
${check_downloaded}     C:\\Users\\abhis\\Downloads\\file.txt

*** Test Cases ***
File Upload
    Open Browser    ${url}   chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/upload"]
    Sleep   2s
    ${path}    Normalize Path    ${CURDIR}/sample.txt
    Choose File    id=file-upload    ${path}
    Sleep   2s
    Click Button    id=file-submit
    Sleep    2s
    Close Browser

File Download
    Open Browser  ${url}    chrome
    Maximize Browser Window
    Click Element    xpath=//a[@href="/download"]
    Sleep    2s
    Click Element    xpath=//a[@href="download/file.txt"]
    Wait Until Created    ${check_downloaded}     timeout=10s
    File Should Exist    ${check_downloaded}
    Log To Console    it downloaded successfully
    Sleep    5s
    Close Browser