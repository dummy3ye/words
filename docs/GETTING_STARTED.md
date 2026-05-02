GETTING STARTED

1. Setup
- Make sure you have Python and Node installed.
- Open your terminal in this folder and run `pip install -r requirements.txt`.

2. How to use it
- Open `urls.txt` and paste in any website links you want to grab words from, one per line.
- If you notice a lot of annoying junk words in your list later, just open `config/blacklist.txt` and add those words there.

3. Running the system
- Simply run `python run.py`. It does all the hard work for you: syncs your links, scrapes the data, cleans it up, and formats it.
- If you're a Node person, you can also just type `npm start`.

4. Where to find your stuff
- Everything ends up in the `dist/` folder.
- `words.txt` is your final, clean, alphabetized dictionary.
- `linear.json` shows you how the script handled the words.
