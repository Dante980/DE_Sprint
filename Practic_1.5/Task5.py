import pandas as pd
# задача 1 - достать дынне
our_csv = pd.read_csv("ds_salaries.csv", delimiter=",")
# our_csv = our_csv.drop(our_csv.columns[[0]], axis=1)
# print(our_csv)

# задача 2 - сгруппировать по направлениям
job_title_list = our_csv.job_title.unique()
# print (job_title_list)
'''
                            # подзадача - привести все зарплаты в рубли
                            currency = {'EUR':59.01,  'USD':60.20, 'GBP':67.12, 'HUF':0.14, 'INR':0.74, 'JPY':0.42,
                                'CNY':8.46, 'MXN':2.99, 'CAD':43.52, 'DKK':7.93, 'PLN':12.16, 'SGD':42.04, 'CLP':0.062, 
                                'BRL':11.12, 'TRY':3.25, 'AUD':38.52, 'CHF':60.89}
                            our_csv["RUB_"] = our_csv["salary_currency"].map(currency)

                            our_csv["RUB_SALAEY"] = our_csv["salary"] * our_csv["RUB_"]
                            # print(our_csv["RUB_SALAEY"])
'''

# задача 3 - средняя и медианная зарплата по группам вакансий в 
agg_functions = {"salary_in_usd" : ['mean', 'median']}
temp_df = our_csv.groupby("job_title").agg(agg_functions).round(2)
# print(temp_df)

# задача 4 - средняя и медианная зарплата по регионам
agg_functions = {"salary_in_usd" : ['mean', 'median']}
temp_df = our_csv.groupby("company_location").agg(agg_functions).round(2)
# print(temp_df)

# задача 5 - самая высокооплачиваемая группа вакансий
agg_functions = {"salary_in_usd" : 'mean'}
temp_df = our_csv.groupby("job_title").mean().round(2)
temp_df = temp_df["salary_in_usd"]
# print(temp_df[temp_df == temp_df.max()])

# задача 6 - процентное соотношение каждого региона по вакансиям от всех вакансий
# print(our_csv.groupby('company_location').size() / len(our_csv) * 100)

# задача 7 - корреляция уровня опыта от зарплаты 
"""
temp_df = our_csv[["experience_level", "salary_in_usd"]]
temp_df.plot.scatter(x="experience_level", y="salary_in_usd")
print(temp_df["salary_in_usd"].corr(temp_df["experience_level"]))
"""
# задача 8 - сколько должностей в наборе
# print(len(our_csv.job_title.unique()))

# какие 10 наиболее встречающихся должностей
agg_functions = {"Unnamed: 0" : 'count'}
# print(our_csv.groupby("job_title", as_index=False).agg(agg_functions).sort_values("Unnamed: 0", ascending=False).head(10))
