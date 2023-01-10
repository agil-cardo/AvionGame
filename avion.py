import pygame

class Avion(pygame.sprite.Sprite):
    """
    docstring
    """
    
    def __init__(self, Weapon):
        super(Avion, self).__init__()
        self.image = pygame.image.load("assets/spaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.PV = 50
        self.PV_MAX = 100
        self.weapon = Weapon() # TOdo creer class weapon 
        self.attack_ship = 10
        self.speed_x = 5
        self.speed_y = 2
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 50
        self.keyboard = {}

    def move_left(self):
        self.rect.x -= self.speed_x
    
    def move_right(self):
        self.rect.x += self.speed_x
    
    def move_up(self):
        self.rect.y -= self.speed_y

    def move_down(self):
        self.rect.y += self.speed_y

    def rotate_bar(self, pos_y, color):
        surface_bar = pygame.Surface([pos_y, 5])
        surface_bar.fill(color)
        surface_bar = pygame.transform.rotate(surface_bar, 90)
        return surface_bar
    
    def update_pv(self, surface):
        color = (11,210,46)
        back_color = (250,0,0) #rouge

        surface.blit(self.rotate_bar(self.PV_MAX, back_color), (self.rect.x - 8, self.rect.y))
        surface.blit(self.rotate_bar(self.PV, color), (self.rect.x - 8, self.rect.y))
        

        

    