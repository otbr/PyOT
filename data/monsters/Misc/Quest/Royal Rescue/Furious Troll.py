furious_troll = genMonster("Furious Troll", 281, 7926)
furious_troll.health(245)
furious_troll.type("blood")
furious_troll.defense(armor=13, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1.05, drown=1)
furious_troll.experience(185)
furious_troll.speed(195)#incorrect
furious_troll.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
furious_troll.walkAround(energy=0, fire=0, poison=0)
furious_troll.immunity(paralyze=0, invisible=1, lifedrain=0, drunk=0)
furious_troll.voices("Slice! Slice!", "DIE!!!")
furious_troll.summon("Mechanical Fighter", 10)
furious_troll.melee(100)
furious_troll.loot( (2148, 100, 149), ("platinum coin", 7.0), ("bunch of troll hair", 4.5) )