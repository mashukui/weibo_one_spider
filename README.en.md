# weibo_one_spider

> 🔥 Weibo data collection tool / Weibo crawler GUI, supporting keyword Weibo post collection, profile post collection, comment collection, user profile collection, and CSV export.
>
> 💡 Supports Windows/macOS with no Python environment required. This repository is used for software introduction, release distribution, usage documentation, and issue feedback. The complete source code is not publicly available.
>
> [⬇️Download Latest Release](https://github.com/mashukui/weibo_one_spider/releases/) | [🎬Video Demo](https://www.bilibili.com/video/BV1ayvYBNEFb/) | [🏠Homepage](https://mashukui.github.io/weibo_one_spider/) | [💳Purchase Access](https://mgnb.pro/product/weibo)

<p align="center">
  <a href="README.md">简体中文 README</a> | <a href="README.en.md">English README</a>
</p>

## 👋 Overview

`weibo_one_spider` is a desktop GUI tool designed for Weibo data collection scenarios. It combines keyword Weibo post collection, creator profile post collection, post comment collection, and user profile collection into one client. Users do not need to install or configure a Python environment. Download the client, log in, and start using it.

It is suitable for the following scenarios:

| Scenario | Description |
| --- | --- |
| ✅ Academic research | Collect Weibo topics, posts, comments, and user profiles for communication, sociology, journalism, and related research |
| ✅ Public opinion analysis | Track hot events and public issues, and analyze discussion trends, sentiment shifts, and propagation paths |
| ✅ Text mining | Export Weibo post text and comments for keyword extraction, topic modeling, sentiment analysis, and related tasks |
| ✅ Market monitoring | Monitor brand keywords, competitor creator updates, and comment feedback under popular content |

## ⚙️ Features

| Feature | Description | Output |
| --- | --- | --- |
| ✅ Keyword Weibo post collection | Search Weibo posts by keyword and collect basic post data | CSV |
| ✅ Profile Weibo post collection | Collect Weibo post lists from creator profile links | CSV |
| ✅ Comment collection | Collect comment data from Weibo post links | CSV |
| ✅ User profile collection | Collect user profile, verification, follower, and interaction fields | CSV |
| ✅ Incremental saving | Save data to CSV after each page to reduce data loss caused by interruptions | CSV |
| ✅ Runtime logs | Record runtime logs for troubleshooting | logs files |

## 🚀 Quick Start

1. Open [Releases](https://github.com/mashukui/weibo_one_spider/releases/) and download the latest version.
2. Extract the package and run the client for your operating system.
3. Use the built-in cookie helper to configure your cookie.
4. Log in to the software account.
5. Select a collection module and enter a keyword, Weibo post link, or creator profile link.
6. Click "Start" and wait for the collection task to finish.
7. Check the CSV files and log files in the software directory.

## 💻 Supported Platforms

| Platform | Support |
| --- | --- |
| Windows | Supported. Download and run the Windows client |
| macOS | Supported. Download and run the macOS client |

## 🖼️ Screenshots

### Keyword Weibo Post Collection

Keyword Weibo post collection interface:

![Interface 1: Weibo keyword post search](https://files.mdnice.com/user/32110/b3733f08-bc3c-45c9-816a-a6c4e31bd5f4.jpg)

Keyword Weibo post collection result:

![Result 1: Weibo keyword posts](https://files.mdnice.com/user/32110/82fb0f17-ff01-4575-b8eb-d9544698b2db.png)

### Profile Weibo Post Collection

Profile Weibo post collection interface:

![Interface 2: Profile post collection](https://files.mdnice.com/user/32110/129dcbc2-2e5c-4c18-9781-6d89504e77e5.jpg)

Profile Weibo post collection result:

![Result 2: Profile posts](https://files.mdnice.com/user/32110/2bc591c3-1d37-4bb6-92f4-708c9f592d95.png)

### Comment Collection

Comment collection interface:

![Interface 3: Comment collection from post](https://files.mdnice.com/user/32110/6de6ec3c-4a5f-4e77-8bb9-d36b84158888.jpg)

Comment collection result:

![Result 3: Post comments](https://files.mdnice.com/user/32110/9bafd8c5-06d0-40cb-9b89-d1e4cbeb0220.png)

### User Profile Collection

User profile collection interface:

![Interface 4: User profile collection](https://files.mdnice.com/user/32110/d9925556-0d44-4024-adba-b63b832cc9ab.jpg)

User profile data 1/2:

![v2.0 data 1](https://files.mdnice.com/user/32110/3cda495c-36aa-49b5-835f-83c4c8ebac8b.png)

User profile data 2/2:

![v2.0 data 2](https://files.mdnice.com/user/32110/94e2d80b-8598-414d-b18a-d3b8499409f0.png)

## 📊 Output Fields

The software generates different CSV files based on the selected collection module. Since there are many fields, the main field groups are shown first. You can expand the sections below to view the full field lists.

### Keyword Weibo Post Data

- Collection info: keyword, page
- Weibo post info: Weibo id, Weibo link, published time, Weibo content
- User info: user nickname, user profile link
- Interaction data: reposts, comments, likes

<details>
<summary>View full keyword Weibo post fields</summary>

Keyword, page, Weibo id, Weibo link, user nickname, user profile link, published time, reposts, comments, likes, Weibo content

</details>

### Profile Weibo Post Data

- Collection info: page
- Creator info: creator nickname, creator id
- Weibo post info: Weibo id, Weibo bid, Weibo link, published time, source, topic tags, Weibo content
- Interaction data: reposts, comments, likes

<details>
<summary>View full profile Weibo post fields</summary>

Creator nickname, creator id, page, Weibo id, Weibo bid, Weibo link, published time, source, reposts, comments, likes, topic tags, Weibo content

</details>

### Comment Data

- Collection info: Weibo link, Weibo id, page
- Commenter info: commenter nickname, commenter followers, commenter following, commenter profile link, commenter gender, commenter bio
- Comment info: comment time, likes, comment IP location, comment level, comment content

<details>
<summary>View full comment fields</summary>

Weibo link, Weibo id, page, commenter nickname, commenter followers, commenter following, commenter profile link, commenter gender, commenter bio, comment time, likes, comment IP location, comment level, comment content

</details>

### User Profile Data

- Basic info: user profile link, uid, nickname, gender, IP location, location
- Verification info: verification type, verification information, Sunshine Credit, Zhima Credit, real-name status
- Account info: short description, profile bio, membership level, custom domain, Weibo ID, user tags, avatar URL
- Statistics: followers, following, Weibo count, total reposts, total comments, total likes, total interactions
- Other info: top user status, celebrity flag, birthday, registration time

<details>
<summary>View full user profile fields</summary>

User profile link, uid, nickname, gender, IP location, location, verification type, verification information, short description, profile bio, followers, following, Weibo count, total reposts, total comments, total likes, total interactions, Sunshine Credit, Zhima Credit, membership level, real-name status, custom domain, Weibo ID, user tags, top user status, celebrity flag, avatar URL, birthday, registration time

</details>

## 🛠️ Technical Notes

The software is developed in Python. Core modules include:

| Module | Purpose |
| --- | --- |
| tkinter | GUI interface |
| requests | API requests |
| json | Response parsing |
| pandas | CSV export |
| logging | Runtime logging |

The software collects data through interface requests and does not rely on browser automation or RPA-style operations. During collection, results are saved by page by default. The request interval is usually about 1-2 seconds, which helps control the collection pace and reduce data loss caused by unexpected interruptions.

## 💰 Pricing

| Plan | Duration | Price | Recommended Usage |
| --- | --- | --- | --- |
| Day pass | 1 day | 9.9 CNY | Trial use or small one-time tasks |
| Monthly pass | 1 month | 149 CNY | Short-term collection needs |
| Quarterly pass | 3 months | 399 CNY | Medium-term collection needs |
| Yearly pass | 1 year | 799 CNY | Long-term stable use |

Purchase page: [https://mgnb.pro/product/weibo](https://mgnb.pro/product/weibo)

## 🔐 License and Activation Rules

- The software uses a one-device-one-license mechanism. One license key can only be used on one computer.
- Only one software instance is allowed on a single computer. Multiple concurrent instances are not supported.
- The software is maintained by the author, and future versions will be published through GitHub Releases.

## ❓ FAQ

### Do I need to install Python?

No. The software is packaged as a desktop client. Download the version for your operating system and run it directly.

### What is the cookie used for?

The cookie allows the software to access platform data under your current account session. Please use your own account cookie and keep related files secure.

### Will collected data be lost if the task is interrupted?

The software saves CSV files by page instead of waiting until the whole task is complete. If the task is interrupted, data from completed pages is usually still preserved in the result files.

### Where are result files saved?

By default, result files are saved in the software directory. CSV files and log files are generated by feature module.

### How much data can it collect?

The actual amount of data depends on the keyword, account status, platform API response, network environment, and collection frequency. It is recommended to set a reasonable collection range and request interval.

### What should I do if an error occurs?

Check the log files under the `logs` directory first. When reporting an issue, please provide:

- Software version
- Operating system
- Feature module used
- Keyword, creator profile link, or Weibo post link entered
- Error screenshot
- Log content around the time when the error occurred

## ⚠️ Compliance Statement

This software is intended only for lawful data analysis, learning, research, and authorized business scenarios. Users are responsible for complying with the target platform's terms of service, privacy policy, and applicable laws and regulations.

Do not use this software for:

- High-frequency, malicious, or destructive requests
- Unauthorized collection, distribution, or sale of sensitive personal information
- Activities that infringe the lawful rights of platforms, creators, or users
- Any other behavior that violates laws, regulations, or platform rules

Users are solely responsible for risks and liabilities caused by improper use.

## 📦 Get the Software

- GitHub Releases: [https://github.com/mashukui/weibo_one_spider/releases/](https://github.com/mashukui/weibo_one_spider/releases/)
- WeChat official account: `老男孩的平凡之路`
- Reply in the WeChat official account: `微博`

<img width="573" height="196" alt="二维码-公众号放底部v4" src="https://github.com/user-attachments/assets/4c616078-69d0-49ba-9322-4d8aba56d425" />
