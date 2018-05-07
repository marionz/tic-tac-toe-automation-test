from selenium import webdriver

"""
TC5: Click the reverse button, we should verify:

1. The game board will stay the same
2. The sequence of steps will be reversed except the 'Go to game start' button
3. Click the reverse button again, the sequence will be changed back
"""


def initial_game_board(_driver):
	squares = _driver.find_elements_by_class_name('square')
	squares[0].click()
	squares[1].click()
	squares[3].click()
	squares[6].click()
	squares[4].click()
	squares[5].click()
	squares[7].click()
	squares[8].click()
	squares[2].click()


def verify_game_square_text(_driver):
	squares = _driver.find_elements_by_class_name("square")
	assert squares[0].text == 'X'
	assert squares[1].text == 'O'
	assert squares[3].text == 'X'
	assert squares[6].text == 'O'
	assert squares[4].text == 'X'
	assert squares[5].text == 'O'
	assert squares[7].text == 'X'
	assert squares[8].text == 'O'
	assert squares[2].text == 'X'


def get_step_text_list(_driver):
	step_button_web_element = _driver.find_elements_by_xpath("html/body/div/div/div[2]/ol/li")
	step_text_list = list()
	for square in step_button_web_element:
		step_text_list.append(square.text)
	return step_text_list


def verify_step_list_text_reversed(_original, _reversed):
	assert _original[0] == _reversed[0]
	assert _original[1::1] == _reversed[-1:0:-1]


driver = webdriver.Firefox()
driver.get('http://localhost:3000/')

try:

	initial_game_board(driver)
	verify_game_square_text(driver)
	original_step_text_list = get_step_text_list(driver)

	# Find the 'Reverse' button and click it
	driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/button").click()
	verify_game_square_text(driver)
	reversed_step_text_list = get_step_text_list(driver)
	verify_step_list_text_reversed(original_step_text_list, reversed_step_text_list)

	# Click the 'Reverse' button again
	driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/button").click()
	verify_game_square_text(driver)
	reversed_again_step_text_list = get_step_text_list(driver)
	verify_step_list_text_reversed(reversed_step_text_list, reversed_again_step_text_list)

finally:
	driver.quit()
