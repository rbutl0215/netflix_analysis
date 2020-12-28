import pandas
import numpy
import matplotlib.pyplot as plt 

def pick_name(names_list, which_name):
    names_list = str(names_list)
    num_com = names_list.count(',')
    if(which_name == 0 and num_com == 0):
        return names_list
    elif(which_name != 0 and num_com ==0):
        return ""
    elif(which_name > num_com):      
        return ""
    else:
        return names_list.split(',')[which_name]

def take_three(string):
    string = str(string)
    return string[0:3]

def output_data(df_, file_name):
    df_.to_csv(file_name, index = False)
    return

def read_data(string,dropna = False,filter_us = False):
    df = pandas.read_csv(string)
    if(dropna):
        df = df.dropna()
    if(filter_us):   
        df = df[df.country == 'United States']
    return df

def display_bar_chart(df_,x_axis,y_axis):
    df_length_by_rating = df_.groupby(x_axis).agg(average_duration = pandas.NamedAgg(column = y_axis, aggfunc ='mean'))
    df_length_by_rating = df_length_by_rating.sort_values(['average_duration'])
    df_length_by_rating.reset_index().plot.bar(x_axis,'average_duration',rot=0)
    plt.show()
