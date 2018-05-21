import pandas as pd

table_url = "https://space-facts.com/mars/"
mars_facts = pd.read_html(table_url)
mars_facts = mars_facts[0]
mars_facts_dict = {
    mars_facts[0][0]:mars_facts[1][0],
    mars_facts[0][1]:mars_facts[1][1],
    mars_facts[0][2]:mars_facts[1][2],
    mars_facts[0][3]:mars_facts[1][3],
    mars_facts[0][4]:mars_facts[1][4],
    mars_facts[0][5]:mars_facts[1][5],
    mars_facts[0][6]:mars_facts[1][6],
    mars_facts[0][7]:mars_facts[1][7],
    mars_facts[0][8]:mars_facts[1][8]}

print(mars_facts_dict)