#!/usr/bin/env python3
# encoding: utf-8

import random
import sys
import math
import time
import pygame
import os



Rect = pygame.Rect

from util import *
from Team import Team
from Handler import *
from Contest import Contest
from pygame import mixer

currentDirectory = os.getcwd()
strin = currentDirectory + "\\musicas\\"
songName = os.listdir(strin)


#songName=["Tongo","sky","beegees","Ghost3","Epic","Banheira","taste","JetQueer","eiffel65","panamericano","iwantbreakfree","underground","theoutfield","faith","FollowYou","Samin","Momentos","thisgirl","Vengaboys","chinara","jump","VolbeatCrown","PiratasCaribe","Laurent","Feeling","Pharrell","Cant","eradivano","maroonsugar","stand","seconds","Nickelback","chariots","aviciilevels","TheScore"]
songNameChampions=["92-rock.mp3","91-Final.mp3","93-champions.mp3","94-senna.mp3","90-chariots.mp3"]
COUNT = -1
CONT = -1
teamRank = 0
QtdeMusicas = len(songName)


class TeamHandler (Handler):
    def __init__(self, teamID, returnTo, timeout = 5000.0):
        Handler.__init__(self)
        if teamID is None:
            teamID = random.choice(list(Handler.contest.teamMap.keys()))
        self.team = Team(teamID)
        self.returnTo = returnTo

        self.teamPhoto = Handler.contest.teamPhotos.get(teamID)

        self.timeout = timeout
        self.timeoutTimer = Timer()

        pygame.mouse.set_visible(False)
    
    def on_event(self, event):

        if Handler.on_event(self, event):

                return True
        #if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_PAGEDOWN:

            if self.timeoutTimer.clock > 500:
                self.nextHandler = self.returnTo
                BLACK = (0, 0, 0)
                WHITE = (255, 255, 255)
                font = pygame.font.SysFont(None, 25)
                if teamRank <= 4:
                    pygame.mixer.init()
                    global CONT
                    CONT = (CONT+1)
                    pygame.mixer.music.load(strin + songNameChampions[CONT])
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.2)
                    volume = 0.2
                    coluna= 70
                    text = font.render("Volume: {:.1f}".format(volume), True, WHITE,BLACK)
                    #text = font.render('Volume: ', True, WHITE,BLACK)
                    get_screen().blit(text, [6,6])
                    pygame.display.flip()
                    while 1:
                        event = pygame.event.wait()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_PAGEUP:
                                coluna = coluna +1
                                volume = volume+0.1
                                text = font.render("Volume: {:.1f}".format(volume), True, WHITE,BLACK)
                                #text = font.render('|', True, WHITE)
                                #get_screen().blit(text, [coluna,6])
                                get_screen().blit(text, [6,6])
                                pygame.display.flip()
                                print('volume ',volume)
                                pygame.mixer.music.set_volume(volume)
                                if volume > 0.8:
                                    break
                else:
                    pygame.mixer.init()
                    global COUNT
                    global QtdeMusicas
                    COUNT = (COUNT+1) % (QtdeMusicas - 4)
                    pygame.mixer.music.load(strin + songName[COUNT])
                    pygame.mixer.music.play()
                    pygame.mixer.music.set_volume(0.2)
                    volume = 0.2
                    coluna= 70
                    text = font.render("Volume: {:.1f}".format(volume), True, WHITE,BLACK)
                    #text = font.render('Volume: ', True, WHITE,BLACK)
                    get_screen().blit(text, [6,6])
                    pygame.display.flip()
                    while 1:
                        event = pygame.event.wait()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_PAGEUP:
                                coluna = coluna +1
                                volume = volume+0.1
                                text = font.render("Volume: {:.1f}".format(volume), True, WHITE,BLACK)
                                #text = font.render('|', True, WHITE)
                                #get_screen().blit(text, [coluna,6])
                                get_screen().blit(text, [6,6])
                                pygame.display.flip()
                                print('volume ',volume)
                                pygame.mixer.music.set_volume(volume)
                                if volume > 0.8:
                                    break
    def tick(self):
        Handler.tick(self)
        

        if self.teamPhoto == None: # no point being in this handler
            return self.returnTo

        self.timeoutTimer.tick(self.delta())
        if self.timeout and self.timeoutTimer.clock > self.timeout:
            self.nextHandler = self.returnTo

        Handler.contest.rank_teams()
        global teamRank
        teamRank = [_[0] for _ in Handler.contest.teamRanking
            if _[1] == self.team.key][0]

        teamUni, teamName = Handler.contest.teamMap[self.team.key]

        get_screen().fill((0, 0, 0))

        block_blit(get_screen(),
            render(font('bold', 48), teamUni, '#FFFFFFi'),
            (0, 48, 1024, 0), 'ct')
         
        block_blit(get_screen(),
            render(font('roman', 36), teamName, '#FFFFFF'),
            (0, 104, 1024, 0), 'ct')

        block_blit(get_screen(), self.teamPhoto, (0, 156, 1024, 504), 'cc')


        block_blit(get_screen(),
            render(font('italic', 52), teamRank, '#999999'),
            (0, 680, 60, 60), 'rc')

        get_screen().blit(self.team.draw(True), (68, 680))

        pygame.display.flip()
        pygame.mixer.music.stop()
        return self.nextHandler
        
