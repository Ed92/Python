import pyhame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("a bit racey")

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load("racecar.png")
