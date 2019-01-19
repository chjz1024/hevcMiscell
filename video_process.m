clc;close all;clear all;

%{
%**************************************************************%
????????????????????????cell
a????
b????
c?a-b
delta?????
delta1???dst?idst????????????dct????????
d????????MV?????????
d1?????MV?????????????
%**************************************************************%
%}


obj = VideoReader('/Users/Mr.Zhang/Desktop/abc.mp4');%??????
numFrames = obj.NumberOfFrames;% ????
 for k = 100:101% ???15?
     frame = read(obj,k);%?????
    % imshow(frame);%???
      imwrite(frame,strcat('/Users/Mr.Zhang/Desktop/',num2str(k),'.jpg'),'jpg');% ???
 end

 a=imread('/Users/Mr.Zhang/Desktop/100.jpg');
 b=imread('/Users/Mr.Zhang/Desktop/101.jpg');
a=rgb2gray(a);
b=rgb2gray(b);
c=b-a;
%a 960*544

seg1=4*ones(1,240);
seg2=4*ones(1,136);
A=mat2cell(a,seg1,seg2);
%size(A);%240*136
B=mat2cell(b,seg1,seg2);

delta = im2uint8(zeros(960,544));
DELTA = mat2cell(delta,seg1,seg2);

Cx = zeros(240,136);
Cy = zeros(240,136);
row = 0;
column = 0;

for x=2:239
    for y=2:135
        cp = zeros(3,3);%MSE
        cp(1,1) = sum((sum(B{x,y}-A{x-1,y-1}).^2));
        cp(1,2) = sum((sum(B{x,y}-A{x-1,y}).^2));
        cp(1,3) = sum((sum(B{x,y}-A{x-1,y+1}).^2));
        
        cp(2,1) = sum((sum(B{x,y}-A{x,y-1}).^2));
        cp(2,2) = sum((sum(B{x,y}-A{x,y}).^2));
        cp(2,3) = sum((sum(B{x,y}-A{x,y+1}).^2));
        
        cp(3,1) = sum((sum(B{x,y}-A{x+1,y-1}).^2));
        cp(3,2) = sum((sum(B{x,y}-A{x+1,y}).^2));
        cp(3,3) = sum((sum(B{x,y}-A{x+1,y+1}).^2));
        
        m = min(cp);
        mm = min(m);
        [row,column]=find(cp==mm);
        row = row-2;
        column = column-2;
        DELTA{x,y} = A{x+row(1),y+column(1)} -  B{x,y}  ;
        %if x==100&y==100
           % DELTA{x,y}
        %end
        Cx(x,y) = row(1);
        Cy(x,y) = column(1);
    end
end


delta = cell2mat(DELTA);
dct = dct2(delta);
size(dct);
for x=960
    for y=544
        if abs(dct(x,y)) <=0.0001
            dct(x,y) = 0;
        end
    end
end
idct = idct2(dct);
%max(max(idct))
%min(min(idct))
for x=960
    for y=544
            idct(x,y) = min(max(0,dct(x,y)),255);
        end
end
delta1 = im2uint8(idct);
DELTA1=mat2cell(delta1,seg1,seg2);



%use A&C to reform B
d = zeros(960,544);
D = mat2cell(d,seg1,seg2);
D = A;
D1 = A;
for x=2:239
    for y=2:135
        D1{x,y} = A{x+Cx(x,y),y+Cy(x,y)} - DELTA{x,y};
        D{x,y} = A{x+Cx(x,y),y+Cy(x,y)};
    end
end
d = cell2mat(D);


%{
s = 0;
for x=1:240
    for y = 1:136
        s = sum(sum(abs(D{x,y})));
    end
end


m = sum(sum(abs(d)))
n = sum(sum(abs(Cx)))+sum(sum(abs(Cy)))+s
m/n
%}
figure(1);
subplot(2,2,1);imshow(a);
subplot(2,2,2);imshow(b);
%subplot(2,2,3);imshow(c);
subplot(2,2,3);imshow(d-b);
subplot(2,2,4);imshow(d);

figure(2);imshow(delta);

count  = double(delta);
size(delta);%960*544
max(max(delta));
min(min(delta));
temp = zeros(1,256);
for x=1:960
    for y=1:544
        temp(count(x,y)+1) = temp(count(x,y)+1) +1;
    end
end
max(max(temp));
min(min(delta));
find(temp==0);
figure(3);
bar(temp);axis([1,256,0,max(max(temp))]);


 
 
