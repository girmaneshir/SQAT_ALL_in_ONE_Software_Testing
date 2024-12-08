*** Settings ***
Library    BuiltIn

*** Variables ***
@{ADD_POSITIVE}       5    3
@{ADD_NEGATIVE}       -2    -3
@{ADD_ZERO}           0    7
@{SUBTRACT_POSITIVE}  10    4
@{SUBTRACT_NEGATIVE}  5    8
@{MULTIPLY_POSITIVE}  4    5
@{MULTIPLY_NEGATIVE}  -3    6
@{DIVIDE_POSITIVE}    12    4
@{DIVIDE_ZERO}        5    0

*** Test Cases ***
Test Simple List
    Log    ${ADD_POSITIVE}[0]
    Log    ${ADD_POSITIVE}[1]
Test Addition
    ${result}=    Evaluate    ${ADD_POSITIVE}[0] + ${ADD_POSITIVE}[1]
    Should Be Equal As Numbers    ${result}    8
    ${result}=    Evaluate    ${ADD_NEGATIVE}[0] + ${ADD_NEGATIVE}[1]
    Should Be Equal As Numbers    ${result}    -5
    ${result}=    Evaluate    ${ADD_ZERO}[0] + ${ADD_ZERO}[1]
    Should Be Equal As Numbers    ${result}    7

Test Subtraction
    ${result}=    Evaluate    ${SUBTRACT_POSITIVE}[0] - ${SUBTRACT_POSITIVE}[1]
    Should Be Equal As Numbers    ${result}    6
    ${result}=    Evaluate    ${SUBTRACT_NEGATIVE}[0] - ${SUBTRACT_NEGATIVE}[1]
    Should Be Equal As Numbers    ${result}    -3

Test Multiplication
    ${result}=    Evaluate    ${MULTIPLY_POSITIVE}[0] * ${MULTIPLY_POSITIVE}[1]
    Should Be Equal As Numbers    ${result}    20
    ${result}=    Evaluate    ${MULTIPLY_NEGATIVE}[0] * ${MULTIPLY_NEGATIVE}[1]
    Should Be Equal As Numbers    ${result}    -18

Test Division
    # Test normal division
    ${result}=    Evaluate    ${DIVIDE_POSITIVE}[0] / ${DIVIDE_POSITIVE}[1]
    Should Be Equal As Numbers    ${result}    3
