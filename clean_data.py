import re
import pandas as pd

class Data_Cleanser:
  def __init__(self, min_length=5):
    self.website_drop = re.compile(r"http\S+|www\.\S+")
    self.at_drop = re.compile(r'^Replying to @.*')
    self.useless = re.compile(r'^[@._\s0-9]+$')
    # minimum length of post
    self.min_length = min_length

    # making data usable
  def cleanse_data(self, df):

    # drop duplicate posts
    df.drop_duplicates(subset=["id"])

    # Remove "Translate1/2" artifacts
    df["post"] = df["post"].str.replace("Translate1/2", "", regex=False)

    # Remove empty posts
    df = df[df["post"].str.len() > 0]

    # drop unusable posts
    df = df[~df["post"].str.fullmatch(self.useless, na=False)]

    # drop posts that tag their account IDs
    df = df[~df["post"].str.fullmatch(self.at_drop, na=False)]

    # drop websites
    df["post"] = df["post"].str.replace(self.website_drop, "", regex=True)

    # Remove posts below minimum length
    df = df[df["post"].str.len() >= self.min_length]

    return df
  
  
  def clean_all(self, df):
    df = self.cleanse_data(df)
    return df