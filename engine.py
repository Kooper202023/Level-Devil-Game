import pygame

class GameLevel:
    def __init__(self, level_data):
        self.player = pygame.Rect(50, 300, 30, 30)
        self.gate = pygame.Rect(750, 300, 40, 50)
        self.floors = []
        for floor in level_data["floors"]:
            self.floors.append({
                "rect": pygame.Rect(floor["x"], floor["y"], floor["w"], floor["h"]),
                "direction": floor["direction"],
                "range": floor["range"],
                "speed": floor["speed"],
                "start": floor["y"]
            })

    def update(self):
        for floor in self.floors:
            if floor["direction"] == "updown":
                floor["rect"].y += floor["speed"]
                if abs(floor["rect"].y - floor["start"]) > floor["range"]:
                    floor["speed"] *= -1

    def check_collision(self):
        for floor in self.floors:
            if self.player.colliderect(floor["rect"]):
                return True
        return False

    def is_level_completed(self):
        return self.player.colliderect(self.gate)