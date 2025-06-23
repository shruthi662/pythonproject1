def print_table(table_data):
    # Find the maximum width of each column
    col_widths = [max(len(str(item)) for item in col) for col in table_data]

    # Print each row using zip
    for row in zip(*table_data):
        for i, item in enumerate(row):
            print(str(item).rjust(col_widths[i]), end=' ')
        print()

# Sample table data (each sub-list is a column)
table_data = [
    ['Name', 'Alice', 'Bob', 'Carol'],
    ['Age', '24', '19', '34'],
    ['City', 'Delhi', 'Mumbai', 'Chennai']
]

print_table(table_data)
