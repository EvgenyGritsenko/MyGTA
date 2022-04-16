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
        self.rect = self.image.get_rect(x=0, y=0)
        self.surf.blit(self.image, self.rect)


class CreateRoad(pygame.sprite.Sprite):
    """Create game roads"""
    def __init__(self, surf):
        super().__init__()
        self.surf = surf
        self.image = pygame.image.load("images/new_road.png").convert_alpha()
        self.rect = self.image.get_rect(center=(W // 2, 0))
        self.road_group = pygame.sprite.Group()
        self.add(self.road_group)
        self.surf.blit(self.image, self.rect)

    def move(self):
        self.rect.centery -= 30
        self.surf.blit(self.image, self.rect)
    # def create_road(self):
    #     now_width = W // 2
    #     now_height = H - self.image.get_height() // 2 - self.image.get_height()
    #
    #     for i in range(10):  # генерация дороги из 10 одинаковых изображений
    #         new_image = pygame.image.load("images/road.png").convert_alpha()
    #         new_image_rect = new_image.get_rect(center=(now_width, now_height))
    #         self.road_group.add(new_image)
    #         self.surf.blit(new_image, new_image_rect)
    #         now_height -= new_image.get_height()

    # def full_road_horizontal(self):
    #     # get_height() т.к. высота image равна ширине new_image
    #     now_width = 0 - self.image.get_height() // 2
    #     now_height = H // 2
    #
    #     for i in range(12):  # генерация дороги из 12 одинаковых изображений
    #         new_image = pygame.image.load("images/road_horizontal.png").convert_alpha()
    #         new_image_rect = new_image.get_rect(center=(now_width, now_height))
    #         self.surf.blit(new_image, new_image_rect)
    #         now_width += new_image.get_width()


class CreateShop(pygame.sprite.Sprite):
    """Create shops"""
    def __init__(self, surf, car):
        super().__init__()
        self.car = car
        self.surf = surf
        self.image = pygame.image.load("images/magazine.png")
        self.rect = self.image.get_rect(x=100, y=100)
        self.surf.blit(self.image, self.rect)



