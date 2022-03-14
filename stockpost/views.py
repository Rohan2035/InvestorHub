from django.shortcuts import render, HttpResponse, redirect
from stockpost.models import StockPosts as sp 
from stockpost.models import comments as cm
from django.contrib import messages
import random as rn
import os

# To Login as Admin
# Username : Company 
# Password : 1234

# Create your views here.
def index(request):

    all_post = list(sp.objects.all())

    l = len(all_post)
    item = rn.sample(all_post, l)
    context = {'post' : item}

    return render(request, 'index.html', context) 



def content(request, slug):

    # Fetching the Post
    post = sp.objects.get(slug = slug)

    # Suggestions
    suggestion = list(sp.objects.all())
    items = rn.sample(suggestion, 3)

    # Comments
    comments = cm.objects.filter(post_id = post.post_id)
    if len(comments) == 0:
        comment_context = "No Comments Added"
    else:
        comment_context = comments
        
    context = {'post' : post, 'post1' : items, 'comments' : comment_context}
    return render(request, 'content.html', context)


def search(request):

    query = request.GET['query']
    print(query)

    query = " ".join(query.split())

    if(len(query) == 0):
        return HttpResponse("Search unsucessful please fill the search box")

    elif(len(query) > 1000):
        return HttpResponse("You have filled a long character please enter a smaller keyword")

    else:
        post = sp.objects.filter(Name__icontains=query)
        context = {'post': post}

    return render(request, 'search.html', context)



# Add Content and validate function are connected 
def addContent(request):

    if request.user.is_authenticated:
        return render(request, 'addContent.html')

    else:
        return HttpResponse("Error 404 Not found")



def validate(request):

    if request.method == 'POST':

        name = request.POST['name']
        post = request.POST['post']
        
        img = request.FILES["photo"]

        check_post = sp.objects.filter(Name=name)

        # Few basic checks
        if check_post:
            return HttpResponse("The Post already exists")

        # Creating Slug 
        slug = str(name).lower()
        slug = slug.split()
        slug_list = []

        for i in slug:
            if(i.isalnum):
                slug_list.append(i)
        slug = "".join(slug_list)

        # Name 
        name = name.lower()

        a = request.user
        a = str(a)


        final = sp(Name=name, content=post, slug=slug, img1=img, author = a)
        
        final.save()  
        messages.success(request, "Post Sucessfully added") 
        return redirect("Index")

    else:

        return HttpResponse("Error 404 not found")



def DisplayAll(request):
    post = sp.objects.filter(author = request.user)

    context = {"post" : post}
    
    return render(request, "DisplayAll.html", context)



# These 3 contact function are connected 
def contact(request):
    return render(request, "Contact.html")



def validateContact(request):

    if request.method == 'POST':
        name = request.POST['name']
        s = request.POST['sug']

        if(len(name) < 2 and len(s) < 2):
            return HttpResponse("Invalid")

        f = sp(user_name = name, Suggestions = s)
        f.save()  
        messages.success(request, "Message Sucessfully Sent")
        
        return redirect("Index")

    else:
        return HttpResponse("Error not found")



def deletePost (request):

    if request.method == 'POST':
        id = request.POST['post_del']
        post = sp.objects.get(post_id = id)
        post.delete()
        
        messages.success(request, "Post Deleted")
        return redirect ('Index')
    else:
        return HttpResponse ('Illeagal access')



# These 3 edit functions are connected 
def edit_Handler(post):
    global edit_post
    edit_post = post


def validate_edit(request):
    if request.method == 'POST':

        new_post_name = request.POST['newName']
        new_post_content = request.POST['newPost']

        if len(request.FILES) != 0:
            if len(edit_post.img1) > 0:
                os.remove(edit_post.img1.path)
            edit_post.img1 = request.FILES["photo"]



        edit_post.Name = new_post_name
        edit_post.content = new_post_content
        edit_post.save()

        messages.success(request, "Successfuly Edited")
    else:
        return HttpResponse("Illegal Access")



def edit_post (request):

    if request.method == 'POST':

        post_id = request.POST['post_ed']
        post = sp.objects.get(post_id = post_id)
        
        context = {'post' : post}

        edit_Handler(post)
    
        return render (request, 'editPost.html', context)

    else:    
        return HttpResponse("Access Denied")


def validate_comment(request):
    if request.method == 'POST':
        comment_text = request.POST['comment']
        post_id = sp.objects.get(post_id=2)
        post_name = post_id.Name
        user_name = request.user

        comment = cm(post_id=post_id, comment_text=comment_text, user_name = user_name, post_name = post_name)

        comment.save()

        return HttpResponse("Comment Sucessfully Added")
    else:
        return HttpResponse("Illegal Access")



def test(request):
    return render(request, "Test.html")

