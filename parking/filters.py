from better_profanity import profanity

def initialize_profanity_filter():
    profanity.load_censor_words()

def filter_profanity(text):
    return profanity.censor(text)

custom_foul_words = ["amputa","animal ka","bilat","binibrocha","bobo","bogo","boto","brocha","burat","bwesit","bwisit","demonyo ka","engot","etits","gaga","gagi","gago","habal","hayop ka","hayup","hinampak","hinayupak","hindot","hindutan","hudas","iniyot","inutel","inutil","iyot","kagaguhan","kagang","kantot","kantotan","kantut","kantutan","kaululan","kayat","kiki","kikinginamo","kingina","kupal","leche","leching","lechugas","lintik","nakakaburat","nimal","ogag","olok","pakingshet","pakshet","pakyu","pesteng yawa","poke","poki","pokpok","poyet","pu'keng","pucha","puchanggala","puchangina","puke","puki","pukinangina","puking","punyeta","puta","putang","putang ina","putangina","putanginamo","putaragis","putragis","puyet","ratbu","shunga","sira ulo","siraulo","suso","susu","tae","taena","tamod","tanga","tangina","taragis","tarantado","tete","teti","timang","tinil","tite","titi","tungaw","ulol","ulul","ungas"]

def add_custom_censor_words(custom_censor_words):
    profanity.add_censor_words(custom_censor_words)

