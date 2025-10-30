from ants import GameState, Hive, AssaultPlan, dry_layout, interactive_strategy, ant_types

beehive = Hive(AssaultPlan().add_wave(bee_type=None, bee_health=3, time=2, count=3))
gamestate = GameState(interactive_strategy, beehive, ant_types(), dry_layout, (3, 9), food=10)

print("Starting Ant Colony Simulation...")
gamestate.simulate()
