# Pornhub-Spider
#### A spider to get the videos in pornhub
> 更新日期 2020/4/25  
> 作者 Miscf  
> qq 2831243095  
> 
> 昨晚深夜用appium用到崩溃，所以写写另外的爬虫找找自信  
> 忽然想起一个老哥问过我能不能爬pornhub(不是我自己想看什么，只是为了学习)  
> 能有咱不能爬的东西？  
> 嘿嘿嘿，深夜开干  


## 配置环境
> python3 + 科学上网

* requests库  刚需的东西，必须得有
>pip install requests

* lxml库 解析html文档，用来提取信息
>pip install lxml

## 项目原理
> 经过长时间观察(heihei)，pornhub同一视频下推荐的视频都比较  
> 统一，简单来讲就是你看的视频是美女抠脚，你下面推荐的视频基本  
> 都是美女抠脚  
> 所以程序设计输入起始视频主页，然后不断爬取下面的推荐视频链接  
> 加入爬取列表里(这里我使用了txt用作中转)  
> 然后爬虫程序不断读取下载再获取新的链接  
> 如此而源源不断之  

#### 挑选你喜欢的视频链接，输入程序就ok了，自动爬取类似视频  
#### 视频需要保存在
> F:/ph/
#### 所以需要在F盘新建 ph 文件夹  
#### 当然你也可以在程序里改

## pornhub视频链接的加密
> 一个视频m3u8文件链接 :
> https://d1vh.phncdn.com/hls/videos/202002/08/282888772/,720P_4000K,480P_2000K,240P_400K,_282888772.mp4.urlset/master.m3u8ttl=1587795884&l=0&clientip=47.254.95.205&hash=f02ea34e20bdf70dcf365c45b01e149c
> 有时候也会像另外的，但这都不重要
#### 开始的时候我以为hash=后面跟的是加密值  
#### 看起来挺唬人的，结果屁都不是  
#### 在主页面的js我发现了一串奇奇怪怪的东东
> var quality_720p=/* + ra587796052ra37ra587796052ra37 + */rahttpsdvra45rahttpsdvra45 + /* + ramp4ttl1ra66ramp4ttl1ra66 + */ra1phncdncra64ra1phncdncra64 + /* + ra2549520ra91ra2549520ra91 + */raomvideosra42raomvideosra42 + /* + ra1phncdncra64ra1phncdncra64 + */ra20200208ra71ra20200208ra71 + /* + ra720p1500kra48ra720p1500kra48 + */ra282888772ra63ra282888772ra63 + /* + rars4000cra27rars4000cra27 + */ra720p1500kra48ra720p1500kra48 + /* + ramp4ttl1ra66ramp4ttl1ra66 + */ra282888772ra61ra282888772ra61 + /* + ra5hash213ra10ra5hash213ra10 + */ramp4ttl1ra66ramp4ttl1ra66 + /* + ralientip47ra72ralientip47ra72 + */ra587796052ra37ra587796052ra37 + /* + ra282888772ra63ra282888772ra63 + */rari1024000ra40rari1024000ra40 + /* + ra78926d703cra83ra78926d703cra83 + */rars4000cra27rars4000cra27 + /* + rahttpsdvra45rahttpsdvra45 + */ralientip47ra72ralientip47ra72 + /* + ralientip47ra72ralientip47ra72 + */ra2549520ra91ra2549520ra91 + /* + rafce1b1b37ra78rafce1b1b37ra78 + */ra5hash213ra10ra5hash213ra10 + /* + ramp4ttl1ra66ramp4ttl1ra66 + */ra23b6a0d664ra17ra23b6a0d664ra17 + /* + rars4000cra27rars4000cra27 + */ra78926d703cra83ra78926d703cra83 + /* + ra282888772ra63ra282888772ra63 + */rafce1b1b37ra78rafce1b1b37ra78;



