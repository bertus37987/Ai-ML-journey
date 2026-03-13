#Elementwise addidtion
vec_a = [8.4, 9.4, 3.2]
vec_b = [9.4, 3.1, 5.3]
vec_ab = []
def Elementwise_addiditon(vec_a, vec_b):
    for i in range(len(vec_a)):
        result = vec_a[i] + vec_b[i]
        vec_ab.append(result)
    return result

Elementwise_addiditon(vec_a, vec_b)
print(vec_ab)

