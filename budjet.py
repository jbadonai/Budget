
class Budget:

    """
    This is the Budget class.
    The Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
    1.  Depositing funds to each of the categories
    2.  Withdrawing funds from each category
    3.  Computing category balances
    4.  Transferring balance amounts between categories
    """

    def __init__(self):

        self.value = 0
        pass

    def deposit_funds(self, amount: int):
        """
        Funds can be added to any specified category using this function
        """

        self.value += amount

    def withdraw_fund(self,  amount):
        """
        Funds can be withdrawn from specified category using this function
        """
        self.value -= amount

    def get_balance(self):
        """
        Balance for specified category will be computed here
        """
        return self.value

    def transfer_balance_to(self, to_category: object, amount : int):
        """
        Balance can be transferred from one category (from_category) to another category (to_category)
        """

        pass
        to_category.value += amount
        self.value -= amount


# instantiate each object category
food = Budget()
clothing = Budget()
entertainment = Budget()

# display balance of each category before transactions
print("Balance before transactions")
print(f"food balance: {food.get_balance()}")
print(f"Clothing balance: {clothing.get_balance()}")
print(f"entertainment balance: {entertainment.get_balance()}")
print()




# deposit fund to each category
food.deposit_funds(1000)
clothing.deposit_funds(1000)
entertainment.deposit_funds(1000)

# withdraw fund from category
food.withdraw_fund(200)

# transferring amount between categories
food.transfer_balance_to(clothing, 500)

print()
# display balance of each category after transactions
print(f"food balance: {food.get_balance()}")
print(f"Clothing balance: {clothing.get_balance()}")
print(f"entertainment balance: {entertainment.get_balance()}")

