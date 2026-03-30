*** Settings ***
Documentation    handling checkboxes
Library    SeleniumLibrary
*** Variables ***
${url}  https://the-internet.herokuapp.com/
*** Test Cases ***
Handling Checkboxes
    How to Handle Checkboxes
*** Keywords ***
How to Handle Checkboxes
    [Documentation]    herokuapp checkboxes
    Open Browser    ${url} chrome
    Maximize Browser Window
    Sleep    2s
    Click Element    xpath=//a[text()="Checkboxes"]
    ## shift +f6 to rename all same names, hold ctrl to click on the functions
    Page Should Contain Checkbox    id=checkboxes
    Sleep    3s
    Select Checkbox    xpath=(//input[@type="checkbox"])[1]
    Sleep    3s
    Unselect Checkbox    xpath=(//input[@type="checkbox"])[2]
    Sleep    3s
    Close Browser