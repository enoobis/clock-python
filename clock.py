import pygame
import time
import math

pygame.init()

width = 600
height = 600

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clock")

white = (255, 255, 255)
black = (0, 0, 0)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

def draw_hands(screen, hours, minutes, seconds):
    hour_angle = (hours / 12) * 360
    minute_angle = (minutes / 60) * 360
    second_angle = (seconds / 60) * 360

    hour_x = 100 * math.sin(math.radians(hour_angle))
    hour_y = -100 * math.cos(math.radians(hour_angle))
    minute_x = 150 * math.sin(math.radians(minute_angle))
    minute_y = -150 * math.cos(math.radians(minute_angle))
    second_x = 150 * math.sin(math.radians(second_angle))
    second_y = -150 * math.cos(math.radians(second_angle))

    pygame.draw.line(screen, white, (width // 2, height // 2), (width // 2 + hour_x, height // 2 + hour_y), 5)
    pygame.draw.line(screen, white, (width // 2, height // 2), (width // 2 + minute_x, height // 2 + minute_y), 3)
    pygame.draw.line(screen, white, (width // 2, height // 2), (width // 2 + second_x, height // 2 + second_y), 1)

def draw_numbers(screen):
    for i in range(1, 13):
        angle = math.radians(i / 12 * 360 )
        x = int(width / 2 + 200 * math.sin(angle))
        y = int(height / 2 - 200 * math.cos(angle))
        text = font.render(str(i), True, white)
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    current_time = time.localtime()
    hours = current_time.tm_hour % 12
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    screen.fill(black)
    pygame.draw.circle(screen, white, (width // 2, height // 2), 250, 1)
    draw_hands(screen, hours, minutes, seconds)
    draw_numbers(screen)
    pygame.display.update()

    clock.tick(60)