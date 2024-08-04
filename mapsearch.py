import streamlit as st
import pandas as pd
#url="https://www.amazon.in/realme-Storage-Dimensity-Chipset-Flagship/dp/B0CW61C6LK/ref=sr_1_1?crid=WGR3JSZYX9LY&dib=eyJ2IjoiMSJ9.7jggu5lRm_n7ZaRlbXOCvl8aLFjAY7FVmbg69t1jIzN4dO8dxzQH43id-7bF8fmTKqOH80LIOJG6hX5sRxkZFq3_VKdiHZIXYCpNVsZAzlIlGYzeG3IrQiPzJ_IhQa00Lkh0oVJuk6M_1PkXa0VrJnpL3IIfQD4CQZlltumLT3gYZ9k-AxH5xfho4IOVuZ5x3IbXFUjvkW_lXC5YG879hpM6YRxkvvL6N8ky3E8Ptfsoq-BWa7jHapI8tHXM_zbqyT9XWQMIPLsBpywV7MoVB9hQTCrkA5Hjzg2biJDsKF4.VpSWbP1WOU18sez5XElhrLqIvHzqE7PvHAUC6tPkNaA&dib_tag=se&keywords=realme%2Bnarzo%2B70%2Bpro%2B5g&qid=1722450369&sprefix=real%2Caps%2C276&sr=8-1&th=1"
#url="https://www.amazon.in/Apple-iPhone-Pro-Max-256/dp/B0CHWV2WYK/ref=sr_1_1_sspa?crid=1ZG6WZQT8CMDS&dib=eyJ2IjoiMSJ9.ISrPaf3T6aI3UGMAazziT-s31dOprK158lFIwPS50LGxb6LxJQqddpKbhcaYu2b5WIavgGzKAeVw2iScClW1767jb9uGlzZGgoQunu1MFtev3qIDKqWHkYGprv7DgWfgwz3meo_14h3Pb4DYUSnYAQAFB_ChAkH3M8mkGlur3DIaFNX8GWhubfguAt6VlA6cDd03T4vETTrOAMc5ptB0waDyvUflalREO6hoFgOO5W6hMMFc8xBUE9iG7-Hbz47PPN-85t9vbUL9cJ1WHIoxiiCPasHLo8vemN9lCJk7TFs.lgs-YlwiLku3KHwMyBv3gwqW_4HIcE-nX9ipm05y6Y0&dib_tag=se&keywords=iphone+15+pro+max&qid=1722793412&sprefix=ipho%2Caps%2C260&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
url=st.text_input("url:")
ok=st.button("ok")
if ok:
    tables = pd.read_html(url)
    st.write(tables[1][1])
    st.write(tables[2])
    st.write(tables[3])
    st.write(tables[4])
    url=""





'''import re
import spacy
"""email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}| \d{10}"
email_text = "Contact us at maheshgodike17@gmail.com. or 8008538015"
email_matches = re.findall(email_pattern, email_text)
print(email_matches)"""

nlp=spacy.load("en_core_web_sm")
with open("news_story.txt","r",encoding="utf-8") as file:
    content=file.read()
sent=nlp(content)
nouns=[]
nums=[]
for i in sent:
    if i.pos_=="NOUN":
        nouns.append(i)
    if i.like_num:
        nums.append(i)
count=sent.count_by(spacy.attrs.POS)
print("nouns:\n",nouns,"\nnumbers:\n",nums,"\ncounts:\n",count)

for k,v in count.items():
    word=sent.vocab[k].text
    print(word,"|",v)

pattern=r"\d*\.\d*% |\d{,2}/\d{,2}/\d{2,}"
match=re.findall(pattern,content)
print(match)'''
