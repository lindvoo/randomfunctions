clear all; clc;

% -------------------------------------------------------------------------
% Print SPM table for easy use
%
% need following fuctions:
% spm_print_list.m
% spm_getSPM2.m
%
% lindadevoogd2023
% -------------------------------------------------------------------------

% Set paths [adjust accordingly...]
% -------------------------------------------------------------------------
project.statsdir = 'XXXX';
project.savedir = fullfile(project.statsdir,'csv_files')
mkdir(project.savedir)
project.curdir = fullfile(project.statsdir,'XXXX');
project.subdirs = {'XXXX'}; % this should be the folder where the SPM.mat file is located



% Run the stats
% -------------------------------------------------------------------------

% Loop over contrast folders
for c_con = 1:numel(project.subdirs);

    % Loop over activation and deactivation
    for c_act_deac = 1:2

        % Run the stats using adjusted spm_getSPM so GUI does not ask
        % questions
        [~,xSPM] = spm_getSPM2(fullfile(project.curdir,project.subdirs{c_con}),c_act_deac);

        % Add 2 answers for GUI questions
        spm('defaults','fMRI')
        xSPM.thresDesc = 'none';

        % Run
        [hReg, xSPM, ~] = spm_results_ui('Setup',xSPM);

        % Convert to table
        TabDat = spm_list('List',xSPM,hReg,[]);

        % Save as csv file
        cd(project.savedir)
        spm_print_list(TabDat,project.savedir,[project.subdirs{c_con} '_' num2str(c_act_deac)]);

        % Clean up
        clear xSPM hReg TabDat
        close all
    end

end



