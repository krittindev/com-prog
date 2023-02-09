def add_vector(u, v):
    return [u[0] + v[0], u[1] + v[1], u[2] + v[2]]
    
u = [float(e) for e in input()[1:-1].split(', ')]
v = [float(e) for e in input()[1:-1].split(', ')]
print(u, '+', v, '=', add_vector(u, v))