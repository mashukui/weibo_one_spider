# weibo_one_spider - Weibo Aggregator Spider

**Author:** [@马哥python说](https://github.com/mashukui)

---
<p align="center">
<a href="README.md">中文版 README</a> | <a href="README.en.md">English README</a>
</p>

## Overview
<img width="2158" height="456" alt="image" src="https://github.com/user-attachments/assets/df4e8033-d111-4a68-9d5c-e29f2be3496c" />


Weibo is one of China's most influential social media platforms, known for its real-time nature and massive KOL (Key Opinion Leader) user base, making it the first choice for opinion outbreaks and information dissemination.

To meet different data collection needs, I previously developed three separate tools:
- **Search Spider**: For collecting posts based on search keywords
- **Creator Spider**: For collecting content from specific creators
- **Comment Spider**: For collecting Weibo comments

While these tools were stable and comprehensive in data collection, some users reported that when their collection needs involved both posts and comments, they had to frequently switch between software, which affected the user experience. To address this scenario, I officially merged these three tools and launched the new **"Weibo Aggregator Spider"**. This software integrates three core functions: keyword search, creator homepage collection, and comment collection, aiming to provide users with a one-stop solution for Weibo data collection.

---

## Usage Scenarios

- **Academic Researchers**: Collect Weibo-related topic data for social sentiment analysis, online propagation research, etc.
- **Marketing Professionals**: Monitor brand keyword search results, competitor creator dynamics, and comment feedback on hot marketing content
- **Content Creators**: Analyze content styles and trending topics from top creators to provide references for your own creation
- **Data Enthusiasts**: Collect Weibo data in areas of interest for personalized data analysis and visualization

---

## Features

### Feature 1: Collect Posts by Keyword

**Software Interface:**
<img width="1440" height="1175" alt="image" src="https://github.com/user-attachments/assets/de6fbe48-5f29-4968-a598-38133942fb8c" />

**Collection Results** (11 fields):
- Keyword, Page Number, Weibo ID, Weibo Link, User Nickname, User Profile Link, Publish Time, Retweet Count, Comment Count, Like Count, Weibo Content
<img width="1440" height="696" alt="image" src="https://github.com/user-attachments/assets/fd3e1d58-3517-4a7d-a372-a702ba5e127d" />

---

### Feature 2: Collect Posts by Creator Profile Link

**Software Interface:**
<img width="1440" height="1175" alt="image" src="https://github.com/user-attachments/assets/19882266-a804-4998-af68-c633e14b05b3" />

**Collection Results** (13 fields):
- Creator Nickname, Creator ID, Page Number, Weibo ID, Weibo Bid, Weibo Link, Publish Time, Publish Platform, Retweet Count, Comment Count, Like Count, Topic Tags, Weibo Content
<img width="1440" height="695" alt="image" src="https://github.com/user-attachments/assets/dc976aeb-1697-424a-a3cb-ffdb61e63750" />

---

### Feature 3: Collect Comments by Post Link

**Software Interface:**
<img width="1440" height="1175" alt="image" src="https://github.com/user-attachments/assets/85dfe19a-f221-4e15-802b-3b1aa125ebfc" />

**Collection Results** (14 fields):
- Weibo Link, Weibo ID, Page Number, Commenter Nickname, Commenter Follower Count, Commenter Following Count, Commenter Profile Link, Commenter Gender, Commenter Bio, Comment Time, Like Count, Comment Content IP Location, Comment Level, Comment Content
<img width="1440" height="694" alt="image" src="https://github.com/user-attachments/assets/0247f3c9-d420-4bfe-a4c5-368f0f6ac21e" />
---

## Important Notes

- Works on both Windows and Mac systems without requiring any programming environment setup
- Contains three core functions: post collection by keyword, post collection by creator homepage, and comment collection, with support for filtering under different conditions
- Uses API protocols for data collection (not RPA simulation), ensuring high stability
- After the software completes, CSV result files are generated in the current folder (the folder where the software is located)
- Data is saved after each page is collected, not all at once at the end. This prevents data loss from unexpected interruptions (1-2 second request interval between pages)
- Detailed log files are recorded during collection for easy troubleshooting

---

## Technology Stack

All modules are developed in Python:

- **tkinter**: GUI interface
- **requests**: HTTP requests for the spider
- **json**: Response data parsing
- **pandas**: CSV data output
- **logging**: Runtime log recording

**Note:** Due to copyright concerns, source code is not publicly available. Only the software itself is provided to users.

---

## Code Examples

### Sending Requests and Parsing Data

```python
# Send request
r = requests.get(url, headers=h1, params=params)
# Parse data
json_data = r.json()
```

### Parsing Response Data (Example: Comment Content)

```python
for data in json_data['data']:
    # Comment content
    text = data['text_raw']
    text_list.append(text)
```

### Saving Data to CSV File

```python
# Save data
df = pd.DataFrame({
    'Weibo Link': weibo_url,
    'Weibo ID': weibo_id,
    'Page Number': page,
    'Commenter Nickname': screen_name_list,
    'Commenter Follower Count': followers_count_list,
    'Commenter Following Count': friends_count_list,
    'Commenter Profile Link': user_home_url_list,
    'Commenter Gender': gender_list,
    'Commenter Bio': desc_list,
    'Comment Time': create_time_list,
    'Like Count': like_counts_list,
    'Comment Content IP Location': source_list,
    'Comment Level': comment_level_list,
    'Comment Content': text_list,
})

# Save CSV file
df.to_csv(self.result_file, mode='a+', index=False, header=header, encoding='utf_8_sig')
self.tk_show('Results saved successfully: {}'.format(self.result_file))
```

### Copyright Footer

```python
# Copyright information
copyright = tk.Label(root, text='@马哥python说 All rights reserved.', font=('SimSun', 10), fg='grey')
copyright.place(x=290, y=625)
```

### Logging Module

```python
def get_logger(self):
    self.logger = logging.getLogger(__name__)
    # Log format
    formatter = '[%(asctime)s-%(filename)s][%(funcName)s-%(lineno)d]--%(message)s'
    # Log level
    self.logger.setLevel(logging.DEBUG)
    # Console log
    sh = logging.StreamHandler()
    log_formatter = logging.Formatter(formatter, datefmt='%Y-%m-%d %H:%M:%S')
    # Info log filename
    info_file_name = time.strftime("%Y-%m-%d") + '.log'
    # Save to specific directory
    case_dir = r'./logs/'
    info_handler = TimedRotatingFileHandler(
        filename=case_dir + info_file_name,
        when='MIDNIGHT',
        interval=1,
        backupCount=7,
        encoding='utf-8'
    )
```

---

## Setup Instructions

1. Before starting, use the built-in **"Cookie Tool"** to automatically configure your cookie<img width="1706" height="1250" alt="image" src="https://github.com/user-attachments/assets/ba2733d8-9075-42d2-803e-2aa3fb20dce3" />

2. After login, select the function module you need (Search Posts / Creator Posts / Comments)
3. Set relevant parameters (keywords, time range, creator link, etc.)
4. Click **"Start Execution"** and wait for collection to complete (you can view progress in real-time)
5. After completion, check the CSV data files or images in the default current folder

**Demo Video:** [Tool Demo](https://mp.weixin.qq.com/s/a5z2hQM66XCMAKomhGeqzw)

---

## Pricing

| Plan | Duration | Price | Purchase Limit | Suitable For |
|------|----------|-------|----------------|--------------|
| Daily Pass | 1 day | ¥39 | One-time | Trial or temporary needs |
| Monthly Pass | 1 month | ¥149 | Multiple | Short-term collection needs |
| Quarterly Pass | 3 months | ¥399 | Multiple | Medium-term collection needs |
| Annual Pass | 1 year | ¥799 | Multiple | Long-term collection needs |

### Purchase Options

**Option 1: Self-Service (Recommended)**
- Link: https://mgnb.pro/product/weibo

**Option 2: Self-Service**
- Link: https://kjyjf.xetlk.com/s/1x4Q4F

**Option 3: Manual Setup**
- After payment, add WeChat (493882434) to connect
<img width="2324" height="604" alt="收款码v5" src="https://github.com/user-attachments/assets/8bf1ac21-3207-4c7b-ac29-937bdcb36398" />

---

## Security & Usage Limits

- To prevent software resale, a **one-device-one-code** mechanism is used. Each code can only run on one computer
- Only one software instance is allowed per computer (multi-instance is not supported)

---

## Author Info

This software is independently developed and maintained by me, with long-term updates and stable operation guaranteed.

**Official Account:** "老男孩的平凡之路"
**Reply "爬微博聚合软件" in the account's backend to get the latest installation package.
<img width="1938" height="364" alt="二维码-公众号放底部v2" src="https://github.com/user-attachments/assets/4ca80801-0ac1-4cc2-924d-10c0a95eaa2e" />

---

## Disclaimer

This tool is for **academic exchange purposes only**. Please strictly comply with relevant laws and regulations, ensure the legality and compliance of platform content, and **prohibit any commercial use**!
