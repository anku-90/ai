from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

chatbot = ChatBot("My Bot")

bot_trainer = ChatterBotCorpusTrainer(chatbot)
bot_trainer.train("chatterbot.corpus.english")


print("enter 'quit' to stop")
while True:
	user_input = input("You: ")
	if user_input == 'quit':
		break
	print("Bot:",chatbot.get_response(user_input))
	
	
OUTPUT:
(base) student@student:~/Desktop$ python3 chatbot.py
[nltk_data] Downloading package averaged_perceptron_tagger to
[nltk_data]     /home/student/nltk_data...
[nltk_data]   Package averaged_perceptron_tagger is already up-to-
[nltk_data]       date!
[nltk_data] Downloading package punkt to /home/student/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
[nltk_data] Downloading package stopwords to
[nltk_data]     /home/student/nltk_data...
[nltk_data]   Package stopwords is already up-to-date!
Training ai.yml: [####################] 100%
Training botprofile.yml: [####################] 100%
Training computers.yml: [####################] 100%
Training conversations.yml: [####################] 100%
Training emotion.yml: [####################] 100%
Training food.yml: [####################] 100%
Training gossip.yml: [####################] 100%
Training greetings.yml: [####################] 100%
Training health.yml: [####################] 100%
Training history.yml: [####################] 100%
Training humor.yml: [####################] 100%
Training literature.yml: [####################] 100%
Training money.yml: [####################] 100%
Training movies.yml: [####################] 100%
Training politics.yml: [####################] 100%
Training psychology.yml: [####################] 100%
Training science.yml: [####################] 100%
Training sports.yml: [####################] 100%
Training trivia.yml: [####################] 100%
enter 'quit' to stop
You: hi
Bot: How are you doing?
You: worst
Bot: i could always improve myself compared to the pack.
You: ok
Bot: I can't read.
You: why
Bot: Is there a reason that I should?
You: no
Bot: Should I be? Did something happen?
You: 

