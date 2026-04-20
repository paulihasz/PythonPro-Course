def book_description(title: str, author: str, year:int =2025) -> str|int:
    return f"The book {title} by {author} was released in {year} year"

book1 = book_description("Frankenstein", "Mary Shelley", 1818)
book2 = book_description("The Lord of the Rings", "J.R.R. Tolkien")

