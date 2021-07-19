import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Initializing button"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # design size and features for button
        self.width, self.height = 400, 100
        self.button_color = (0, 200, 200)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # creating rect for button, and place it in center
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # only creating it once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """rendering as image"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # fill the button with color and then write the text
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)