import random
import sqlite3
import argparse


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-a", "--add", required=False, help="Add the quote to the database.")
ap.add_argument("-g", "--give", required=False, help="Ouput a random quote from the database.")
args = vars(ap.parse_args())


class Quote:
    def __init__(self):
        self.quotes = []
        self.path = "quotes.db"
        self.yellow = "\033[33m"
        self.end = "\033[0m"

    def put_quote(self):
        con = sqlite3.connect(self.path)
        c = con.cursor()
        c.execute("INSERT INTO quotes VALUES(?);", (args["add"],))
        con.commit()
        con.close()


    def get_quote(self):
        con = sqlite3.connect(self.path)
        c = con.cursor()
        q = c.execute("SELECT * FROM quotes;")
        for i in q:
            self.quotes.append(i)
        selected_quote = random.choice(self.quotes)
        print(selected_quote)
        con.commit()
        con.close()


quote = Quote()


# main function in our file
def main():
    if args["add"]:
        quote.put_quote()
    else:
        quote.get_quote()

if __name__ == "__main__":
    main()