import time

import pygame
import sys
from src.config import *
from src.entites.player import Player
from src.key_listener import key_listener
from src.menu import Menu, font_path
from src.user_interface import UserInterface
from src.utils import initLevels


def init():
    global display, clock, player, ui, levels, level_index

    pygame.init()
    display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(DISPLAY_CAPTION)
    clock = pygame.time.Clock()
    player = Player(600, 300)
    ui = UserInterface(player)

    levels, level_index = initLevels(display, player), 0
    levels[level_index].current_room.update_info_about_room()

    pygame.mixer.music.load('assets/sounds/bg.wav')


def intro_menu(screen):
    background_image = pygame.transform.scale(pygame.image.load("assets/intro.png").convert(), (1280, 768))
    delay = 15
    prev_time = time.time()
    text = "Бог Войны продолжал искать покой после смерти своей семьи, \nсвергнув некоторых Богов он не обрёл своё " \
           "счастье. Кратоса \nпостоянно угнетали мысли о семье, поэтому \nон решается спуститься в ужасные лабиринты \n" \
           "Аида и отомстить за всё зло, которое ему причинили."

    while time.time() - prev_time < delay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game()

        screen.blit(background_image, (0, 0))

        lines = text.splitlines()
        for i, l in enumerate(lines):
            screen.blit(pygame.font.Font(font_path, 25).render(l, 0, "white"), (30, 640 + 24 * i))

        pygame.display.update()


def show_start_menu(screen):
    start_menu = Menu(["Старт", "Выход"])

    background_image = pygame.transform.scale(pygame.image.load("assets/bg_img.jpg").convert(), (1280, 768))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                option = start_menu.handle_event(event)
                if option == "Старт":
                    return True
                elif option == "Выход":
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))

        start_menu.draw(screen, SCREEN_WIDTH - 50, 50, 30)
        pygame.display.flip()


def pause_menu():
    pause_menu = Menu(["Продолжить", "Вернуться в меню"])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                option = pause_menu.handle_event(event)
                if option == "Продолжить":
                    return False
                elif option == "Вернуться в меню":
                    return True

        display.fill((0, 0, 0))
        pause_menu.draw(display, SCREEN_WIDTH - 50, 50, 30)
        pygame.display.flip()


def end_menu(display):
    end_menu = Menu(["Выход"])

    pygame.mixer.music.stop()
    pygame.mixer.Sound('assets/sounds/win.wav')
    pygame.mixer.music.load('assets/sounds/bg.wav')
    pygame.mixer.music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                option = end_menu.handle_event(event)
                if option == "Выход":
                    pygame.quit()
                    sys.exit()

        display.fill((0, 0, 0))
        game_over_text = pygame.font.Font(font_path, 60).render("Ты прошёл игру!", True, (255, 0, 0))
        game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        display.blit(game_over_text, game_over_text_rect)
        end_menu.draw(display, SCREEN_WIDTH - 50, 50, 30)
        pygame.display.flip()


def game():
    global level_index

    game_over_font = pygame.font.Font(font_path, 60)
    button_font = pygame.font.Font(font_path, 30)
    restart_button = button_font.render("*Рестарт", True, (255, 255, 255))
    restart_button_rect = restart_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    is_playing = show_start_menu(display)
    if is_playing:
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.1)

    while is_playing:
        is_paused = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                elif event.key == pygame.K_ESCAPE and not is_paused:
                    pygame.mixer.music.pause()
                    is_paused = True
                elif event.key == pygame.K_RETURN and player.is_dead:
                    main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.attack(levels[level_index].current_room.enemies)

        if is_paused:
            is_paused = pause_menu()
            if is_paused:
                is_playing = show_start_menu(display)
        else:
            display.fill((0, 0, 0))
            if player.is_dead:
                game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
                game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                display.blit(game_over_text, game_over_text_rect)
                display.blit(restart_button, restart_button_rect)
            else:
                levels[level_index].draw()

                keys = pygame.key.get_pressed()
                key_listener(keys, player)

                if keys[pygame.K_e]:
                    if player.checkPortal():
                        if level_index + 1 == len(levels):
                            end_menu(display)

                        else:
                            pygame.mixer.Sound(SOUND_TELEPORT).play()
                            pygame.mixer.music.stop()
                            pygame.mixer.music.play()
                            level_index += 1
                            levels[level_index].current_room.update_info_about_room()
                    levels[level_index].changeRoom(player)
                    if level_index == 4 and levels[level_index].current_room.is_last_room:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('assets/sounds/boss.mp3')
                        pygame.mixer.music.play()

                player.update(display)
                ui.update(display)

            clock.tick(TICK_RATE)
            pygame.display.update()


def main():
    init()
    while True:
        # game()
        intro_menu(display)

if __name__ == '__main__':
    main()
