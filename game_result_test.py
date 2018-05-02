from selenium import webdriver

"""
TC3: Click the squares in the game board , 
once it comes to 3X or 3O in one row / column / diagonal, 
there will be a winner.

For any case when the game comes to a win, we should verify:
1. This row / column / diagonal will be highlighted
2. The text of the status will display "Winner: X" or "Winner: O"
3. All the squares can't be clicked any more 
"""


def verify_winner_status(_player, _driver):

	# 1. this row / column / diagonal will be highlighted
	highlighted_squares = _driver.find_elements_by_class_name("highlight-square")
	assert len(highlighted_squares) == 3
	assert highlighted_squares[0].text == _player
	assert highlighted_squares[1].text == _player
	assert highlighted_squares[2].text == _player

	# 2. the text of the status will display "Winner: X" or "Winner: O"
	status = _driver.find_element_by_id('status').text
	assert status == 'Winner: {}'.format(_player)

	# 3. all the squares can't be clicked any more
	verify_squares_not_clickable(_driver)


def verify_squares_not_clickable(_driver):
	squares = _driver.find_elements_by_class_name('square')
	for square in squares:
		txt = square.text
		square.click()
		assert square.text == txt


def test_game_win_in_one_row(_driver):
	_driver.refresh()
	squares = _driver.find_elements_by_class_name('square')
	squares[0].click()
	squares[3].click()
	squares[1].click()
	squares[6].click()
	squares[2].click()
	verify_winner_status('X', _driver)


def test_game_win_in_one_column(_driver):
	_driver.refresh()
	squares = _driver.find_elements_by_class_name('square')
	squares[0].click()
	squares[3].click()
	squares[4].click()
	squares[5].click()
	squares[1].click()
	squares[6].click()
	squares[7].click()
	verify_winner_status('X', _driver)


def test_game_win_in_one_diagonal(_driver):
	_driver.refresh()
	squares = _driver.find_elements_by_class_name('square')
	squares[3].click()
	squares[0].click()
	squares[6].click()
	squares[4].click()
	squares[1].click()
	squares[8].click()
	verify_winner_status('O', _driver)

"""
TC4: If there is no 3X or 3O in one row / column / diagonal 
when all the squares in the game board are clicked, 
the result should be a draw.

For any case when the game comes to a draw, we should verify:
1. The text of the status will show "It's a draw!"
2. All the squares cann't be clicked any more 
"""

def test_game_draw(_driver):
	_driver.refresh()
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

	status = _driver.find_element_by_id('status').text
	assert status == 'It\'s a draw!'

	verify_squares_not_clickable(_driver)


driver = webdriver.Firefox()
driver.get('http://localhost:3000/')

try:
	test_game_win_in_one_row(driver)
	test_game_win_in_one_column(driver)
	test_game_win_in_one_diagonal(driver)
	test_game_draw(driver)
finally:
	driver.quit()
