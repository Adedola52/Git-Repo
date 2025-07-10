import pandas as pd
import statistics
import json
import logging
from datetime import datetime
from typing import List, Dict

logging.basicConfig(filename='budgetanalyzer.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s',
                    filemode='w')


class Transaction:
    """
    Represents a financial transaction.
    """

    def __init__(self, date: str, amount: float, category: str):
        """
        Constructor for creating Transaction objects.

        Defines attributes. These attributes can be accessed and used by other methods in the class
        or classes that interact with Transaction objects or takes in the the objects as an argument.
    
        Parameters:
        date (str): The date of the transaction
        amount (float): The transaction amount
        category (str): The category assigned to the transaction
    
        """
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.amount = amount
        self.category = category

    def __repr__(self):
        """
        Returns a readable string representation of the Transaction objects,
        useful for debugging and understanding the object's contents.
        """
        repr = f"<Transaction {self.amount} {self.category} on {self.date.date()}>"
        return repr  # noqa: E501

    def is_expense(self):
        """
        Checks for transactions amount < 0. i.e expenses
        """
        expense = self.amount < 0
        return expense

