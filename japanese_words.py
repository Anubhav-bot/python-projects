import pygame
import random

#initialization
pygame.init()
WIDTH, HEIGHT = (800, 500)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Japanese Vocabulary Practice")

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


#dictionary
myDict = {
	#japanese: english
	
	'neko': 'cat',
	'inu': 'dog',
	
	'te': 'hand',
	'ashi': 'leg',
	'ha': 'tooth',
	'kuchi': 'mouth',
	'me': 'eye',
	'mimi': 'ear',
	'hana': 'nose',
	'yubi': 'finger',
	'atama': 'head',

	'makura': 'pillow',
	'beddo': 'bed',
	'futon': 'quilt',
	'moufu': 'blanket',
	'taoru': 'towel',
	'furo': 'bath',
	'ofuro': 'bath',
	'sekken': 'soap',
	'haburashi': 'toothbrush',
	'kagami': 'mirror',
	'mado': 'window',


	'e': 'drawing',
	'ii': 'good',
	'ai': 'love',
	'au': 'to meet',
	'ue': 'up',
	'iu': 'to say',
	'ie': 'house',
	'ao': 'blue',
	'ou': 'to chase',
	'oi': 'nephew',
	'ei': 'ray fish',
	'iie': 'no',
	'ooi': 'many'

}

#Functions


def draw():
	
	screen.fill(BG)
	# pygame.draw.rect(screen, color, theRect)
	if theWord in myDict.values():
		text = font2.render("Translate the following English word to Japanese: ", True, RED)
	else:
		text = font2.render("Translate the following Japanese word to English: ", True, WHITE)
	screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2), 50))



	text = font3.render(theWord
		, True, GREEN)
	theRect = pygame.rect.Rect((WIDTH // 2) - (text.get_width() // 2), (HEIGHT // 2) - (100 // 2), 100, 100)
	screen.blit(text, (theRect))

	text = font.render('> ', True, BROWN)
	screen.blit(text, (theRect.x - text.get_width(), theRect.y + 100))

	text = font.render(inp, True, YELLOW)
	screen.blit(text, (theRect.x, theRect.y + 100))
	

def check(inp):
	if (myDict.get(inp) == theWord) or (myDict.get(theWord) == inp):
		screen.fill(BG)
		text2 = font3.render('Correct!!', True, WHITE)
		screen.blit(text2, ((WIDTH // 2) - (text2.get_width() // 2),( HEIGHT // 2) - (text2.get_height() // 2)))

	elif 'exit' in inp:
		exit()

	else:
		screen.fill(BG)
		text = font3.render('Wrong!!', True, RED)
		screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2),( HEIGHT // 2) - (text.get_height() // 2) - 100))
		if theWord in myDict.values():
			text = font2.render(f'The correct answer is "{list(myDict.keys())[list(myDict.values()).index(theWord)]}"', True, WHITE)
		else:
			text = font2.render(f'The correct answer is "{myDict.get(theWord)}"', True, WHITE)

		screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2),( HEIGHT // 2) - (text.get_height() // 2)))

	text = font.render('Press Enter to continue...', True, ORANGE)
	screen.blit(text, ((WIDTH // 2) - (text.get_width() // 2),( HEIGHT // 2) - (text.get_height() // 2) + 200))


#Some Variables
inp = ''

font = pygame.font.Font(None, 24)
font2= pygame.font.Font(None, 32)
font3 = pygame.font.Font(None, 64)

theWord = random.choice(list(random.choice(list(myDict.items()))))

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
					check(inp.lower())
					currently_displaying_result = True
				else:
					theWord = random.choice(list(random.choice(list(myDict.items()))))
					currently_displaying_result = False
					inp = ''
			else:
				inp += event.unicode

	if not currently_displaying_result:
		draw()
	
	
	pygame.display.update()


pygame.quit()
