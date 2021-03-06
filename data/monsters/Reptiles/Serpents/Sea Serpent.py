sea_serpent = genMonster("Sea Serpent", 275, 8307)
sea_serpent.health(1750)
sea_serpent.type("blood")
sea_serpent.defense(armor=27, fire=0.7, earth=1, energy=1.05, ice=0, holy=1, death=0.9, physical=1.1, drown=0)
sea_serpent.experience(2300)
sea_serpent.speed(300)
sea_serpent.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=300)
sea_serpent.walkAround(energy=0, fire=0, poison=0)
sea_serpent.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
sea_serpent.voices("CHHHRRRR", "HISSSS")
sea_serpent.melee(250)
sea_serpent.loot( (2148, 100, 244), ("stealth ring", 0.5), ("dragon ham", 60.25), ("small sapphire", 8.0, 3), ("strong health potion", 4.75), ("sea serpent scale", 10.25), ("plate legs", 7.25), ("strong mana potion", 4.0), ("serpent sword", 4.0), ("glacier amulet", 1.0), ("northwind rod", 1.0), ("spirit cloak", 3.0), ("great mana potion", 1.0), ("focus cape", 0.5), ("glacier kilt", 0.5), ("ring of healing", 1.25), ("crystalline armor", 0.0025), ("leviathan's amulet", 0.0025) )