#!/usr/bin/env python3
# encoding: utf-8

import sys, pygame

from util import *
from Contest import Contest

class Handler (object):
    contest = None

    def __init__(self):
        self.nextHandler = self
        self.oldTime = self.newTime = pygame.time.get_ticks()

    def on_event(self, event):
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.display.quit()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            pygame.mixer.music.unpause()
        return False
    
    def delta(self):
        deltaTime = self.newTime - self.oldTime
        if deltaTime < 100:
            return deltaTime
        return 0

    def tick(self):
        self.newTime, self.oldTime = pygame.time.get_ticks(), self.newTime
        gTimer.tick(self.delta())
        return self.nextHandler
