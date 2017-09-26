import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def analyze():
    """
    Analyze my transactions for the month of September to get
    a better understanding of my purchasing behaviors. A thorough
    understanding of this behavior can help with budgeting and reducing
    unneccessary anxiety. The more you know the less anxiety you'll get :).
    """
    pass

def build():
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
    return df

def exampleLine():
    df = build()
    #print(df)
    #dates = [pd.to_datetime(d) for d in df["Date"]]
    #plt.scatter(dates, df["Amount"])
    #plt.show()
    #amounts = [d for d in df["Amount"]]
    dates = [pd.to_datetime(d) for d in df["Date"]]
    indexes = [d for d in range(0, len(df["Amount"]))]
    amounts = [d for d in df["Amount"]]

    # chart stuff
    N = 5
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

    print(dates)
    print(amounts)
    #plt.scatter(dates, amounts)
    plt.scatter(indexes, amounts)
    plt.show()


if __name__ == "__main__":
    exampleLine();
    #analyze()
