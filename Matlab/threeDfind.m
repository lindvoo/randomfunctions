function [roixyz] = threeDfind(scanname,value,direction)

%--------------------------------------------------------------------------
%returns coordinates that above value
%
%lddevoogd2013
%
%2021: added direction
%1=equal
%2-bigger
%3=smaller
%--------------------------------------------------------------------------


%read in ROI
hdr_roitemp=spm_vol(scanname);
data_roitemp=round(spm_read_vols(hdr_roitemp));

%make ROI search volume (X-Y-X coordinates of 1's in the ROI)
xxsv=zeros(hdr_roitemp.dim);
yysv=zeros(hdr_roitemp.dim);
zzsv=zeros(hdr_roitemp.dim);
for xx=1:hdr_roitemp.dim(1)
    xxsv(xx,:,:)=xx;
end
for yy=1:hdr_roitemp.dim(2)
    yysv(:,yy,:)=yy;
end
for zz=1:hdr_roitemp.dim(3)
    zzsv(:,:,zz)=zz;
end

if direction == 1 %equal
    roixx=xxsv(data_roitemp==value);
    roiyy=yysv(data_roitemp==value);
    roizz=zzsv(data_roitemp==value);
elseif direction ==2 %bigger
    roixx=xxsv(data_roitemp>value);
    roiyy=yysv(data_roitemp>value);
    roizz=zzsv(data_roitemp>value);
elseif direction==3 %smaller
    roixx=xxsv(data_roitemp<value);
    roiyy=yysv(data_roitemp<value);
    roizz=zzsv(data_roitemp<value);
end
roixyz=[roixx,roiyy,roizz,ones(size(roixx,1),1)]';
