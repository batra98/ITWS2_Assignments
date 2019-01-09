
class bulletmain:
    def __init__(self, x, y, pyg_font):
        self.x = x
        self.y = y
        self.font = pyg_font

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def move(self, screen):
        if self.y > -100:
            self.y += self.speed

    def hit(self, a, b, d):
        if a < self.x < a+d:
            if b+d > self.y > b:
                return True
