import sys
sys.path.append('/home/sapje1/code/python_mrobjects')
import twixmrs

# Glu Gln phantom
data_dir = '/home/sapje1/data_sapje1/projects/chemistry_glu_gln/twix'
in_file = ['meas_MID00233_FID15875_slaser_dkd_256NEX_TR3.dat']
    
print(in_file)
mrs_data = twixmrs.twixmrs_load_basic(data_dir, in_file)

mrs_data_phased = []
mrs_data_phased.append( mrs_data[0].adjust_phase(0,-0.040) )  

print([ phs.shape for phs in mrs_data_phased ])

# ... incomplete
twixmrs.twixmrs_plot(mrs_data_phased, line_label, xlim=(5,0), ylim=(-50,100))
