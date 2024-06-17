import os

import openpyxl
from openpyxl import load_workbook
import shutil
from datetime import datetime

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


Competitors = []



class CompetitorEntry:
    def __init__(self, DiscordID, CountryTag, Win, Score):
        self.DiscordID = DiscordID
        self.CountryTag = CountryTag
        self.Win = Win
        self.Score = Score

    def test(self):
        return f"{self.DiscordID}, won?: {self.Win}"


def Addplayer():
    person1 = CompetitorEntry(19828388383, "ENG", True, 1000)
    Competitors.append(person1)

def RemovePlayer(Entry):
    
    Competitors.remove(Entry)




def StartNewGame():
    pass


def CompileGameStatistics(WhichGame, Date):






    # This part is resposible for working with the excel File

    shutil.copy("template.xlsx", f"{Date:%Y-%m-%d}_{WhichGame}.xlsx")
    excelFile = f"{Date:%Y-%m-%d}_{WhichGame}.xlsx"
    df_excelFileOut = pd.read_excel(excelFile, sheet_name="GameScore")
    print(df_excelFileOut)

current = datetime.now()




Addplayer()

for person in Competitors:
    print(person.test())