# remove/replace redundant data headers from column names
# list comprehension to the rescue
df.columns = [s.replace('foo_','') for s in list(df.columns.values)]


# replace a specific column name in df.columns.values
df.columns.values[1] = 'newColumnID'


# use groupby to get min date per group
# date was in YYYYMMDD int format
# using method chaining
df['MinDate'] = (
        df.groupby(by=['year'])['date']
            .transform('min')
            .apply(lambda x: pd.to_datetime(str(x), format='%Y%m%d')))
