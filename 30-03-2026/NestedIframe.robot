*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}  https://demo.automationtesting.in/Frames.html
*** Test Cases ***
Handling single Iframe
    Open Browser  ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=(//a[@class="analystic"])[2]
    Select Frame    xpath=//iframe[@src="MultipleFrames.html"]
#    Page Should Contain    Nested iFrames
    Select Frame    xpath=//iframe[@src="SingleFrame.html"]
#    Page Should Contain    iFrame Demo
    Input Text    xpath=//input[@type="text"]    Abhisar
    Unselect Frame
    Sleep    3s
    Unselect Frame
    Close Browser