# Write a program that asks the user to enter some text and then counts how many articles are
# in the text. Articles are the words 'a', 'an', and 'the'

def count_articles(text):
    # Convert the text to lowercase to make the comparison case-insensitive
    text = text.lower()
    # Split the text into words
    words = text.split()
    
    # Define a list of articles
    articles = ['a', 'an', 'the']
    
    # Initialize a counter for articles
    article_count = 0
    
    # Iterate through the words and count the articles
    for word in words:
        if word in articles:
            article_count += 1
            
    return article_count

def main():
    # Ask the user to enter some text
    text = input("Enter some text: ")
    
    # Count the articles in the text
    num_articles = count_articles(text)
    
    # Print the result
    print("Number of articles in the text:", num_articles)

if __name__ == "__main__":
    main()