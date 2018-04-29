from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://localhost:3000/')


def click_and_verify(_square_index, _current_player, _next_player, _column, _row, _step_quantity):
	# get all the square buttons
	squares = driver.find_elements_by_class_name("square")
	# obtain a button and click it
	squares[_square_index].click()
	# check the value of the clicked button
	square_text = squares[_square_index].text
	assert square_text == _current_player
	# check the status div change to the next player
	status_value = driver.find_element_by_id('status').text
	assert status_value == 'Next player: {}'.format(_next_player)
	# check the current step text
	step_text = driver.find_element_by_class_name('bold-button').text
	assert step_text == '{} chose ({}, {})'.format(_current_player, _column, _row)
	# check the quantity of the steps in the steps list
	steps = driver.find_elements_by_xpath("html/body/div/div/div[2]/ol/li")
	assert len(steps) == _step_quantity


try:
	# First, click square (1, 1), the current player is X, the next player is O,
	# the (column, row) is (1, 1), there should be 2 step buttons after the first click
	click_and_verify(0, 'X', 'O', 1, 1, 2)

	# Secondly, click square (2, 1), the current player is O, the next player is X,
	# the (column, row) is (2, 1), there should be 3 step buttons after the second click
	click_and_verify(3, 'O', 'X', 2, 1, 3)

	# Thirdly, click square (3, 1), the current player is X, the next player is O,
	# the (column, row) is (3, 1), there should be 4 step buttons after the third click
	click_and_verify(6, 'X', 'O', 3, 1, 4)

	# Click square (3, 1) again, it should stay the same
	click_and_verify(6, 'X', 'O', 3, 1, 4)

finally:
	driver.quit()