import pygame

class Car:
    def __init__(self, x, emergency=False):
        self.x = x
        self.y = 600
        self.speed = 3
        self.emergency = emergency
        self.counted = False

    def move(self, signal_green):
        if signal_green or self.emergency:
            self.y -= self.speed

    def draw(self, screen):
        color = (255, 0, 0) if self.emergency else (0, 200, 0)
        pygame.draw.rect(screen, color, (self.x, self.y, 30, 50))