#!/usr/bin/env python3


print("=== Game Analytics Dashboard ===")

players = ["alice", "bob", "charlie", "diana"]
scores = [2300, 1800, 2150, 2050]
active_players = ["alice", "bob", "charlie"]
achievements = [
    ("alice", "first_kill"),
    ("alice", "level_10"),
    ("bob", "first_kill"),
    ("charlie", "boss_slayer"),
    ("charlie", "level_10"),
    ("charlie", "first_kill"),
]

regions = ["north", "east", "central", "north"]

print("=== List Comprehension Examples ===")

high_scorers = [players[i] for i in range(len(scores)) if scores[i] > 2000]
print(f"High scorers (>2000): {high_scorers}")

scores_doubled = [s * 2 for s in scores]
print(f"Scores doubled: {scores_doubled}")

active = [p for p in active_players]
print(f"Active players: {active}")

print("=== Dict Comprehension Examples ===")

player_scores = {players[i]: scores[i] for i in range(len(players))}
print(f"Player scores: {player_scores}")

score_categories = {
    "high": len([s for s in scores if s > 2000]),
    "medium": len([s for s in scores if 1500 <= s <= 2000]),
    "low": len([s for s in scores if s < 1500])
}
print(f"Score categories: {score_categories}")

achievement_counts = {
    p: len([a for (player, a) in achievements if player == p])
    for p in players
}
print(f"Achievement counts: {achievement_counts}")

print("=== Set Comprehension Examples ===")

unique_players = {p for p in players}
print(f"Unique players: {unique_players}")

unique_achievements = {a for (_, a) in achievements}
print(f"Unique achievements: {unique_achievements}")

active_regions = {r for r in regions}
print(f"Active regions: {active_regions}")

print("=== Combined Analysis ===")

total_players = len(players)
print(f"Total players: {total_players}")

total_unique_achievements = len(unique_achievements)
print(f"Total unique achievements: {total_unique_achievements}")

average_score = sum(scores) / len(scores)
print(f"Average score: {average_score}")

top_index = scores.index(max(scores))
top_player = players[top_index]
top_score = scores[top_index]
top_achievements = achievement_counts[top_player]

print(f"Top performer: {top_player} ({top_score} points, {top_achievements} achievements)")
