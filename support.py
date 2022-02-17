import pygame


def import_image(path,widht=None,height=None):
	img = pygame.image.load(path).convert_alpha()
	if [widht,height] == [None,None]:
		return img
	else:
		img = pygame.transform.scale(img, (widht,height))
		return img

def sprite_sheet(path,widht=88,height=92):
	sprite_sheet = pygame.image.load(path).convert_alpha()
	img_h = sprite_sheet.get_height()//88
	img_w = sprite_sheet.get_width()//92
	sprites = []
	for r in range(img_h):
		for c in range(r):
			x = widht*c
			y = height*r
			img = pygame.Surface((widht,height),flags=pygame.SRCALPHA)
			img.blit(sprite_sheet, pygame.Rect(x, y, widht, height))
			sprites.append(img)

	return sprites