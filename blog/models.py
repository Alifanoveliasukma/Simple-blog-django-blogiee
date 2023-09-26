from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='profile/', blank=True, null=True)  # Tambahkan bidang foto profil (opsional)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    
class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=255)  # Tambahkan bidang email
#     nomor_telepon = models.CharField(max_length=15, blank=True, null=True)  # Tambahkan bidang nomor telepon (opsional)
#     jenis_kelamin = models.CharField(max_length=10, choices=[('L', 'Laki-laki'), ('P', 'Perempuan')], blank=True, null=True)  # Tambahkan bidang jenis kelamin (opsional)
#     alamat = models.TextField(blank=True, null=True)  # Tambahkan bidang alamat (opsional)
#     foto_profil = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Tambahkan bidang foto profil (opsional)

#     def __str__(self):
#         return self.user.username