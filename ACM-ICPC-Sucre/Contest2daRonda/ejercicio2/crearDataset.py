import random
from resolucion import merge_the_tools

def generate_dataset(size):
    dataset = []
    for _ in range(size):
        n = random.randint(5, 15)
        k = random.randint(1, n)
        s = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=n))
        dataset.append((s, k))
    return dataset

def calculate_expected_output(s, k):
    subsequences = merge_the_tools(s, k)
    return subsequences

dataset = generate_dataset(10)

results = []
for data in dataset:
    output = calculate_expected_output(*data)
    results.append(output)

# Guardar el conjunto de datos y las salidas esperadas en archivos
with open('dataset.txt', 'w') as f:
    for data, output in zip(dataset, results):
        f.write(f"{data[0]} {data[1]}\n")
        for subsequence in output:
            f.write(f"{subsequence}")
        f.write('\n')
