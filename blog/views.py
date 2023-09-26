from django.shortcuts import render, redirect
from .models import Post, Category, Comment
from .forms import PostForm, CategoryForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Like

@login_required  
def create_post(request):
    # Cek apakah metode permintaan adalah POST (pengguna mengirimkan formulir)
    if request.method == 'POST':
        # Inisialisasi formulir dengan data yang dikirimkan oleh pengguna
        form = PostForm(request.POST)
        # Periksa apakah formulir valid
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Simpan data dari formulir ke database
            form.save()
            # Redirect pengguna ke halaman 'list_posts' setelah posting berhasil dibuat
            return redirect('list_posts')  # Ganti 'list_posts' dengan nama URL yang sesuai
    else:
        # Jika metode permintaan adalah GET (pengguna membuka halaman)
        # Inisialisasi formulir kosong untuk membuat posting baru
        form = PostForm()
    
    # Render halaman 'create_post.html' dengan formulir
    return render(request, 'create_post.html', {'form': form})

def list_posts(request):
    # Ambil semua posting dari database
    posts = Post.objects.all()
    categories = Category.objects.all()
    
    # Cek apakah ada parameter 'category' dalam query string
    category = request.GET.get('category')
    if category:
        # Jika ada parameter 'category', filter posting berdasarkan kategori
        posts = posts.filter(category__name=category)

    context = {
        'posts': posts,
        'categories': categories,
        'selected_category': category,  # Menambahkan parameter 'selected_category' ke konteks
    }
    
    # Kirim data posting ke template
    return render(request, 'list_posts.html', context)

@login_required  
def post_detail(request, pk):
    # Ambil posting berdasarkan primary key (pk)
    post = get_object_or_404(Post, pk=pk)
    kategoris = Category.objects.all()
    
    # Kirim data posting ke template
    return render(request, 'post_detail.html', {'post': post,'kategori': kategoris})

@login_required  
def update_post(request, pk):
    # Ambil posting berdasarkan primary key (pk)
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # Jika metode permintaan adalah POST (pengguna mengirimkan formulir)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            # Jika formulir valid, simpan perubahan ke database
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        # Jika metode permintaan adalah GET (pengguna hanya membuka halaman)
        form = PostForm(instance=post)

    return render(request, 'update_post.html', {'form': form, 'post': post})

@login_required  
def delete_post(request, pk):
    # Ambil posting berdasarkan primary key (pk)
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        # Jika metode permintaan adalah POST (pengguna mengonfirmasi penghapusan)
        post.delete()
        return redirect('list_posts')
    
    return render(request, 'delete_post.html', {'post': post})

def list_kategori(request):
    # Ambil semua posting dari database
    kategoris = Category.objects.all()
    
    # Kirim data posting ke template
    return render(request, 'list_kategori.html', {'kategoris': kategoris})

@login_required  
def create_kategori(request):
    # Cek apakah metode permintaan adalah POST (pengguna mengirimkan formulir)
    if request.method == 'POST':
        # Inisialisasi formulir dengan data yang dikirimkan oleh pengguna
        form = CategoryForm(request.POST)
        # Periksa apakah formulir valid
        if form.is_valid():
            # Simpan data dari formulir ke database
            form.save()
            # Redirect pengguna ke halaman 'list_posts' setelah posting berhasil dibuat
            return redirect('list_posts')  # Ganti 'list_posts' dengan nama URL yang sesuai
    else:
        # Jika metode permintaan adalah GET (pengguna membuka halaman)
        # Inisialisasi formulir kosong untuk membuat posting baru
        form = CategoryForm()
    
    # Render halaman 'create_post.html' dengan formulir
    return render(request, 'create_kategori.html', {'form': form})

def kategori_detail(request, pk):
    # Ambil posting berdasarkan primary key (pk)
    kategoris = get_object_or_404(Category, pk=pk)
    
    # Kirim data posting ke template
    return render(request, 'kategori_detail.html', {'kategori': kategoris})

@login_required  
def update_kategori(request, pk):
    # Ambil posting berdasarkan primary key (pk)
    kategoris = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        # Jika metode permintaan adalah POST (pengguna mengirimkan formulir)
        form = CategoryForm(request.POST, instance=kategoris)
        if form.is_valid():
            # Jika formulir valid, simpan perubahan ke database
            form.save()
            return redirect('kategori_detail', pk=kategoris.pk)
    else:
        # Jika metode permintaan adalah GET (pengguna hanya membuka halaman)
        form = CategoryForm(instance=kategoris)

    return render(request, 'update_kategori.html', {'form': form, 'kategori': kategoris})

def delete_kategori(request, pk):
    # Ambil posting berdasarkan primary key (pk)
    kategoris = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        # Jika metode permintaan adalah POST (pengguna mengonfirmasi penghapusan)
        kategoris.delete()
        return redirect('list_kategori')
    
    return render(request, 'delete_kategori.html', {'kategori': kategoris})

@login_required  
# coment
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form': form})


