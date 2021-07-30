# REİSLERMUSİC TELEGRAM VC MÜZİK BOT 
[![W2HMusic logo](https://telegra.ph/file/c7b9b1cdcade78b30eeb9.jpg)](https://t.me/ReislerMuzikBot)


-xdays müzik projesinden ve Hamkercat'in telegram ses robotundan esinlenmiştir.
Ne xdays müzik projesi , ne de pytgcalls kararlı değil


<p align="center">
<a href="https://app.codacy.com/gh/W2HGalaxy-Op/W2HMusic?utm_source=github.com&utm_medium=referral&utm_content=W2HGalaxy-Op/W2HMusic&utm_campaign=Badge_Grade_Settings" alt="Codacy Badge">
<img src="https://api.codacy.com/project/badge/Grade/6141417ceaf84545bab6bd671503df51" /> </a>
<a href="https://github.com/W2HGalaxy-Op/W2HMusic" alt="Libraries.io dependency status for GitHub repo"> <img src="https://img.shields.io/librariesio/github/W2HGalaxy-Op/W2HMusic" /> </a>
<a href="http://hits.dwyl.com/W2HGalaxy-Op/W2HMusic" alt="HitCount"> <img src="http://hits.dwyl.com/W2HGalaxy-Op/W2HMusic.svg" /> </a>
</p>
<p align="center">
<a href="https://github.com/ReislerSupport/bomba" alt="GitHub closed issues"> <img src="https://img.shields.io/github/issues-closed-raw/W2HGalaxy-Op/W2HMusic?style=flat&logo=github&color=success" /> </a>
<a href="https://github.com/ReislerSupport/bomba" alt="GitHub commit activity"> <img src="https://img.shields.io/github/commit-activity/m/W2HGalaxy-Op/W2HMusic" /> </a>
<a href="https://github.com/ReislerSupport/bomba/graphs/contributors" alt="GitHub contributors"> <img src="https://img.shields.io/github/contributors/W2HGalaxy-Op/W2HMusic?style=flat&logo=github" /> </a>
<a href="https://github.com/ReislerSupport/bomba/network/members" alt="GitHub forks"> <img src="https://img.shields.io/github/forks/W2HGalaxy-Op/W2HMusic?label=Forks&logo=github" /> </a>
<a href="https://github.com/ReislerSupport/bomba" alt="GitHub closed pull requests"> <img src="https://img.shields.io/github/issues-pr-closed-raw/W2HGalaxy-Op/W2HMusic?color=success" /> </a>
<a href="https://github.com/ReislerSupport/bomba" alt="GitHub issues"> <img src="https://img.shields.io/github/issues-raw/W2HGalaxy-Op/W2HMusic?style=flat&logo=github&color=yellow" /> </a>
</p>
<p align="center">
<a href="https://github.com/ReislerSupport/bomba" alt="GitHub release (latest by date including pre-releases)"> <img src="https://img.shields.io/github/v/release/W2HGalaxy-Op/W2HMusic?include_prereleases?style=flat&logo=github" /> </a>
<a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat&logo=python&color=blue" /> </a>
<a href="https://github.com/ReislerSupport/bomba" alt="Docker!"> <img src="https://aleen42.github.io/badges/src/docker.svg" /> </a>
<a href="https://github.com/ReislerSupport/bomba" alt="GitHub repo size"> <img src="https://img.shields.io/github/repo-size/W2HGalaxy-Op/W2HMusic" /> </a>
<a href="https://github.com/ReislerSupport/bombas/blob/master/LICENSE" alt="GPLv3 license"> <img src="https://img.shields.io/badge/License-GPLv3-blue.svg" /> </a>
</p>
<p align="center">
<a href="https://t.me/ReislerSupport" alt="Telegram!"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>
<a href="https://github.com/ReislerSupport/bomba/graphs/commit-activity" alt="Maintenance"> <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" /> </a>
<a href="https://makeapullrequest.com" alt="PRs Welcome"> <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" /> </a>
</p>


## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/ReislerSupport/bomba)

## Dağıtım 

### Yapılandırma 

'example.env' öğesini '.env' için kopyalayın ve kimlik bilgilerinizle doldurun.

### Docker olmadan

1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

## Bu Botu dağıtmanın en kolay yolu
### HEROKU
<a href="https://heroku.com/deploy?template=https://github.com/ReislerSupport/bomba"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-red?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

### StringSession

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@AdizKaptan/W2HMusicBot) 


### Mandatory Vars.

- Some Of The Mandatory Vars Are :-
   - `API_ID` :  Give API_ID of your Alternate Telegram Account. also get from here [@APIInfoBot](https://t.me/APIinfoBot)
   - `API_HASH` :  Give API_HASH of your Alternate Telegram Account. also get from here [@APIInfoBot](https://t.me/APIinfoBot)
   - `STRING_NAME` :  Make a string session from [here](https://replit.com/@AdizKaptan/W2HMusicBot)
   - `BOT_TOKEN` :  Make a Bot from [@Botfather](https://t.me/botfather) and fill it's bot token.
   - `SUDO_USERS` :  Fill Userid of yhe users whom you want to be able to control the bot. You can add multiple id by giving a space in b/w each id.


### Komut🛠
#### Gruptaki herkes için
- `/play <song name>` - istediğin şarkıyı çal
- `/dplay <song name>` - deezer ile istediğin şarkıyı çal
- `/splay <song name>` - jio saavn ile istediğin şarkıyı çal
- `/playlist` - Şimdi çalma listesini göster
- `/current` - Şimdi çalan göster
- `/bul <song name>` - hızlıca istediğiniz şarkıları indirin
- `/arama <query>` - ayrıntılarla youtube'da video arayın
- `/deezer <song name>` - deezer ile istediğiniz şarkıları hızlıca indirin
- `/saavn <song name>` - saavn ile istediğiniz şarkıları hızlıca indirin
- `/video <song name>` - istediğiniz videoları hızlı bir şekilde indirin


#### Yalnızca yöneticiler
- `/player` - open music player settings panel
- `/pause` - pause song play
- `/Resume` - resume song play
- `/skip` - play next song
- `/end` - stop music play
- `/joinchat` - invite assistant to your chat
- `/sg` - remove assistant from your chat
- `/admincache` - Refresh admin list

- Inline search is also supported.

* Bot Link:  <a href="https://t.me/ReislerMuzikBot" alt="ReislerMuzikBot"> <img src="https://img.shields.io/badge/%F0%9F%A4%96%20-W2HMusic-blue" /> </a>
* News channel: <a  href="https://t.me/SancakAilesi" alt="Sohbet Group"> <img  src="https://img.shields.io/badge/%F0%9F%92%A1-W2HMusic%20Updates-9cf" /> </a>

## Support
- [Channel](https://t.me/ReislerKanal)
- [Group](https://t.me/ReisleeSupport)

## Credits
- [DaisyXMusic](https://github.com/TeamDaisyX/DaisyXMusic)
- [IisGaurav](https://github.com/IisGaurav):DEV
- [hamker cat](https://github.com/thehamkercat/Telegram_VC_Bot)
- [Roj](https://github.com/rojserbest)
- [Marvin](https://github.com/BlackStoneReborn)
- [Laky](https://github.com/Laky-64) & [ADSİZ](https://github.com/ReislerSupport): PyTgCalls

