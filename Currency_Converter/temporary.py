# CurrencyConverter ক্লাস তৈরি করা হয়েছে যা মুদ্রা রূপান্তরের কাজ করে
class CurrencyConverter:
    # ক্লাস অ্যাট্রিবিউট: এক্সচেঞ্জ রেট সংরক্ষণ করা হচ্ছে একটি ডিকশনারিতে
    exchange_rates = {
        'USD': 1.0,       # Base currency
        'EUR': 0.85,
        'GBP': 0.75,
        'BDT': 109.5,
        'INR': 83.2
    }

    def __init__(self, amount, from_currency, to_currency):
        # ইনস্ট্যান্স অ্যাট্রিবিউট
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()

    # স্ট্যাটিক মেথড: কারেন্সি কোড valid কিনা যাচাই করে
    @staticmethod
    def is_valid_currency(currency_code):
        return currency_code in CurrencyConverter.exchange_rates

    # ক্লাস মেথড: এক্সচেঞ্জ রেট আপডেট করে
    @classmethod
    def update_exchange_rate(cls, currency_code, new_rate):
        if cls.is_valid_currency(currency_code):
            cls.exchange_rates[currency_code] = new_rate
        else:
            print(f"Invalid currency code: {currency_code}")

    # ইনস্ট্যান্স মেথড: রূপান্তরের কাজ সম্পন্ন করে
    def convert(self):
        if not self.is_valid_currency(self.from_currency) or not self.is_valid_currency(self.to_currency):
            raise ValueError("Invalid currency code provided.")
        
        # রূপান্তরের জন্য USD কে base currency হিসেবে ধরা হয়েছে
        amount_in_usd = self.amount / CurrencyConverter.exchange_rates[self.from_currency]
        converted_amount = amount_in_usd * CurrencyConverter.exchange_rates[self.to_currency]
        return round(converted_amount, 2)


# Logger ক্লাস: ইউজারের রূপান্তর লগ করে
class Logger:
    def log(self, user, amount, result):
        # সহজভাবে কনসোলে লগ দেখানো হচ্ছে
        print(f"[LOG] User: {user} | Amount: {amount} | Converted Amount: {result}")


# ব্যবহার উদাহরণ
if __name__ == "__main__":
    amount= float(input("Enter amount: "))
    from_currency= input("Enter your currency")
    to_currency= input("Enter your currency")
    logger = Logger()

    # CurrencyConverter অবজেক্ট তৈরি (Association: Logger আলাদাভাবে তৈরি করা হয়েছে)
    converter = CurrencyConverter(amount, from_currency, to_currency)

    # রূপান্তর সম্পন্ন করা হচ্ছে
    try:
        result = converter.convert()
        logger.log("Shahadat", "100 USD to BDT", result)
    except ValueError as e:
        print(f"Error: {e}")

    # নতুন এক্সচেঞ্জ রেট আপডেট করা হচ্ছে
    # CurrencyConverter.update_exchange_rate('BDT', 110.0)
