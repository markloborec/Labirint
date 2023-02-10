import pygame
from settings import *
from tile import Tile
from player import Player
from coin import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.player = None
        self.coins = []
        self.text = None
        self.max_coins = 0





    def setup_level(self,level):
        for i in level:
            self.max_coins += i.count("O")
        print(self.max_coins)
        for row_index,row in enumerate (level):
            for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE
                if col == "X":
                    Tile((x,y),[self.visible_sprites, self.collision_sprites])
                if col == "P":
                    self.player = Player((x,y),[self.visible_sprites,self.active_sprites], self.collision_sprites)
                if col == "O":
                    coin = Coin((x,y),[self.visible_sprites, self.collision_sprites])
                    self.coins.append(coin)


    def run(self):
        self.active_sprites.update()
        for coin in self.coins:
            dx = coin.rect.x - self.player.rect.x
            dy = coin.rect.y - self.player.rect.y
            distanca = (dx**2 + dy**2)**0.5
            if distanca < 30:
                coin.kill()
                self.coins.remove(coin)
                self.player.points += 1
        self.text = FONT.render(f"Points: {self.player.points}",False,TEXT_COLOR)
        self.visible_sprites.draw(self.display_surface)
        self.display_surface.blit(self.text,[0,0])
        if self.player.points == self.max_coins:
            return False
        else:
            return True




