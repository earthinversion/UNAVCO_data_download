from download_gps_data import download_data
from extract_stations import extract_stations, output_extracted_stations
import pandas as pd
from plot_extracted_stations import plot_extracted_stations


## PARAMETERS
minLatitude = -90
maxLatitude = 90
minLongitude = -180
maxLongitude = 180

sttime = "2017-01-01" #starttime of data request
edtime = "2017-12-31" #endtime of data request

plot_stations = 1
##################################################
extracted_stations, ext_stns_df = extract_stations(minlat=minLatitude,maxlat=maxLatitude,minlon=minLongitude,maxlon=maxLongitude)
# output_extracted_stations(ext_stns_df)
# stn = extracted_stations[0]

downloaded_data = pd.DataFrame(columns=['StnCode','Latitude','Longitude','Elev'])
k=0
for i,stn in enumerate(extracted_stations):
    # exitcode = download_data(stn,sttime,edtime,analysisCenter= "cwu",referenceFrame= "nam14",dataPostProcessing = "Cleaned",refCoordOption = "from_analysis_center")
    exitcode = download_data(stn,sttime,edtime)
    if exitcode:
        print(ext_stns_df.iloc[i,0:4].values)
        downloaded_data.loc[k] = ext_stns_df.iloc[i,0:4].values
        k+=1
downloaded_data.to_csv(f"allStations_{sttime}_{edtime}_downloaded.csv",index=False)

if plot_stations:
    print("Plotting downloaded stations")
    plot_extracted_stations(downloaded_data,plot_global=True)
    # plot_extracted_stations(downloaded_data,plot_global=False)
