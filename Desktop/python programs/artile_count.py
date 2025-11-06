def count_article(para):
    a = 0
    an = 0
    the = 0
    word = ""
    start = 0

    for i in range(len(para)):
        if i == 0 and para[i] == "a":
            a+=1
        elif para[i] == "a" and para[i-1] == " " and para[i+1] == " ":
            a+=1

        elif para[i] == "a"and para[i+1] == "n" and para[i+2] == " " and para[i-1] == " ":
            an+=1

        elif para[i] == "t" and para[i+1] == "h" and para[i+2] == "e" and para[i+3] == " " and para[i-1] == " ":
            the +=1

    total = a + an + the
    print("Total no.of articles in the paragraph : {} ".format(total))
    print("Number of 'a' in the paragraph : {}".format(a))
    print("Number of 'an' in the paragraph : {}".format(an))
    print("Number of 'the' in the paragraph : {}".format(the))

paragraph = "a young girl walked into a library with an old, tattered book in her hand. She was searching for a quiet corner to read, but the noise from a nearby group distracted her. The librarian, noticing her struggle, pointed to a secluded section behind the large shelves. There, she found an empty chair and a wooden table with a small lamp. As she flipped through the pages, she discovered a hidden note between the chapters — a message from an unknown author who had visited the library years ago. The mystery intrigued her, and she decided to spend the afternoon solving the clues left behind India."
count_article(paragraph)
