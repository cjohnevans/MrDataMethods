import sys
sys.path.append('/home/sapje1/code/python_mrdatamethods')
import twixmrs

# wand 3T MRS
#data_dir = '/home/sapje1/data_sapje1/projects/wand/mrs/19_06_14-11_17_09-DST-1_3_12_2_1107_5_2_43_66073/scans/502-RAW_anonymised/resources/TWIX/files'
#in_file = 'meas_MID00465_FID13471_mpress_AC_met.dat'
#covid bbb brainstem 7t cubric pilot
data_dir = '/home/sapje1/data_sapje1/projects/covidbbb'
in_file = [ 'pilot220315/meas_MID165_sLaser_Brainstem_20_12_12_FID118913.dat',             'oxford017/meas_MID156_sLaser_Brainstem_20_12_12_FID7821.dat',             'oxford018/meas_MID112_sLaser_Brainstem_20_12_12_FID8065.dat' ]
#in_file = ['pilot220315/meas_MID165_sLaser_Brainstem_20_12_12_FID118913.dat']
#covid bbb brainstem 7t cubric pilot
data_dir = '/home/sapje1/data_sapje1/projects/covidbbb'
in_file = [ 'pilot220315/meas_MID165_sLaser_Brainstem_20_12_12_FID118913.dat',             'oxford017/meas_MID156_sLaser_Brainstem_20_12_12_FID7821.dat',             'oxford018/meas_MID112_sLaser_Brainstem_20_12_12_FID8065.dat' ]
# Jiaxiang 469_decision pilot
data_dir = '/home/sapje1/scratch_sapje1/projects/469_decision/mrs'
in_file = [ '240322-401_pilot/meas_MID00551_FID47096_PRESS30_AC_128avg.dat', \
            '240322-401_pilot/meas_MID00575_FID47120_PRESS30_OCC_128avg.dat' ]

print(in_file)
mrs_data = twixmrs.twixmrs_load_basic(data_dir, in_file)

mrs_data_phased = []
mrs_data_phased.append( mrs_data[0].adjust_phase(0,-0.040) )  #acc
mrs_data_phased.append( mrs_data[2].adjust_phase(0,-0.0345) )   # occ

print([ phs.shape for phs in mrs_data_phased ])
line_label = ['ACC', 'Occipital' ]
twixmrs.twixmrs_plot(mrs_data_phased, line_label, xlim=(5,0), ylim=(-50,100))
