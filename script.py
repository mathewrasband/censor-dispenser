# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor(text, document):
  for i in document:
    censored_document = document.replace(text, '****')
  return censored_document

email_one_censored = censor('learning algorithms', email_one)

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", " her ", "herself"]

def censor_terms(terms, document):
  for term in terms:
    for i in document:
      document = document.replace(term, ' * ')
  new_terms = []    
  for term in terms:
    new_terms.append(term.title())
  for term in new_terms:
    for i in document:
      document = document.replace(term, ' * ')
  return document

email_two_censored = censor_terms(proprietary_terms, email_two)

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_negatives(negative, terms, document):
  for neg in negative:
    for i in document:
      document = document.replace(neg, ' * ')
  new_neg = []
  for n in negative:
    new_neg.append(n.title())
  for neg in new_neg:
    for i in document:
      document = document.replace(neg, ' * ')
  for term in terms:
    for i in document:
      document = document.replace(term, ' * ')
  new_terms = []    
  for term in terms:
    new_terms.append(term.title())
  for term in new_terms:
    for i in document:
      document = document.replace(term, ' * ')
  return document

email_three_censored = censor_negatives(negative_words, proprietary_terms, email_three)


  


    