import pandas as pd

basepath = "./"
filename = "countries.csv"
# list countries + codes and macro-regions
file = basepath + filename
df_country = pd.read_csv(file,'r',
    	delimiter=",", 
    	header = 0)

def country2region(country_reference, country_reference_type, region): # region / sub region  country_name alpha_2 alpha_3 country_code iso_3166_2 
	'''A function returning a:
	 - country_name, region or sub_region 
	using one of these country reference type:
	 - country_name alpha_2 alpha_3 country_code iso_3166_2'''
	index = pd.Index(list(df_country[country_reference_type]))
	return df_country[region].iloc[index.get_loc(country_reference)]

# Some examples:
print(country2region('IT', 'alpha_2' ,'country_name'))
print(country2region('ITA', 'alpha_3' ,'region'))
print(country2region('Italy', 'country_name' ,'sub_region'))
