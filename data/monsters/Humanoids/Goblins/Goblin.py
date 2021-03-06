goblin = genMonster("Goblin", 61, 6002)
goblin.health(50)
goblin.type("blood")
goblin.defense(armor=7, fire=1, earth=1.1, energy=0.8, ice=1, holy=0.8, death=1.1, physical=1, drown=1)
goblin.experience(25)
goblin.speed(200)
goblin.behavior(summonable=290, hostile=True, illusionable=True, convinceable=290, pushable=True, pushItems=False, pushCreatures=False, targetDistance=1, runOnHealth=10)
goblin.walkAround(energy=1, fire=1, poison=1)
goblin.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
goblin.voices("Zig Zag! Gobo attack!", "Me green, me mean!", "Bugga! Bugga!", "Help! Goblinkiller!", "Me have him!")
goblin.melee(10)
goblin.distance(25, ANIMATION_SMALLSTONE, chance(21))
goblin.loot( ("goblin ear", 1.0), ("dagger", 1.5), ("bone", 1.25), ("leather helmet", 1.75), ("bone club", 4.75), ("short sword", 9.0), (2235, 0.75), ("leather armor", 2.75), ("small axe", 10.5), ("fish", 13.0), (2148, 100, 9), ("small stone", 15.25) )