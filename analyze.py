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
            parts = line.split(',')
            date = parts[0]
            merchant = parts[1]
            amount = parts[2]
            category = parts[3]
            data.append([date, merchant, amount, category])

    df = pd.DataFrame(data, columns=['Date', 'Merchant', 'Amount', 'Category'])
    return df

def scatterPurchases():
    """
    Simple scatter chart of purchases
    """
    df = build()
    #print(df)
    #dates = [pd.to_datetime(d) for d in df['Date']]
    #plt.scatter(dates, df['Amount'])
    #plt.show()
    #amounts = [d for d in df['Amount']]
    dates = [pd.to_datetime(d) for d in df['Date']]
    indexes = [d for d in range(0, len(df['Amount']))]
    amounts = [d for d in df['Amount']]

    # chart stuff
    N = 5
    colors = np.random.rand(N)
    area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii

    print(dates)
    print(amounts)
    #plt.scatter(dates, amounts)
    plt.scatter(indexes, amounts)
    plt.show()


def metaInfo():
    """
    Meta info about data frame
    """
    df = build()
    print(df.head())
    print('=============')
    print(df.describe())
    print('=============')
    print(df.dtypes)

def group():
    """
    Group by each merchant
    """
    df = build()
    merchants_group = df.groupby('Merchant')
    print(merchants_group.size())

def groupByMerchant():
    """
    Show sum total from each merchant
    """
    df = build()
    df['Amount'] = [float(d) for d in df['Amount']]
    merchants_group = df.groupby('Merchant')
    total = merchants_group.sum()
    print(total)

def groupByMerchantAndPlot():
    """
    Bar chart of total purchases per merchant
    """
    df = build()
    df['Amount'] = [float(d) for d in df['Amount']]
    merchants_group = df.groupby('Merchant')
    total = merchants_group.sum()
    plt.show(total.plot(kind='bar'))

def groupByMerchantAndPlotAndSort():
    """
    Bar chart [sorted]of total purchases per merchant
    """
    df = build()
    df['Amount'] = [float(d) for d in df['Amount']]
    merchants_group = df.groupby('Merchant')
    total = merchants_group.sum()
    total.sort_values('Amount').head()
    plot = total.sort_values('Amount', ascending=False).plot(kind='bar', legend=None, title='Total purchases by merchant')
    plot.set_xlabel('Merchants')
    plot.set_ylabel('Amount')
    plt.show(plot)

def groupByMerchants():
    """
    Group purchases by frequency
    """
    df = build()
    new_df = df[['Merchant', 'Amount']] #create a new df
    merchant_group = new_df.groupby(['Merchant']).count()
    print(merchant_group)

def groupByDates():
    """
    Break down purchases by dates
    """
    df = build()
    category_group = df.groupby(['Merchant', 'Date', 'Amount']).sum()
    print(category_group)

def groupByDatesAndPlot():
    """
    Break down purchases by dates and plot in a stacked bar chart. This
    chart will show you the `size` of each purchase made at a merchant
    """
    df = build()
    # making a new df
    new_df = df[['Merchant', 'Date', 'Amount']]
    new_df['Amount'] = [float(a) for a in df['Amount']]

    # group by merchant and date, take the sum of the amount
    merchant_group = new_df.groupby(['Merchant', 'Date']).sum()

    #print(merchant_group)
    my_plot = merchant_group.unstack().plot(kind='bar', stacked=True,title='Total purchases')
    my_plot.set_xlabel('Merchants')
    my_plot.set_ylabel('Amount')
    plt.show(my_plot)

def histoChart():
    """
    Histo chart to see how large each purchase is. The x axis
    represents the amount, the y axis represents the qunatity
    """
    df = build()
    df['Amount'] = [float(d) for d in df['Amount']]
    purchase_plot = df['Amount'].hist(bins=20)
    purchase_plot.set_xlabel('Amount')
    purchase_plot.set_ylabel('Frequency')
    plt.show(purchase_plot)

if __name__ == "__main__":
    histoChart()
    #groupByDatesAndPlot()
    #groupByDates()
    #groupByMerchantAndPlotAndSort()
    #groupByMerchantAndPlot()
    #groupByMerchant()
    #group()
    #metaInfo()
    #scatterPurchases();
    #analyze()
