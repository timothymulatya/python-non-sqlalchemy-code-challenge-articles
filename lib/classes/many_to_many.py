class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self.author = author  # This triggers the setter
        self.magazine = magazine  # This triggers the setter
        self.title = title  # This triggers the setter
        Article.all.append(self)
        # Note: The setters already handle appending to author/magazine lists
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if hasattr(self, "_title"):
            raise AttributeError("Title cannot be changed")
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author")
        # Remove from old author's list
        if hasattr(self, "_author") and self._author:
            self._author._articles.remove(self)
        # Add to new author's list
        if not hasattr(author, '_articles'):
            author._articles = []
        author._articles.append(self)
        self._author = author
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine")
        # Remove from old magazine's list
        if hasattr(self, "_magazine") and self._magazine:
            self._magazine._articles.remove(self)
        # Add to new magazine's list
        if not hasattr(magazine, '_articles'):
            magazine._articles = []
        magazine._articles.append(self)
        self._magazine = magazine
        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass