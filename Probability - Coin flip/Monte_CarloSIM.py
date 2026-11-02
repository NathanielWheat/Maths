import random

experiments = 10_000
successful_experiments = 0

for _ in range(experiments):
    flips = [random.choice(["H", "T"]) for _ in range(100)]

    has_run = False
    consecutive_heads = 0

    for flip in flips:
        if flip == "H":
            consecutive_heads += 1
        else:
            consecutive_heads = 0

        if consecutive_heads == 5:
            has_run = True
            break

    if has_run:
        successful_experiments += 1

probability = successful_experiments / experiments

print(f"Estimated probability: {probability:.2%}")