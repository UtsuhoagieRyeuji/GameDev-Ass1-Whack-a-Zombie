from .Image import Image

class Zombie(Image):
    def __init__(self, screen, x, y, image, width, height):
        super().__init__(screen, x, y, image, width, height)