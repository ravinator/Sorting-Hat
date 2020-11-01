# -----------------------------
# Imported modules & libraries
# -----------------------------


import sys
import time
import pygame

pygame.init()
pygame.font.init()
pygame.mixer.init()

# -----------------------------
# Defining global variables
# -----------------------------


# Globally Defined Variables
game_state = "splash"
q_answered = True
q_count = 1
iat = 0
bdam = 0
se = 0
fict = 0

# Window & Cursor
icon = pygame.image.load('./image/window/goose_communist_32px.png')
cursor = pygame.image.load('./image/window/wand_black_64px.png')
title = "Sorteerhoed --- AlphenseFederatie\u2122"
screen = pygame.display.set_mode((1280, 720))

# Images
bg_splash = pygame.image.load('./image/background/bg_splash.png')
bg_menu = pygame.image.load('./image/background/bg_menu.jpg')
bg_quiz = pygame.image.load('./image/background/bg_quiz.jpg')
bg_result = [pygame.image.load('./image/background/bg_result_iat.jpg'),
             pygame.image.load('./image/background/bg_result_bdam.jpg'),
             pygame.image.load('./image/background/bg_result_se.jpg'),
             pygame.image.load('./image/background/bg_result_fict.jpg')]
btn_menu = pygame.image.load('./image/button/btn_menu.png')
btn_menu_hover = pygame.image.load('./image/button/btn_menu_hover.png')
btn_quiz = pygame.image.load('./image/button/btn_quiz.png')
btn_quiz_hover = pygame.image.load('./image/button/btn_quiz_hover.png')

# Sounds
sound_goose = pygame.mixer.Sound('./sound/goose.ogg')

# Get size of object
cursor_rect = cursor.get_rect()


# -----------------------------
# Defining classes
# -----------------------------


class Button:
    def __init__(self, id, img_def, img_hov, text, text_size, position):
        # Center text
        font = pygame.font.Font('./font/opensans/OpenSans-Light.ttf', text_size)
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
                onclickAction(self)


# -----------------------------
# Defining functions
# -----------------------------


def init():
    print(pygame.font.get_fonts())
    pygame.mouse.set_visible(False)
    pygame.display.set_caption(title)
    pygame.display.set_icon(icon)

def vragen_ophalen(vragen):
    with open(vragen)as lees:
        text = lees.read()
    return(text)

def puntensysteem(antwoord, vraagnummer):
    systeem = {1: {'A': [2, 0, 0, 0], 'B': [1, 0, 0, 0], 'C': [0, 0, 0, 0]},
               2: {'A': [2, 0, 0, 0], 'B': [0, 2, 0, 0], 'C': [0, 0, 0, 2], 'D': [0, 0, 2, 0]},
               3: {'A': [2, 0, 0, 0], 'B': [1, 0, 0, 0], 'C': [0, 0, 0, 0], 'D': [-1, 0, 0, 0]},
               4: {'A': [0, 0, 0, 2], 'B': [0, 0, 0, 1], 'C': [0, 0, 0, 0]},
               5: {'A': [0, 0, 0, 2], 'B': [2, 0, 0, 0], 'C': [0, 0, 0, 0]},
               6: {'A': [0, 0, 2, 0], 'B': [2, 0, 0, 0], 'C': [0, 0, 0, 2], 'D': [0, 2, 0, 0]},
               7: {'A': [0, 0, 2, 0], 'B': [0, 2, 0, 0], 'C': [0, 0, 0, 0]},
               8: {'A': [0, 0, 2, 0], 'B': [0, 0, 1, 0], 'C': [0, 0, 0, 0]},
               9: {'A': [0, 2, 0, 0], 'B': [0, 0, 0, 2], 'C': [2, 0, 0, 0], 'D': [0, 0, 2, 0]},
               10: {'A': [2, 0, 0, 0], 'B': [0, 0, 2, 0], 'C': [0, 2, 0, 0], 'D': [0, 0, 0, 2]},
               11: {'A': [0, 1, 0, 0], 'B': [0, 2, 0, 0], 'C': [0, 0, 0, 0], 'D': [0, -1, 0, 0]},
               12: {'A': [0, 2, 0, 0], 'B': [0, 1, 0, 0], 'C': [0, 0, 0, 0]},
               13: {'A': [0, 0, 0, 2], 'B': [0, 0, 0, 1], 'C': [0, 0, 0, 0], 'D': [0, 0, 0, -1]},
               14: {'A': [0, 0, 2, 0], 'B': [0, 0, 1, 0], 'C': [0, 0, 0, 0], 'D': [0, 0, -1, 0]},
               15: {'A': [0, 0, 0, 2], 'B': [0, 0, 2, 0], 'C': [0, 2, 0, 0], 'D': [2, 0, 0, 0], 'E': [0, 0, 0, 0]}
               }
    vraagnummer -= 1
    punten = systeem[vraagnummer][antwoord]
    return punten

def draw_buttons(btn_list, event):
    for button in btn_list:
        if button.rect_img.collidepoint(pygame.mouse.get_pos()):
            screen.blit(button.img_hov, button.rect_img)
            screen.blit(button.text, button.rect_txt)
        else:
            screen.blit(button.img_def, button.rect_img)
            screen.blit(button.text, button.rect_txt)

        if event.type == pygame.MOUSEBUTTONDOWN:
            button.on_click(event)


def onclickAction(btn):
    global game_state
    global q_answered
    global q_count
    global iat
    global bdam
    global se
    global fict

    if game_state == "menu":
        if btn.id == 'start':
            game_state = "quiz"
        if btn.id == 'result':
            game_state = "result"
        if btn.id == 'quit':
            pygame.quit()
            sys.exit()
    elif game_state == "quiz":
        if btn.id == 0:
            antwrd = 'A'
        if btn.id == 1:
            antwrd = 'B'
        if btn.id == 2:
            antwrd = 'C'
        if btn.id == 3:
            antwrd = 'D'
        if btn.id == 4:
            antwrd = 'E'
        puntenreeks = puntensysteem(antwrd,q_count)
        iat += puntenreeks[0]
        bdam += puntenreeks[1]
        se += puntenreeks[2]
        fict += puntenreeks[3]
        q_answered = True
    elif game_state == "result":
        game_state = "menu"


def main():
    global game_state
    loop_active = True

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
            btn_list_menu = [Button('start', btn_menu, btn_menu_hover, 'Start', 24, (570, 145)),
                             Button('result', btn_menu, btn_menu_hover, 'Results', 24, (495, 200)),
                             Button('quit', btn_menu, btn_menu_hover, 'Quit', 24, (645, 200))]

            screen.fill((255, 255, 255))
            screen.blit(bg_menu, (0, 0))
            draw_buttons(btn_list_menu, event)
            screen.blit(cursor, cursor_rect)

        if game_state == "quiz":
            vragenlijst = vragen_ophalen('sorteerhoed_vragenlijst.txt')
            vragenlijst = vragenlijst.split('\n\n')
            vraagnummer = 0
            questions = {}
            answers = {}
            for vraag in vragenlijst:
                vraagnummer=vraagnummer+1
                split_vraag = vraag.split('\n')
                questions[vraagnummer]=split_vraag[0]
                split_vraag.remove(split_vraag[0])
                answers[vraagnummer] = split_vraag
            #questions = {
            #    1: "Question 1",
            #}
            #answers = {
            #    1: ["Answer 1", "Answer 2","test 3"],
            #}
            btn_locations = [(460, 315), (835, 315), (460, 420), (835, 420), (655, 525)]

            global q_answered
            global q_count
            a_count = 0

            if q_answered and q_count > len(questions):
                game_state = "result"
                q_count = 1
            elif q_answered and q_count <= len(questions):
                btn_list_quiz = []
                for a in answers[q_count]:
                    btn_list_quiz.append(Button(a_count, btn_quiz, btn_quiz_hover, answers[q_count][a_count], 24, btn_locations[a_count]))
                    font = pygame.font.Font('./font/opensans/OpenSans-SemiBold.ttf', 36)
                    text = font.render(questions[q_count], True, (0, 0, 0))
                    a_count += 1

                a_count = 0
                q_count += 1
                q_answered = False
            else:
                screen.fill((255, 255, 255))
                screen.blit(bg_quiz, (0, 0))
                draw_buttons(btn_list_quiz, event)
                screen.blit(cursor, cursor_rect)
                screen.blit(text, (640 - int(font.size(questions[q_count - 1])[0] / 2), 120))

        if game_state == "result":
            verdomme = 0
            screen.fill((255, 255, 255))
            if iat > bdam and iat > se and iat > fict:
                verdomme = 0
            elif bdam > iat and bdam > se and bdam > fict:
                verdomme = 1
            elif se > iat and se > bdam and se > fict:
                verdomme = 2
            elif fict > iat and fict > bdam and fict > se:
                verdomme = 3
            #else:
            #    resultaat = 4
            screen.blit(bg_result[verdomme], (0, 0))
            btn_list_result = [Button('back', btn_menu, btn_menu_hover, 'Back to Menu', 18, (570, 600))]
            draw_buttons(btn_list_result, event)
            screen.blit(cursor, cursor_rect)

        # Updates game screen & cursor
        screen.blit(cursor, cursor_rect)
        pygame.display.update()


# -----------------------------
# Calling defined function(s)
# -----------------------------


init()
main()
