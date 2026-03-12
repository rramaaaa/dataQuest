#!/usr/bin/env python3

if __name__ == "__main__":
    players = ["alice", "bob", "charlie", "diana"]
    scores = {"alice": 2300, "bob": 1800, "charlie": 2150, "diana": 2050}
    achievements = {"alice": ["first_kill", "level_10",
                              "boss_slayer", "treasure_hunter"],
                    "bob": ["first_kill", "level_10",
                            "boss_slayer", "collector"],
                    "charlie": ["level_10", "treasure_hunter",
                                "boss_slayer", "speed_demon", "perfectionist"],
                    "diana": ["boss_slayer", "collector"]}
    regions = {"alice": "north", "bob": "north",
               "charlie": "east", "diana": "central"}

    status = {"alice": 1, "bob": 0, "charlie": 1, "diana": 1}
    print("=== Game Analytics Dashboard ===")
    print()
    print("=== List Comprehension Examples ===")
    high_scorers = [name for name in players if scores[name] > 2000]
    scores_doubled = [scores[player] * 2 for player in players]
    active_players = [player for player in players if status[player] == 1]
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {scores_doubled}")
    print(f"Active players: {active_players}")
    print()
    print("=== Dict Comprehension Examples ===")
    score_categories = {
            "high": len([score for score in scores if scores[score] > 2000]),
            "medium": len([score for score in scores
                           if 1500 < scores[score] <= 2000]),
            "low": len([score for score in scores if scores[score] <= 1500])
    }

    achievement_counts = {name: len(achievements[name]) for name in players}
    print(f"Player scores: {scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}")
    print()
    print("=== Set Comprehension Examples ===")
    unique_players = {name for name in players}
    unique_achievements = {a for p in players for a in achievements[p]}
    active_regions = {regions[r] for r in active_players}
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}")
    print()
    print("=== Combined Analysis ===")
    total_players = len(unique_players)
    total_unique_achievements = len(unique_achievements)
    average_score = sum(scores[p] for p in players) / total_players
    top_performer = max(players, key=lambda p: scores[p])
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {average_score: .2f}")
    print(f"Top performer: {top_performer} ({scores[top_performer]}", end="")
    print(f" points, {len(achievements[top_performer])} achievements)")
    print()
