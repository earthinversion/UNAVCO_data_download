import pandas as pd

stn = "MDMT"
sttime = "2013-01-01"
edtime = "2018-01-01"
url = f'http://web-services.unavco.org/gps/data/position/{stn}/v3?analysisCenter=cwu&referenceFrame=nam14&starttime={sttime}&endtime={edtime}&report=short&dataPostProcessing=Cleaned&refCoordOption=from_analysis_center'

df = pd.read_csv(url, skiprows=8)
print(df.head())
print(df.shape)

output_filename = f"{stn}_{sttime}_{edtime}.csv"
df.to_csv(output_filename,index=False)