import nltk
from nltk.chat.util import Chat, reflections

reflections = {"i am": "you are",
               "i was": "you were",
               "i": "you",
               "i'm ": "you are",
               "i'd": "you would",
               "i've": "you have",
               "i'll": 'you will',
               "my": "your",
               "you are": "I am",
               "you were": "I was",
               "you have": "I have",
               "you will": "I will",
               "your": "my",
               "yours": "mine",
               "me": "you",
               "you": 'me'}
bot_name = "MyBot"
pairs = [
    [r"my name is (.*)",
     ["Hello %1, How are you today ?", "Hello %1, How do you do?", "Hello %1, How are you doing ?", ]],
    [r"I'm (.*)|I am (.*)|i am (.*)|i'm (.*)|I am(.*)|IAM (.*)",
     ["Hello %1, How are you today ?", "Hello %1, How do you do?", "Hello %1, How are you doing ?", ]],
    [r"(.*), how are you?|are you okay?|okay?|ok?|are you alright?", ["I'm Fine", ]],
    [r"hi|hey|hello|Is anyone there?|Good day",
     ["Hello", "Hey there", "Hey :-)", "Hi there, what can I do for you?", "Hi there, how can I help?", ]],
    [r"what is your name ?", ["I am a bot. you can call me crazy!", ]],
    [r"how are you ?", ["I'm doing good How about You ?", ]],
    [r"sorry (.*)|it's my fault", ["Its alright", "Its OK, never mind", ]],
    [r"I am fine|very good|(.*) great|(.*) very well|everything is good|good|fine|great|all good|doing well",
     ["Great to hear that, How can I help you?", ]],
[r"i'm (.*) doing good", ["Nice to hear that", "How can I help you?:)", ]],
    [r"(.*) age?", ["I'm a computer program dude Seriously you are asking me this?", ]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse", ]],
    [r"(.*) created ?", ["Sara created me using Python's NLTK library ", "top secret ;)", ]],
    [r"(.*) (location|city) ?", ['Indore, Madhya Pradesh', ]],
    [r"how is weather in (.*)?",
     ["Weather in %1 is awesome like always", "Too hot man here in %1", "Too cold man here in %1",
      "Never even heard about %1"]],
    [r"i work in (.*)?", ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.", ]],
    [r"(.*)raining in (.*)", ["No rain since last week here in %2", "Damn its raining too much here in %2"]],
    [r"how (.*) health(.*)", ["I'm a computer program, so I'm always healthy ", ]],
    [r"How long does delivery take?|How long does shipping take?|When do I get my delivery?",
     ["Delivery takes 2-4 days", "Shipping takes 2-4 days",
      ]],
    [r"Do you take credit cards?|Do you accept Mastercard?|Can I pay with Paypal?|Are you cash only?", [
        "We accept VISA, Mastercard and Paypal","We accept most major credit cards, and Paypal",
    ]],
   [r"I want (.*)|give me (.*)", [
        "What Size You want?",
    ]],
   [r"Do you have any baked goods?", [
        "We have the following baked items:Chocolate donut, cookie and croissant",
    ]],
  [r"can i have (.*)", [
        "Yes, sure",
    ]],
[r"Large|small|medium", [
        "your order have been placed,Do you need any thing else?",
    ]],
    [r"Which items do you have?|What kinds of items are there?|What do you sell?|what kind of drinks do you offer",
        [
            "we have the following hot drinks: Black Coffe,Cappucino,and mocha.we have the following cold drinks:Iced Coffe",
        ]
    ],
    [r"quit|q|Q|Bye",
     ["Bye take care. See you soon :) ", "It was nice talking to you. See you soon :)", "Have a nice day", ]],
    [r"Thanks|Thank you|That's helpful|thank's a lot!|No, thanks|No, thank you", ["Happy to help!", "Any time!", "My pleasure", ]],
    [r"tell me something funny|Do you know a joke?|Tell me a joke!",
     ["Why did the hipster burn his mouth? He drank the coffee before it was cool.",
      "What did the buffalo say when his son left for college? Bison."]],

]

def chat(message):
    chat = Chat(pairs, reflections)
    return chat.respond(message)


# initiate the conversation
if __name__ == "__main__":
    chat()
