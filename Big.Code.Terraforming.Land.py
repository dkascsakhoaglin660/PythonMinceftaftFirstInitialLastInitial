import mcpi.minecraft as minecraft
from ISStreamer.Streamer import Streamer
import mcpi.block as block
import time, datetime, psutil

for pros in psutil.pids():
    if psutil.Process(pros).name() == 'minecraft-pi' and len(psutil.Process(pros).cmdline()) == 1
        pm = psutil.Process(pros)
streamer = Streamer(
    bucket_name =":muchroom: Terraforming", bucket_key="<enter here>", access_key= "<eneter here>")
Free_accound = False

def upload_data_to_IS(
    print('Uploading to Initial State')
    streamer.log(":snail: Run Speed", speed)
    streamer.log(":jack_o_lantern: Run2 Time since last " + str(num_blocks) + "blocks",elapsed)
    streamer.log(":volcano: Run2 Total Blocks",blocks_processed)
    streamer.log)
streamer.log(