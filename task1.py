import pandas as pd
import numpy as np
import warnings
import csv
import mysql.connector

warnings.filterwarnings("ignore")

def read_data_from_csv():
    hotels = pd.read_csv('zomato.csv')
    hotels = hotels.drop(columns=['address', 'phone'], axis=1)
    return hotels

def remove_unwanted_columns():
    hotels = read_data_from_csv()
    return hotels

def rename_columns():
    hotels = remove_unwanted_columns()
    hotels.rename(columns={'rate': 'rating', 'listed_in(type)': 'type', 'approx_cost(for two people)': 'approx_cost'}, inplace=True)
    return hotels

def null_value_check():
    hotels = rename_columns()
    hotels.dropna(subset=['name'], inplace=True)

    hotels['online_order'].fillna('NA', inplace=True)
    hotels['book_table'].fillna('NA', inplace=True)
    hotels['location'].fillna('NA', inplace=True)
    hotels['rest_type'].fillna('NA', inplace=True)
    hotels['dish_liked'].fillna('NA', inplace=True)
    hotels['cuisines'].fillna('NA', inplace=True)

    hotels['votes'].fillna(0, inplace=True)
    hotels['approx_cost'].fillna(0, inplace=True)
    hotels['rating'].fillna(0,inplace=True)
    hotels['type'].fillna('NA', inplace=True)

    return hotels

def find_duplicates():
    hotels = null_value_check()
    hotels.drop_duplicates(keep='first', inplace=True)
    return hotels

def removing_irrelevant_text():
    hotels = find_duplicates()
    
    hotels=hotels[hotels['name'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['online_order'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['book_table'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['rating'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['votes'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['location'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['rest_type'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['dish_liked'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['cuisines'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['approx_cost'].str.contains('RATED|Rated')==False]
    hotels=hotels[hotels['type'].str.contains('RATED|Rated')==False]
    return hotels

#task6: check for unique values in each column and handle the irrelevant values
def check_for_unique_values():
    #DO NOT REMOVE FOLLOWING LINE
    
    #call removing_irrelevant_text() function to get dataframe
    hotels=removing_irrelevant_text()
    hotels = hotels[hotels['online_order'].str.contains('Yes|No',regex=True)]
    hotels['rating'] = hotels['rating'].str.replace('/5', '')
    
    def replace_rating(rating):
        if rating == 'NEW' or rating == '-':
          return 0
        else:
          return rating
    hotels['rating'] = hotels['rating'].apply(replace_rating)
    return hotels

def remove_the_unknown_character():
#DO NOT REMOVE FOLLOWING LINE
#call check_for_unique_values() function to get dataframe
    dataframe=check_for_unique_values()
#remove unknown character from dataset

#dataframe.replace({r&#39;[^\x00-\x7F]+&#39;:&#39;&#39;}, regex=True, inplace=True)
#for column in dataframe:
#column = column.str.replace(&#39;[^a-zA-Z]&#39;, &#39;&#39;)
    dataframe['name'] = dataframe['name'].str.replace('[Ãx][^A-Za-z]+','',regex=True)
#dataframe = dataframe.replace(to_replace=&quot;[^A-Za-z\s]+&quot;,&quot;&quot;,regex=True)
#export cleaned Dataset to newcsv file named &quot;zomatocleaned.csv&quot;
    dataframe.to_csv('zomatocleaned1.csv')

    return dataframe
    
  #check if mysql table is created using &quot;zomatocleaned.csv&quot;
#Use this final dataset and upload it on the provided database for performing analysis in MySQL
#To Run this task first Run the appliation for Terminal to create table named &#39;Zomato&#39; and then run test.
def start():
    remove_the_unknown_character()

def task_runner():
    start()
