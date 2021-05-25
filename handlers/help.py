from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""❤ Komutlar ve orada kullanımı burada açıklanmıştır ❤
**Gruptaki herkes için**
- `/oynat <şarkı adı>` - istediğin şarkıyı çal
- `/doynat <şarkı adı>` -deezer ile istediğin şarkıyı çal
- `/soynat <şarkı adı>` - jio saavn ile istediğin şarkıyı çal
- `/oynatmalistesi` - Şimdi çalma listesini göster
- `/current` - Şimdi çalan göster
- `/song <şarkı adı>` - hızlıca istediğiniz şarkıları indirin
- `/arama <query>` - ayrıntılarla youtube'da video arayın
- `/deezer <şarkı adı>` - deezer ile istediğiniz şarkıları hızlıca indirin
- `/saavn <şarkı adı>` - saavn ile istediğiniz şarkıları hızlıca indirin
- `/video <şarkı adı>` - istediğiniz videoları hızlı bir şekilde indirin

**Yalnızca yöneticiler**
- `/player` - müzik çalar ayarları panelini aç
- `/durdur` - şarkı çalmayı duraklat
- `/devam` - şarkı çalmaya devam et
- `/atla` - sonraki şarkıyı çal
- `/bitir` - müzik çalmayı durdur
- `/katil` - asistanı sohbetinize davet edin
- `/ayril` - asistanı sohbetinizden çıkarın
- `/admincache` - Yönetici listesini yenile""")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""❤ Komutlar ve orada kullanımı burada açıklanmıştır ❤
**Gruptaki herkes için**
- `/oynat <şarkı adı>` - istediğin şarkıyı çal
- `/doynat <şarkı adı>` - deezer ile istediğin şarkıyı çal
- `/soynat <şarkı adı>` -jio saavn ile istediğin şarkıyı çal
- `/oynatmalistesi` - Şimdi çalma listesini göster
- `/cparca` - Şimdi çalan göster
- `/bul <şarkı adı>` - hızlıca istediğiniz şarkıları indirin
- `/arama <query>` - ayrıntılarla youtube'da video arayın
- `/deezer <şarkı adı>` - deezer ile istediğiniz şarkıları hızlıca indirin
- `/saavn <şarkı adı>` - saavn ile istediğiniz şarkıları hızlıca indirin
- `/video <şarkı adı>` - istediğiniz videoları hızlı bir şekilde indirin

**Admins only**
- `/player` - müzik çalar ayarları panelini aç
- `/durdur` - şarkı çalmayı duraklat
- `/devam` - şarkı çalmaya devam et
- `/atla` - sonraki şarkıyı çal
- `/bitir` - müzik çalmayı durdur
- `/katil` - asistanı sohbetinize davet edin
- `/ayril` - asistanı sohbetinizden çıkarın
- `/admincache` - Yönetici listesini yenile""") 
