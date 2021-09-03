# ----- Window --------------------------------------
WIDTH, HEIGHT = 600,600

# ----- Colors --------------------------------------
BLACK = (0,0,0)
GRAY = (100,100,100)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (252,227,0)

class ScoreController:
    def __init__(self, screen, score, win, font):
        self._screen = screen
        self.score = score
        self.miss = 0
        self.win = win
        self._font = font

        self._scoreText = "Your score: 0"
        self._missText = "You missed: 0"
    
    def getScore(self) -> int:
        return self.score

    def getMiss(self) -> int:
        return self.miss

    def toString(self,type) -> str:
        if type == "score":
            return str(self.score)
        elif type == "miss":
            return str(self.miss)

    def setScore(self,score):
        self.score = score

    def incrScore(self):
        self.score += 1

    def incrMiss(self):
        self.miss += 1

    def isWon(self) -> bool:
        return self.score >= self.win

    def update(self):
        self.scoreText = "You score: " + str(self.score)
        self.missText = "You missed: " + str(self.miss)

    def draw(self):
        str = self._font.render(self._scoreText, 1, BLACK)

        self._screen.blit(str, (WIDTH//2 - str.get_width()//2, 30))

        str = self._font.render(self._missText, 1, BLACK)

        self._screen.blit(str, (WIDTH//2 - str.get_width()//2, 70))
