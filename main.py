import random
import telebot
from dotenv import load_dotenv
import os

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(bot_token)

quotes_list = [
    "Keberhasilan tidak datang secara kebetulan. Ini adalah hasil dari kerja keras, ketekunan, belajar, pengorbanan, dan yang terpenting, cinta terhadap apa yang Anda lakukan.",
    "Jangan takut akan kegagalan. Jadikan itu sebagai pelajaran berharga dan kesempatan untuk tumbuh lebih kuat. Keberanian sejati adalah melanjutkan meskipun Anda merasa takut.",
    "Jadikan setiap hari sebagai kesempatan baru untuk meraih impianmu. Jangan biarkan kegagalan atau keraguan merampas semangatmu. Tetaplah berjuang dan percaya pada dirimu sendiri.",
    "Kebahagiaan bukan tujuan akhir, melainkan cara hidup. Nikmatilah perjalananmu, terima tantangan, dan jadikan setiap momen berarti.",
    "Ketika jalan ke depan tampak sulit, jangan berhenti. Hanya orang-orang yang terus berjalanlah yang dapat mencapai tujuan mereka.",
    "Jadikan kesalahan sebagai batu loncatan untuk kesuksesanmu. Kegagalan bukan akhir dari cerita, tetapi bagian dari proses menuju kesuksesan yang lebih besar.",
    "Jangan menunggu kesempurnaan untuk memulai tindakan. Mulailah dengan apa yang Anda miliki, di tempat yang Anda berada, dan lakukan yang terbaik. Kesempurnaan adalah hasil dari tindakan berkelanjutan.",
    "Hidup adalah petualangan yang singkat, jangan sia-siakan waktu dengan mengkhawatirkan hal-hal kecil. Lakukan hal-hal yang penting, kejar impianmu, dan hargai setiap momen yang diberikan.",
    "Ketika Anda merasa putus asa, ingatlah mengapa Anda memulai. Ingatlah impianmu, gairahmu, dan tujuanmu. Tetaplah fokus dan terus maju, karena Anda memiliki potensi untuk mencapai hal-hal yang hebat.",
    "Kesuksesan bukanlah kunci kebahagiaan. Kebahagiaanlah yang merupakan kunci kesuksesan. Jika Anda mencintai apa yang Anda lakukan, Anda akan sukses.",
]

pantun_list = [
    "Kelap kelip di tengah hutan - Ada bintang indah menawan - Walau cinta banyak rintangan - Ku jaga kau dengan kesetiaan",
    "Satu satu ditambah dua - Dua dua dikurang tiga - Aku dan kamu hidup bersama - Sekarang esok dan slamanya",
    "Keliling kota sambil bernyanyi - Tidak lupa makan delima - Saat kau berada di sini - Aku bisa tersenyum lebih lama",
    "Bunga mawar tumbuh di taman - Baunya sedap menyejukkan mata - Jangan ragu untuk berdekatan - Karena aku orangnya setia",
    "Patah dahan disambungkan - Jangan lupa direkatkan - Kepada Tuhan kita mohonkan - Agar cepat disatukan",
    "Ambillah bambu buat sembilu - Terbanglah debu dari cerutu - Nama indahmu ku sebut slalu - Di dalam doa setiap waktu",
    "Langit biru terlihat sendu - Warna ungu berubah semu - Jarak jauh tumbuhkan rindu - Ingin selalu dekat denganmu",
    "Kamar kos bentuknya persegi - Disewa sama tukang roti - Aku ucapkan selamat pagi - Untuk dikau sang pemilik hati",
    "Si buaya darat berkata merdu - Si buaya air hanya membisu - Sungguh berat rasanya rindu - Waktu sehari terasa seminggu",
    "Kucing lucu mandi di atas papan - Papannya dari kayu pohon kelapa - Badan kurus bukan karena kurang makan - Tapi, gara-gara mikirin kamu yang jauh di sana",
]

sad_list = [
    "Bodohnya aku terlena dalam untaian kata indah darimu, hingga akhirnya ku tenggelam dengan kenanganmu",
    "Tahukah kau jika diri ini telah menikmati setiap detik saat kita bersama, karena ku tahu ketika kau pergi, maka semua itu sudah dalam ingatanku",
    "Ada masa ketika kau memberikan isyarat cinta, namun ada juga saat kau memberikan isyarat untuk pergi",
    "Jika kau tanya untuk apa hujan membasahi bumi, maka ia tidak tahu, beda dengan air mata yang tahu untuk siapa ia terjatuh",
    "Teruslah menemukan cinta yang kau inginkan, karena biarpun aku menantimu dalam hujan, engkau tak akan membuka hati yang kuinginkan",
    "Dirimu layaknya bintang sejati, yang terus bersinar di langit malam. Sementara aku hanyalah kerdil yang ingin mati, mengharap cintamu yang tak kunjung datang",
    "Sadarkah kau jika kita sedang di arah yang berbeda, mungkin aku yang berjalan menjauh, atau kamu yang sedang menyimpang?",
    "Untuk apa kau ajari aku cara terbang jika kemudian kau patahkan lagi sayap ini?",
    "Indahnya bulan dan bintang selalu hadir di setiap malam, tidak seperti dirimu yang meninggalkanku dalam kegelapan",
    "Teganya kau ajari aku cara mencintaimu, namun tak pernah kau ajarkan untuk melupakanmu",
]

sindiran_list = [
    "Kebohonganmu lebih panjang daripada daftar belanjaanku",
    "Tidak perlu mengirim undangan, aku tidak tertarik menghadiri pertunjukan dramamu",
    "Kamu pandai memutar balik fakta, mungkin seharusnya kamu mempertimbangkan karier sebagai politisi",
    "Kamu seperti kulkas kosong, tak ada apa pun yang menarik untuk ditemukan di dalamnya",
    "Jangan sia-siakan oksigen yang kamu hirup cuma buat ngurusin hidup orang",
    "Jangan sok menjauh sama seseorang yang belum berhasil, karena saat dia berhasil kamu bukan tipenya lagi",
    "Tahu nggak kalau kamu itu sebastian, sebatas teman tanpa adanya kepastian",
    "Aku mengenali meraka yang tanpa tentara mau berperang melawan diktator dan yang tanpa uang mau memberantas korupsi",
    "Bangsa ini tidak kekurangan orang yang pintar, tetapi kekurangan orang yang jujur",
    "Kampanye untuk negeri, tetapi mencuri untuk diri sendiri",
]

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, f"Welcome {message.from_user.first_name}! Halo, Selamat Datang di Bot Quotes 2023! Silahkan Memilih Menu Yang Tersedia Pada Bot Ini.")

@bot.message_handler(commands=["quotes", "help"])
def quotes(message):
    random_quote = random.choice(quotes_list)
    bot.reply_to(message, f"Quotes untuk {message.from_user.first_name}! {random_quote}")

@bot.message_handler(commands=["pantun", "help"])
def pantun(message):
    random_pantun = random.choice(pantun_list)
    bot.reply_to(message, f"Pantun untuk {message.from_user.first_name}! {random_pantun}")

@bot.message_handler(commands=["sad", "help"])
def sad(message):
    random_sad = random.choice(sad_list)
    bot.reply_to(message, f"Kata Kata Sad untuk {message.from_user.first_name}! {random_sad}")

@bot.message_handler(commands=["sindiran", "help"])
def sindiran(message):
    random_sindiran = random.choice(sindiran_list)
    bot.reply_to(message, f"Kata Kata Sindiran untuk {message.from_user.first_name}! {random_sindiran}")

bot.infinity_polling()
