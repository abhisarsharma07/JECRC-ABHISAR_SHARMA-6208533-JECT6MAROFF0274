*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/home/jaipur
*** Test Cases ***
Screenshots
    Set Screenshot Directory    ${CURDIR}/Screenshots
#    Set Screenshot Directory    ${CURDIR}/../Screenshots
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    5s
    Capture Page Screenshot    fullpage.png
    Sleep    3s
    Capture Element Screenshot    xpath=//img[@alt="Dhurandhar The Revenge"]    file2.jpg
    Sleep    3s
    Close Browser




