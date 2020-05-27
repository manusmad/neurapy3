from neurapy.neuralynx import lynxio
import logging
import os
import re
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)

nlxDir = '/Volumes/DomeDataSSD/Rat883/200306_Rat883-07/Neuralynx'
epoch_name = 'm1d'

# nrd_file_name = os.path.join(nlxDir,'RawData.nrd')
nrd_file_name = '/Volumes/manusmadNSB/RawDataNRD/Rat883/883-07_RawData.nrd'

defaults_file_name = os.path.join(nlxDir, 'Defaults')
# defaults_file_name  = '/Volumes/DomeDataSSD/Rat883/200226_Rat883-04/Neuralynx/Defaults'

# Parse Neuralynx directory name
exp_str = re.findall('\d+_Rat\d+-\d+',nlxDir)[0]
exp_date = datetime.strptime(exp_str[:6], '%y%m%d')
exp_date = datetime.strftime(exp_date, '%Y%m%d')
exp_str = exp_date + exp_str[6:]

mda_dir_name = '/Volumes/DomeDataSSD/franklab_mountainsort_test/Rat883/preprocessing/{}/{}_{}.mda'.\
    format(exp_date, exp_str, epoch_name)
mda_file_prefix = os.path.join(mda_dir_name, exp_str) + '_'
# Make output directory if not present
if not os.path.exists(mda_dir_name):
    try:
        os.makedirs(mda_dir_name)
    except OSError as exc:  # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise

tt_channel_dict = {x: list(range(4*(x-1), 4*x)) for x in range(1,17)}
lynxio.nrd2mda_epochs(nrd_filename=nrd_file_name, def_filename=defaults_file_name, mda_prefix=mda_file_prefix,
                      channel_dict=tt_channel_dict, epoch_names=epoch_name)