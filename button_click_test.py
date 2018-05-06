from selenium import webdriver


def initial_game_board(_squares):
	"""
	Initialize the game board with starting a few steps,
	so that we could test the functional buttons of the game.
	"""
	_squares[0].click()
	_squares[3].click()
	_squares[1].click()
	_squares[6].click()
	_squares[2].click()


def verify_next_player_status(_driver, _player):
	status = _driver.find_element_by_id('status').text
	assert status == 'Next player: {}'.format(_player)


"""
TC6: Click the start button, a new game will be started, we should verify:
1. all the squares in the game board are cleaned
2. the status is "Next player: X"
"""


def test_click_start_button(_driver):
	_driver.refresh()
	squares = _driver.find_elements_by_class_name('square')
	initial_game_board(squares)
	# Click the start button
	_driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ol/li[1]/button").click()
	assert squares[0].text == ''
	assert squares[1].text == ''
	assert squares[2].text == ''
	assert squares[3].text == ''
	assert squares[4].text == ''
	assert squares[5].text == ''
	assert squares[6].text == ''
	assert squares[7].text == ''
	assert squares[8].text == ''
	verify_next_player_status(_driver, 'X')


"""
TC7: Click any of the step buttons, the game board status will change back to that step
Click the step 3 button
Check the game board will reappear the status of the step 3
The square (1, 1) is X, the square (2, 1) is O, the other squares are empty
"""


def test_click_step_button(_driver):
	_driver.refresh()
	squares = _driver.find_elements_by_class_name('square')
	initial_game_board(squares)
	# Click the 3rd step button
	driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ol/li[3]/button").click()
	assert squares[0].text == 'X'
	assert squares[3].text == 'O'
	assert squares[1].text == ''
	assert squares[2].text == ''
	assert squares[4].text == ''
	assert squares[5].text == ''
	assert squares[6].text == ''
	assert squares[7].text == ''
	assert squares[8].text == ''
	verify_next_player_status(_driver, 'X')


"""
TC8: Click any of the step buttons except the last one, 
then click a haven't been clicked square in the game board, we should verify:
1. The steps after the selected step will be deleted.
2. A new step will be created in the step list.

For example: 
Click squares (2, 2)
Step 4 will change to "X chose (2, 2)"
Step 5 and step 6 will be disappeared, check the quantity of the original_steps is 4

"""


def test_withdraw_and_start_a_new_step(_driver):
	_driver.refresh()
	squares = _driver.find_elements_by_class_name('square')
	initial_game_board(squares)
	# Click the 3rd step button
	_driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/ol/li[3]/button").click()
	# Click the square (2, 2)
	squares[4].click()
	step_text = _driver.find_element_by_class_name('bold-button').text
	assert step_text == 'X chose (2, 2)'
	# Check the quantity of the steps
	steps = _driver.find_elements_by_xpath("html/body/div/div/div[2]/ol/li")
	assert len(steps) == 4
	verify_next_player_status(_driver, 'O')


driver = webdriver.Firefox()
driver.get('http://localhost:3000/')

try:
	test_click_start_button(driver)
	test_click_step_button(driver)
	test_withdraw_and_start_a_new_step(driver)
finally:
	driver.quit()

