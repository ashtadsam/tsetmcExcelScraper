# Scrap StockMarket Price

You can easily run this and get latest or specific day price from `http://www.tsetmc.com/` website! The `.xlsx` file will automatically save on your PC!

### ENV

In order to run this program you need :

1. Download GeckoDriver (Firefox).
2. Set GeckoDriver in your environment variable.
3. Create a .env file in root directory
4. Specify `DIR` variable in .env (It a path in your computer to save downloaded data there...)


## Run
```bash
> pip3 install virtualenv
> virtualenv env
> source env/bin/activate
> (env) pip3 install -r requirements.txt
> (env) python3 src/main.py
```