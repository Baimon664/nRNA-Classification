seq = input("sequence = ")

k=3
def ThreeMer(seq):
    data = []
    for i in range(len(seq)-(k-1)):
        data.append(seq[i:i+k])
    return data

print(ThreeMer(seq))