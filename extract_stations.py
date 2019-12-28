import pandas as pd

def extract_stations(minlat,maxlat,minlon,maxlon,info_file='GPS_stations.txt'):
    '''
    minlat: minimum latitude (ranges from -90 to 90)
    maxlat: maximum latitude (ranges from -90 to 90)
    minlon: minimum longitude (ranges from -180 to 180)
    maxlon: maximum longitude (ranges from -180 to 180)
    '''
    
    if minlat<-90 or minlat>90 or maxlat<-90 or maxlat>90 or minlon<-180 or minlon>180 or maxlon<-180 or maxlon>180 or maxlat<minlat:
        raise Exception("Incorrect input value for latitude/Longitude")

    ## read stations file
    all_stations = pd.read_csv(info_file)
    # print(f"minLong: {all_stations['Long'].min()}")
    # print(f"maxLong: {all_stations['Long'].max()}")
    # print(f"minLat: {all_stations['Lat'].min()}")
    # print(f"maxLat: {all_stations['Lat'].max()}")
    # print(all_stations.shape)

    ## filter
    all_stations = all_stations[(all_stations['Lat']>=minlat) & (all_stations['Lat']<=maxlat) & (all_stations['Long']>=minlon) & (all_stations['Long']<=maxlon)]
    print(f"minLong: {all_stations['Long'].min()}")
    print(f"maxLong: {all_stations['Long'].max()}")
    print(f"minLat: {all_stations['Lat'].min()}")
    print(f"maxLat: {all_stations['Lat'].max()}")

    # print(all_stations.shape)
    # print(all_stations.head())
    ext_stns = all_stations['StnCode'].values
    return ext_stns, all_stations

def output_extracted_stations(all_stations):
    all_stations = all_stations.sort_values(by='Long', na_position='first')
    numOut = all_stations.shape[0]
    for i in range(numOut):
        print(all_stations.iloc[i,:].values)
    



if __name__ == "__main__":
    extract_stations(minlat=50,maxlat=90,minlon=-60,maxlon=180)
