def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    bits = []
    while n > 0:
        bits.append(n % 2)
        n //= 2
    
    return ''.join(map(str, reversed(bits)))

while True:
    user_input = input("Enter a decimal number ")
    
    print(f"Binary: {decimal_to_binary(int(user_input))}")
