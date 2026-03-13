'''Dot product, skalarmultiplikation'''
vector_a = [3.4, 4.3, 4.5]
vector_b = [5.4, 2.3, 3.2]
vec_ab = []

def dot_product(vector_a, vector_b):
    product = 0
    for i in range(len(vector_a)):
        result = vector_a[i] * vector_b[i]
        vec_ab.append(result)
    for j in range(len(vec_ab)):
        product += vec_ab[j]

    return product

product = dot_product(vector_a, vector_b)
print(product)