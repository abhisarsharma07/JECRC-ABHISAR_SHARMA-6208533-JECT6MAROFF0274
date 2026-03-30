*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://inc.in
*** Test Cases ***
handling js
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    3s
    Execute Javascript  window.scrollTo(0,document.body.scrollHeights)
    Sleep    3s
    Close Browser