class CurrencyConverter :
    exchange_rates = {
        "USD" : 1.0,
        "BD"  : 121.00,
        "EURO": 0.88,
        "GBP" : 0.75
    }
    
    def __init__(self,amount,from_currency,to_currency):
        
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
    #instance method: রূপান্তরের কাজ সম্পন্ন করে    
    def convert(self):
        if self.from_currency not in CurrencyConverter.exchange_rates or \
        self.to_currency not in CurrencyConverter.exchange_rates:
            return "invalid currency not in our system"
        
        base_amount =  self.amount/ CurrencyConverter.exchange_rates[self.from_currency]
        converted_amount = base_amount * CurrencyConverter.exchange_rates[self.to_currency]
        return round(converted_amount,2)
    #classmethod: এক্সচেঞ্জ রেট আপডেট করে
    @classmethod
    def update_rate(cls,currency,new_rate):
        cls.exchange_rates[currency] = new_rate
    #Static method :কারেন্সি কোড valid কিনা যাচাই করে
    @staticmethod
    def is_valid_currency(user_given_value):
        return user_given_value.upper() in CurrencyConverter.exchange_rates 

# class Logger:
#     def Log(self,user,converter):
#         result = converter.convert()
#         print(f"record: {user} converted {converter.amount} {converter.from_currency} ->{result} {converter.to_currency}")

#এই ক্লাসে log(user, amount, result) নামের একটি মেথড থাকতে হবে যা ইউজারের conversion log করবে
class Logger:
    def log(self, user, amount, result):
        result=converter.convert()
        from_curr=converter.from_currency
        to_curr = converter.to_currency
        
        print(f"[LOG] User: {user} | Currency Amount: {amount} {from_curr} | Converted Amount: {result} {to_curr}")

        
if __name__ == "__main__" :
    CurrencyConverter.update_rate("BD",130)
    amount = float(input("Enter amount: "))
    from_curr = input("Enter  your currency: ")
    to_curr = input("Enter  your converted currency: ")
    user = input("Enter your name: ")
    #CurrencyConverter অবজেক্ট তৈরি (Association: Logger আলাদাভাবে তৈরি করা হয়েছে)
    converter = CurrencyConverter(amount,from_curr,to_curr)    
    
    if not CurrencyConverter.is_valid_currency(from_curr) or not CurrencyConverter.is_valid_currency(to_curr):
        print("invalid currency we dont have that currency")
        
    else:
        Logger= Logger()
        Logger.log(user,amount,converter)