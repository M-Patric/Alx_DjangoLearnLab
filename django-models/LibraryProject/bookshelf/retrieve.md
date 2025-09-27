
### 2. **retrieve.md**
```md
# Retrieve Operation

```python
retrieved_book = Book.objects.get(id=book.id)
retrieved_book.title, retrieved_book.author, retrieved_book.publication_year
# Output: ('1984', 'George Orwell', 1949)
