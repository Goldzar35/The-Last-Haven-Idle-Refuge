class Fortification:
    def __init__(self, player):
        '''Initialize the Fortification entity'''
        self.player = player
        self.background_index = 0

    def change_background(self, backgrounds):
        '''Change the background image for the Fortification menu'''
        self.background_index = (self.background_index + 1) % backgrounds
