'''
Exercise 4: Add code to the above program to figure out who has the
most messages in the file. After all the data has been read and the dictionary has been created, look through the dictionary using a maximum
loop (see Chapter 5: Maximum and minimum loops) to find who has
the most messages and print how many messages the person has.
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

try:
    with open("./files/mbox.txt") as f:
        peoples = dict()
        for line in f:
            if line.startswith("From "):
                words = line.split()
                name = words[1]
                peoples[name] = peoples.get(name, 0) + 1
        # to find the person who msg the most
        maximum = dict()
        count = None
        for name in peoples:
            if count is None or peoples[name] > count:
                count = peoples[name]
                maximum[count] = name

        print(f"{maximum[max(maximum)]} : {max(maximum)}")

except:
    print("File not Found!!")
