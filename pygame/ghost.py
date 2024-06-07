import pygame

class Ghost(pygame.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/ghost-x4.gif")
        self.image = pygame.transform.scale(self.image, [100,100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed_x = 0
        self.acceleration_x = 0.1
        self.speed_y = 0
        self.acceleration_y = 0.1


    def update(self, *args):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.speed_y -= self.acceleration_y
        elif keys[pygame.K_s]:
            self.speed_y += self.acceleration_y
        elif keys[pygame.K_a]:
            self.speed_x -= self.acceleration_x
        elif keys[pygame.K_d]:
            self.speed_x += self.acceleration_x
        else:
            self.speed_x *= 0.95
            self.speed_y *= 0.95

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed_y = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed_y = 0
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed_x = 0
        elif self.rect.right > 840:
            self.rect.right = 840
            self.speed_x = 0



