# Telegram-Message-Stats

Script that recieves exported JSON file with messages from a desktop version of Telegram and makes a wordcloud of the most popular words.
NOTE that the opportunity to export messages is only available in a desktop version. Future developments and implementations are to be followed.
Availiable only in Russian. If you like to change the language, you'll have to use the correspondig file with stop-words and NLTK instead of Razdel for tokenization. Actually, when working with text messages, you will see that the main problem is about deleting stop-words properly, so that to make something meaningful.
