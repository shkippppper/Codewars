def peak_height(mountain):
    height = 0
    for i in range(len(mountain)):
        for j in range(len(mountain[i])):
            if i == 0:
                if mountain[i][j] == "^":
                    x = mountain[i][j].replace("^","1")


    return mountain[i]


print(peak_height([
          "^^^^^^        ",
          " ^^^^^^^^     ",
          "  ^^^^^^^     ",
          "  ^^^^^       ",
          "  ^^^^^^^^^^^ ",
          "  ^^^^^^      ",
          "  ^^^^        "
        ]))