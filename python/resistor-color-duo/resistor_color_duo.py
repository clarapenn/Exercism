def value(bands_to_check_list):
    colors_list = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
    numbers_to_concat = []

    for band_color in bands_to_check_list:
        index = colors_list.index(band_color)
        if index == -1:
            print("not found")
            return

        numbers_to_concat.append(index)

    summed_number = str(numbers_to_concat[0]) + str(numbers_to_concat[1])

    return int(summed_number)