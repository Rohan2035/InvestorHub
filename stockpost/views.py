from django.shortcuts import render, HttpResponse, redirect
from stockpost.models import StockPosts as sp
from django.contrib import messages
import random as rn

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

    context = {'post' : post, 'post1' : items}
    return render(request, 'content.html', context)



def category(request, Category):
    post = sp.objects.filter(Category=Category)
    context = {"cat" : post}
    return render(request, 'cat.html', context)



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


        # Few basic checks

        # Slug Checks
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
    if(len(post) == 0):
        return HttpResponse('<h1 align> No Post Added </h1>')
    context = {"post" : post}
    return render(request, "DisplayAll.html", context)



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

def deletePost(request, slug):

    if request.user.is_authenticated:
        deletePost = sp.objects.get(slug = slug)
        deletePost.delete()
        messages.success(request, 'Post Sucessfully Deleted!!')
        return redirect('Index')
    else:
        return HttpResponse('<h1>Error</h1>')


# Remove this 
def test(request):

    if request.method == 'POST':
        id = request.POST['postId']
        return HttpResponse(id)
    else:
        return HttpResponse('Illegal Access')
