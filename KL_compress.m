function KL_compress(imgpath)
%                                   %ʹ��K-L�任����ͼ��ѹ��
    f=imread(imgpath);   %��ȡͼƬ·��
    f=im2double(f);         %��ͼ���������ݴ�int8ת��Ϊdouble
    y=[];                          %Ԥ������
    [m,n]=size(f);             %��ȡͼ���������������

    %  ���ͼ��,��8*8��ͼ��С��չ����1*64��������K-L�任�ı任����ֻ��ά���йأ���ֻ��64*64�ı任����Ϳ�����
    %  ��Ȼ�������㽵���˼��㸴�Ӷ� �����ǲ�û����ȫ����С��֮�������ԣ���ʵ��������Ч������
    for i=1:m/8
        for j=1:n/8
            ii=(i-1)*8+1;
            jj=(j-1)*8+1;
            y_append=reshape(f(ii:ii+7,jj:jj+7),1,64);  % ��ͼ��ֳ�8*8��С�飬��չ����1*64������
            y=[y;y_append];
        end
    end

    % K-L�任
    [coeff,score,latent]=pca(y);%����matlab�Դ���pca(���ɷַ���)��������K-L�任
    k1=y*coeff;

    k11=k1;
    k12=k1;
    k13=k1;
    % ��0ѹ������
    k11(:,64:64)=0;         %ѹ����=32/64=50%
    k12(:,17:64)=0;         %ѹ����=16/64=75%
    k13(:,9:64)=0;           %ѹ����=8/64=87.5%

    % K-L��任
    k11_inverse=k11*coeff';
    k12_inverse=k12*coeff';
    k13_inverse=k13*coeff';
    k=1;
    %  ����ͼ��
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
    figure(1);imshow(image1);title('δѹ��');
    figure(2);imshow(image2);title('ѹ��75%');
    figure(3);imshow(image3);title('ѹ��87.5%');
end
