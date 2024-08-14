
<br />
<p align="center">
   <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="img/icon.png" alt="Logo">
  </a>
 
  <h1 align="center">Crypto Telegram Bot</h1>

  <p align="center">
    Financial Freedom
</p>

# About

CTB (Crypto Telegram Bot) analyzes cryptocurrency indicators and performs technical analysis using various built-in libraries. If a signal is generated, it shares the information as a draft in the designated Telegram group.

# Installation

* Since our code is written in Python, you need to have Python installed on your computer. You can download it [here](https://www.python.org/downloads/).
* PyCharm EDU was used as the Python IDE. You can download it [here](https://www.jetbrains.com/pycharm-edu/).

Once the necessary programs are installed, it's time to set up the required libraries. You can install these libraries either using PyCharm or via the command line. The installation instructions below will use the command line. Make sure that `pip` is installed on your computer.

* First, let's install the TA-Lib library, which we will use for calculating our technical analysis. Use the command below:

```sh
  pip install TA_Lib-0.4.20-cp38-cp38-win_amd64.whl
  ```
  
* Next, install the `numpy` library:

```sh
  pip install numpy
  ```
  
* For the Telegram bot, install the `pyTelegramBotApi` library:

```sh
  pip install pyTelegramBotApi
  ```
  
* And most importantly, install the `Binance API` to fetch the data:

```sh
  pip install python-binance
  ```
  
With the library installations complete, you're now ready to use the program.
