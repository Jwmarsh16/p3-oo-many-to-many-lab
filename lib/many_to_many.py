class Author:
    def __init__(self, name):
        self.name = name
        self._contracts = []
        

    def get_contracts(self, contract):
        if isinstance(contract, Contract):
            self.related_contracts.append(contract)


    def books(self, book):
        if isinstance(book, Book):
            self.related_books.append(book)

    def total_royalties(self):
        for contract in self.related_contracts:
            self.royalties += contract.royalties
        return self.royalties

    def sign_contract(book, date, royalties):
        if isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int):
            self.royalties += royalties
            return Contract(self, book, date, royalties)
        else:
            return None
    
        
    pass


class Book:
    def __init__(self, title):
        self.title = title
    pass


class Contract:
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties


    def contracts_by_date(cls, date):
        for contract in cls.related_contracts:
            if contract.date == date:
                return contract

    pass