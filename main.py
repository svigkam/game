import pygame
import sys
from src.config import *
from src.entites.player import Player
from src.key_listener import key_listener
from src.menu import Menu, font_path
from src.user_interface import UserInterface
from src.utils import initLevels

pygame.init()
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(DISPLAY_CAPTION)
clock = pygame.time.Clock()
player = Player(600, 300)

level = initLevels(display, player)

new_room_info = "Null"

def show_start_menu(screen):
    start_menu = Menu(["Start", "Exit"])

    background_image = pygame.image.load("assets/bg_img.jpg").convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                option = start_menu.handle_event(event)
                if option == "Start":
                    return True
                elif option == "Exit":
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))

        start_menu.draw(screen, SCREEN_WIDTH - 50, 50, 30)
        pygame.display.flip()

def pause_menu():
    pause_menu = Menu(["Continue", "Return to Menu"])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                option = pause_menu.handle_event(event)
                if option == "Continue":
                    return False
                elif option == "Return to Menu":
                    return True

        display.fill((0, 0, 0))
        pause_menu.draw(display, SCREEN_WIDTH - 50, 50, 30)
        pygame.display.flip()


def game():
    game_over_font = pygame.font.Font(font_path, 60)
    button_font = pygame.font.Font(font_path, 30)
    restart_button = button_font.render("*Restart", True, (255, 255, 255))
    restart_button_rect = restart_button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

    is_playing = show_start_menu(display)

    while is_playing:
        is_paused = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and is_paused:
                    is_paused = False
                elif event.key == pygame.K_ESCAPE and not is_paused:
                    is_paused = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                btn = pygame.mouse.get_pressed()
                player.attack(level.current_room.enemies)

        if is_paused:
            is_paused = pause_menu()
            if is_paused:
                is_playing = show_start_menu(display)
        else:
            if player.is_dead:
                game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
                game_over_text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                display.fill((0, 0, 0))
                display.blit(game_over_text, game_over_text_rect)
                display.blit(restart_button, restart_button_rect)
            else:
                # display.fill((0, 0, 0))
                level.draw()

                keys = pygame.key.get_pressed()
                key_listener(keys, player, level)
                player.update(display)

            clock.tick(TICK_RATE)  # fps
            pygame.display.update()


ui = UserInterface(player)

def game_loop():
    display.fill((0, 0, 0))
    level.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            btn = pygame.mouse.get_pressed()
            player.attack(level.current_room.enemies)


    keys = pygame.key.get_pressed()
    key_listener(keys, player, level)
    player.update(display)
    ui.update(display)

    clock.tick(TICK_RATE)  # fps
    pygame.display.update()


def main():
    while True:
        game_loop()


if __name__ == '__main__':
    main()
