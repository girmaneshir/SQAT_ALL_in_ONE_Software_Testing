from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Adjust this if you're using a different browser

def test_addition(x, y, expected):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.ID, "num1").send_keys(str(x))
    driver.find_element(By.ID, "num2").send_keys(str(y))
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    time.sleep(1)  # Wait for the result
    result = driver.find_element(By.ID, "result").text
    assert expected in result, f"Expected '{expected}' but got '{result}'"
    return result

def test_subtraction(x, y, expected):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.ID, "num1").send_keys(str(x))
    driver.find_element(By.ID, "num2").send_keys(str(y))
    driver.find_element(By.XPATH, "//button[text()='Subtract']").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "result").text
    assert expected in result, f"Expected '{expected}' but got '{result}'"
    return result

def test_multiplication(x, y, expected):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.ID, "num1").send_keys(str(x))
    driver.find_element(By.ID, "num2").send_keys(str(y))
    driver.find_element(By.XPATH, "//button[text()='Multiply']").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "result").text
    assert expected in result, f"Expected '{expected}' but got '{result}'"
    return result

def test_division(x, y, expected):
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.ID, "num1").send_keys(str(x))
    driver.find_element(By.ID, "num2").send_keys(str(y))
    driver.find_element(By.XPATH, "//button[text()='Divide']").click()
    time.sleep(1)
    result = driver.find_element(By.ID, "result").text
    assert expected in result, f"Expected '{expected}' but got '{result}'"
    return result

def run_tests():
    try:
        print("Running Tests...")
        
        # Test Addition
        add =test_addition(5, 3, "Result: 8")
        print("Addition is ", add)
        
        # Test Subtraction
        sub=test_subtraction(10, 4, "Result: 6")
        print("Subtraction is ", sub)
        
        # Test Multiplication
        mul=test_multiplication(4, 5, "Result: 20")
        print("Multiplication is ", mul)
        
        # Test Division
        div= test_division(12, 4, "Result: 3")
        print("Divition is ", div)
                
        # Test Division by Zero
        test_division(5, 0, "Error: Division by zero is undefined.")

        print("All tests passed successfully!")

    except AssertionError as e:
        print(e)

    finally:
        driver.quit()

if __name__ == "__main__":
    run_tests()