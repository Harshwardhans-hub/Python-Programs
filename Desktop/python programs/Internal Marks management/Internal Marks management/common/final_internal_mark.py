def addfinalmarks(sub):
    f1 = "Internalfirst.txt.{}".format(sub)
    f2 = "Internalsecond.txt.{}".format(sub)
    f3 = "Internalthird.txt.{}".format(sub)

    def readmarks(file):
        d = {}
        with open(file, 'r') as f:
            for line in f:
                line = line.replace('\n', '')
                detail = line.split(',')
                if len(detail) == 2:
                    d[detail[0]] = int(detail[1])
        return d

    m1 = readmarks(f1)
    m2 = readmarks(f2)
    m3 = readmarks(f3)

    with open("student.txt", 'r') as f:
        studs = f.readlines()

    result = ""
    for s in studs:
        s = s.replace('\n', '')
        d = s.split(',')
        roll = d[0]
        total = m1.get(roll, 0) + m2.get(roll, 0) + m3.get(roll, 0)
        result += "{},{}\n".format(roll, total)

    with open("final_internal_marks.txt", 'w') as f:
        f.write(result)

    print("Final marks added successfully.")

def viewfinalmarks():
    with open("final_internal_marks.txt", 'r') as f:
        data = f.readlines()
        if len(data) == 0:
            print("No final marks found.")
            return
        print("Final Internal Marks")
        for i in data:
            i = i.replace('\n', '')
            d = i.split(',')
            if len(d) == 2:
                print("Roll No:", d[0], "Marks:", d[1])
