#!/usr/bin/env python3


def event_stream(n):
    players = ("alice", "bob", "charlie")
    events = ("killed monster", "found treasure", "leveled up")
    for i in range(n):
        player = players[i % len(players)]
        level = (i % 3) % 20 + 1
        event = events[i % len(events)]
        yield (i + 1, player, level, event)


def fibonacci_sequence() -> int:
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        first_num, second_num = second_num, first_num + second_num


def prime_numbers() -> None:
    num = 2

    while True:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num

        num += 1


print("=== Game Data Stream Processor ===")
total_event: int = 0
high_level: int = 0
treasure: int = 0
level_up: int = 0

print("Processing 1000 game events...")
print()

total: int = 0
for event_id, player, level, event in event_stream(1000):
    total += 1
    if level >= 10:
        high_level += 1
    if event == "found treasure":
        treasure += 1
    if event == "leveled up":
        level_up += 1
    if event_id < 4:
        print(f"Event {event_id}: Player {player} (level {level}) {event}")

print("...")
print()

print("=== Stream Analytics ===")
print(f"Total events processed: {total}")
print(f"High-level players (10+): {high_level}")
print(f"Treasure events: {treasure}")
print(f"Level-up events: {level_up}")
print()

print("Memory usage: Constant (streaming)")
print()

print("=== Generator Demonstration ===")
fibonacci = fibonacci_sequence()
print("Fibonacci sequence (first 10): ", end="")
for num in range(10):
    value = next(fibonacci)
    if num < 9:
        print(value, end=", ")
    else:
        print(value)

prime = prime_numbers()
print("Prime numbers (first 5): ", end="")
for i in range(5):
    value = next(prime)
    if i < 4:
        print(value, end=", ")
    else:
        print(value)

