def to_bitstring(string: str) -> str:
    code = 0
    for char in string.upper():
        code += ord(char)
    return bin(code)

def get_code(bitstr: str) -> int:
    return bitstr.lstrip("0b")

def getInput():
    user_answer = input("What is your answer: ")
    print("Thank you\n")
    print("The output bitstring that you will be encoding is", get_code(to_bitstring(user_answer)),'\n')

if __name__ == '__main__':
    getInput()