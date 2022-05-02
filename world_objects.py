import pygame
pygame.init()
W = 1000
H = 1000


class CreateBackground(pygame.sprite.Sprite):
    """Создает и отображает игровой фон"""
    def __init__(self, surf):
        super().__init__()
        self.surf = surf
        self.image = pygame.image.load("images/background.png").convert_alpha()
        self.rect = self.image.get_rect(x=0, y=-1000)
        self.surf.blit(self.image, self.rect)
        self.speed = 3

    def move(self):
        """Циклично двигает задний фон"""
        if self.rect.y > -10:
            self.rect.y = -1000
        self.rect.y += self.speed
        self.surf.blit(self.image, self.rect)



