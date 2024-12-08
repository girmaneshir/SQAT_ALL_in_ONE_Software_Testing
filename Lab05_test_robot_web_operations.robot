*** Settings ***
Library    SeleniumLibrary
Suite Setup    Open Browser    http://127.0.0.1:5000    chrome
Suite Teardown    Close Browser

*** Test Cases ***
Test Addition
    [Documentation]    Test the addition operation through the web interface
    Input Number    5    3
    Click Element    //button[text()='Add']
    Verify Result    Result: 8

Test Subtraction
    [Documentation]    Test the subtraction operation through the web interface
    Input Number    10    4
    Click Element    //button[text()='Subtract']
    Verify Result    Result: 6

Test Multiplication
    [Documentation]    Test the multiplication operation through the web interface
    Input Number    4    5
    Click Element    //button[text()='Multiply']
    Verify Result    Result: 20

Test Division
    [Documentation]    Test the division operation through the web interface
    Input Number    12    4
    Click Element    //button[text()='Divide']
    Verify Result    Result: 3

Test Division By Zero
    [Documentation]    Test division by zero handling through the web interface
    Input Number    5    0
    Click Element    //button[text()='Divide']
    Verify Result    Error: Division by zero is undefined.

*** Keywords ***
Input Number
    [Arguments]    ${num1}    ${num2}
    Input Text    id=num1    ${num1}
    Input Text    id=num2    ${num2}

Verify Result
    [Arguments]    ${expected_result}
    ${result}=    Get Text    id=result
    Should Contain    ${result}    ${expected_result}