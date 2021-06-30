<br />
<p align="center">
   <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="img/icon.png" alt="Logo">
  </a>
 
  <h1 align="center">Crypto Telegram Bot</h1>

  <p align="center">
    Finansal Özgürlük
</p>

# Hakkında

CTB, içerisinde barındırdığı kütüphaneler ile kripto paralara ait göstergeleri inceler ve teknik analizlerini yapar daha sonrasında eğer sinyal oluşuyorsa bunları bir taslak halinde telegram grubunda paylaşır. 

# Kurulum

* Kodlarımızı Python dilinde yazdığımız için için öncelikle bilgisayarımızda Python kurulu olmalıdır. [Şuradan](https://www.python.org/downloads/) indirebilirsiniz.
* Python IDE'si olarak Pycharm EDU kullanıldı. [Şuradan](https://www.jetbrains.com/pycharm-edu/) indilerbilirsiniz.

Gerekli programları kurduktan sonra sıra kullanacağımız kütüphanelerde. İster Pycharm kullanarak istersekte komut istemini kullanarak kütüphanlerimizi kurabilir. Burada komut istemi kullanılarak kurulumlar yapılacaktır.
Kurulumların yapılabilmesi için bilgisayarımızda <b>pip</b> in kurulu olması gereklidir.

* Öncelikle teknik analizlerimizi hesaplarken kullanacağımı TA-Lib kütüphanesini kuralım. Aşağıdaki kodu kullanın.

```sh
  pip install TA_Lib-0.4.20-cp38-cp38-win_amd64.whl
  ```
  
 * Sırada <b>numpy</b> kütüphanemiz var.

```sh
  pip install numpy
  ```
  
 * Telegram botumuz için <b>pyTelegramBotApi</b>

```sh
  pip install pyTelegramBotApi
  ```
  
 * Ve tabi en önemlisi verileri çekeceğimiz <b>Binance Api</b>'si

```sh
  pip install python-binance
  ```
  
 Kütüphne kurulumlarını yaptığımıza göre artık programı kullanmaya hazırsınız. 
