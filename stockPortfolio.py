import requests
import json

class StockPortfolioTracker:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        if ticker in self.portfolio:
            self.portfolio[ticker]['shares'] += shares
        else:
            self.portfolio[ticker] = {'shares': shares, 'price': 0.0}
        print(f"Added {shares} shares of {ticker} to your portfolio.")

    def remove_stock(self, ticker, shares):
        if ticker in self.portfolio:
            if self.portfolio[ticker]['shares'] > shares:
                self.portfolio[ticker]['shares'] -= shares
                print(f"Removed {shares} shares of {ticker} from your portfolio.")
            elif self.portfolio[ticker]['shares'] == shares:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker} from your portfolio.")
            else:
                print(f"You don't own enough shares of {ticker} to remove.")
        else:
            print(f"{ticker} is not in your portfolio.")

    def fetch_stock_price(self, ticker):
        api_key = "cs7j761r01qtqcar5do0cs7j761r01qtqcar5dog"  #test api key of stock website for live stock reviews 
        base_url = f"https://finnhub.io/api/v1/quote?symbol={ticker}&token={api_key}"
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            return data.get('c', 0.0)
        else:
            print(f"Failed to fetch price for {ticker}. Status code: {response.status_code}")
            return 0.0

    def update_prices(self):
        for ticker in self.portfolio:
            price = self.fetch_stock_price(ticker)
            self.portfolio[ticker]['price'] = price

    def view_portfolio(self):
        self.update_prices()
        total_value = 0.0
        print("\nYour Portfolio:")
        print(f"{'Ticker':<10}{'Shares':<10}{'Price':<10}{'Value':<10}")
        print("-" * 40)
        for ticker, details in self.portfolio.items():
            shares = details['shares']
            price = details['price']
            value = shares * price
            total_value += value
            print(f"{ticker:<10}{shares:<10}{price:<10.2f}{value:<10.2f}")
        print("-" * 40)
        print(f"Total Portfolio Value: Rs{total_value:.2f}\n")

if __name__ == "__main__":
    tracker = StockPortfolioTracker()

    while True:
        print("\nOptions:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares: "))
            tracker.add_stock(ticker, shares)

        elif choice == "2":
            ticker = input("Enter stock ticker: ").upper()
            shares = int(input("Enter number of shares to remove: "))
            tracker.remove_stock(ticker, shares)

        elif choice == "3":
            tracker.view_portfolio()

        elif choice == "4":
            print("Exiting from the program..!")
            break

        else:
            print("Invalid choice. Please try again.")
