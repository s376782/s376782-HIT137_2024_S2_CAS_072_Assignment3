import pygame
from typing import Any, override
from contracts.screen_interfaces import IPlayScreen, IRollScreen
from settings import SCREEN_WIDTH

bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, direction):
		super().__init__()
		self.speed = 10
		self.image = bullet_img
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.direction = direction

	@override
	def update(self, *args: Any, **kwargs: Any) -> None:
		screen = args[0]
		if screen and isinstance(screen, IRollScreen):
			# move bullet
			self.rect.x += (self.direction*self.speed) + screen.get_screen_scroll()

			# check if bullet has gone off screen
			if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
				self.kill()
		
		if screen and isinstance(screen, IPlayScreen):
			if pygame.sprite.spritecollide(self, screen.get_obstacle_group(), False):
				# check for collision with level
				self.kill()

			# check collision with player
			player = screen.get_player()
			if player.alive and pygame.sprite.collide_rect(player, self):
				player.health -= 5
				self.kill()
			
			# check collision with enemies
			for enemy in screen.get_enemy_group():
				if enemy.alive and pygame.sprite.collide_rect(enemy, self):
					enemy.health -= 25
					self.kill()