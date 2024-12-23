def xor(a, b):
    """Perform XOR operation between two binary strings."""
    result = []
    for i in range(1, len(b)):
        result.append('1' if a[i] != b[i] else '0')
    return ''.join(result)

def mod2div(dividend, divisor):
    """
    Perform Modulo-2 Division.
    dividend: Binary string of the data to be divided
    divisor: Binary string of the divisor (generator polynomial)
    """
    pick = len(divisor)
    tmp = dividend[:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0' * pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0' * pick, tmp)

    return tmp

def encodeData(data, generator):
    """
    Encode the data using the generator polynomial.
    data: Binary string of the original data
    generator: Binary string of the generator polynomial
    """
    l_gen = len(generator)
    appended_data = data + '0' * (l_gen - 1)
    remainder = mod2div(appended_data, generator)
    codeword = data + remainder
    return codeword

def checkData(received_data, generator):
    """
    Check if the received data is error-free.
    received_data: Binary string of the received data
    generator: Binary string of the generator polynomial
    """
    remainder = mod2div(received_data, generator)
    return all(bit == '0' for bit in remainder)

# Main Function
if __name__ == "__main__":
    # Input Data
    data = input("Enter the binary data: ")
    generator = input("Enter the generator polynomial (binary): ")

    # Encoding the data
    print("\n--- Sender Side ---")
    transmitted_data = encodeData(data, generator)
    print(f"Original Data: {data}")
    print(f"Generator Polynomial: {generator}")
    print(f"Transmitted Data: {transmitted_data}")

    # Simulating data reception
    print("\n--- Receiver Side ---")
    received_data = input("Enter the received data: ")
    if checkData(received_data, generator):
        print("No error detected in received data.")
    else:
        print("Error detected in received data.")
