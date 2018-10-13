import pyexcel 
from collections import OrderedDict


data = [
    OrderedDict({
        "Name": "Quan",
        "Age": 20,
        "City": "Hanoi",
    }),
    OrderedDict({
        "Name": "Hong",
        "Age": 18,
        "City": "Hanoi",
    }),
    OrderedDict({
        "Name": "An",
        "Age": 25,
        "City": "Hanoi",
    }),
]
pyexcel.save_as(records=data,dest_file_name="sampled.xlsx")