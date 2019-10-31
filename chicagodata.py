#!/usr/bin/env python
import csv

FILE_NAME = "DATA/city-of-chicago-salaries.csv"

def get_row_count():
    row_count = 0
    with open(FILE_NAME) as city_info_in:
        next(city_info_in) # skip header
        for row in city_info_in:
            row_count += 1
    return row_count

def get_salary_data_as_list(max_rows=None):
    with open(FILE_NAME) as city_info_in:
        headers = next(city_info_in) # skip headers
        rdr = csv.reader(city_info_in)
        for i, row in enumerate(rdr):
            if (max_rows is not None) and (i == max_rows):
                break
            row[-1] = float(row[-1][1:]) # turn "$999.99" into float
            yield row  # make this function a generator

if __name__ == '__main__':
    salary_gen = get_salary_data_as_list(10)
    for row in salary_gen:
        print(row)
