*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Click Button  Register
    Title Should Be  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set Password Confirmation  testi123
    Click Button  Register
    Register Should Fail With Message  Username is too short

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  testi
    Set Password Confirmation  testi
    Click Button  Register
    Register Should Fail With Message  Password is too short

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  testitesti
    Set Password Confirmation  testitesti
    Click Button  Register
    Register Should Fail With Message  Password cannot be only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi456
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  testi123
    Set Password Confirmation  testi123
    Click Button  Register
    Register Should Fail With Message  Username is already in use

Login After Successful Registration
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi123
    Click Button  Register
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  testi
    Set Password  testi123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Set Username  testi
    Set Password  testi123
    Set Password Confirmation  testi456
    Click Button  Register
    Register Should Fail With Message  Passwords do not match
    Click Link  Login
    Set Username  testi
    Set Password  testi123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}