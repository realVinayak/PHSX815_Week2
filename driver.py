from Random import Random
import matplotlib.pyplot as plt
if __name__ == "__main__":
    random = Random(76)
    N = 1000
    data = {0: 0, 1:0, 2:0}
    for n in range(N):
        category = random.Three_Categorical_Distribution([0.3, 0.5])
        data[category] += 1
    keys = list(data.keys())
    values = list(data.values())
    plt.title("1000 samples")
    plt.xlabel("Probability of 0, 1, 2 is 0.3, 0.5 and 0.2 respectively")
    plt.bar(keys, values, width=0.1)
    plt.savefig('categorical_data.png')
    plt.show()
    print(data)
