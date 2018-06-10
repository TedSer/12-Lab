import re

if __name__ == "__main__":
    count = 0
    with open("access.log.txt") as file:
        for line in file:
            if re.search('26/Mar/2009:[1-2][4-9]:[4-5][0-9]:[2-6][3-6]',
                         str(line)) or re.search('2[7-9]/Mar/2009',
                                                 str(line)) or re.search('30/Mar/2009:0[1-9]:[1-5][1-9]:[3-6][0-6]',
                                                                                            str(line)) and re.search(' 200 ',
                                                                                                                     str(line))and re.search("GET ",
                                                                                                                                             str(line)) and re.search("robot",
                                                                                                                                                                      str(line)):
                count += 1
                print(line)
    print(count)
