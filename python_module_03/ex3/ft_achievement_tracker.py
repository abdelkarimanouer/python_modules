if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon',
               'perfectionist'}

    print("Player alice achievements:", alice.intersection(bob))
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)
    print()

    print("=== Achievement Analytics ===")
    print("All unique achievements:", alice.union(bob, charlie))
    print("Total unique achievements:", len(alice.union(bob, charlie)))
    print()

    print("Common to all players:", alice.intersection(bob, charlie))
    alice_only = alice - bob - charlie
    bob_only = bob - alice - charlie
    charlie_only = charlie - alice - bob
    rare = alice_only.union(bob_only, charlie_only)
    print("Rare achievements (1 player):", rare)
    print()

    print("Alice vs Bob common:", alice.intersection(bob))
    print("Alice unique:", alice.difference(bob))
    print("Bob unique:", bob.difference(alice))
