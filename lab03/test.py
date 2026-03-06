import numpy as np

def compute_age_coeff(value):
    '''Рассчет коэффициента возгорания дерева в зависисмости от времени жизни'''
    fire_coeff = 2 / (1 + np.exp(-value/10))
    print(f"fire_coeff {fire_coeff}")
    return fire_coeff

for i in range(0, 50):
    print(f"compute_age_coeff({i}) = {compute_age_coeff(i)}")