matrix = []
with open('./exercise3/data.txt', 'r', encoding='UTF-8') as file:
    for line in file:
        row = [int(num) for num in line.split()]
        matrix.append(row)

rows = len(matrix)
columns = len(matrix[0])

squares_count = 0
circles_count = 0

def finder(r, c):
    if r < 0 or r >= rows or c < 0 or c >= columns or matrix[r][c] != 1:
        return []

    matrix[r][c] = 0
    cells = [(r, c)]

    cells += finder(r + 1, c)
    cells += finder(r - 1, c)
    cells += finder(r, c + 1)
    cells += finder(r, c - 1)

    return cells

for r in range(rows):
    for c in range(columns):
        if matrix[r][c] == 1:
            figure_cells = finder(r, c)

            rows_indecses = [point[0] for point in figure_cells]
            columns_indecses = [point[1] for point in figure_cells]
            
            min_r = min(rows_indecses)
            max_r = max(rows_indecses)
            min_c = min(columns_indecses)
            max_c = max(columns_indecses)
            
            actual_area = len(figure_cells)
            heigth = max_r - min_r + 1
            width = max_c - min_c + 1
            
            expected_square_area = width * heigth
            
            if actual_area == expected_square_area:
                squares_count += 1
            else:
                circles_count += 1

print(squares_count, circles_count)