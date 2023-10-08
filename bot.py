import telebot
import json
import time
import os
import requests


bot_token = 'YOUR BOT TOKEN'
bot = telebot.TeleBot(token=bot_token)
print("⭐ Bot script is running.⭐\nPlease enter /senddata to ⚡️ activate ⚡️ the bot in telegram.")
li_number = 0
bookmarkers = []
coefficients = []
rate = []


@bot.message_handler(commands=['senddata'])
def send_data(message):
    print("⚡️ Bot is activated ⚡️")
    while True:
        try:
            # Read the JSON file
            with open('bot.json', 'r') as file:
                json_data = json.load(file)
            
            number_bookmarkers = len(json_data['bookmarkers'])
            global li_number
            li_number = number_bookmarkers
            # Access the data fields
            percent = json_data['percent']
            sport_name = json_data['sport_name']
            updated_at = json_data['updated_at']
            global bookmarkers
            bookmarkers = json_data['bookmarkers']
            dates = json_data['dates']
            teams = json_data['teams']
            leagues = json_data['leagues']
            markets = json_data['markets']
            global coefficients
            coefficients = json_data['coefficients']
            global rate
            rate = json_data['rate']
            os.remove('bot.json')
            if number_bookmarkers ==2:
                                # When Bookmark[0] is set as an input value
                c0= float(coefficients[0])
                c1 =float(coefficients[1])

                if "Superbet" in bookmarkers:
                    if bookmarkers[0] == "Superbet":

                        table_2_1 = [
                        [bookmarkers[0], bookmarkers[1], '💰(€)'],
                        [800, round((800/rate*c0/c1),2), round((800/rate*c0-800/rate-800/rate*c0/c1),2)],
                        [900, round((900/rate*c0/c1),2), round((900/rate*c0-900/rate-900/rate*c0/c1),2)],
                        [1000, round((1000/rate*c0/c1),2), round((1000/rate*c0-1000/rate-1000/rate*c0/c1),2)],
                        [1100, round((1100/rate*c0/c1),2), round((1100/rate*c0-1100/rate-1100/rate*c0/c1),2)],
                        [1250, round((1250/rate*c0/c1),2), round((1250/rate*c0-1250/rate-1250/rate*c0/c1),2)],
                        [1500, round((1500/rate*c0/c1),2), round((1500/rate*c0-1500/rate-1500/rate*c0/c1),2)]
                        ]

                        table_2_2 = [
                        [bookmarkers[0], bookmarkers[1], '💰(€)'],
                        [round((50*rate*c1/c0),2), 50, round((50*c1-50-50*c1/c0),2)],
                        [round((100*rate*c1/c0),2), 100, round((100*c1-100-100*c1/c0),2)],
                        [round((150*rate*c1/c0),2), 150, round((150*c1-150-150*c1/c0),2)],
                        [round((200*rate*c1/c0),2), 200, round((200*c1-200-200*c1/c0),2)],
                        [round((250*rate*c1/c0),2), 250, round((250*c1-250-250*c1/c0),2)],
                        [round((300*rate*c1/c0),2), 300, round((300*c1-300-300*c1/c0),2)]
                        ]

                        data_2_1 = "\n"
                        for row in table_2_1:
                            data_2_1 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                        data_2_1 += ""

                        data_2_2 = ""
                        for row in table_2_2:
                            data_2_2 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                        data_2_2 += ""

                        response = f"💫💫💫 SureBet News( {updated_at} ago ) 💫💫💫\n\n⭐ Percent: {percent}\n\n🎲 Bookmarker -> {bookmarkers[0]}  :  {bookmarkers[1]}\n\n⚽ {sport_name} : {teams[0]}\n\n⏳ Date : {dates[0]}\n\n🏆 League : {leagues[0]}\n\n⚡️ {bookmarkers[0]}  ->  {markets[0]} | {coefficients[0]}\n\n⚡️ {bookmarkers[1]}  ->  {markets[1]} | {coefficients[1]}\n\n{data_2_1}\n\n{data_2_2}"
                        
                        if bookmarkers[1] =="OrbitEx":
                            table_2_1 = [
                            [bookmarkers[0], bookmarkers[1], '💰(€)'],
                            [800, round((800/rate*c0/(c1-0.03)),2), round((800/rate*c0-800/rate-800/rate*c0/(c1-0.03)),2)],
                            [900, round((900/rate*c0/(c1-0.03)),2), round((900/rate*c0-900/rate-900/rate*c0/(c1-0.03)),2)],
                            [1000, round((1000/rate*c0/(c1-0.03)),2), round((1000/rate*c0-1000/rate-1000/rate*c0/(c1-0.03)),2)],
                            [1100, round((1100/rate*c0/(c1-0.03)),2), round((1100/rate*c0-1100/rate-1100/rate*c0/(c1-0.03)),2)],
                            [1250, round((1250/rate*c0/(c1-0.03)),2), round((1250/rate*c0-1250/rate-1250/rate*c0/(c1-0.03)),2)],
                            [1500, round((1500/rate*c0/(c1-0.03)),2), round((1500/rate*c0-1500/rate-1500/rate*c0/(c1-0.03)),2)]
                            ]

                            table_2_2 = [
                            [bookmarkers[0], bookmarkers[1], '💰(€)'],
                            [round((50*rate*(c1-0.03)/c0),2), 50, round((50*(c1-0.03)-50-50*(c1-0.03)/c0),2)],
                            [round((100*rate*(c1-0.03)/c0),2), 100, round((100*(c1-0.03)-100-100*(c1-0.03)/c0),2)],
                            [round((150*rate*(c1-0.03)/c0),2), 150, round((150*(c1-0.03)-150-150*(c1-0.03)/c0),2)],
                            [round((200*rate*(c1-0.03)/c0),2), 200, round((200*(c1-0.03)-200-200*(c1-0.03)/c0),2)],
                            [round((250*rate*(c1-0.03)/c0),2), 250, round((250*(c1-0.03)-250-250*(c1-0.03)/c0),2)],
                            [round((300*rate*(c1-0.03)/c0),2), 300, round((300*(c1-0.03)-300-300*(c1-0.03)/c0),2)]
                            ]

                            data_2_1 = "\n"
                            for row in table_2_1:
                                data_2_1 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                            data_2_1 += ""

                            data_2_2 = ""
                            for row in table_2_2:
                                data_2_2 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                            data_2_2 += ""

                            response = f"💫💫💫 SureBet News( {updated_at} ago ) 💫💫💫\n\n⭐ Percent: {percent}\n\n🎲 Bookmarker -> {bookmarkers[0]}  :  {bookmarkers[1]}\n\n⚽ {sport_name} : {teams[0]}\n\n⏳ Date : {dates[0]}\n\n🏆 League : {leagues[0]}\n\n⚡️ {bookmarkers[0]}  ->  {markets[0]} | {coefficients[0]}\n\n⚡️ {bookmarkers[1]}  ->  {markets[1]} | {coefficients[1]}\n\n{data_2_1}\n\n{data_2_2}"
                            
                    if bookmarkers[1] == "Superbet":
                        table_2_1 = [
                        [bookmarkers[0], bookmarkers[1], '💰(€)'],
                        [round((800/rate*c1/c0),2), 800, round((800/rate*c1-800/rate-800/rate*c1/c0),2)],
                        [round((900/rate*c1/c0),2), 900, round((900/rate*c1-900/rate-900/rate*c1/c0),2)],
                        [round((1000/rate*c1/c0),2), 1000, round((1000/rate*c1-1000/rate-1000/rate*c1/c0),2)],
                        [round((1100/rate*c1/c0),2), 1100, round((1100/rate*c1-1100/rate-1100/rate*c1/c0),2)],
                        [round((1250/rate*c1/c0),2), 1250, round((1250/rate*c1-1250/rate-1250/rate*c1/c0),2)],
                        [round((1500/rate*c1/c0),2), 1500, round((1500/rate*c1-1500/rate-1500/rate*c1/c0),2)]
                        ]

                        table_2_2 = [
                        [bookmarkers[0], bookmarkers[1], '💰(€)'],
                        [50, round((50*rate*c0/c1),2), round((50*c0-50-50*c0/c1),2)],
                        [100, round((100*rate*c0/c1),2), round((100*c0-100-100*c0/c1),2)],
                        [150, round((150*rate*c0/c1),2), round((150*c0-150-150*c0/c1),2)],
                        [200, round((200*rate*c0/c1),2), round((200*c0-200-200*c0/c1),2)],
                        [250, round((250*rate*c0/c1),2), round((250*c0-250-250*c0/c1),2)],
                        [300, round((300*rate*c0/c1),2), round((300*c0-300-300*c0/c1),2)]
                        ]

                    
                        data_2_1 = "\n"
                        for row in table_2_1:
                            data_2_1 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                        data_2_1 += ""

                        data_2_2 = ""
                        for row in table_2_2:
                            data_2_2 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                        data_2_2 += ""

                        response = f"💫💫💫 SureBet News( {updated_at} ago ) 💫💫💫\n\n⭐ Percent: {percent}\n\n🎲 Bookmarker -> {bookmarkers[0]}  :  {bookmarkers[1]}\n\n⚽ {sport_name} : {teams[0]}\n\n⏳ Date : {dates[0]}\n\n🏆 League : {leagues[0]}\n\n⚡️ {bookmarkers[0]}  ->  {markets[0]} | {coefficients[0]}\n\n⚡️ {bookmarkers[1]}  ->  {markets[1]} | {coefficients[1]}\n\n{data_2_1}\n\n{data_2_2}"

                        if bookmarkers[0] =="OrbitEx":
                                table_2_1 = [
                                [bookmarkers[0], bookmarkers[1], '💰(€)'],
                                [round((800/rate*c1/(c0-0.03)),2), 800, round((800/rate*c1-800/rate-800/rate*c1/(c0-0.03)),2)],
                                [round((900/rate*c1/(c0-0.03)),2), 900, round((900/rate*c1-900/rate-900/rate*c1/(c0-0.03)),2)],
                                [round((1000/rate*c1/(c0-0.03)),2), 1000, round((1000/rate*c1-1000/rate-1000/rate*c1/(c0-0.03)),2)],
                                [round((1100/rate*c1/(c0-0.03)),2), 1100, round((1100/rate*c1-1100/rate-1100/rate*c1/(c0-0.03)),2)],
                                [round((1250/rate*c1/(c0-0.03)),2), 1250, round((1250/rate*c1-1250/rate-1250/rate*c1/(c0-0.03)),2)],
                                [round((1500/rate*c1/(c0-0.03)),2), 1500, round((1500/rate*c1-1500/rate-1500/rate*c1/(c0-0.03)),2)]
                                ]

                                table_2_2 = [
                                [bookmarkers[0], bookmarkers[1], '💰(€)'],
                                [50, round((50*rate*(c0-0.03)/c1),2), round((50*(c0-0.03)-50-50*(c0-0.03)/c1),2)],
                                [100, round((100*rate*(c0-0.03)/c1),2), round((100*(c0-0.03)-100-100*(c0-0.03)/c1),2)],
                                [150, round((150*rate*(c0-0.03)/c1),2), round((150*(c0-0.03)-150-150*(c0-0.03)/c1),2)],
                                [200, round((200*rate*(c0-0.03)/c1),2), round((200*(c0-0.03)-200-200*(c0-0.03)/c1),2)],
                                [250, round((250*rate*(c0-0.03)/c1),2), round((250*(c0-0.03)-250-250*(c0-0.03)/c1),2)],
                                [300, round((300*rate*(c0-0.03)/c1),2), round((300*(c0-0.03)-300-300*(c0-0.03)/c1),2)]
                                ]

                            
                                data_2_1 = "\n"
                                for row in table_2_1:
                                    data_2_1 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                                data_2_1 += ""

                                data_2_2 = ""
                                for row in table_2_2:
                                    data_2_2 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                                data_2_2 += ""

                                response = f"💫💫💫 SureBet News( {updated_at} ago ) 💫💫💫\n\n⭐ Percent: {percent}\n\n🎲 Bookmarker -> {bookmarkers[0]}  :  {bookmarkers[1]}\n\n⚽ {sport_name} : {teams[0]}\n\n⏳ Date : {dates[0]}\n\n🏆 League : {leagues[0]}\n\n⚡️ {bookmarkers[0]}  ->  {markets[0]} | {coefficients[0]}\n\n⚡️ {bookmarkers[1]}  ->  {markets[1]} | {coefficients[1]}\n\n{data_2_1}\n\n{data_2_2}"
                else:
                    if bookmarkers[0] == "OrbitEx":
                            table_2_1 = [
                            [bookmarkers[0], bookmarkers[1], '💰(€)'],
                            [50, round((50*(c0-0.03)/c1),2), round((50*(c0-0.03)-50-50*(c0-0.03)/c1),2)],
                            [100, round((100*(c0-0.03)/c1),2), round((100*(c0-0.03)-100-100*(c0-0.03)/c1),2)],
                            [150, round((150*(c0-0.03)/c1),2), round((150*(c0-0.03)-150-150*(c0-0.03)/c1),2)],
                            [200, round((200*(c0-0.03)/c1),2), round((200*(c0-0.03)-200-200*(c0-0.03)/c1),2)],
                            [250, round((250*(c0-0.03)/c1),2), round((250*(c0-0.03)-250-250*(c0-0.03)/c1),2)],
                            [300, round((300*(c0-0.03)/c1),2), round((300*(c0-0.03)-300-300*(c0-0.03)/c1),2)]
                            ]
                            
                            # When Bookmark[1] is set as an input value

                            table_2_2 = [
                            [bookmarkers[0], bookmarkers[1], '💰(€)'],
                            [round((50*c1/(c0-0.03)),2), 50, round((50*c1-50-50*c1/(c0-0.03)),2)],
                            [round((100*c1/(c0-0.03)),2), 100, round((100*c1-100-100*c1/(c0-0.03)),2)],
                            [round((150*c1/(c0-0.03)),2), 150, round((150*c1-150-150*c1/(c0-0.03)),2)],
                            [round((200*c1/(c0-0.03)),2), 200, round((200*c1-200-200*c1/(c0-0.03)),2)],
                            [round((250*c1/(c0-0.03)),2), 250, round((250*c1-250-250*c1/(c0-0.03)),2)],
                            [round((300*c1/(c0-0.03)),2), 300, round((300*c1-300-300*c1/(c0-0.03)),2)]
                            ]

                            data_2_1 = "\n"
                            for row in table_2_1:
                                data_2_1 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                            data_2_1 += ""

                            data_2_2 = ""
                            for row in table_2_2:
                                data_2_2 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                            data_2_2 += ""

                            response = f"💫💫💫 SureBet News( {updated_at} ago ) 💫💫💫\n\n⭐ Percent: {percent}\n\n🎲 Bookmarker -> {bookmarkers[0]}  :  {bookmarkers[1]}\n\n⚽ {sport_name} : {teams[0]}\n\n⏳ Date : {dates[0]}\n\n🏆 League : {leagues[0]}\n\n⚡️ {bookmarkers[0]}  ->  {markets[0]} | {coefficients[0]}\n\n⚡️ {bookmarkers[1]}  ->  {markets[1]} | {coefficients[1]}\n\n{data_2_1}\n\n{data_2_2}"
                
                    elif bookmarkers[1] == "OrbitEx":
                            table_2_1 = [
                            [bookmarkers[0], bookmarkers[1], '💰(€)'],
                            [50, round((50*c0/(c1-0.03)),2), round((50*c0-50-50*c0/(c1-0.03)),2)],
                            [100, round((100*c0/(c1-0.03)),2), round((100*c0-100-100*c0/(c1-0.03)),2)],
                            [150, round((150*c0/(c1-0.03)),2), round((150*c0-150-150*c0/(c1-0.03)),2)],
                            [200, round((200*c0/(c1-0.03)),2), round((200*c0-200-200*c0/(c1-0.03)),2)],
                            [250, round((250*c0/(c1-0.03)),2), round((250*c0-250-250*c0/(c1-0.03)),2)],
                            [300, round((300*c0/(c1-0.03)),2), round((300*c0-300-300*c0/(c1-0.03)),2)]
                            ]
                            
                            # When Bookmark[1] is set as an input value

                            table_2_2 = [
                            [bookmarkers[0], bookmarkers[1], '💰(€)'],
                            [round((50*(c1-0.03)/c0),2), 50, round((50*(c1-0.03)-50-50*(c1-0.03)/c0),2)],
                            [round((100*(c1-0.03)/c0),2), 100, round((100*(c1-0.03)-100-100*(c1-0.03)/c0),2)],
                            [round((150*(c1-0.03)/c0),2), 150, round((150*(c1-0.03)-150-150*(c1-0.03)/c0),2)],
                            [round((200*(c1-0.03)/c0),2), 200, round((200*(c1-0.03)-200-200*(c1-0.03)/c0),2)],
                            [round((250*(c1-0.03)/c0),2), 250, round((250*(c1-0.03)-250-250*(c1-0.03)/c0),2)],
                            [round((300*(c1-0.03)/c0),2), 300, round((300*(c1-0.03)-300-300*(c1-0.03)/c0),2)]
                            ]

                            data_2_1 = "\n"
                            for row in table_2_1:
                                data_2_1 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                            data_2_1 += ""

                            data_2_2 = ""
                            for row in table_2_2:
                                data_2_2 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                            data_2_2 += ""

                            response = f"💫💫💫 SureBet News( {updated_at} ago ) 💫💫💫\n\n⭐ Percent: {percent}\n\n🎲 Bookmarker -> {bookmarkers[0]}  :  {bookmarkers[1]}\n\n⚽ {sport_name} : {teams[0]}\n\n⏳ Date : {dates[0]}\n\n🏆 League : {leagues[0]}\n\n⚡️ {bookmarkers[0]}  ->  {markets[0]} | {coefficients[0]}\n\n⚡️ {bookmarkers[1]}  ->  {markets[1]} | {coefficients[1]}\n\n{data_2_1}\n\n{data_2_2}"
                    
                    else:
                        table_2_1 = [
                        [bookmarkers[0], bookmarkers[1], '💰(€)'],
                        [50, round((50*c0/c1),2), round((50*c0-50-50*c0/c1),2)],
                        [100, round((100*c0/c1),2), round((100*c0-100-100*c0/c1),2)],
                        [150, round((150*c0/c1),2), round((150*c0-150-150*c0/c1),2)],
                        [200, round((200*c0/c1),2), round((200*c0-200-200*c0/c1),2)],
                        [250, round((250*c0/c1),2), round((250*c0-250-250*c0/c1),2)],
                        [300, round((300*c0/c1),2), round((300*c0-300-300*c0/c1),2)]
                        ]
                        
                        # When Bookmark[1] is set as an input value

                        table_2_2 = [
                        [bookmarkers[0], bookmarkers[1], '💰(€)'],
                        [round((50*c1/c0),2), 50, round((50*c1-50-50*c1/c0),2)],
                        [round((100*c1/c0),2), 100, round((100*c1-100-100*c1/c0),2)],
                        [round((150*c1/c0),2), 150, round((150*c1-150-150*c1/c0),2)],
                        [round((200*c1/c0),2), 200, round((200*c1-200-200*c1/c0),2)],
                        [round((250*c1/c0),2), 250, round((250*c1-250-250*c1/c0),2)],
                        [round((300*c1/c0),2), 300, round((300*c1-300-300*c1/c0),2)]
                        ]

                        data_2_1 = "\n"
                        for row in table_2_1:
                            data_2_1 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                        data_2_1 += ""

                        data_2_2 = ""
                        for row in table_2_2:
                            data_2_2 += "| " + " | ".join(str(cell) for cell in row) + " |\n"
                        data_2_2 += ""

                        response = f"💫💫💫 SureBet News( {updated_at} ago ) 💫💫💫\n\n⭐ Percent: {percent}\n\n🎲 Bookmarker -> {bookmarkers[0]}  :  {bookmarkers[1]}\n\n⚽ {sport_name} : {teams[0]}\n\n⏳ Date : {dates[0]}\n\n🏆 League : {leagues[0]}\n\n⚡️ {bookmarkers[0]}  ->  {markets[0]} | {coefficients[0]}\n\n⚡️ {bookmarkers[1]}  ->  {markets[1]} | {coefficients[1]}\n\n{data_2_1}\n\n{data_2_2}"
            # Send the message
            bot.send_message(message.chat.id, response)
            

        except:
            continue


bot.polling()
