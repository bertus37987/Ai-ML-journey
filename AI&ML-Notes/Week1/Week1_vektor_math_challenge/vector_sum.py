#Vector sum exercise (grokking deep learning)
vector_a = [3.2, 34.3, 44.2]

def Vector_sum(vector_a):
    result = 0
    for i in range(len(vector_a)):
        result += vector_a[i]
    return result

result = Vector_sum(vector_a)
print(result)
