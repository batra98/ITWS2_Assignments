class spaceship:

    def __init__(self, x, y, pyg_font):
        self.x = x
        self.y = y
        self.char = 'M'
        self.font = pyg_font
        self.surface = self.font.render(self.char, False, [245, 130, 48])

    def draw(self, screen, surf, flip):
        screen.blit(self.surface, (self.x, self.y))
        screen.blit(surf, (275, 20))
        flip()
