function [shells,b0s]=write_siemens_b_vecs(dirs,filename)

%% From Chantal in Jan 2024:
%% function to write b-vec files
%% I usually use this tool http://www.emmanuelcaruyer.com/q-space-sampling.php, which 1) can distribute gradient directions over multiple shells 2) takes into account that if the acquisition is cut short you still have a more or less optimal distribution and 3) flips directions to the other hemisphere to later correct better for eddy currents with FSL. But you could also use Camino.


mags=sum(dirs.^2,2).^0.5;
nnz_mags=mags(mags~=0);

shells=unique(round(nnz_mags*100)/100);
b0s=size(mags,1)-size(nnz_mags,1);

header1=['# NumShells: ' num2str(length(shells)) ', Relscales: ' num2str(transpose(shells(:)),'%0.4f,') ' b0s: ' num2str(b0s) ', Directions: ' num2str(length(nnz_mags))];
header2=['[directions=' num2str(size(dirs,1)) ']'];
header3='Normalisation = none';
header4='CoordinateSystem = xyz';

fid=fopen(filename,'w');
fprintf(fid,'%s\n%s\n%s\n%s\n\n',header1,header2,header3,header4);


for dir_idx=1:size(dirs,1)
    print_str=['vector[' num2str(dir_idx-1) '] = (' num2str(dirs(dir_idx,:),'%0.8f,') ')'];
    fprintf(fid,'%s\n',print_str);
end

fclose(fid);

return;
