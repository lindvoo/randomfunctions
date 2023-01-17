function spm_print_list(TabDat,savedir,savename)

% -------------------------------------------------------------------------
% Print SPM table for easy use
%
% adjusted by lindadevoogd2023
% -------------------------------------------------------------------------
  
%names for table
tablenames={'set-level(d)','set-level(d)',...
    'cluster-level(FWE-cor)','cluster-level(FDR-cor)','voxnum','cluster-level(un-cor)',...
    'peak-level(FWE-cor)','peak-level(FDR-cor)','T','Z','peak-level(un-cor)',...
    'x(mm)','y(mm)','z(mm)','side'}

%get coordinates out cell structure
for cc=1:size(TabDat.dat,1)
    
    coor(cc,:)=cell2mat(TabDat.dat(cc,12))';
    
    if coor(cc,1)>0
        
        side(cc,:)='R';
        
    else
    
        side(cc,:)='L';
        
    end
    
end

%put in one table
tableout=[TabDat.dat(:,1:11) num2cell(coor) cellstr(side)];

%add names
newtable=[cellstr(tablenames);tableout];

%save in CSV file
cell2csv(fullfile(savedir,[savename '.csv']),newtable,',');
