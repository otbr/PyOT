mutated_rat = genMonster("Mutated Rat", 305, 9871)
mutated_rat.health(550)
mutated_rat.type("blood")
mutated_rat.defense(armor=35, fire=1.1, earth=0, energy=1, ice=1, holy=0.9, death=0, physical=1, drown=0)
mutated_rat.experience(450)
mutated_rat.speed(245)
mutated_rat.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
mutated_rat.walkAround(energy=0, fire=0, poison=0)
mutated_rat.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
mutated_rat.voices("Grrrrrrrrrrrrrr!", "Fcccccchhhhhh")
mutated_rat.melee(155, condition=CountdownCondition(CONDITION_POISON, 5), conditionChance=100)
mutated_rat.loot( (2235, 1.0), ("skull", 20.5), ("stone herb", 4.75), ("halberd", 3.0), ("mutated rat tail", 4.0), (2148, 100, 130), ("plate shield", 4.0), ("spellbook of enlightenment", 0.5), ("health potion", 0.5), ("green mushroom", 1.5), ("stealth ring", 0.5), ("tower shield", 0.0025) )
