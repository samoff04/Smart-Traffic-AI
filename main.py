import pygame
import random

from car import Car
from signal import TrafficSignal
from stats import Stats
from config import WIDTH, HEIGHT, LANES

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Traffic Simulator - Polished Version")

clock = pygame.time.Clock()

cars = []
signal = TrafficSignal()
stats = Stats()

frame = 0

def draw_road():
    screen.fill((20, 20, 20))

    pygame.draw.rect(screen, (60, 60, 60), (200, 0, 500, HEIGHT))

    for x in LANES:
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, HEIGHT), 2)

def draw_signal(state):
    color = (0, 255, 0) if state == "GREEN" else (255, 0, 0)
    pygame.draw.circle(screen, color, (70, 80), 20)

running = True

while running:
    clock.tick(60)
    frame += 1

    draw_road()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    signal.update()
    draw_signal(signal.state)

    if frame % 40 == 0:
        emergency = random.random() < 0.15
        cars.append(Car(random.choice(LANES), emergency))

    for car in cars:
        car.move(signal.state == "GREEN")
        car.draw(screen)

    stats.update(cars)

    cars = [c for c in cars if c.y > -100]

    font = pygame.font.SysFont(None, 28)

    text1 = font.render(f"Cars Passed: {stats.cars_passed}", True, (255, 255, 255))
    screen.blit(text1, (600, 30))

    text2 = font.render(f"Active Cars: {len(cars)}", True, (255, 255, 255))
    screen.blit(text2, (600, 60))

    pygame.display.update()

pygame.quit()