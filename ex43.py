from ex43_classes import (
            Scene, Engine, Map,
            Death,
            CentralCorridor,
            LaserWeaponArmory,
            TheBridge,
            EscapePod,
            Finished 
            )

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
