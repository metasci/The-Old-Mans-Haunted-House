#-----------------------------------
# THIS IS THE MAP
#-----------------------------------
import game_scenes

class Map(object):

    scenes = {
        'death': game_scenes.Death(),
        'front_gate': game_scenes.FrontGate(),
        'yard': game_scenes.Yard(),
        'shed': game_scenes.Shed(),
        'garden': game_scenes.Garden(),
        'bed_1': game_scenes.BedOne(),
        'hall': game_scenes.Hall(),
        'bed_2': game_scenes.BedTwo(),
        'bed_3': game_scenes.BedThree(),
        'bed_4': game_scenes.BedFour(),
        'living_room': game_scenes.LivingRoom(),
        'cellar': game_scenes.Cellar(),
        'roof': game_scenes.Roof(),
        'atticd': game_scenes.Attic(),
        'finished': game_scenes.Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
        
        
        
        
        
