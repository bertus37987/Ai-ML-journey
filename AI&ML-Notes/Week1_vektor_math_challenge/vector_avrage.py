#vector avrage
vector_a = [21.3, 3.4, 12.3]

def VectorAvrage(vector_a):
    result = 0
    for i in range(len(vector_a)):
        result += vector_a[i]
    result /= len(vector_a)
    return result

result = VectorAvrage(vector_a)

print(result)