In the `basic_filter` code, the following operations are performed:

- Sentence splitting
- Punctuation removal
- Converting all words to lowercase
- Removing numbers and all numerical expressions
- Removing stopwords, i.e., ineffective words
- Removing 1-2 letter words
- Removing characters outside the English alphabet
- Checking if the sentence is longer than 3 words
- Checking if the sentence is in English
- Writing the results in a neat way to a new text file (txt)

In the `filter_with_keyword` file, you can also collect sentences containing the keywords you want in the code. The usage of the keyword file is explained below.

Specify the complex English data you want to scan in txt format as `input.txt`.

Run the `basic_filter.py` file for general filtering.

If you want sentences containing only specific keywords, in the `filter_with_keyword.py` file, you can write in place of `word1` or `word2` in the `keywords = ["keyword1", "keyword2"]` section at the top of the code.

Add extra words you will add by keeping them in parentheses (") in quotes and adding a comma between each keyword.

Don't forget to delete the quotes and comma if you're going to delete a keyword.

- Adding a keyword -> `keywords = ["keyword1", "keyword2", "keyword3"]` -> We wrote `keyword3` in quotes and put a comma before it.
- Removing a keyword -> `keywords = ["keyword1"]` -> We deleted `keyword2` along with its quotes and removed the comma in between.

! Operations may vary depending on the length of the text or the power of your computer.
The probable waiting time for a 400,000-line text file is 3-5 minutes.

Instead of changing the name of your own complex data txt file, you can change the `input.txt` part in the `process_text('input.txt', 'final.txt')` section at the bottom of the codes with your own file name. Similarly, by changing the `final.txt` part, you can also edit the name of the text file where the results will be printed.



-----------------------------------------------------------------------------------------------------------
The code is a very simple start, I liked it so I'm thinking of continuing. It's a job I started as a university project, I put the complex data I collected from the internet related to the word "Game" in the `input.txt` section as an example. You can test it. There will be extra studies on filtering and analysis, maybe I can turn it into a service with a visual interface. I'm thinking of integrating a service to collect data from the desired source (Twitter, Reddit, Articles, Documents, Forums, etc.) according to the keyword.

For questions/requests or any other matter, you can reach me via Discord: @nsk or LinkedIn: https://www.linkedin.com/in/enes-ertu%C4%9Frul-k-a7a52410b/