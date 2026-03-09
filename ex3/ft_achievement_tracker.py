#!/usr/bin/env python3

print("=== Achievement Tracker System ===")
print()
alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
print(f"Player alice achievements: {alice}")
bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
print(f"Player bob achievements: {bob}")
charlie = {
   'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'
}
print(f"Player charlie achievements: {charlie}")
print()
print("=== Achievement Analytics ===")
uni = alice.union(bob, charlie)
print(f"All unique achievements: {uni}")
print(f"Total unique achievements: {len(uni)}")
print()
inters = alice.intersection(bob, charlie)
print(f"Common to all players: {inters}")
alice_int_bob = alice.intersection(bob)
alice_int_charlie = alice.intersection(charlie)
bob_int_charlie = bob.intersection(charlie)
rare = uni.difference(
   inters, alice_int_bob, alice_int_charlie, bob_int_charlie
)
print(f"Rare achievements (1 player): {rare}")
print()
alice_vs_bob = alice.difference(bob)
print(f"Alice vs Bob common: {alice_vs_bob}")
uni_alice = alice.difference(bob)
print(f"Alice unique: {uni_alice}")
uni_bob = bob.difference(alice)
print(f"Bob unique: {uni_bob}")
