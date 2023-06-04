import pygame
import random

#initialization
pygame.init()
WIDTH, HEIGHT = (800, 500)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Japanese Colors Practice")

#colors
GREEN = (0, 255, 0)
BLUE = ( 0, 0 ,255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
PINK = (255, 50, 150)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
BROWN = (150, 100, 0)
BG = (30, 30, 30)



myDict = {
	'midori': GREEN,
	'ao': BLUE,
	'aka': RED,
	'haiiro': GRAY,
	'pinku': PINK,
	'orange': ORANGE,
	'murasaki' : PURPLE,
	'chairo': BROWN,
	'kiiro' : YELLOW,
	'shiro' : WHITE,
	'kuro' : BLACK
}


#Functions

def draw():
	
	screen.fill(BG)

	text = font2.render("Type the japanese name of the color shown below: ", True, color)
	screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2), 100))
	
	color_rect = pygame.rect.Rect((WIDTH // 2) - (100 // 2), (HEIGHT // 2) - (100 // 2), 100, 100)
	pygame.draw.rect(screen, color, color_rect)

	text = font.render(inp, True, color)
	screen.blit(text, (color_rect.x, color_rect.y + 100))
	

def check(inp):

	if color == myDict.get(inp):  # Checks if the given input corresponds to the shown color.
		screen.fill(BG)
		text2 = font3.render('Correct!!', True, WHITE)
		screen.blit(text2, ((WIDTH // 2) - (text2.get_width() // 2),( HEIGHT // 2) - (text2.get_height() // 2)))

	elif 'exit' in inp:
		exit()

	else:
		screen.fill(BG)
		text = font3.render('Incorrect!!', True, RED)
		screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2),( HEIGHT // 2) - (text.get_height() // 2) - 100))

		text = font2.render(f'The correct answer is "{list(myDict.keys())[list(myDict.values()).index(color)]}"', True, WHITE)
		screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2),( HEIGHT // 2) - (text.get_height() // 2)))

	text = font.render('Press Enter to continue...', True, ORANGE)
	screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2),( HEIGHT // 2) - (text.get_height() // 2) + 200))



#Some Variables
inp = ''

font = pygame.font.Font(None, 24)
font2= pygame.font.Font(None, 32)
font3 = pygame.font.Font(None, 64)



color = random.choice(list(myDict.values()))  #Choose a random color from the values in the dictionary

running = True
currently_displaying_result = False

#Main loop
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_BACKSPACE:
				inp = inp[0:-1]
				currently_displaying_result = False

			elif event.key == pygame.K_RETURN:
				if not currently_displaying_result:
					check(inp)
					currently_displaying_result = True
				else:
					color = random.choice(list(myDict.values()))
					currently_displaying_result = False
					inp = ''
			else:
				inp += event.unicode

	if not currently_displaying_result:
		draw()
	
	
	pygame.display.update()

	





#var += event.unicode.

'''
create a empty variable
when user enters something, store it in the variable
After the user hits enter, check if the value inside var leads to the shown colour.
'''



pygame.quit()