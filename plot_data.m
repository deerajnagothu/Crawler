
fid = fopen('export.csv');
out = textscan(fid,'%s%f%s%f','delimiter',',');
fclose(fid);
col1 = out{1};
col2 = out{2};
col3 = out{3};
col4 = out{4};
subplot(1,1,1)
plot(col2)
subplot(1,2,1)
plot(col4)
%set(gca,'xticklabel',col1.')