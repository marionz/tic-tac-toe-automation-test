from selenium import webdriver
import time


driver = webdriver.Firefox()
try:
    # open tic tac toe index page
    driver.get('http://localhost:3000/')
    time.sleep(2)

    # check the game board has a 3*3 empty squares
    squares = driver.find_elements_by_class_name('square')
    assert len(squares) == 9

    # check the default status is "the Next player：X"
    default_status = driver.find_element_by_id("status").text
    assert default_status == 'Next player: X'

    # check the Reverse button exist
    reverse_button = driver.find_element_by_id('reverse_button')
    assert reverse_button

    # check the go to game start button exist
    start_button = driver.find_element_by_class_name('bold-button')
    assert start_button


finally:
    driver.quit()
