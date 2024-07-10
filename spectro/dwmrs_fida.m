% Loading DWMRS data (Minnesota sequence) via FID-A
% CJE 10/7/2024

fpath = '/home/sapje1/scratch_sapje1/2024/240710_dwmrs3T/twix/240709_dwmrs_caliberphantom/'
flist = { ...
   'meas_MID00298_FID21938_dwmrs_slaser_diff_b1882_centrevial.dat', ...
   'meas_MID00299_FID21939_dwmrs_slaser_diff_b0460_centrevial.dat', ...
   'meas_MID00319_FID21959_dwmrs_slaser_diff_b1882_edgevial.dat', ...
   'meas_MID00320_FID21960_dwmrs_slaser_diff_b0460_edgevial.dat', ...
   }

%% load and coil combine

fin = strcat(fpath, flist{4});

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

%% fudge the title
title('low b, low diffusivity')
xlabel('ppm')
xlim([4.5,5])
set(gca, 'XDir', 'Reverse')
