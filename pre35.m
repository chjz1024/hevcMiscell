clc;
clear all;
N=32;
a=zeros(65);
for x=1:65 
    a(1,x)=255-mod((x-1)*16,255);
    a(x,1)=255-mod((x-1)*16,255);
end
for x=2:65
    for y=2:65
        a(x,y)=255;
    end
end

A=cell(1,35);

for x=1:N        %mode planar
    for y=1:N
        a(x+1,y+1)=ceil(((N-x)*a(1,y+1)+(x)*a(N+2,1)+(N-y)*a(x+1,1)+y*a(1,N+2))/(2*N));
    end
end
A{1,1}=uint8(a);

dc=0;
for x=2:N+1        %mode DC
    dc=dc+a(x,1);
end
for y=2:N+1
    dc=dc+a(1,y);
end
dc=ceil(dc/(2*N));
a(2,2)=ceil((a(2,1)+a(1,2))/4);
for x=2:32
    a(x+1,2)=ceil((a(x+1,1)+3*dc)/4);
end
for y=2:32
    a(2,y+1)=ceil((a(1,y+1)+3*dc)/4);
end
for x=3:33
    for y=3:33
        a(x,y)=dc;
    end
end
A{1,2}=uint8(a);


for x=1:32            %mode 10
    for y=1:32
        if x==1 a(x+1,y+1)=ceil(a(1,y+1)/2)+a(1,1);
        else 
        a(x+1,y+1)=a(x+1,1);
        end
    end
end
A{1,11}=uint8(a);


for x=1:32            %mode 26
    for y=1:32
        if y==1 a(x+1,y+1)=ceil(a(x+1,1)/2)+a(1,1);
        else 
        a(x+1,y+1)=a(1,y+1);
        end
    end
end
A{1,27}=uint8(a);

offset=[0,32,26,21,17,13,9,5,2,0,-2,-5,-9,-13,-17,-21,-26,-32,-26,-21,-17,-13,-9,-5,-2,0,2,5,9,13,17,21,26,32];

for M=18:34
    if M~=26
    
   ref=zeros(1,200);
    

if offset(M)<0
    for x=offset(M):offset(M)+2*N
        if x>=0
            ref(x+33)=a(1,x+1);
        else
            ref(x+33)=a(round((32*x)/offset(M))+1,1);
        end
    end
else for x=0:64
        ref(x+33)=a(1,x+1);
    end
end


for x=1:N
    for y=1:N
        pos=floor((x*offset(M))/32);
        w=mod(x*offset(M),32);
        a(x+1,y+1)=ceil(((32-w)*ref(y+pos+33)+w*ref(y+pos+1+33))/32);
    end
end
A{1,M+1}=uint8(a);
    end
end

   
for M=2:17
    if M~=10
ref=zeros(1,200);
if offset(M)<0
    for y=offset(M):offset(M)+2*N
        if y>=0
            ref(y+33)=a(1,y+1);
        else
            ref(y+33)=a(round((32*y)/offset(M))+1,1);
        end
    end
else for y=0:64
        ref(y+33)=a(1,y+1);
    end
end


for x=1:N
    for y=1:N
        pos=floor((y*offset(M))/32);
        w=mod(y*offset(M),32);
        a(x+1,y+1)=ceil(((32-w)*ref(x+pos+33)+w*ref(x+pos+1+33))/32);
    end
end
A{1,M+1}=uint8(a);
    end
end

