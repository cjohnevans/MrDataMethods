% Loading DWMRS data (Minnesota sequence) via FID-A
% CJE 10/7/2024

fpath = '/home/sapje1/scratch_sapje1/2024/240716_dwmrs3Tinvivo/'
flist = { ...
'meas_MID00120_FID22721_dwmrs_slaser_LHippo_met.dat', ...
'meas_MID00123_FID22724_dwmrs_slaser_Lhippo_ref.dat', ...
'meas_MID00348_FID22949_dwmrs_slaser_LHippo_met.dat', ...
'meas_MID00349_FID22950_dwmrs_slaser_Lhippo_ref.dat' ...
   }

%% load and coil combine

fin = strcat(fpath, flist{1});

dwmrs = io_loadspec_twix(fin);
% coil combine
combos = op_getcoilcombos(dwmrs, 1, 'w');
combos.ref = 'Not sure';
%averaging
dwmrs = op_addrcvrs(dwmrs,1,'h', combos);
dwmrs = op_averaging(dwmrs)

%% averaging
figure()
plot(dwmrs.ppm, squeeze(real(dwmrs.specs)))
legend('1','2','3','4','5','6','7')
dwmrs.name = 'test'
io_writelcm(dwmrs, '/home/sapje1/scratch_sapje1/2024/240716_dwmrs3Tinvivo/meas_MID00120_FID22721_dwmrs_slaser_LHippo_met_lcmodel.raw', 85)

%% fudge the title
title('low b, low diffusivity')
xlabel('ppm')
xlim([4.5,5])
set(gca, 'XDir', 'Reverse')
