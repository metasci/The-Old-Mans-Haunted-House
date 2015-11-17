
import game_map
import engine



a_map = game_map.Map('front_gate')
a_game = engine.Engine(a_map)
a_game.play()
