# Write code that explores your data set

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def set_pandas_display_options(dataframe):
    """
    Sets the display options for the dataframe

    Args:
        dataframe: pandas dataframe

    Returns: N/A

    """
    pd.set_option('display.max_rows', dataframe.shape[0] + 1)
    pd.set_option('display.max_columns', dataframe.shape[1] + 1)


def explore_structure(dataframe):
    """
    Prints the major feature of a dataframe: column and rows, first 4 rows, column name and datatype and null values
    per column.

    Args:
        dataframe: pandas dataframe

    Returns: N/A

    """
    print('The DBData dataframe has {0} rows and {1} columns'.format(dataframe.shape[0], dataframe.shape[1]))
    print(dataframe.head(4))
    print(dataframe.info(verbose=True))
    print(dataframe.isnull().sum(axis=0))


if __name__ == '__main__':
    # Read and explore DBData
    df = pd.read_csv('Data Set/DBJoint.csv')
    set_pandas_display_options(df)

    # OUTLIERS ANALYSIS
    unique_IN = df['Indicator Name'].unique()
    df_outliers = pd.DataFrame(columns=df.columns)

    for ind in range(len(unique_IN)):
        indicator_df = df[df['Indicator Name'] == unique_IN[ind]]
        boxplot = indicator_df.boxplot(column=indicator_df.columns.values[6:21].tolist(), rot=90)
        plt.title(unique_IN[ind])
        plt.show()

        df_outlier_ind = indicator_df
        stats = indicator_df.describe(exclude=[object])
        mean = np.array(stats.loc['mean', :].to_list())
        std_dev = np.array(stats.loc['std', :].to_list())
        upper = mean + 3*std_dev
        lower = mean - 3*std_dev

        for year in range(len(indicator_df.columns.vales[6:21])):
            up, low = upper[year], lower[year]
            for row in range(len(df_outlier_ind)):
                val = df_outlier_ind.iloc[row, year+6]
                if up > val > low:
                    df_outlier_ind.iat[row, year+6] = np.nan
        df_outliers = df_outliers.append(df_outlier_ind)

    df_outliers = df_outliers.sort_index()
    df_out = pd.DataFrame(columns=df.columns)
    for Row in range(len(df_outliers)):
        if df_outliers.iloc[Row, 6:21].isnull().sum() < 15:
            df_out = df_out.append(df_outliers.iloc[Row, :])
    df_out.to_csv('Data\DBOutliers.csv', index=False)

    # REGIONAL ANALYSIS
    unique_R = df['Region'].unique()
    chosen_ind = 'Starting a business - Score'

    chosen_ind_df = df[df['Indicator Name'] == chosen_ind]
    chosen_ind_df.reset_index(drop=True, inplace=True)
    df_mean = []

    for reg in range(len(unique_R)):
        region_df = chosen_ind_df[chosen_ind_df['Region'] == unique_R[reg]]
        region_df.reset_index(drop=True, inplace=True)

        reg_mean = []
        focus = region_df[region_df.columns[6:21]]
        for year in range(len(focus.columns)):
            reg_mean.append(focus.iloc[:, year].mean())
        df_mean.append(reg_mean)

    years = region_df.columns[6:21]
    for reg in range(len(unique_R)):
        plt.plot(years, df_mean[reg])
    plt.title('Starting a Business: Score - Regional Averages')
    plt.xticks(rotation=45)
    plt.legend(unique_R)
    plt.show()

    # GENDER ANALYSIS
    unique_R = df['Region'].unique()
    chosen_inds = ['Starting a business: Time - Women (days)', 'Starting a business: Time - Men (days)']
    e_array, m_array, f_array = [], [], []
    for reg in range(len(unique_R)):
        check_list = []
        region_df = df[df['Region'] == unique_R[reg]]
        region_df.reset_index(drop=True, inplace=True)

        F_region_df = region_df[region_df['Indicator Name'] == chosen_inds[0]]
        F_list = F_region_df['2020'].tolist()

        M_region_df = region_df[region_df['Indicator Name'] == chosen_inds[1]]
        M_list = M_region_df['2020'].tolist()

        for i in range(len(F_list)):
            check_list.append('M' if M_list[i] < F_list[i] else 'F' if M_list[i] > F_list[i] else 'E')
        count = Counter(check_list)
        size = len(check_list)
        e, m, f = count['E']/size, count['M']/size, count['F']/size
        e_array.append(e)
        m_array.append(m)
        f_array.append(f)

    me_array = np.array(m_array)+np.array(e_array)
    width = 0.5
    plt.figure(333)
    fig, ax = plt.subplots()
    ax.bar(unique_R, e_array, width, label='Equal')
    ax.bar(unique_R, m_array, width, bottom=e_array, label='Men')
    ax.bar(unique_R, f_array, width, bottom=me_array, label='Women')
    ax.set_ylabel('Percentage')
    ax.set_title('Regional gender inequality insight for days to start a business (%)')
    ax.legend()
    plt.xticks(rotation=60)
    plt.gcf().subplots_adjust(bottom=0.4)
    plt.show()

    # INCOME GROUP ANALYSIS
    unique_IG = df['Income Group'].unique()
    chosen_inds = ['Starting a business: Time - Women (days)',
                   'Starting a business: Procedures required - Women (number)',
                   'Starting a business: Cost - Women (% of income per capita)']

    df_IG_mean = []

    for inc_g in range(len(unique_IG)):
        income_df = df[df['Income Group'] == unique_IG[inc_g]]
        income_df.reset_index(drop=True, inplace=True)

        ind_mean = []
        for ind in range(len(chosen_inds)):
            ind_df = income_df[income_df['Indicator Name'] == chosen_inds[ind]]
            ind_df.reset_index(drop=True, inplace=True)
            IG_mean_year = []
            focus = ind_df[ind_df.columns[6:21]]
            for year in range(len(focus.columns)):
                IG_mean_year.append(focus.iloc[:, year].mean())
            ind_mean.append(IG_mean_year)
        df_IG_mean.append(ind_mean)

    years = income_df.columns[6:21]
    colours = ['r', 'g', 'b']
    for inc_g in range(len(unique_IG)):
        fig, axs = plt.subplots(3, 1, constrained_layout=True)
        fig.suptitle(unique_IG[inc_g])
        for ind in range(len(chosen_inds)):
            axs[ind].plot(years, df_IG_mean[inc_g][ind], colours[ind], label=chosen_inds[ind])
            axs[ind].legend(loc="upper right", fontsize=10)
            axs[ind].tick_params(axis='x', labelrotation=45, labelsize=10)
    plt.show()
