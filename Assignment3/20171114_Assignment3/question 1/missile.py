import BULLETMAIN


class missile(BULLETMAIN.bulletmain):
    def __init__(self, x, y, pyg_font):
        BULLETMAIN.bulletmain.__init__(self, x, y, pyg_font)
        self.char = '|'
        self.surface = self.font.render(self.char, False, [230, 25, 75])
        self.speed = -10
        self.updated = False
