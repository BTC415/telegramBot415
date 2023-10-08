import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
import string
import json
import os
from datetime import datetime, timedelta


# Initialize the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
# Navigate to the login page
driver.get('https://www.betburger.com/users/sign_in')

# Enter your email/username and password

email_field =driver.find_element(By.NAME, 'betburger_user[email]')
email = 'example@mail.com'
for char in email:
    email_field.send_keys(char)
    time.sleep(0.1)

password_field = driver.find_element(By.NAME,'betburger_user[password]')
password = 'password'

for char in password:
    password_field.send_keys(char)
    time.sleep(0.1)

# Click on the login button
login_button = driver.find_element(By.CSS_SELECTOR,'.submit')
login_button.click()

# Wait for the page to load
time.sleep(60)

driver.get('https://www.betburger.com/arbs')
driver.implicitly_wait(60)

while True:
    #initializing  scroll bar
    number_list = len(driver.find_elements(By.CSS_SELECTOR, '.arbs-list li'))
    try:
        first_li = driver.find_element(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(1)')
        driver.execute_script(f"arguments[0].scrollIntoView();",first_li )
    except:
        continue

    print(f'----------Number of Data :{number_list}----------')

    keys =['percent','sport_name', 'updated_at','bookmarkers','dates','teams','leagues','markets','coefficients']
    time.sleep(1)
    li_list_before_scroll = driver.find_elements(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(n+1):nth-of-type(-n+11)')
    time.sleep(1)
    scrap_data_before_scroll = []
    
    for i,li in enumerate(li_list_before_scroll, start=1):
        if li:
            try:
                percent_data, sport_name_data, updated_data, bookmarker_data, date_data, match_data, league_data, market_data, coefficient_data = ([] for i in range(9))
                data_before_scroll =[]
                # print(f'----------------------------------{i}-----------------------------------------')
                percent = li.find_element(By.CSS_SELECTOR, "span.percent")
                sport_name = li.find_element(By.CSS_SELECTOR, "span.sport-name")
                updated_time = li.find_element(By.CSS_SELECTOR, "span.updated-at")
                bookmarker_names = li.find_elements(By.CSS_SELECTOR, ".bookmaker-name .text-ellipsis")
                dates = li.find_elements(By.CSS_SELECTOR, ".date")
                matches = li.find_elements(By.CSS_SELECTOR, ".name a.text-ellipsis")
                leagues = li.find_elements(By.CSS_SELECTOR, ".league")
                markets = li.find_elements(By.CSS_SELECTOR, ".market a span")
                coefficients = li.find_elements(By.CSS_SELECTOR, "a.coefficient-link") 
                try:
                    percent_text = percent.get_attribute("textContent")
                    
                except:
                    li_list_before_scroll = driver.find_elements(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(n+1):nth-of-type(-n+11)')
                    percent_text = percent.get_attribute("textContent")
                    
                try:
                    updated_time_text = updated_time.get_attribute("textContent")
                    
                except:
                    li_list_before_scroll = driver.find_elements(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(n+1):nth-of-type(-n+11)')
                    updated_time_text = updated_time.get_attribute("textContent")
                

                sport_name_text = sport_name.get_attribute("textContent")

                # print(f'{percent_text} {sport_name_text} {updated_time_text}')
                percent_data.append(percent_text)
                sport_name_data.append(sport_name_text)
                updated_data.append(updated_time_text)

                n=0
                for bookmarker_name in bookmarker_names:
                    bookmarker_name_text = bookmarker_name.get_attribute("textContent") 
                    # print('--------------')
                    # print(f'{bookmarker_name_text}')
                    date = dates[n]
                    date_text = date.get_attribute("textContent")
                    match = matches[n]
                    match_text = match.get_attribute("textContent") 
                    league = leagues[n]
                    league_text = league.get_attribute("textContent")
                    market = markets[n]
                    market_text = market.get_attribute("textContent")
                    try:
                        coefficient = coefficients[n]
                        coefficient_text = coefficient.get_attribute("textContent")
                    except:
                        li_list_before_scroll = driver.find_elements(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(n+1):nth-of-type(-n+11)')
                        coefficient = coefficients[n]
                        coefficient_text = coefficient.get_attribute("textContent")
                    # print(f'{date_text} {match_text} {league_text} {market_text} {coefficient_text}')
                    bookmarker_data.append(bookmarker_name_text)
                    date_data.append(date_text)
                    match_data.append(match_text)
                    league_data.append(league_text)
                    market_data.append(market_text)
                    coefficient_data.append(coefficient_text)
                    
                    n +=1
                data_list = [percent_data, sport_name_data, updated_data, bookmarker_data, date_data, match_data, league_data, market_data, coefficient_data]
                data_before_scroll = dict(zip(keys, data_list))
                clean_data_before = {}
                for key, values in data_before_scroll.items():    
                    clean_values = [value.strip() for value in values]
                    clean_data_before[key] = clean_values

                keys_to_clean = ['percent', 'sport_name', 'updated_at']

                cleaned_data_before = {}
                for key, values in clean_data_before.items():
                    if key in keys_to_clean:
                        cleaned_data_before[key] = values[0]
                    else:
                        cleaned_data_before[key] = values
                # print(cleaned_data_before)
                scrap_data_before_scroll.append(cleaned_data_before)
            except:
                continue
    

    #scroll down to bottom
    if number_list >=12:
        if (number_list ==12):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(12)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass
        elif(number_list ==13):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(13)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass
        elif(number_list ==14):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(14)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass
        elif(number_list ==15):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(15)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass
        elif(number_list ==16):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(16)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass
        elif(number_list ==17):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(17)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass
        elif(number_list ==18):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(18)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass
        elif(number_list ==19):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(19)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass
        elif(number_list ==20):
            try:
                last_li = driver.find_element(By.CSS_SELECTOR,'.arbs-list li:nth-of-type(20)')
                driver.execute_script(f"arguments[0].scrollIntoView();",last_li )
            except:
                pass

        #scrap data after scoll down
        driver.implicitly_wait(1)
        time.sleep(1)

        li_list_after_scroll = driver.find_elements(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(n+12)')
        time.sleep(1)
        scrap_data_after_scroll =[]
        
        for j,li in enumerate(li_list_after_scroll, start=11):
            if li:
                try:
                    percent_data, sport_name_data, updated_data, bookmarker_data, date_data, match_data, league_data, market_data, coefficient_data = ([] for i in range(9))
                    data_after_scroll =[]
                    # print(f'^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^{j}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
                    percent = li.find_element(By.CSS_SELECTOR, "span.percent")
                    sport_name = li.find_element(By.CSS_SELECTOR, "span.sport-name")
                    updated_time = li.find_element(By.CSS_SELECTOR, "span.updated-at")
                    bookmarker_names = li.find_elements(By.CSS_SELECTOR, ".bookmaker-name .text-ellipsis")
                    dates = li.find_elements(By.CSS_SELECTOR, ".date")
                    matches = li.find_elements(By.CSS_SELECTOR, ".name a.text-ellipsis")
                    leagues = li.find_elements(By.CSS_SELECTOR, ".league")
                    markets = li.find_elements(By.CSS_SELECTOR, ".market a span")
                    coefficients = li.find_elements(By.CSS_SELECTOR, "a.coefficient-link") 
                    try:
                        percent_text = percent.get_attribute("textContent")
                        
                    except:
                        li_list_after_scroll = driver.find_elements(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(n+12)')
                        percent_text = percent.get_attribute("textContent")
                        
                    try:
                        updated_time_text = updated_time.get_attribute("textContent")
                        
                    except:
                        li_list_after_scroll = driver.find_elements(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(n+12)')
                        updated_time_text = updated_time.get_attribute("textContent")
                    

                    sport_name_text = sport_name.get_attribute("textContent")

                    # print(f'{percent_text} {sport_name_text} {updated_time_text}')
                    percent_data.append(percent_text)
                    sport_name_data.append(sport_name_text)
                    updated_data.append(updated_time_text)
                    n=0
                    for bookmarker_name in bookmarker_names:
                        bookmarker_name_text = bookmarker_name.get_attribute("textContent") 
                        # print('--------------')
                        # print(f'{bookmarker_name_text}')
                        date = dates[n]
                        date_text = date.get_attribute("textContent")
                        match = matches[n]
                        match_text = match.get_attribute("textContent") 
                        league = leagues[n]
                        league_text = league.get_attribute("textContent")
                        market = markets[n]
                        market_text = market.get_attribute("textContent")
                        try:
                            coefficient = coefficients[n]
                            coefficient_text = coefficient.get_attribute("textContent")
                        except:
                            li_list_after_scroll = driver.find_elements(By.CSS_SELECTOR, '.arbs-list li:nth-of-type(n+12)')
                            coefficient = coefficients[n]
                            coefficient_text = coefficient.get_attribute("textContent")
                        # print(f'{date_text} {match_text} {league_text} {market_text} {coefficient_text}')
                        bookmarker_data.append(bookmarker_name_text)
                        date_data.append(date_text)
                        match_data.append(match_text)
                        league_data.append(league_text)
                        market_data.append(market_text)
                        coefficient_data.append(coefficient_text)
                        n +=1
                    data_list = [percent_data, sport_name_data, updated_data, bookmarker_data, date_data, match_data, league_data, market_data, coefficient_data]
                    data_after_scroll = dict(zip(keys, data_list))
                    clean_data_after = {}
                    for key, values in data_after_scroll.items():    
                        clean_values = [value.strip() for value in values]
                        clean_data_after[key] = clean_values
                    keys_to_clean = ['percent', 'sport_name', 'updated_at']

                    cleaned_data_after = {}
                    for key, values in clean_data_after.items():
                        if key in keys_to_clean:
                            cleaned_data_after[key] = values[0]
                        else:
                            cleaned_data_after[key] = values
                    # print(cleaned_data_after)  
                    
                    scrap_data_after_scroll.append(cleaned_data_after)
                except:
                    continue
    scrap_data =[]
    for before_data in scrap_data_before_scroll:
        scrap_data.append(before_data)
    try:
        for after_data in scrap_data_after_scroll:
            scrap_data.append(after_data)
    except:
        pass
    # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    # print(scrap_data)

    time_threshold = timedelta(seconds=1)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def generate_short_id():
        timestamp = str(int(time.time()))
        random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        short_id = timestamp + random_chars
        return short_id
    def get_exchange_rate():
        base_currency = 'EUR'
        target_currency = 'RON'
        url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        response = requests.get(url)
        data = response.json()
        exchange_rate = data['rates'][target_currency]
        return exchange_rate
    for item in scrap_data:
        item['time_stamp'] = current_time
        item['ID'] = generate_short_id()
        item['rate'] =get_exchange_rate()
    if os.path.exists('db.json'):
        # Read the existing JSON file
        with open('db.json', 'r') as file:
            existing_data = json.load(file)
    else:
        # If the JSON file doesn't exist, initialize with an empty list
        existing_data = []
    filtered_data = [item for item in scrap_data if item]


    for item in filtered_data:
        match_key = (item['sport_name'], item['bookmarkers'], item['teams'], item['markets'])
        matching_item = next((data for data in existing_data if (data['sport_name'], data['bookmarkers'], data['teams'], data['markets']) == match_key), None)
        if matching_item:

            if matching_item['percent'] !=item['percent']:
                with open('bot.json', 'w') as file:
                    json.dump(item, file, indent=2)
                    print("✅ Data found with percentage values changed!")
            else:
                print('❌ No data with percentage values changed!')
            matching_item.update(item)
            
        else:
            existing_data.append(item)
            print('❌ No data with percentage values changed!')
    existing_data = [item for item in existing_data if (datetime.strptime(current_time, "%Y-%m-%d %H:%M:%S") - datetime.strptime(item.get('time_stamp', '1970-01-01'), "%Y-%m-%d %H:%M:%S")) <= time_threshold]
    # Write the updated data to the JSON file
    with open('db.json', 'w') as file:
        json.dump(existing_data, file, indent=2)
    time.sleep(5)
    c = time.time()
    b= 1684518157
    d = b-c
    if d <= 0:
        break
