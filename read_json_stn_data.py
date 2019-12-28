import json
import pandas as pd

with open('all_GPS_stations_data.json') as json_file:
    data = json.load(json_file)
    # print(json.dumps(data, indent=4))

df = pd.DataFrame(columns=['StnCode','Lat','Long','Elev','StnName'])

for i in range(len(data)):
    df.loc[i] = [data[i]['fourcharid'], data[i]['stnlat'],data[i]['stnlong'],data[i]['stnelev'],data[i]['stnname']]

print(f"minLong: {df['Long'].min()}")
print(f"maxLong: {df['Long'].max()}")
print(f"minLat: {df['Lat'].min()}")
print(f"maxLat: {df['Lat'].max()}")

df.to_csv('GPS_stations.txt',index=False,sep=',')


# print(df.head())