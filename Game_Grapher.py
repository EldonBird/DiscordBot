import pandas as pd
import matplotlib.pyplot as plt

def GraphFunction(df, playerName):

    elements = []
    empty = []
    amount = 0
    wins = 0

    row_index = df.index[df['Players'] == playerName].tolist()

    for x in range(0, df.shape[1]):

        cell = df.iloc[row_index[0], x]
        if((cell == "Rebel Win") or (cell == "Empire Win") or (cell == "Const Win")):
            amount += 1
            wins += 1
        if((cell == "Rebel Loss") or (cell == "Empire Loss") or (cell == "Const Loss")):
            amount += 1
        
        if(amount != 0):
            temp = GetWinRate(amount, wins)
            elements.append(temp)

    for t in range(0, len(elements)):
        empty.append(t)


    plt.plot(empty, elements)

    plt.ylabel = "Win %"
    plt.xlabel = "# of Games"

    plt.xlim([0, len(empty)])
    plt.ylim([-1, 101])

    plt.show()

    return elements




def GetWinRate(games, wins):
    
    val = round((wins / games) * 100)

    return val

def LoadDataFrame(fileName):

    df = pd.read_csv(fileName)
    return df



def GetPlayerInfo(df, playerName):
    Wins = 0
    Games = 0

    try:

        row_index = df.index[df['Players'] == playerName].tolist()

        for x in range(0, df.shape[1]):
            cell = df.iloc[row_index[0], x]

            if((cell == "Rebel Win") or (cell == "Empire Win") or (cell == "Const Win")):
                print("WINNER")
                Wins += 1
                Games += 1
            if((cell == "Rebel Loss") or (cell == "Empire Loss") or (cell == "Const Loss")):
                print("LOSER")
                Games += 1

        return Wins, Games
    except:
        print("NOT FOUND")
    


def main():

    playerIn = input("Which player Do you want info for : ")
    
    df = LoadDataFrame("Score.csv")

    wins, games = GetPlayerInfo(df, playerIn)

    percent = GetWinRate(games, wins)

    print(f"Wins: {wins}, Games: {games} with a win% of, {percent}%")

    GraphFunction(df, playerIn)



if __name__ == "__main__":
    main()