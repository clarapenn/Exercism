def label(bands_to_check_list):
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

    first_two_bands = [bands_to_check_list[0], bands_to_check_list[1]]

    for band_color in first_two_bands:
        index = colors_list.index(band_color)
        if index == -1:
            print("not found")
            return

        numbers_to_concat.append(index)

    summed_number = str(numbers_to_concat[0]) + str(numbers_to_concat[1])

    third_band_index = colors_list.index(bands_to_check_list[2])

    summed_number_plus_zeros = int(summed_number) * (10 **(third_band_index))

    if summed_number_plus_zeros >= 1000:
        number_in_kiloohms = summed_number_plus_zeros // 1000
        return f"{number_in_kiloohms} kiloohms"
    else:
        return f"{summed_number_plus_zeros} ohms"
