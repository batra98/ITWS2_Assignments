import BULLETMAIN


class Bullet(BULLETMAIN.bulletmain):

    def __init__(self, x, y, pyg_font):

        BULLETMAIN.bulletmain.__init__(self, x, y, pyg_font)
        self.char = '*'

        self.surface = self.font.render(self.char, False, [255, 225, 25])
        self.speed = -5
        self.updated = True
