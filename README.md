# weibo_one_spider
> 马哥原创：爬微博聚合软件。支持3个功能，含：根据搜索关键词爬帖子、根据主页链接爬帖子、根据帖子爬评论
> 
> 本工具仅限学术交流使用，严格遵循相关法律法规，符合平台内容的合法及合规性，禁止用于任何商业用途！

<p align="center">
<a href="README.md">中文版 README</a> | <a href="README.en.md">English README</a>
</p>

# 一、背景分析与结果展示
## 1.1 开发背景
我是 [@马哥python说](https://github.com/mashukui)，一枚10年+程序猿，现全职独立开发。
<img width="1079" height="228" alt="weibo_slogon" src="https://github.com/user-attachments/assets/1146d83c-e79f-4426-a837-20fdbd7a2bc3" />

微博作为中国最具影响力的社交媒体平台之一，以其实时性和庞大的KOL用户群体，成为舆论爆发和信息传播的首选阵地。之前，为了满足不同的数据需求，我曾分别开发了针对关键词搜索的“[爬微博搜索软件](https://github.com/mashukui/weibo_search_pc_tool)”、针对特定博主的“[爬微博博主软件](https://github.com/mashukui/weibo_user_post_tool)”以及针对微博评论的“[爬微博评论软件](https://github.com/mashukui/weibo_comment_pc_tool)”。

虽然采集性能稳定、数据全面，但也有部分用户反馈，采集需求涵盖帖子和评论，需要频繁地切换软件，影响体验。为了满足这一场景，我正式将这三款软件合并，推出全新的“**爬微博聚合软件**”。该软件集成了关键词搜索、博主主页采集、评论采集三大核心功能，旨在为用户提供一站式的微博数据采集解决方案。

## 1.2 适用人群与场景
该软件适用于：
- **学术研究者**：采集微博相关话题数据，用于社会舆情分析、网络传播研究等；
- **市场从业者**：监测品牌关键词搜索结果、竞品博主动态、热门营销内容的评论反馈；
- **内容创作者**：分析优质博主的内容风格、热门话题趋势，为自身创作提供参考；
- **数据爱好者**：收集感兴趣领域的微博数据，进行个性化数据分析与可视化。

## 1.3 结果展示
功能1，根据关键词采集帖子

软件界面1：
![界面1：微博搜索帖子](https://files.mdnice.com/user/32110/b3733f08-bc3c-45c9-816a-a6c4e31bd5f4.jpg)
 
采集结果1：（含11个字段：关键词,页码,微博id,微博链接,用户昵称,用户主页链接,发布时间,转发数,评论数,点赞数,微博内容）
![结果1：微博搜索帖子](https://files.mdnice.com/user/32110/82fb0f17-ff01-4575-b8eb-d9544698b2db.png)

 
功能2，根据主页链接采集帖子

软件界面2：
![界面2：根据主页采集帖子](https://files.mdnice.com/user/32110/129dcbc2-2e5c-4c18-9781-6d89504e77e5.jpg)
 
采集结果2：（含13个字段：博主昵称,博主id,页码,微博id,微博bid,微博链接,发布时间,发布于,转发数,评论数,点赞数,话题标签,微博内容）
![结果2：根据主页采集帖子](https://files.mdnice.com/user/32110/2bc591c3-1d37-4bb6-92f4-708c9f592d95.png)

 
功能3，根据帖子链接采集评论

软件界面3：
![界面3：根据帖子采集评论](https://files.mdnice.com/user/32110/6de6ec3c-4a5f-4e77-8bb9-d36b84158888.jpg)

 
采集结果3：（含14个字段：微博链接,微博id,页码,评论者昵称,评论者粉丝数,评论者关注数,评论者主页链接,评论者性别,评论者签名,评论时间,点赞数,评论内容IP属地,评论级别,评论内容）
![结果3：根据帖子采集评论](https://files.mdnice.com/user/32110/9bafd8c5-06d0-40cb-9b89-d1e4cbeb0220.png)

 
## 1.4 软件说明
几点说明，请详读：

1. Windows系统、Mac系统均可直接运行，无需配置编程环境
2. 软件含三个核心功能：搜索帖子、主页帖子、评论的采集，并支持不同条件的筛选
3. 软件通过接口协议采集，并非通过模拟浏览器等RPA类，稳定性较高
4. 软件运行完成后，会在当前文件夹（即，软件所在文件夹）生成csv结果文件
5. 爬取过程中，每爬一页，存一次csv。并非爬完最后一次性保存！防止因异常中断导致丢失前面的数据（每页请求间隔1~2s）
6. 爬取过程中，有log文件详细记录运行过程，方便回溯

# 二、主要技术
## 2.1 模块分工
软件全部模块采用python语言开发，主要分工如下:
```python
tkinter：GUI软件界面
requests：爬虫发送请求
json：解析返回的响应数据
pandas：保存csv数据结果
logging：运行过程中日志记录
```
出于版权考虑，暂不公开源码，仅向用户提供软件使用。 

## 2.2 部分代码
部分代码实现： 

发送请求并解析数据：
```python
# 发送请求
r = requests.get(url, headers=h1, params=params)
# 解析数据
json_data = r.json()
```
解析响应数据，以“评论内容”字段为例：
```python
for data in json_data['data']:
	# 评论内容
	text = data['text_raw']
	text_list.append(text)
```
保存结果数据到csv文件：
```python
# 保存数据
df = pd.DataFrame(
	{
		'微博链接': weibo_url,
		'微博id': weibo_id,
		'页码': page,
		'评论者昵称': screen_name_list,
		'评论者粉丝数': followers_count_list,
		'评论者关注数': friends_count_list,
		'评论者主页链接': user_home_url_list,
		'评论者性别': gender_list,
		'评论者签名': desc_list,
		'评论时间': create_time_list,
		'点赞数': like_counts_list,
		'评论内容IP属地': source_list,
		'评论级别': comment_level_list,
		'评论内容': text_list,
	}
)
# 保存csv文件
df.to_csv(self.result_file, mode='a+', index=False, header=header, encoding='utf_8_sig')
self.tk_show('结果保存成功:{}'.format(self.result_file))
```
底部版权声明：
```python
# 版权信息
copyright = tk.Label(root, text='@马哥python说 All rights reserved.', font=('仿宋', 10), fg='grey')
copyright.place(x=290, y=625)
```
日志记录模块：
```python
def get_logger(self):
    self.logger = logging.getLogger(__name__)
    # 日志格式
    formatter = '[%(asctime)s-%(filename)s][%(funcName)s-%(lineno)d]--%(message)s'
    # 日志级别
    self.logger.setLevel(logging.DEBUG)
    # 控制台日志
    sh = logging.StreamHandler()
    log_formatter = logging.Formatter(formatter, datefmt='%Y-%m-%d %H:%M:%S')
    # info日志文件名
    info_file_name = time.strftime("%Y-%m-%d") + '.log'
    # 将其保存到特定目录
    case_dir = r'./logs/'
    info_handler = TimedRotatingFileHandler(filename=case_dir + info_file_name,
                                        when='MIDNIGHT',
                                        interval=1,
                                        backupCount=7,
                                        encoding='utf-8')
```
# 三、功能与使用
## 3.1 一键配置cookie
开始采集前，先用内置的《cookie小工具》自动配置好cookie。
![4bffc01d81a41633019f25f9ec6c27d0](https://github.com/user-attachments/assets/079b6231-a6ca-4d0e-80ce-3dc62377e967)

这样，获取到的cookie值就自动写入cookie.txt文件中了，告别繁琐的手动获取。
## 3.2 软件登录
用户登录界面：需要登录。
## 3.3 启动采集
1. 登录成功之后，选择需要的功能模块（搜索帖子/博主帖子/评论）；
2. 设置相关参数（如关键词、时间范围、博主链接等）；
3. 点击「开始执行」，等待采集完成（可实时查看采集进度）；
4. 采集完成后，在默认的当前文件夹中查看csv数据文件或图片等。

## 3.4 演示视频
软件使用的完整过程演示：[【工具演示】爬微博聚合软件](https://mp.weixin.qq.com/s/a5z2hQM66XCMAKomhGeqzw)

# 四、付费说明
## 4.1 卡密说明
付费如下：
```python
日卡：使用期限1天，39元。日卡仅能购买一次。适合试用等临时需求
月卡：使用期限1个月，149元。月卡可多次购买。适合短期采集需求
季卡：使用期限3个月，399元。季卡可多次购买。适合中期采集需求
年卡：使用期限1年，799元。年卡可多次购买。适合长期采集需求
```
**方式一：自助开通（推荐）**

开通入口：https://mgnb.pro/product/weibo

**方式二：自助开通**

开通入口：https://kjyjf.xetlk.com/s/1x4Q4F

**方式三：手动开通，付费后加v（493882434）对接**
<img width="2324" height="604" alt="收款码v5" src="https://github.com/user-attachments/assets/5e92edbd-625c-41dd-bcdc-78600eb5c535" />

## 4.2 一机一码
为防止软件被恶意转卖，采用一机一码机制，一个卡密只能在一台电脑运行、不可多电脑运行。
## 4.3 软件多开
一台电脑仅允许运行一个软件，不支持软件多开。

## 4.4 软件维护
软件由本人独立原创开发，长期维护更新，提供稳定运行。

# 五、软件获取
公众号"**老男孩的平凡之路**"，后台回复"**爬微博聚合软件**"获取最新版软件安装包。<img width="1938" height="364" alt="二维码-公众号放底部v2" src="https://github.com/user-attachments/assets/a6f577f4-4d20-4757-8369-befa01e69f1d" />
