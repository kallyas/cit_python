"""
1. Create a table called "BankStatement" the rows are 
the Balance,Deposit,and withdraw.
The columns is the amount in the dataframe. 
Print only the Deposit amount.
"""
import pandas as pd


def BankStatement():
    df = pd.DataFrame(
        {
            "Balance": [100, 200, 320],
            "Deposit": [300, 400, 700],
            "Withdraw": [10, 210, 300],
        }
    )

    df["Date"] = pd.date_range("2019-01-01", periods=3)
    # save the dataframe to a csv file
    df.to_csv("BankStatement.csv")
    print(df["Deposit"])


"""
2. The "BankStatement" dataframe you created, 
we need to see it in 2 different graphs(subplot).
"""

def plot_bank_statement(plt):
    df = pd.read_csv("BankStatement.csv")
    fig, ax = plt.subplots(nrows=1, ncols=2)
    df.plot(kind="bar", x="Date", ax=ax[0])
    df.plot(kind="line", x="Date", ax=ax[1])
    plt.show()
    


"""
3. Go to any website and download the csv file of that data. 
Then find out the mean, and
standard deviation of that data.
"""

def download_csv(requests, url):
    print("Downloading nba_data.csv...")
    response = requests.get(url)
    with open("nba_data.csv", "wb") as f:
        f.write(response.content)


def mean_std():
    df = pd.read_csv("nba_data.csv")
    print(df.mean())
    print(df.std())


"""
4. The new csv file you download, we need to see 
the data in any graph of 1 paticular row.
"""

def plot_nba_data_one_row(plt):
    df = pd.read_csv("nba_data.csv")
    df.plot(kind="bar", x='Shooter', y='ShotDist')
    plt.title("Shooter vs ShotDist")
    plt.show()


def main():
    import matplotlib.pyplot as plt
    import requests
    import os

    BankStatement()
    plot_bank_statement(plt)

    # if the file nba_data.csv is not present, download it

    if not os.path.exists("nba_data.csv"):
        download_csv(requests, "https://sports-statistics.com/database/basketball-data/nba/2019-20_pbp.csv")
    else:
        print("nba_data.csv is present")

    mean_std()

    plot_nba_data_one_row(plt)


if __name__ == "__main__":
    main() 

