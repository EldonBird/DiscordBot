import pytest
import Game_Grapher
import pandas as pd


def test_GetWinRate():
    assert Game_Grapher.GetWinRate(10, 5) == 50, \
        "FAILED"

    assert Game_Grapher.GetWinRate(100, 20) == 20, \
        "FAILED"
    

def test_GetPlayerInfo():

    file = pd.read_csv("Score.csv")

    wins, games = Game_Grapher.GetPlayerInfo(file, "Maddy")

    assert games == 5, \
        "FAILED"

    wins, games = Game_Grapher.GetPlayerInfo(file, "Eldon")
    
    assert games == 7, \
        "FAILED"

def test_Graph():
    
    df = pd.read_csv("Score.csv")

    elements1 = []
    amount = 0
    wins = 0

    row_index = df.index[df['Players'] == "Eldon"].tolist()

    for x in range(0, df.shape[1]):

        cell = df.iloc[row_index[0], x]
        if((cell == "Rebel Win") or (cell == "Empire Win") or (cell == "Const Win")):
            amount += 1
            wins += 1
        if((cell == "Rebel Loss") or (cell == "Empire Loss") or (cell == "Const Loss")):
            amount += 1
        
        if(amount != 0):
            temp = Game_Grapher.GetWinRate(amount, wins)
            elements1.append(temp)


    assert Game_Grapher.GraphFunction(df, "Eldon") == elements1, \
        "FAILED THE GRAPH"

    elements2 = []
    amount2 = 0
    wins2 = 0

    row_index2 = df.index[df['Players'] == "Maddy"].tolist()

    for x in range(0, df.shape[1]):

        cell = df.iloc[row_index2[0], x]
        if((cell == "Rebel Win") or (cell == "Empire Win") or (cell == "Const Win")):
            amount2 += 1
            wins2 += 1
        if((cell == "Rebel Loss") or (cell == "Empire Loss") or (cell == "Const Loss")):
            amount2 += 1
        
        if(amount2 != 0):
            temp = Game_Grapher.GetWinRate(amount2, wins2)
            elements2.append(temp)


    assert Game_Grapher.GraphFunction(df, "Maddy") == elements2, \
        "FAILED THE GRAPH Test for MADDY"







pytest.main(["-v", "--tb=line", "-rN", __file__])
