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
    data = [["09/12/2017","B&B",14.50], ["09/13/2017", "MHM", 10.35]]
    df = pd.DataFrame(data, columns=["Date", "Place", "Amount"])
    print(df)
    pass

if __name__ == "__main__":
    example()
    #analyze()
