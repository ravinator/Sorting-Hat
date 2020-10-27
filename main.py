# -----------------------------
# Imported modules & libraries
# -----------------------------


import sys
import time
import pygame


# -----------------------------
# Defining classes
# -----------------------------


class Button:
    def __init__(self, id, img_def, img_hov, text, position):
        # Center text
        size_txt = list(font.size(text))
        pos_txt = list(position)
        pos_txt[0] += int((img_def.get_size()[0] / 2) - (size_txt[0] / 2))
        pos_txt[1] += int((img_def.get_size()[1] / 2) - (size_txt[1] / 2))
        pos_txt = tuple(pos_txt)

        # Assign variables
        self.id = id
        self.img_def = img_def
        self.img_hov = img_hov
        self.text = font.render(text, True, (0, 0, 0))
        self.rect_img = img_def.get_rect(topleft=position)
        self.rect_txt = img_def.get_rect(topleft=pos_txt)

    def on_click(self, event):
        time.sleep(0.05)
        if event.button == 1:
            if self.rect_img.collidepoint(event.pos):
                if self.id == 'start':
                    print('START')
                if self.id == 'result':
                    print('RESULTS')
                if self.id == 'quit':
                    print('QUIT')
                    pygame.quit()
                    sys.exit()


# -----------------------------
# Defining global variables
# -----------------------------


pygame.init()
pygame.font.init()
pygame.mixer.init()

# Window & Cursor
icon = pygame.image.load('./image/goose_communist_32px.png')
cursor = pygame.image.load('./image/wand_black_64px.png')
title = "Sorteerhoed || AlphenseFederatie\u00a9"
screen = pygame.display.set_mode((1280, 720))
font = pygame.font.SysFont('couriernew', 42)

# Images
bg_splash = pygame.image.load('./image/bg_splash.png')
bg_menu = pygame.image.load('./image/bg_menu.jpg')
btn_default = pygame.image.load('./image/btn_default.png')
btn_hover = pygame.image.load('./image/btn_hover.png')

# Sounds
sound_goose = pygame.mixer.Sound('./sound/goose.ogg')

# Get size of object
cursor_rect = cursor.get_rect()

# Create objects
btn_menu = [Button('start', btn_default, btn_hover, 'Start', (460, 320)),
            Button('result', btn_default, btn_hover, 'Results', (460, 430)),
            Button('quit', btn_default, btn_hover, 'Quit', (460, 540))]


# -----------------------------
# Defining functions
# -----------------------------


def init():
    print(pygame.font.get_fonts())
    pygame.mouse.set_visible(False)
    pygame.display.set_caption(title)
    pygame.display.set_icon(icon)


def main():
    loop_active = True
    game_state = "splash"

    while loop_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop_active = False

        cursor_rect.center = pygame.mouse.get_pos()

        # Game state loops
        if game_state == "splash":
            screen.fill((0, 0, 0))
            screen.blit(bg_splash, (0, 0))
            pygame.display.flip()
            pygame.mixer.Sound.play(sound_goose)
            time.sleep(sound_goose.get_length() + 0.5)
            game_state = "menu"

        if game_state == "menu":
            screen.fill((255, 255, 255))
            screen.blit(bg_menu, (0, 0))

            # Action on click & hover
            for button in btn_menu:
                if button.rect_img.collidepoint(pygame.mouse.get_pos()):
                    screen.blit(button.img_hov, button.rect_img)
                    screen.blit(button.text, button.rect_txt)
                else:
                    screen.blit(button.img_def, button.rect_img)
                    screen.blit(button.text, button.rect_txt)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    button.on_click(event)

            screen.blit(cursor, cursor_rect)

        # Updates game screen & cursor
        screen.blit(cursor, cursor_rect)
        pygame.display.update()


# -----------------------------
# Calling defined function(s)
# -----------------------------


init()
main()
