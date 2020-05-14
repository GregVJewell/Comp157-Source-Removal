def read_graph(filename):
    file = open(filename, "r")
    matrix = file.readlines()  # read in whole file as 1D list of strings
    for row in range(len(matrix)):
        # strip off trailing newline and break each row into a list, creating a 2D list
        matrix[row] = list(matrix[row].strip())
        for col in range(len(matrix[row])):
            # convert each '0' into 0 and '1' into 1 so have numerical matrix instead of character one
            matrix[row][col] = int(matrix[row][col])
    return matrix

def main():
    print("I still need to be written")

if __name__ == "__main__":
    main()