import pandas
import numpy
import functions_sub_pkg.functions as sb
import matplotlib.pyplot as plt

#use function to transform columns of listed names into multiple columns for every unique name listed 
def create_new_columns(df_):
    for i in range(0,15):
        j = i+1
        col_name = 'act'+str(j)
        df_[col_name] = df_.apply(lambda row : sb.pick_name(row['cast'],i), axis = 1)
    return

def format_two_people(df_):
    col_list = ['act1','act2','act3','act4','act5','act6','act7','act8','act9','act10','act11','act12','act13','act14', 'act15']

    #create dataframe with only the newly added columns
    act_dir = df_[col_list]

    #unpivot the data in order to get a 2 column data fram with one actor/director and another actor/director
    act_dir_unpivot = act_dir.melt(id_vars=['act1'], var_name = 'position', value_name = 'name')
    act_dir_unpivot.columns = ['posa','posb_title','posb']

    for i in col_list:
        act_dir_loop = act_dir.melt(id_vars=[i], var_name = 'position', value_name = 'name')
        act_dir_loop.columns = ['posa','posb_title','posb']
        act_dir_unpivot.append(act_dir_loop)

    #ref_table = act_dir_unpivot[['posb', 'posb_title']]
    #ref_table = ref_table.drop_duplicates()
    #ref_table['pos_title'] = df.apply(lambda row : take_three(row['posb_title']), axis=1)

    act_dir_unpivot = act_dir_unpivot[['posa','posb']]
    act_dir_unpivot['posa'].replace('', numpy.nan, inplace=True)
    act_dir_unpivot['posb'].replace('', numpy.nan, inplace=True)
    act_dir_unpivot = act_dir_unpivot.dropna()
    act_dir_unpivot = act_dir_unpivot.drop_duplicates()
    act_dir_unpivot = act_dir_unpivot.sort_values(['posa','posb'])
    act_dir_unpivot['posa'] = act_dir_unpivot['posa'].str.strip()
    act_dir_unpivot['posb'] = act_dir_unpivot['posb'].str.strip()
    return act_dir_unpivot

#preliminary function to diplay sorted by chart
def movie_length_by_rating(df_):
    df_ = df_[df_.type == 'Movie']
    df_['mins'] = df_.apply(lambda row: str(row['duration']).split(' ')[0], axis = 1)
    df_ = df_.astype({'mins':'float'})
    sb.display_bar_chart(df_,'rating','mins')
    return


def main():
    df = sb.read_data("netflix_titles.csv",True,True)
    create_new_columns(df)
    df = format_two_people(df)
    sb.output_data(df,'working_relationships.csv')

if __name__ == "__main__":
    main()