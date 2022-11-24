def convert_to_text(matrix):
    decoded_word = ""
    try:
        for line_i in range(len(matrix)):
            for letter_i in range(len(matrix[line_i])):
                if (line_i + 1) % 2 == 0 and (letter_i + 1) % 2 == 0:
                    decoded_word += matrix[line_i][letter_i]
                elif (line_i + 1) % 2 != 0 and (letter_i + 1) % 2 != 0:
                    decoded_word += matrix[line_i][letter_i]
                else:
                    continue
        return decoded_word
    except TypeError:
        print('Your input must be a matrix(list of lists)')

