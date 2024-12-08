# Math Operations Web Application

This project is a simple web application that allows users to perform basic mathematical operations (addition, subtraction, multiplication, and division) through a user-friendly interface. It includes functionality and usability testing using various testing frameworks.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Installation](#installation)
- [Execution](#execution)
- [Testing](#testing)
  - [Test Cases](#test-cases)
  - ## Testing

### Test Cases
| Test ID | Test Steps                                   | Inputs                   | Expected Output                          |
|---------|----------------------------------------------|--------------------------|------------------------------------------|
| TC01    | Open the math application                    | N/A                      | Application loads successfully           |
| TC02    | Input numbers and click Add                  | x: 5, y: 3              | Result: 8                               |
| TC03    | Input numbers and click Subtract             | x: 10, y: 4             | Result: 6                               |
| TC04    | Input numbers and click Multiply             | x: 4, y: 5              | Result: 20                              |
| TC05    | Input numbers and click Divide               | x: 12, y: 4             | Result: 3                               |
| TC06    | Input numbers and click Divide               | x: 5, y: 0              | Error: Division by zero is undefined    |
| TC07    | Input numbers and click Add                  | x: 0, y: 0              | Result: 0                               |
| TC08    | Input numbers and click Subtract             | x: -5, y: -3            | Result: -2                              |
| TC09    | Input numbers and click Multiply             | x: -2, y: 3             | Result: -6                              |
| TC10    | Input numbers and click Divide               | x: -10, y: -2           | Result: 5                               |

### Unit Testing

#### Using Unittest
Run the unit tests:
```bash
python -m unittest Lab01_test_unittest_operations.py
  - [Unit Testing](#unit-testing)
  - [Integration Testing](#integration-testing)
  - [UI Testing](#ui-testing)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Features
- Perform basic mathematical operations: Addition, Subtraction, Multiplication, and Division.
- Handles division by zero with appropriate error messages.
- User-friendly web interface.

## Technologies Used
- **Flask**: Python web framework for the backend.
- **HTML/CSS/JavaScript**: Frontend technologies for the user interface.
- **Selenium**: For automated UI testing.
- **unittest**: For unit testing.
- **pytest**: For advanced testing.

## Setup
### Prerequisites
- Python 3.x
- pip (Python package installer)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/math-operations.git
   cd math-operations
