no2 = pd.read_csv('data/20000101_20161231-NO2.csv', sep=';', skiprows=[1], na_values=['n/d'],
                  index_col=0, parse_dates=True)
no2.head()
