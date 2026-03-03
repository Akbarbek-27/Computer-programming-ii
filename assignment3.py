class CryptoHolding:
    def __init__(self,token_name: str, usd_price: float,coin_amount: int):
        self.token_name = token_name
        self.usd_price = usd_price
        self.coin_amount = coin_amount
    def __str__(self):
        return f"{self.token_name}: {self.coin_amount} coin(s) at ${self.usd_price}"
    def __repr__(self):
        return f"CryptoHolding('{self.token_name}', {self.usd_price}, {self.coin_amount})"
    def __add__(self,other):
        if isinstance(other,CryptoHolding):
            if other.token_name == self.token_name:
                combined_crypto = CryptoHolding(self.token_name, self.usd_price, self.coin_amount + other.coin_amount)
                return combined_crypto
            return NotImplemented
        if isinstance(other,int):
            combined_crypto = CryptoHolding(self.token_name, self.usd_price, self.coin_amount + other)
            return combined_crypto
        return NotImplemented
    def __eq__(self,other):
        if not isinstance(other,CryptoHolding):
            return NotImplemented
        return self.token_name == other.token_name and self.usd_price == other.usd_price
    def __bool__(self):
        return bool(self.coin_amount)
holding1 = CryptoHolding("Bitcoin", 65000.0, 2)
holding2 = CryptoHolding("Bitcoin", 65000.0, 1)
holding3 = CryptoHolding("Ethereum", 3500.0, 0)

print(str(holding1))
print(repr(holding1))
print(holding1 + holding2)
print(holding1 + 4)
print(holding1 == holding2)
print(bool(holding1))
print(bool(holding3))
