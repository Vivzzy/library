import pandas as pd

# ЗАДАНИЕ 1

authors = pd.DataFrame({'author_id':[1, 2, 3],
                        'author_name':['Тургенев', 'Чехов', 'Островский']},
                       columns=['author_id', 'author_name'])
print(authors)

book = pd.DataFrame({'author_id':[1, 1, 1, 2, 2, 3, 3],
                     'book_title':['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий', 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
                     'price':[450, 300, 350, 500, 450, 370, 290]},
                    columns=['author_id', 'book_title', 'price'])
print(book)

# ЗАДАНИЕ 2

authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
print(authors_price)

# ЗАДАНИЕ 3

top5 = authors_price.nlargest(5, 'price')
print(top5)

# ЗАДАНИЕ 4

authors_stat = authors_price.groupby('author_name').agg({'price':['min', 'max', 'mean']})
authors_stat = authors_stat.rename(columns={'min':'min_price', 'max':'max_price', 'mean':'mean_price'})
print(authors_stat)
