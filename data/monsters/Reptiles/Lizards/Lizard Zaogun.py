lizard_zaogun = genMonster("Lizard Zaogun", 343, 11284)
lizard_zaogun.health(2955)
lizard_zaogun.type("blood")
lizard_zaogun.defense(armor=46, fire=0.55, earth=0, energy=0.8, ice=0.85, holy=1, death=0.9, physical=0.5, drown=1)
lizard_zaogun.experience(1700)
lizard_zaogun.speed(420)
lizard_zaogun.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=150)
lizard_zaogun.walkAround(energy=0, fire=0, poison=0)
lizard_zaogun.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
lizard_zaogun.voices("Hissss!", "Cowardzz!", "Softzzkinzz from zze zzouzz!", "Zztand and fight!")
lizard_zaogun.melee(350)
lizard_zaogun.loot( ("great health potion", 13.25, 3), ("zaoan shoes", 1.0), ("zaogun flag", 6.0), ("small emerald", 8.0, 5), (2148, 100, 289), ("lizard scale", 7.0, 3), ("red lantern", 2.0), ("platinum coin", 7.25, 2), ("lizard leather", 1.0), ("strong health potion", 2.0), ("tower shield", 1.0), ("zaoan legs", 0.75), ("zaoan armor", 0.5) )