import pandas as pd
import os

def download_data(stn,sttime="2017-12-31",edtime="",analysisCenter= "cwu",referenceFrame= "nam14",dataPostProcessing = "Cleaned",refCoordOption = "from_analysis_center",output_dir="Data"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)
    
    output_filename = f"{output_dir}/{stn}_{sttime}_{edtime}.csv"
    if os.path.exists(output_filename):
        print(f"{output_filename} already exists!")
        return 1

    try:
        if edtime:
            url = f'http://web-services.unavco.org/gps/data/position/{stn}/v3?analysisCenter={analysisCenter}&referenceFrame={referenceFrame}&starttime={sttime}&endtime={edtime}&report=short&dataPostProcessing={dataPostProcessing}&refCoordOption={refCoordOption}'
        else:
            url = f'http://web-services.unavco.org/gps/data/position/{stn}/v3?analysisCenter={analysisCenter}&referenceFrame={referenceFrame}&starttime={sttime}&report=short&dataPostProcessing={dataPostProcessing}&refCoordOption={refCoordOption}'

        df = pd.read_csv(url, skiprows=8)
        # print(df.head())
        # print(df.shape)

        df.to_csv(output_filename,index=False)
        print(f"{output_filename} downloaded successfully")
        exitcode = 1
        return exitcode
    except Exception as e:
        exitcode = 0
        print(e)
        print(f"{output_filename} download failed")
        return exitcode




if __name__ == "__main__":
    # stn = "MDMT" #The four character station identifier.
    stn = "KULU" #The four character station identifier.

    analysisCenter = "cwu" #GPS station position solutions are available from 4 different Analysis Centers (AC's).
    #other options are - pbo, nmt, unr
    # CWU is the default AC and is the standard GAGE data product as of 2018-09-16. PBO and NMT solutions are only available up until 2018-09-15. PBO solutions were a combination of NMT and CWU solutions and are considered to be the standard GAGE data product.

    referenceFrame = "nam14" #Reference Frame used for the position coordinates. 
    #Coordinates in NAM14 are available from all AC's with the exception of UNR. Coordinates in a North America fixed reference frame are also available from all AC's but PBO, NMT, CWU use "NAM08" while UNR uses "NA12". NAM08 and NA12 are realized in different ways.

    sttime = "2013-01-01" #starttime of data request
    edtime = "2018-01-01" #endtime of data request
    # edtime = "" for last date available.

    dataPostProcessing = "Cleaned" #Processing performed on data after retrieved. 
    #"Uncleaned" - no post processing performed - data is returned as retrieved (default) "Cleaned" - The offset values for North, East or Up are set to NULL when the Standard deviation for the timestamp and direction > 20 millimeters.

    refCoordOption = "from_analysis_center"
    #Select whether position solution offsets are relative to the "reference position" indicated in the source file (default) or whether the coordinate for the first epoch is adjusted to be 0.000m. The actual relative station displacements through time are the same regardless of option selected.
    # options - "from_analysis_center" or "first_epoch"

    # download_data(stn,sttime,edtime,analysisCenter= "cwu",referenceFrame= "nam14",dataPostProcessing = "Cleaned",refCoordOption = "from_analysis_center")

    download_data(stn,sttime,edtime)