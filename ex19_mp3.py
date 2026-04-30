#Programa que ebra e reproduza o áudio de um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('Local do arquivo mp3')
pygame.mixer.music.play()
pygame.event.wait()