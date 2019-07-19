if __name__ == '__main__':

    counter = 0
    with open('data/indexing/1', encoding="utf8", errors='ignore') as f:

        for line in f:

            line_list = list(line.split())

            counter = counter+len(line_list)

    print (counter)
