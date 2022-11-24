def deleteComments(filename):
    try:
        deleted_comments_count = 0
        # create a new filename
        if "/" in filename:
            split_path = filename.split("/")
            split_path = split_path[-1]
            split_path = split_path.split(".")
            new_filename = "clean-" + split_path[0] + ".txt"
        else:
            split_path = filename.split(".")
            new_filename = "clean-" + split_path[0] + ".txt"

        # clean the code
        with open(filename, 'r') as fileobj:
            clean_code = ""
            file_content_list = fileobj.readlines()
            for line in file_content_list:
                if "#" not in line:
                    clean_code += line
                else:
                    deleted_comments_count += 1

        # write the code into the new file
        with open(new_filename, 'w') as clean_file:
            clean_file.write(clean_code)
        return deleted_comments_count

    except OSError:
        print("An error occurred with accessing the files")



