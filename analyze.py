import pandas as pd
import numpy as np


def analyze():
    """
    Analyze my transactions for the month of September to get
    a better understanding of my purchasing behaviors. A thorough
    understanding of this behavior can help with budgeting and reducing
    unneccessary anxiety. The more you know the less anxiety you'll get :).
    """
    pass

def example():
    """
    Example using pandas
    """

    data = []
    # loop through file line by line
    with open('./transactions.csv') as f:
        for line in f:
            parts = line.split(",")
            date = parts[0]
            place = parts[1]
            amount = parts[2]
            data.append([date, place, amount])


    df = pd.DataFrame(data, columns=["Date", "Place", "Amount"])
    print(df)
    pass

if __name__ == "__main__":
    example()
    #analyze()
