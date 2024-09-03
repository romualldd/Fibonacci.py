def pertence_fibonacci(num):
    if num < 0:
        return False
    
    a, b = 0, 1
    

    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    
    return False

def main():
    try:
        num = int(input("Digite um número e verificarei se ele pertence à sequência de Fibonacci: "))
        
        if pertence_fibonacci(num):
            print(f"O número {num} pertence à sequência de Fibonacci.")
        else:
            print(f"O número {num} não pertence à sequência de Fibonacci.")
    
    except ValueError:
        print("Não é um número válido")

if __name__ == "__main__":
    main()