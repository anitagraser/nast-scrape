import csv
import pickle
import sys

data = pickle.load(open('tagesdaten.pickle', 'rb'))
writer = csv.DictWriter(open('tagesdaten.csv', 'w'),
                        ['jahr','monat','tag','stelle', 'zaehlung_r1', 'zaehlung_r2', 'zaehlung_summe',
                         'regen', 'schnee', 'temp_min', 'temp_max', 'temp_7', 'temp_19'])
writer.writeheader()
writer.writerows(data)
