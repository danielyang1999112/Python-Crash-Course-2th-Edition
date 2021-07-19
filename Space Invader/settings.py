class Settings:
    """Storage for Space Invader settings classes"""

    def __init__(self):
        """Initializing game settings"""
        # Screen
        self.screen_width = 1600
        self.screen_height = 900
        self.bg_color = (230, 230, 230)

        # Ship
        self.ship_speed = 2
        self.ship_limit = 3

        # Bullet
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 for right, -1 for left
        self.fleet_direction = 1

        # Fast speed and Higher score
        self.speedup_scale = 1.1
        self.score_scale = 25

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initializing changing pace"""
        self.ship_speed = 2.0
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1

        # score
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed += self.speedup_scale

        self.bullet_speed *= self.speedup_scale
        self.bullet_width += 1
        self.bullet_height += 1
        self.bullets_allowed += 1

        self.alien_speed *= self.speedup_scale
        self.alien_points += self.score_scale
