# Atom - A Basic Blog Website

A simple blog website built with Django where users can create posts, comment on them, and manage their content.

## Features

### User Authentication
- Register new accounts
- Login/Logout functionality
- Protected routes for authenticated users

### Posts
- Create new posts
- Edit own posts
- Delete own posts
- View all posts on homepage

### Comments
- Add comments to posts
- Edit own comments
- Delete own comments
- View comment count

## Technical Stack
- Django 5.1.3
- SQLite database
- Django Forms
- Django Authentication


## Models

### Post
```python
class Post(models.Model):
title = models.CharField(max_length=200)
content = models.TextField()
created_at = models.DateTimeField(auto_now_add=True)
author = models.ForeignKey(User, on_delete=models.CASCADE)
def str(self):
return self.title
```

### Comment
```python
class Comment(models.Model):
post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
user = models.ForeignKey(User, on_delete=models.CASCADE)
content = models.TextField()
created_at = models.DateTimeField(auto_now_add=True)
def str(self):
return f'{self.user.username} - {self.content[:20]}'
```

## Setup

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/atom.git
cd atom
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
python -m venv env
```

Activate the virtual environment:

- **Windows:**
  ```bash
  env\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source env/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

*If you don't have a `requirements.txt` file, you can install Django directly:*

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

To access the Django admin panel, create a superuser account.

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```


Open your browser and navigate to `http://127.0.0.1:8000/` to view the application.

## Usage

- **Homepage:** View all posts.
- **Register:** Create a new user account.
- **Login:** Access your account.
- **Create Post:** Add a new blog post.
- **Edit/Delete Post:** Manage your own posts.
- **Post Detail:** View a single post and its comments.
- **Add Comment:** Leave a comment on a post.
- **Edit/Delete Comment:** Manage your own comments.

## Admin Panel

Access the Django admin panel to manage users, posts, and comments.

1. Navigate to `http://127.0.0.1:8000/admin/`.
2. Log in with the superuser credentials you created earlier.
3. **Manage Models:**
   - **Posts:** Add, edit, or delete posts.
   - **Comments:** Add, edit, or delete comments.
   - **Users:** Manage user accounts.

### Registering Models in Admin


```python
from django.contrib import admin
from .models import Post, Comment
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
list_display = ('title', 'author', 'created_at')
list_filter = ('created_at', 'author')
search_fields = ('title', 'content')
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
list_display = ('content', 'user', 'post', 'created_at')
list_filter = ('created_at', 'user')
search_fields = ('content', 'userusername', 'post_title')
ordering = ('-created_at',)
```

## Future Improvements

- **Styling:** Enhance the UI with CSS or integrate a frontend framework like Bootstrap.
- **User Profiles:** Allow users to have detailed profiles.
- **Image Uploads:** Enable image uploads for posts.
- **Rich Text Editor:** Implement a WYSIWYG editor for richer post content.
- **Pagination:** Add pagination to the homepage and post detail pages.
- **Search Functionality:** Implement search across posts and comments.
- **Responsive Design:** Make the application mobile-friendly.
- **Testing:** Add automated tests for views, models, and forms.

## License

[MIT License](LICENSE)

*Feel free to contribute to this project by opening issues or submitting pull requests.*
