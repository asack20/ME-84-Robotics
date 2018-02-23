%% Instructions
% Plot will appear showing region arm can reach (Left of semicircle)
% Left Click: Add a point to the list
% Middle Click: Toggle pen up/down
% Right Click: End recording and save
% Arm coordinates are saved to a text file which can be used by the python
% program

%% Code
clear all;
close all;

saveName = 'square2.txt'; % name of coordinate file
r = 12; % Total length of arm (L1+L2) 

% Initial Locations
xLast = r;
yLast = 0;
pen = 1; % pen engaged (down)

% Plot size
yBound = -r:0.1:r;
xBound = sqrt(r.^2 - yBound.^2);

button = 1; % start with a left click

% Create figure and plot max-reach semicircle
figure;
hold on;

plot(xBound,yBound, 'b');
title('Pen is down')
daspect([1 1 1])
xlim([0 r])
ylim([-r r])

fid = fopen(saveName, 'wt'); % open writeable text file

% main loop
while (button ~= 3) % while not right click
    [x,y,button]=ginput(1); %get input
    if (button == 1) % left click
        fprintf(fid, '%0.2f\t%0.2f\t%d\n',x,y,pen); %save values to file
        
        % color of plotted line is different based on pen value
        if (pen == 0) % up/disengaged
            color = 'r'; % red
        else % down/engaged 
            color = 'g'; % green
        end
        plot([xLast x], [yLast y],color); % plot latest line segment
        
        % update last values
        xLast = x;
        yLast = y;
   
    elseif (button == 2) % right click
        pen = ~pen; % toggle pen value
        % Change title based on value
        if (pen == 0) % up
            title('Pen is up')
        else % down
            title('Pen is down')
        end
    end
end

fclose(fid); % close file
hold off;