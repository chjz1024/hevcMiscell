function KL_compress(imgpath)
%                                   %使用K-L变换来对图像压缩
    f=imread(imgpath);   %读取图片路径
    f=im2double(f);         %将图像像素数据从int8转换为double
    y=[];                          %预设数组
    [m,n]=size(f);             %获取图像矩阵行数和列数

    %  拆分图像,将8*8的图像小块展开成1*64的向量，K-L变换的变换矩阵只和维度有关，故只需64*64的变换矩阵就可以了
    %  虽然这样计算降低了计算复杂度 ，但是并没有完全消除小块之间的相关性，但实验结果表明效果良好
    for i=1:m/8
        for j=1:n/8
            ii=(i-1)*8+1;
            jj=(j-1)*8+1;
            y_append=reshape(f(ii:ii+7,jj:jj+7),1,64);  % 将图像分成8*8的小块，并展开成1*64的向量
            y=[y;y_append];
        end
    end

    % K-L变换
    [coeff,score,latent]=pca(y);%利用matlab自带的pca(主成分分析)函数进行K-L变换
    k1=y*coeff;

    k11=k1;
    k12=k1;
    k13=k1;
    % 置0压缩过程
    k11(:,64:64)=0;         %压缩率=32/64=50%
    k12(:,17:64)=0;         %压缩率=16/64=75%
    k13(:,9:64)=0;           %压缩率=8/64=87.5%

    % K-L逆变换
    k11_inverse=k11*coeff';
    k12_inverse=k12*coeff';
    k13_inverse=k13*coeff';
    k=1;
    %  重组图像
    for i=1:m/8
        for j=1:n/8
            y1=reshape(k11_inverse(k,1:64),8,8);
            y2=reshape(k12_inverse(k,1:64),8,8);
            y3=reshape(k13_inverse(k,1:64),8,8);
            ii=(i-1)*8+1;
            jj=(j-1)*8+1;
            image1(ii:ii+7,jj:jj+7)=y1;
            image2(ii:ii+7,jj:jj+7)=y2;
            image3(ii:ii+7,jj:jj+7)=y3;
            k=k+1;
        end
    end
    figure(1);imshow(image1);title('未压缩');
    figure(2);imshow(image2);title('压缩75%');
    figure(3);imshow(image3);title('压缩87.5%');
end
