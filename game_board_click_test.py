from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://localhost:3000/')

try:

	# get all the square buttons
	squares = driver.find_elements_by_class_name("square")
	# obtain a button and click it
	squares[0].click()
	# check the value of the clicked button is 'X'
	square_0_text = squares[0].text
	assert square_0_text == 'X'
	# check the status div change to 'O'
	status_0 = driver.find_element_by_id('status').text
	assert status_0 == 'Next player: O'
	# check the step1 result is X chose (1, 1)
	step1_text = driver.find_element_by_class_name('bold-button').text
	assert step1_text == 'X chose (1, 1)'
	# check there are 2 buttons in the steps list
	steps = driver.find_elements_by_xpath("html/body/div/div/div[2]/ol/li")
	assert len(steps) == 2

	# obtain the second button and click it
	squares[3].click()
	# check the value of the second clicked button is 'O'
	square_3_text = squares[3].text
	assert square_3_text == 'O'
	# check the status div change to 'X'
	status_3 = driver.find_element_by_id('status').text
	assert status_3 == 'Next player: X'
	# check the step2 result is O chose (2, 1)
	step2_text = driver.find_element_by_class_name('bold-button').text
	assert step2_text == 'O chose (2, 1)'
	# check there are 3 buttons in the steps list
	steps = driver.find_elements_by_xpath("html/body/div/div/div[2]/ol/li")
	assert len(steps) == 3

	# obtain the third button and click it
	squares[6].click()
	# check the value of the third clicked button is 'X'
	square_6_text = squares[6].text
	assert square_6_text == 'X'
	# check the status div change to 'O'
	status_6 = driver.find_element_by_id('status').text
	assert status_6 == 'Next player: O'
	# check the step3 result is X chose (3, 1)
	step3_text = driver.find_element_by_class_name('bold-button').text
	assert step3_text == 'X chose (3, 1)'
	# check there are 4 buttons in the steps list
	steps = driver.find_elements_by_xpath("html/body/div/div/div[2]/ol/li")
	assert len(steps) == 4

	# check the clicked button can not be clicked again
	squares[6].click()
	# check the value of this button is not changed to 'O'
	square_6_text = squares[6].text
	assert square_6_text == 'X'
	# check the status div change to 'O'
	status_6 = driver.find_element_by_id('status').text
	assert status_6 == 'Next player: O'
	# check the step3 result is X chose (3, 1)
	step3_text = driver.find_element_by_class_name('bold-button').text
	assert step3_text == 'X chose (3, 1)'
	# check there are 4 buttons in the steps list
	steps = driver.find_elements_by_xpath("html/body/div/div/div[2]/ol/li")
	assert len(steps) == 4


finally:
	driver.quit()