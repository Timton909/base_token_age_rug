import requests, time

def age_rug_risk():
    print("Base — Age vs Rug Risk (high liq but very young = potential honeypot)")
    while True:
        try:
            r = requests.get("https://api.dexscreener.com/latest/dex/pairs/base")
            for pair in r.json().get("pairs", []):
                age_sec = time.time() - pair.get("pairCreatedAt", 0) / 1000
                liq = pair["liquidity"]["usd"]
                if age_sec < 60 and liq > 100_000:  # <1 min old, >$100k liq
                    token = pair["baseToken"]["symbol"]
                    print(f"HIGH RUG RISK TOKEN\n"
                          f"{token} — ${liq:,.0f} liq in {age_sec:.0f}s\n"
                          f"https://dexscreener.com/base/{pair['pairAddress']}\n"
                          f"→ Too much liq too fast = possible honeypot trap\n"
                          f"{'RISK'*30}")
        except:
            pass
        time.sleep(4.1)

if __name__ == "__main__":
    age_rug_risk()
