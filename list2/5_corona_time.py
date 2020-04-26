#!/usr/bin/python
#  -*- coding: utf-8 -*-

# pip install beautifulsoup4
# pip install requests
# pip install lxml

import requests
import lxml
from bs4 import BeautifulSoup
import re

def print8(item):
    print(str(item).encode("utf-8"))

class CoronaTime():

    def __init__(self, table_name):
        link = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Poland"
        self.get_data(link, table_name)
        self.data_for_barplot()

    def get_data(self, link ,table_name):
        result = requests.get(link)

        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        tables = soup.find_all("table")

        my_arr = []

        for table in tables:
            if table_name in table.text:
                tbody_s = table.find_all("tbody")

                for tr1 in tbody_s:
                    tr_s = tr1.find_all("tr")

                    for tr2 in tr_s:
                        arrr = []
                        td_s = tr2.find_all("td")

                        if td_s == []:
                            td_s =  tr2.find_all("th")

                        for td in td_s:
                            arrr.append(td.text.replace("\n", ""))
                        my_arr.append(arrr)
                tbody_s = table.find_all("tbody")

        my_arr = self.del_square_brac(my_arr)
        self.separate_values(my_arr)

    def del_square_brac(self, my_arr):
        # deleting all square braccets in the list -- links in it
        nr1 = 0
        while nr1 < len(my_arr):
            nr2 = 0
            while nr2 < len(my_arr[nr1]):
                my_arr[nr1][nr2] = re.sub(r'\[[^()]*\]', "", my_arr[nr1][nr2])

                if my_arr[nr1][nr2] == '':
                    my_arr[nr1][nr2] = '0'
                nr2 += 1
            nr1 += 1
        return my_arr

    def separate_values(self, arr):
        # leave only number of confirmed cases in all voivodships
        # and get name of  columns (voivodships)
        for f in range(3):
            del arr[-1]

        # names of array of cases
        self.arr_names = arr[1]
        for f in range(2):
            del arr[0]

        # array of cases
        self.my_arr = arr

    def data_for_barplot(self):
        # taking sum of voivodships and dates
        self.cases_table = []
        self.col_name = []

        for mn in self.my_arr:
            self.col_name.append(mn[0])
            self.cases_table.append(int(mn[-1]))

    def print_table(self):
        # simple printing data with col names
        print8(self.arr_names)
        for mn in self.my_arr:
            print8(mn)

    def print_line(self, n):
        # graphical representation of cases by printing lines
        for mn in self.my_arr:
            numb = 0
            mn.pop()
            for k in mn[1:]:
                numb += int(k)
            print(mn[0], ": ", "-"*(int(numb/n)))

    def graf(self):
        # show bar plot
        import numpy as np
        import matplotlib.pyplot as plt

        from datetime import datetime
        cases_sum = self.cases_table
        date_cas = []
        for k in self.col_name:
            datetime_object = datetime.strptime(k, '%d %B %Y').strftime("%d-%b")
            date_cas.append(datetime_object)
        print(date_cas)

        plt.bar(date_cas, cases_sum, color = 'coral', edgecolor = "blue", orientation = "vertical")
        #plt.grid(zorder=0)
        plt.xticks(date_cas[-1::-10],  rotation='horizontal')
        plt.yticks(range(600)[0:650: 25],  rotation='horizontal')
        plt.title("Coronavirus cases in Poland")
        plt.ylabel('Number of Cases')
        plt.xlabel('Date of Corona      last day:  {}\n    together: {}'.format(cases_sum[-1] ,sum(cases_sum)))
        plt.subplots_adjust(left=None, bottom=0.15, right=None, top=None, wspace=None, hspace=None)

        from scipy.stats import gaussian_kde
        import scipy.stats as stats
        k = (cases_sum)
        n = 0
        new = []
        while len(cases_sum) > n:
            for kn in range(int(cases_sum[n])):
                new.append(n)
            n += 1

        nparam_density = stats.kde.gaussian_kde(new)
        x = np.linspace(0, len(cases_sum), 500)
        nparam_density = nparam_density(x)
        nb = 1/(sum(nparam_density)/len(nparam_density))*((sum(cases_sum))/len(cases_sum))
        plt.plot(x, nparam_density*nb, 'b-', label='non-parametric density' )

        plt.show()


cases = CoronaTime("New confirmed cases")
deaths = CoronaTime("deaths in Poland by voivodeship")

cases.print_table()
cases.print_line(5)
cases.graf()

print("\n"*5)

deaths.print_table()
deaths.print_line(1)
deaths.graf()
