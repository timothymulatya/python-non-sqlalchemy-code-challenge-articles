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
        self._articles = []
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if hasattr(self, "_name"):
            raise AttributeError("Name cannot be changed")
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
    
    def articles(self):
        return self._articles
    
    def magazines(self):
        return list({article.magazine for article in self._articles})
    
    def add_article(self, magazine, title):
        new_article = Article(self, magazine, title)
        return new_article
    
    def topic_areas(self):
        if not self._articles:
            return None
        categories = {article.magazine.category for article in self._articles}
        return list(categories)

class Magazine:
    all = []
    
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("Category must be a string")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = category
    
    def articles(self):
        return self._articles
    
    def contributors(self):
        return list({article.author for article in self._articles})
    
    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]
    
    def contributing_authors(self):
        author_counts = {}
        for article in self._articles:
            author_counts[article.author] = author_counts.get(article.author, 0) + 1
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None
    
    @classmethod
    def top_publisher(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda mag: len(mag.articles()))