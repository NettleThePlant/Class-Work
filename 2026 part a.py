# Function to calculate readability score of text 
def calculate_readability_score(text): 

    # Split the text into a list of words 
    words = text.split() 
    print("The list of words in the text is:\n", words) 

   # Initialise the word counters 
    word_count = len(words) # Number of words in list
    #counting short words
    short_word_count = 0
    for x in words:
        if len(x) <=2:
            short_word_count += 1
        else:
            continue
    print('Short words:', short_word_count)
    
    #complex words
    vowel_count = 0
    complex_words = 0
    for x in words:
        if "a" in x:
            vowel_count += 1
        elif "e" in x:
            vowel_count += 1
        elif "i" in x:
            vowel_count += 1
        elif "o" in x:
            vowel_count += 1
        elif "u" in x:
            vowel_count += 1
        elif vowel_count >= 3:
            complex_words += 1
    print('Complex words: ',complex_words)
    
    # Initialise the number of sentences 
    sentence_count = text.count(".")
    sentence_count += text.count("!")
    
    # Calculate the readability score
    wordDivideSent = word_count/sentence_count
    wordSentplus = wordDivideSent+100
    
    wordMinShword = word_count- short_word_count
    wordShwordDivide = wordMinShword/word_count
    
    total1 = wordSentplus * wordShwordDivide
    score = 0.4*total1
    
    '''
    score = word_count * sentence_count 
    score = round(score, 2) # Round the score to 2 d.p. 
    '''
    return score 

# Set the text for analysis 
text1 = "Elaborate sentences influence readability in subtle and unpredictable ways." 
text2 = "I do not like green eggs and ham! I do not like them Sam I am!" 
  
# Calculate the score for text1 
score1 = calculate_readability_score(text1)

print('Readability score 1:',score1, '\n')

score2 = calculate_readability_score(text2)
print('Readability score 2:',score2,'\n')

#Which score is easier to read
if score1 == score2:
    print('Both scores are the same')
elif score1<score2:
    print('The first score is easier to read')
elif score2<score1:
    print('The second score is easier to read')
    
