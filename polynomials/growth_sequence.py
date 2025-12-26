def exponential_growth(n, factor, days):
    growth_sequence = [n]
    for i in range(days):
        growth_sequence.append(growth_sequence[i] * factor)
    
    
    return growth_sequence

print(exponential_growth(10, 2, 4))