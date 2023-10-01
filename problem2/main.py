def draw_xyz(N):
    pattern = ""
    for i in range(N):
        row = []
        for j in range(N):
            value = (i * N + j + 1)
            if value % 3 == 0:
                row.append('X')
            elif value % 2 != 0:
                row.append('Y')
            else:
                row.append('Z')
        pattern += " ".join(row)
        pattern += " \n"
        
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """