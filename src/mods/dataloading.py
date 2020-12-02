import wget
import os
import zipfile

def pullkagglezip(targetdir='data/extracted/'):
    """Pulls data files from Kaggle. 
    
            Parameters:
                targetdir (str): Where files are to be saved.
            Returns:
                file_locs (list of str): Returns locations for all the extracted files.
                
        Dependencies: wget, os
    """
    # Append slash if not at end of targetdir
    if targetdir[-1] != '/':
        targetdir += '/'
    
    # Make targetdir if doesn't exist
    if not os.path.isdir(targetdir):
        os.mkdir(targetdir)
    
    # create target zip location 
    targetzip = targetdir + 'data.zip'
    
    # if target zip exists do nothing, else download
    if os.path.isfile(targetzip):
        pass
    else:
        url = 'https://storage.googleapis.com/kaggle-data-sets/44267/525696/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20201201%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20201201T190854Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=a76dcfd307e6057861ed15134e403a9c15d2519728fbd2b6f1de7aa8bd19a47a08d408b60b5edcde3e7052d325e408b98c985b46c656f06e275ba150ffb8a13452bbb1d8f373790aa9017900bc66a4f182dcfa8b0c6a34d3eff217933e98cede6b611fc9e5f9e3f4993f2be3600b38d884c86ad983811c7e978f959476b306a814ab8e4b3e93fd582339b84fd1d2be19e76412a3b0294a6d7e238db120ba869cdb01fbcc4c39f4bd7abe360a77669e2617ec400b094399942cc9645f4f9651e085698e7038713dad79f3b65f877aa70a5041b6a46fab8049c242556d7f922e65896c2369a51c37f8c58da2690d460da3e8ef8542f37b5700ae7e04433e98c390'
        wget.download(url, targetzip)
    
    # Unzip images and save locations of same 
    file_locs = Unzip(targetzip)

    return file_locs

def Unzip(targetzip):
    """Unzip a file.
    
            Parameters:
                targetzip (str): String of path to target zip file.
            Returns:
                file_locs (list of str): Returns locations for all the extracted files.
                
        Dependencies: os, zipfile
    """

    # Set and/or create sub-folder
    sub_folder = targetzip.rsplit('/',1)[0] + '/'
    try:
        os.mkdir(sub_folder)
    except:
        pass
    
    # Unzipping file        
    try:
        
        with zipfile.ZipFile(targetzip, 'r') as zip_ref:
            zip_ref.extractall(sub_folder)
            # Get list of files names in zip
            files = zip_ref.namelist()
    except:
        raise
        
    # Return list of locations of extracted files   
    file_locs = [] 
    for file in files:
        file_locs.append(sub_folder + file)
    
    return file_locs