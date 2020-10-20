# -----------------------------
# Imported modules & libraries
# -----------------------------

import pygame

# -----------------------------
# Defining global variables
# -----------------------------

icon = pygame.image.load('./static/goose_communist_32px.png')
cursor = pygame.image.load('./static/wand_black_64px.png')
title = "Sorteerhoed || AlphenseFederatie\u00a9"
screen = pygame.display.set_mode((1280, 720))

cursor_rect = cursor.get_rect()

# -----------------------------
# Defining functions
# -----------------------------


def init():
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_caption(title)
    pygame.display.set_icon(icon)
    main();


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        cursor_rect.center = pygame.mouse.get_pos()
        screen.blit(cursor, cursor_rect)
        pygame.display.update()


# -----------------------------
# Calling defined function(s)
# -----------------------------


init()
