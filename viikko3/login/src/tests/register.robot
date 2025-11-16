*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Go To Register Page
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  pe
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Click Button  Register
    Register Should Fail With Message  Username should be atleast three characters

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  janne
    Set Password  janne1
    Set Password Confirmation  janne1
    Click Button  Register
    Register Should Fail With Message  Password should be atleast eight characters

Register With Valid Username And Invalid Password
    Go To Register Page
    Set Username  lauri
    Set Password  laurilauri
    Set Password Confirmation  laurilauri
    Click Button  Register
    Register Should Fail With Message  Password can not contain only letters

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  pertti
    Set Password  pertti123
    Set Password Confirmation  pertti213
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Go To Register Page
    Set Username  pekka
    Set Password  pekka555
    Set Password Confirmation  pekka555
    Click Button  Register
    Go To Register Page
    Set Username  pekka
    Set Password  pekka555
    Set Password Confirmation  pekka555
    Click Button  Register
    Register Should Fail With Message  Username already in use

*** Keywords ***

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page