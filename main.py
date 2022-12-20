from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

header ={
    "Accept-Language":"en-US,en;q=0.9,hi;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}

account_sid = "AC2e20a369d5e3da6c80a498db4aacb245"
auth_token = "f052eff30cd84a05af4338a5f8fc910c"
client = Client(account_sid,auth_token)

def get_url():
    url = "https://www.amazon.in/gp/product/B09VPV28W3/ref=s9_acss_bw_cg_mstls_2a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-5&pf_rd_r=SP6NN4HDPXPG63RDP9EX&pf_rd_t=101&pf_rd_p=75ab1a7a-0478-464e-b175-9f2be362b034&pf_rd_i=28207169031"
    content = requests.get(url=url,headers=header).text
    soup = BeautifulSoup(content,"html.parser")
    price,value= ((soup.find("span",class_="a-price-whole").text.replace(",","").split(".")))
    int_price = int(price)
    if int_price <35000:
        message = client.messages.create(
            body="your probuct price leass than 35000",
            from_="+18045384041",
            to="+919712549013"
        )
        return message.sid

def main():
    print(get_url())

if __name__ == ("__main__"):
    main()


