clear all;
close all;

saveName = 'square.txt';
r = 12;
button = 1;
yBound = -r:0.1:r;
xBound = sqrt(r.^2 - yBound.^2);

% Initial Locations
xLast = r;
yLast = 0;
pen = 1;

figure;
hold on;

plot(xBound,yBound);
title('Pen is down')
daspect([1 1 1])
xlim([0 r])
ylim([-r r])

fid = fopen(saveName, 'wt'); % open writeable text file

while (button ~= 3)
    [x,y,button]=ginput(1);
    if (button == 1)
        fprintf(fid, '%0.2f\t%0.2f\t%d\n',x,y,pen);
        
        if (pen == 0)
            color = 'r';
        else
            color = 'g';
        end
        plot([xLast x], [yLast y],color); 
        
        xLast = x;
        yLast = y;
   
    elseif (button == 2)
        pen = ~pen;
        if (pen == 0)
            title('Pen is up')
        else 
            title('Pen is down')
        end
    end
end



fclose(fid);

hold off;
close all;