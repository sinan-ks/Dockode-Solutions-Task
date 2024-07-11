def hexagonal_mesh(rows,columns):
    
    for i in range(rows):
        for _ in range(columns):
            if i <=0:
                print(" ___    ",end="")
        print()

        for _ in range(columns):
            if _ <columns-1:
                print("/   \\___", end="")
            else:
                print("/   \\", end="")
        print()

        #print the last row
        for _ in range(columns):
            print("\\___/   ", end="")
        #print()

def main():
    ins = input('inputs :- ').split(" ")
    rows, column = int(ins[0]), int(ins[1])   
    column = column+rows-column
    hexagonal_mesh(rows, column)

if __name__ == "__main__":
    main()
