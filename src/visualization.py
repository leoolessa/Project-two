import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import src.extracting as ext


def Filter_comic_class(conditional, reference_column, principal_column):
    """summary:
    1. Get a conditional, reference_column and principal_column
    2. Groupby the condition by reference_column and principal_column
    3. The size() function is applied to count the number of occurrences for each unique combination of reference_column and principal_column.
    4. The index of the resulting DataFrame from the groupby operation is reset, and the resulting Series is converted back into a DataFrame.
        - The new column containing the count is named 'Count'.
    5. The DataFrame is sorted first by the principal_column column in ascending order.
    6. The drop_duplicates function is used to keep only the first occurrence for each year, removing duplicates.
    7. Returns the filtered values ​​to the DF 
    Args:
        conditional: Get the conditional 
        reference_column: Get a column from DF as a reference 
        principal_column: Get a column from DF as principal

    Returns:
        Returns the filtered values ​​to the DF 
    """
    filter_ = (
    conditional.groupby([reference_column, principal_column])
    .size()
    .reset_index(name='Count')
    .sort_values(principal_column, ascending=True)
    .drop_duplicates(reference_column)
    )
    return filter_


def sort_one_column(df, column, column_value):
    """summary:
    1. Get a DF, column from DF and the specific column's value
    2. Sort a specific value from the column
    3. Return the column sorted by the specific value
    Args:
        df (DataFrame): Get a DF
        column: Get a column
        column_value : Get one value from the column

    Returns:
        Return the column sorted by the specific value
    """
    sort = df[df[column] == column_value]
    return sort


def sort_two_columns(df, column, column_one_value, column_two_value):
    """summary:
    1. Get a DF, column from DF and two specifics column's value
    2. Sort the two specific values from the column
    3. Return the column sorted by the specific values
    Args:
        df (DataFrame): Get a DF
        column: Get a column
        column_one_value: Get the first value from the column to be checked
        column_two_value: Get the second value from the column to be checked
    Returns:
        Return the column sorted by the specific values
    """
    sort = df[(df[column] == column_one_value) | (df[column] == column_two_value)]
    return sort


def add_conditial(variable, principal_column, reference_column):
    """summary:
    1. Get a variable, principal_column and reference_column
    2. Get the 8 hightest values from the from principal column
    3. Reference column match the values with the principal column 
    4. Return the 8 hightest values
    Args:
        variable: Get the variable sorted by the previous functions (sort_one_column)
        principal_column: Get the principal column
        reference_column: Get the reference column

    Returns:
        Return the 8 hightest values
    """
    cond = variable.nlargest(8, principal_column)[[reference_column, principal_column]]
    return cond

def add_conditial_20(variable, principal_column, reference_column):
    cond = variable.nlargest(20, principal_column)[[reference_column, principal_column]].drop_duplicates()
    return cond


def sort_two_columns_(df, column, column_one_value, column_two_value):
    sort = df[(df[column] == column_one_value) | (df[column] == column_two_value)].drop_duplicates()
    return sort


def visual_plot(variable, x_column, y_column, x_lable, y_lable, title ):
    sns.barplot(x=x_column, y=y_column, data=variable, palette="Blues")
    plt.xlabel(x_lable)
    plt.ylabel(y_lable)
    plt.title(title)
    plt.xticks(rotation=45, ha='right')
    plt.savefig(f'images/test-{title}.png', format='png')
    plt.show()



# Calling the sort functions
avengers_hero_sort = sort_one_column(ext.marvel_all_characters_df,'Class', 'Avengers')

avengers_villain_sort = sort_one_column(ext.marvel_all_characters_df,'Class', 'Villain_Avengers')

avengers_and_villain_sort = sort_two_columns(ext.marvel_all_characters_df, 'Class', 'Avengers', 'Villain_Avengers')


# Calling the conditional function
top_avengers = add_conditial(avengers_hero_sort, 'Comics', 'Name')

top_villain = add_conditial(avengers_villain_sort, 'Comics', 'Name')

top_comics_avengers_world = add_conditial(avengers_and_villain_sort, 'Comics', 'Name')

top_comics_marvel_world = add_conditial_20(ext.marvel_all_characters_df, 'Comics', 'Name')


# Calling the Filter function
top_8_avengers = Filter_comic_class(top_avengers, 'Name', 'Comics')

top_8_villain = Filter_comic_class(top_villain, 'Name', 'Comics')

top_8_avengers_world = Filter_comic_class(top_comics_avengers_world, 'Name', 'Comics')

top_marvels_world = Filter_comic_class(top_comics_marvel_world, 'Name', 'Comics')


# Conclusion code (Percentage)
total_avengers_comics_ = sort_two_columns_(ext.marvel_all_characters_df, 'Class', 'Avengers', 'Villain_Avengers')
total_xmen_comics_ = sort_two_columns_(ext.marvel_all_characters_df, 'Class', 'X-Men', 'Villain_X-Men')


percentage_avengers = (total_avengers_comics_['Comics'].sum() / (total_avengers_comics_['Comics'].sum() + total_xmen_comics_['Comics'].sum())) * 100
percentage_xmen = 100 - percentage_avengers  


result_df = pd.DataFrame({'Class': ['Avengers', 'X-Men'], 'Percentage': [percentage_avengers, percentage_xmen]})


perc = result_df['Percentage']
lab = result_df['Class']


