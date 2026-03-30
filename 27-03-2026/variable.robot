*** Settings ***
Documentation  Opening of Browser
Library  SeleniumLibrary
*** Variables ***
#scalar variables
${url}  https://www.crickbuzz.com/
#list variables
@{bikes}  ktm  kwaski  honda  pulsar
## dict variables
&{cars}  nissan=gtr  honda=civic  bmw=m5


*** Test Cases ***
Opening Edge Browser
    [Documentation]  Edge browser navigating to https://www.cricbuzz.com/
    Open Browser    ${url}
    Maximize Browser Window

    Log To Console    Navigated to cricbuzz
    Log To Console    ${bikes}[1]
    Log To Console    ${cars.nissan}
    Close Window
    Sleep    3s