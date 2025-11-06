    def add_marks(internal_file):
    roll_no = input("Enter Roll.No: ")
    mark = input("Enter marks: ")

    entry = "{},{}\n".format(roll_no, mark)
    file = open(internal_file, "a")
    file.write(entry)
    file.close()
    print("Marks added successfully.")


def view_marks(internal_file):
    file = open(internal_file, "r")
    read = file.readlines()
    file.close()

    if len(read) == 0:
        print("No marks found.")
        return

    print("Marks list:")
    for i in read:
        i = i.replace("\n", "")
        detail = i.split(",")
        print("Roll No:", detail[0])
        print("Marks:", detail[1])
        print("++++++++++++++++")


def update_marks(internal_file):
    roll_no = input("Enter Roll.No to update marks: ")
    file = open(internal_file, "r")
    read = file.readlines()
    file.close()

    file = open(internal_file, "w")
    updated = 0

    for i in read:
        temp = i.split(",")
        current_roll = temp[0]

        if current_roll == roll_no:
            mark = input("Enter new marks: ")
            file.write("{},{}\n".format(roll_no, mark))
            updated = 1
        else:
            file.write(i)
    file.close()

    if updated == 1:
        print("Marks updated successfully.")
    else:
        print("Roll.No not found.")


def delete_marks(internal_file):
    roll_no = input("Enter Roll.No to delete marks: ")
    file = open(internal_file, "r")
    read = file.readlines()
    file.close()

    file = open(internal_file, "w")
    deleted = 0

    for i in read:
        temp = i.split(",")
        current_roll = temp[0]

        if current_roll == roll_no:
            deleted = 1
            continue
        else:
            file.write(i)
    file.close()

    if deleted == 1:
        print("Marks deleted successfully.")
    else:
        print("Roll.No not found.")
