import pandas as pd
#Extract Tables from Websites
simpsons = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes')
print(len(simpsons))
print(simpsons[1])


#Extract CSV Files from Websites
#reasing 1 csv file from the website
df_premire21=pd.read_csv("https://www.football-data.co.uk/mmz4281/2122/E0.csv")


#showing dataframe
print(df_premire21)

#rename columns
df_premire21.rename(columns={
        'FTHG': 'home_goals',
        'FTAG' :'aways_goals'    
},inplace=True)
