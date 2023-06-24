import random
from resolucion import minion_game

def generate_string(length):
    vowels = 'AEIOU'
    consonants = 'BCDFGHJKLMNPQRSTVWXYZ'
    string = ''
    for _ in range(length):
        if random.random() < 0.5:
            string += random.choice(vowels)
        else:
            string += random.choice(consonants)
    return string

def generate_dataset(size):
    dataset = []
    for _ in range(size):
        length = random.randint(5, 15)
        string = generate_string(length)
        dataset.append((string,))
    return dataset

dataset = generate_dataset(10)

results = []
for data in dataset:
    output = minion_game(*data)
    results.append(output)

with open('dataset.txt', 'w') as f:
    for data, output in zip(dataset, results):
        f.write(f"Input: {data[0]}\n")
        f.write(f"Output: {output}\n")
        f.write('\n')