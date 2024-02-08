filename = '/Users/chantal/Documents/Code/CONNECTOM_BKUP_170920/CONNECTOM_BKUP_170920/Dirtabs/samples(1).txt';
delimiter = '\t';
startRow = 23;
formatSpec = '%f%f%f%f%[^\n\r]';
fileID = fopen(filename,'r');
dataArray = textscan(fileID, formatSpec, 'Delimiter', delimiter, 'HeaderLines' ,startRow-1, 'ReturnOnError', false, 'EndOfLine', '\r\n');
fclose(fileID);
dirs = [dataArray{1:end-1}];
shells = dirs(:,1);
dirs = dirs(:,2:4);
clearvars filename delimiter startRow formatSpec fileID dataArray ans;

necessary_bvals = 7000;%logspace(log10(200),log10(3000),4); %[200 1450 270 4000];
scanner_bval = max(necessary_bvals); %3000;%s/mm2 as set on the scanner

if max(shells) ~= length(necessary_bvals)
    error('number of shells in direction file and necessary_bvals should be the same')
end

norms = sum(dirs.^2,2);
dirs = dirs./repmat(sqrt(norms),[1 3]);

amplitude_scaling = (necessary_bvals/scanner_bval).^0.5;%sqrt for Grad strength because b-value squares with G
scaled_dirs = repmat(amplitude_scaling(shells),[1 3]) .* dirs; % sometimes transform

% add b0 images
intersp = 10; % b0 every nth image
sz=size(scaled_dirs,1);
cols = ceil(sz/intersp);
zeropad = cols*intersp - sz;
scaled_dirs_z = [scaled_dirs;zeros(zeropad,3)];
scaled_dirs_z = reshape(scaled_dirs_z, [intersp cols 3]);
scaled_dirs_z = cat(1, scaled_dirs_z, zeros(1,cols,3));
sznew = size(scaled_dirs_z);
scaled_dirs_z = reshape(scaled_dirs_z,[prod(sznew(1:2)) 3]);
scaled_dirs_z = scaled_dirs_z(1:end-zeropad-1,:);

write_siemens_b_vecs(scaled_dirs_z,'bvec30_Maryam.txt')