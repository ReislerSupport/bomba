# Mehmet babanin müzik botları prjosi
# Aynen öyle baba ahaha 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""

Selam , Ben {bn} 🎵

Grubunuzun sesli aramasında müzik çalabilirim. [sancaklar_federasyon](https://t.me/sancaklar_federasyon) tarafından geliştirilmiştir.
Şu anda desteklediğim komutlar şunlardır:
▶️ /oynat - __Yanıtlanan ses dosyasını veya YouTube videosunu bağlantı üzerinden çalar.__
⏸️ /durdur - __Sesli Sohbet Müziğini Duraklat.__
⏩ /devam - __Sesli Sohbet Müziğine Devam Et.__
⏭️ /atla - __Sesli Sohbette Çalan Geçerli Müziği Atlar.__
🛑 /bitir - __Sırayı temizler ve Sesli Sohbet Müziği'ni sona erdirir.__
🔎 /bul - __Müziği bulup gruba gönderir. Örnek /Bul uzi kervan.__
🔀 /arama - __Müziği direk youtubeden arar ve linkler halinde sıralama yapar.__


Beni grubunuza ekleyin ve özgürce müzik çalın !**
         """,
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "Owner 🇹🇷", url="https://t.me/@pumaefe"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/hirasetkanal"
                    )
              ],[ 
                    InlineKeyboardButton(
                        "Sohbet Grup 🇹🇷", url="https://t.me/hirasetsohbet"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**🔴 Müzik çalar yayında**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🚨 Support Kanal 🚨", url="https://t.me/hirasetkanal")
                ]
            ]
        )
   )

