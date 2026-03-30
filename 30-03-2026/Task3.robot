*** Settings ***
Library     SeleniumLibrary
*** Variables ***
${url}      https://www.amazon.in/
*** Test Cases ***
Task 3
    Open Browser    ${url}      chrome
    Maximize Browser Window
    Sleep    3s
    Click Element    xpath=//a[text()=" Electronics "]
    Sleep    2s
    Execute Javascript  window.scrollTo(0,500)
    Sleep    1s
    Click Element    xpath=(//span[text()="boAt"])[2]
    Execute JavaScript    window.scrollBy(0,500)
    Sleep    2s
    ${product_name}=    Get Text    (//div[@data-cy="title-recipe"])[5]/descendant::span
    Log To Console    Product_Name: ${product_name}
    Click Element    xpath=(//div[@data-cy="title-recipe"])[5]/descendant::span
    Sleep    3s
    Switch Window    NEW
    Sleep    3s
    ${Page-Title}=    Get Text    id=productTitle
    Page Should Contain    ${Page-Title}
    ${Actual_price}=  Get Text  xpath=(//span[@class="a-price a-text-price apex-basisprice-value"]/span)[2]
    ${discount}=  Get Text  xpath=//span[@class="apex-savings-container"]/following-sibling::span/span[2]/span[2]
    ${discount%}=  Get Text  xpath=//span[@class="apex-savings-container"]/span
    Log To Console    Actual Price: ${Actual_price}
    Log To Console    Discount: ${discount}
    Log To Console    Discount %: ${discount%}
    Scroll Element Into View    id=add-to-cart-button
    Click Button    id=add-to-cart-button
    Sleep    3s
    Click Element    id=nav-cart
    Sleep    3s
    Page Should Contain     ${Page-Title}
    Close Browser




