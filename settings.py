from game_data import level_map

class Settings():
    
    def __init__(self):
        
        #screen setting        
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = 0,0,0
        self.background_multiplier = 10
        
        # level setting
        self.tile_size = self.screen_height /10.3
        
        #overworld setting
        self.start_level = 0
        self.current_level = 1
        self.max_level = 1        
        
        self.mario_limit = 3
        
        # camera
        CAMERA_BORDERS = {
            'left': 100,
            'right': 200,
            'top': 100,
            'bottom': 150
        }