import os
import sys
sys.path.append('/home/sapje1/code/python_mrobjects')
import twix_utils
import datetime

def get_one_bad_twix_file():
    return(['/cubric/scanners/mri/7t/transfer/314_WAND/314_73512_2C/meas_MID104_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID73231.dat'])

def get_ian_mp2rage_files():
#    search_dir = '/cubric/scanners/mri/7t/transfer/314_WAND'
    search_dir = '/cubric/scanners/mri/7t/transfer/314_WAND/'
    ppt_list = []
    ppt_list_file = open('/home/sapje1/code/python_mrscripts/missingRR20220629.txt', 'r')
    next_ppt = ppt_list_file.readline()
    while(next_ppt):
        ppt_list.append(next_ppt[0:-1] + "_2C")  # append, after stripping '\n'
        next_ppt = ppt_list_file.readline()
    ppt_list_file.close()

    ian_mp2rage_to_proc = []
    for (path, dirs, files) in os.walk(search_dir):
        for ppt in ppt_list:
            if ppt in path.split('/')[-1]:
#                print("ppt " + ppt + " is in  " + path.split('/')[-1])
                for dat_file in files:
                    if 'MP2RAGE_UK7T_081018_tfl_wip944_b17stx' in dat_file:
#                        print("MP2RAGE file is ", os.path.join(path, dat_file))
                        ian_mp2rage_to_proc.append(os.path.join(path, dat_file))
    print(ian_mp2rage_to_proc)
    print(len(ian_mp2rage_to_proc))
    return(ian_mp2rage_to_proc)

def all_mp2rage_files():
    all_twix = [ '314_01187_2C/meas_MID97_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID115298.dat', \
    '314_04843_2C/meas_MID135_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID107659.dat', \
    '314_05117_2C/meas_MID160_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID85450.dat', \
    '314_06400_2C/meas_MID196_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID115400.dat', \
    '314_06783_2C/meas_MID117_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID91229.dat', \
    '314_08033_2C/meas_MID161_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID93264.dat', \
    '314_09188_2C/meas_MID25_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID100881.dat', \
    '314_09188_2C/meas_MID26_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID100882.dat', \
    '314_09540_2C/meas_MID121_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID78125.dat', \
    '314_09720_2C/meas_MID91_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID108967.dat', \
    '314_10677_2C/meas_MID95_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID109315.dat', \
    '314_10677_2C/meas_MID96_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID109316.dat', \
    '314_10839_2C/meas_MID156_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID81657.dat', \
    '314_11220_2C/meas_MID167_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID73787.dat', \
    '314_12054_2C/meas_MID534_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID84768.dat', \
    '314_12653_2C/meas_MID28_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID95588.dat', \
    '314_13206_2C/meas_MID205_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID99503.dat', \
    '314_13953_2C/meas_MID104_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID112113.dat', \
    '314_14445_2C/meas_MID99_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID113338.dat', \
    '314_14900_2C/meas_MID181_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID79212.dat', \
    '314_14936_2C/meas_MID148_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID106177.dat', \
    '314_17726_2C/meas_MID441_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID115897.dat', \
    '314_19230_2C/meas_MID197_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID114386.dat', \
    '314_20028_2C/meas_MID337_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID76170.dat', \
    '314_22482_2C/meas_MID213_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID98696.dat', \
    '314_22786_2C/meas_MID184_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID78461.dat', \
    '314_22943_2C/meas_MID95_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID108455.dat', \
    '314_23322_2C/meas_MID234_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID89572.dat', \
    '314_24372_2C/meas_MID32_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID82314.dat', \
    '314_2442_2C/meas_MID270_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID75510.dat', \
    '314_24613_2C/meas_MID158_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID92766.dat', \
    '314_26383_2C/meas_MID88_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID110287.dat', \
    '314_27711_2C/meas_MID140_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID99134.dat', \
    '314_27934_2C/meas_MID358_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID91592.dat', \
    '314_28276_2C/meas_MID362_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID101248.dat', \
    '314_28617_2C/meas_MID185_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID94840.dat', \
    '314_30090_2C/meas_MID276_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID74979.dat', \
    '314_30648_2C/meas_MID105_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID80602.dat', \
    '314_31017_2C/meas_MID150_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID81379.dat', \
    '314_33184_2C/meas_MID106_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID83582.dat', \
    '314_33639_2C/meas_MID106_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID90128.dat', \
    '314_35814_2C/meas_MID151_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID108338.dat', \
    '314_38552_2C/meas_MID212_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID111805.dat', \
    '314_38989_2C/meas_MID23_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID116756.dat', \
    '314_39332_2C/meas_MID127_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID77562.dat', \
    '314_41590_2C/meas_MID172_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID107512.dat', \
    '314_42863_2C/meas_MID233_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID98938.dat', \
    '314_43240_2C/meas_MID195_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID106388.dat', \
    '314_43425_2C/meas_MID485_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID100227.dat', \
    '314_43766_2C/meas_MID301_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID88927.dat', \
    '314_45148_2C/meas_MID264_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID107934.dat', \
    '314_46263_2C/meas_MID28_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID105681.dat', \
    '314_47206_2C/meas_MID150_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID77042.dat', \
    '314_47803_2C/meas_MID132_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID104615.dat', \
    '314_49618_2C/meas_MID274_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID115140.dat', \
    '314_51896_2C/meas_MID125_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID75239.dat', \
    '314_52967_2C/meas_MID220_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID78679.dat', \
    '314_53696_2C/meas_MID44_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID71329.dat', \
    '314_54552_2C/meas_MID117_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID116598.dat', \
    '314_60324_2C/meas_MID152_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID87479.dat', \
    '314_61696_2C/meas_MID216_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID108578.dat', \
    '314_62452_2C/meas_MID149_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID89228.dat', \
    '314_62533_2C/meas_MID111_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID93495.dat', \
    '314_63392_2C/meas_MID184_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID112849.dat', \
    '314_64564_2C/meas_MID291_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID99286.dat', \
    '314_64812_2C/meas_MID95_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID114955.dat', \
    '314_64907_2C/meas_MID250_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID120441.dat', \
    '314_64988_2C/meas_MID95_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID112435.dat', \
    '314_66055_2C/meas_MID184_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID86208.dat', \
    '314_67613_2C/meas_MID220_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID78954.dat', \
    '314_67731_2C/meas_MID138_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID113099.dat', \
    '314_68443_2C/meas_MID134_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID114172.dat', \
    '314_69577_2C/meas_MID97_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID112327.dat', \
    '314_69988_2C/meas_MID185_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID112628.dat', \
    '314_70695_2C/meas_MID199_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID71540.dat', \
    '314_71675_2C/meas_MID139_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID80785.dat', \
    '314_72337_2C/meas_MID333_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID80365.dat', \
    '314_72753_2C/meas_MID318_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID72651.dat', \
    '314_72783_2C/meas_MID94_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID106545.dat', \
    '314_73378_2C/meas_MID531_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID88023.dat', \
    '314_73512_2C/meas_MID104_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID73231.dat', \
    '314_74182_2C/meas_MID245_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID76693.dat', \
    '314_74193_2C/meas_MID29_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID99713.dat', \
    '314_74516_2C/meas_MID132_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID97345.dat', \
    '314_75056_2C/meas_MID187_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID117674.dat', \
    '314_75086_2C/meas_MID238_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID96039.dat', \
    '314_75861_2C/meas_MID413_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID79978.dat', \
    '314_76147_2C/meas_MID132_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID119326.dat', \
    '314_76456_2C/meas_MID32_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID92060.dat', \
    '314_77660_2C/meas_MID441_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID72019.dat', \
    '314_77780_2C/meas_MID533_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID79560.dat', \
    '314_79577_2C/meas_MID103_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID94468.dat', \
    '314_80244_2C/meas_MID177_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID116157.dat', \
    '314_80780_2C/meas_MID119_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID95226.dat', \
    '314_81668_2C/meas_MID34_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID85172.dat', \
    '314_82107_2C/meas_MID737_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID70677.dat', \
    '314_83170_2C/meas_MID135_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID83262.dat', \
    '314_83997_2C/meas_MID254_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID104886.dat', \
    '314_84917_2C/meas_MID97_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID111916.dat', \
    '314_85522_2C/meas_MID100_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID107105.dat', \
    '314_87034_2C/meas_MID184_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID84423.dat', \
    '314_87051_2C/meas_MID112_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID101479.dat', \
    '314_88548_2C/meas_MID23_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID101865.dat', \
    '314_88686_2C/meas_MID106_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID93989.dat', \
    '314_89440_2C/meas_MID26_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID88546.dat', \
    '314_89448_2C/meas_MID147_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID95756.dat', \
    '314_93064_2C/meas_MID253_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID81084.dat', \
    '314_95017_2C/meas_MID163_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID81999.dat', \
    '314_95862_2C/meas_MID31_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID84014.dat', \
    '314_95985_2C/meas_MID183_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID72978.dat', \
    '314_97923_2C/meas_MID380_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID70317.dat', \
    '314_98476_2C/meas_MID286_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID94278.dat', \
    '314_99501_2C/meas_MID181_MP2RAGE_UK7T_081018_tfl_wip944_b17stx_FID86800.dat' ]
    return all_twix

#twix_top_dir = '/cubric/scanners/mri/7t/transfer/314_WAND/'
twix_top_dir = '/home/sapje1/scratch_sapje1/projects/314_wand/twix_mp2rage'
out_dir = os.path.join(twix_top_dir, 'mp2rage_twix_fix')

twix_file_list = get_ian_mp2rage_files()
#twix_file_list = get_one_bad_twix_file()

for twix_file in twix_file_list:
    one_twix = twix_utils.TwixFix(twix_file)
    one_twix.dump_data()
    one_twix.find_header_start()
    if(one_twix.header_is_good()):
        print(twix_file, "is good")
    else:
        print(twix_file, "is bad")
        twix_file_out = twix_file.split('.')[0] + '_headerfix_' + \
                        datetime.datetime.now().strftime("%Y%m%d%H%M%S") + '.dat' 
        one_twix.partial_write(twix_file_out)


