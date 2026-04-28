*** Settings ***
Library           RequestsLibrary
Library           Collections
Library           JSONLibrary

*** Variables ***
${BASE_URL}   https://petstore.swagger.io/v2

*** Test Cases ***
Add a pet
    [Documentation]    Add a new pet to the store
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=   Load Json From File   ${CURDIR}/../data/add_pet.json
    ${response}=    POST On Session    petapi  /pet     json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Update Pet
    [Documentation]    Update an existing pet in the store
    Create Session    petapi    ${BASE_URL}  verify=True
    ${payload}=   Load Json From File   ${CURDIR}/../data/update_pet.json
    ${response}=    PUT On Session    petapi  /pet     json=${payload}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Get Pet by ID
    [Documentation]    Get a pet by its ID
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=    GET On Session    petapi  /pet/1
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Get Pet by status
    [Documentation]    Get pets by their status
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=    GET On Session    petapi    /pet/findByStatus    params={'status': 'available'}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    {body}
    Log To Console    ${response.json()}
Upload an Image
    [Documentation]    Upload an image for a pet
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=    Create Dictionary    additionalMetadata=Bantu's Img
    ${file_path}=    Set Variable    ${CURDIR}/../data/img.png
    ${files}=     Create Dictionary    file    ${file_path}
    ${response}=    POST On Session    petapi    /pet/55/uploadImage    data=${form_data}    files=${files}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Update a pet in the store with form data
    [Documentation]    Update a pet in the store with form data
    Create Session    petapi    ${BASE_URL}  verify=True
    ${form_data}=    Create Dictionary    name=HarshPart2    status=sold
    ${response}=    POST On Session    petapi  /pet/1     data=${form_data}
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}
Delete a pet
    [Documentation]    Delete a pet from the store
    Create Session    petapi    ${BASE_URL}  verify=True
    ${response}=    DELETE On Session    petapi  /pet/1
    Should Be Equal As Integers    ${response.status_code}    200
    Log To Console    ${response.json()}