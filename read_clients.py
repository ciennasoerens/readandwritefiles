def main():
    infile= open('clients.txt', 'r')

    counter=1

    for line in infile:
        print(f"{counter}. {line.rstrip("\n")}")
        counter += 1
    
    print(f"The total number of clients is: {counter-1}")
main()