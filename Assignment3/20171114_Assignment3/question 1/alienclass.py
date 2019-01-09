class Aliens:
    def __init__(self, x, y, d, pyg_font, pyg_time):
        self.x = x
        self.y = y
        self.d = d
        self.char = 'Y'
        self.char2 = 'y'
        self.time = pyg_time
        self.font = pyg_font
        self.surface = self.font.render(self.char, False, [230, 25, 75])
        self.font1 = pyg_font
        self.surface1 = self.font1.render(self.char2, False, [255, 225, 25])
        self.new = True

    def draw(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def draw2(self, screen):
        screen.blit(self.surface1, (self.x, self.y))
