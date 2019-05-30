#! python3

# tablePrinter.py - Prints a table from a list

table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

def print_table(table):
    col_widths = [0] * len(table)

    for column in range(len(table)):
        for item in table[column]:
            if col_widths[column] < len(item):
                col_widths[column] = len(item)
    
    for row in range(len(table[0])):
        for column in range(len(table)):
            print(table[column][row].rjust(col_widths[column]),end=' ')
        print()

print_table(table_data)
