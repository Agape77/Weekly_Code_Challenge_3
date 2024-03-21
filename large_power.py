def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
    
    #Test the function
print(large_power(10,15))
print(large_power(2, 10))