#!/usr/bin/python

import csv, operator

class Score_Difference():
    def __init__(self, data_name):
        data = self.read_file(data_name)
        diff = self.make_diff_dict(data)
        sorted_data = self.sort_data(diff)
        for team in sorted_data:
            print(team)

    def read_file(self, data_name):
        football_data = []
        with open(data_name, newline='') as csvfile:
             football_obj = csv.reader(csvfile, delimiter=',')
             for team in football_obj:
                football_data.append(team)
        print(football_data)
        football_data = football_data[1:]
        return(football_data)

    def make_diff_dict(self, data):
        score = {}
        for team in data:
            score[team[0]] = abs(int(team[5]) - int(team[6]))
        return(score)

    def sort_data(self, data):
        data = sorted(data.items(), key=operator.itemgetter(1))
        return(data)

if __name__=="__main__":
    Score_Difference("football.csv")
