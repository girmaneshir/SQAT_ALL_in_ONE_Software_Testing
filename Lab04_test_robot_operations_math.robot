*** Settings ***
Library    math_operations.py

*** Variables ***
@{ADD_POSITIVE}       5    3
@{ADD_NEGATIVE}       -2    -3
@{ADD_ZERO}           0    7
@{SUBTRACT_POSITIVE}  10    4
@{SUBTRACT_NEGATIVE}  5    8
@{MULTIPLY_POSITIVE}  4    5
@{MULTIPLY_NEGATIVE}  -3    6
@{DIVIDE_POSITIVE}    12    4


*** Test Cases ***
Test Simple List
    Log    ${ADD_POSITIVE}[0]
    Log    ${ADD_POSITIVE}[1]

Test Addition
    ${result}=    Add    ${ADD_POSITIVE}[0]    ${ADD_POSITIVE}[1]
    Should Be Equal As Numbers    ${result}    8
    ${result}=    Add    ${ADD_NEGATIVE}[0]    ${ADD_NEGATIVE}[1]
    Should Be Equal As Numbers    ${result}    -5
    ${result}=    Add    ${ADD_ZERO}[0]    ${ADD_ZERO}[1]
    Should Be Equal As Numbers    ${result}    7

Test Subtraction
    ${result}=    Subtract    ${SUBTRACT_POSITIVE}[0]    ${SUBTRACT_POSITIVE}[1]
    Should Be Equal As Numbers    ${result}    6
    ${result}=    Subtract    ${SUBTRACT_NEGATIVE}[0]    ${SUBTRACT_NEGATIVE}[1]
    Should Be Equal As Numbers    ${result}    -3

Test Multiplication
    ${result}=    Multiply    ${MULTIPLY_POSITIVE}[0]    ${MULTIPLY_POSITIVE}[1]
    Should Be Equal As Numbers    ${result}    20
    ${result}=    Multiply    ${MULTIPLY_NEGATIVE}[0]    ${MULTIPLY_NEGATIVE}[1]
    Should Be Equal As Numbers    ${result}    -18

Test Division
    # Test normal division
    ${result}=    Divide    ${DIVIDE_POSITIVE}[0]    ${DIVIDE_POSITIVE}[1]
    Should Be Equal As Numbers    ${result}    3

