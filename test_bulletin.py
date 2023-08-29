def simple_addition(a, b):
    expected_result = a + b
    assert simple_addition_calculate(a, b) == expected_result, f"Error: {a} + {b} = {expected_result} waiting!"
    
def simple_addition_calculate(a, b):
    return a + b

# Testler
simple_addition(5, 10)
simple_addition(3, 7)
simple_addition(0, 0)

print("Tests done!")
