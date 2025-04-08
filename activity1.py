class Movie():
    def __init__(self, title, year, top10):
        self.title = title
        self.year = year
        self.top10 = top10

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Currently in Top 10: {self.top10}")

# inheritance from the Movie class
class Series(Movie):
    pass

# objects
my_movie = Movie("Venom: The last dance", 2025, True)
my_series = Series("Queen of the South", 2016, False)

# calling methods
my_movie.describe()
print()
my_series.describe()
