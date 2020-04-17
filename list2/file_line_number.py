import os

class Python_Line_Counter():

    def __init__(self, directory):
        numb_dict = self.find_and_count(directory)
        for i in numb_dict:
            print(i,": ", numb_dict[i])

    def find_and_count(self, directory):
        file_dict = {}
        for root, subFolders, files in os.walk(directory):
             for file_name in files:
                 if file_name[-3:] == ".py":
                     file_root_name = root+"\\"+file_name
                     file_dict[root+"\\"+file_name] = self.count_lines(root+"\\"+file_name)

        return(file_dict)

    def count_lines(self, file):
        num_lines = sum(1 for line in open(file))
        return(num_lines)


if __name__ == '__main__':
    Python_Line_Counter("E:\\Przyrod-master\\2\\Prog Lang 2")
