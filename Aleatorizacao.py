import random
import pandas as pd
# List of participants
participants = [f'Participant_{i}' for i in range(1, 41)]  # 20 participants
# Study conditions
conditions = ['Folicular', 'Lútea']
random.seed(7)
# Function to randomize the order of conditions for each participant
def balanced_randomization_random_order(participants, conditions):
    # Split participants into two groups for balanced starting conditions
    random.shuffle(participants)  # Shuffle participants for randomness
    half = len(participants) // 2
    group1 = participants[:half]  # First group starts with Control
    group2 = participants[half:]  # Second group starts with Mental Fatigue
    # Create randomized assignments
    randomization = []
    for participant in group1:
        randomization.append({
            'Participante': participant,
            'Sessão_1': conditions[1],  # Control
            'Sessão_2': conditions[0]   # Mental Fatigue
        })
    for participant in group2:
        randomization.append({
            'Participante': participant,
            'Sessão_1': conditions[0],  # Mental Fatigue
            'Sessão_2': conditions[1]   # Control
        })
    # Shuffle the final list for random order
    random.shuffle(randomization)
    return randomization
# Generate randomization
randomization_results = balanced_randomization_random_order(participants, conditions)
df_randomization = pd.DataFrame(randomization_results)
df_randomization = df_randomization.sort_values(
    by='Participante',
    key=lambda x: x.str.extract(r'(\d+)$')[0].astype(int)  # Extracts the numeric part and sorts it
).reset_index(drop=True)
# Display the results
print(df_randomization)
