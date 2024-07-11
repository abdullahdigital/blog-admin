# blog/views.py

from django.shortcuts import render, get_object_or_404,redirect
from django.http import JsonResponse
from .models import Post, Writer, Article
import json
def index(request):
    # Retrieve the latest three posts
    latest_posts = Post.objects.order_by('-created_at')[:3]
    context = {
        'latest_posts': latest_posts
    }
    return render(request, 'index.html', context)

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post.html', {'post': post})

def chart_data(request):
    labels = []
    data = []
    queryset = Writer.objects.all()
    for writer in queryset:
        labels.append(writer.name)
        data.append(writer.article_set.count())  

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

""" def blog_list(request):
    all_posts = Post.objects.all()
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog_list.html', context) """

def blog_list(request):
    all_posts = Post.objects.all().order_by('-created_at')  # Ensure posts are ordered by date, newest first
    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog_list.html', context)

def about_page(request):
    return render(request, 'about.html', {'title': 'About Us - Abdullah\'s Blog'})

from django.contrib import messages
from django import forms
from .models import ContactSubmission

def contact_submission(request):
    class ContactSubmissionForm(forms.ModelForm):
        class Meta:
            model = ContactSubmission
            fields = ['name', 'email', 'message']

    if request.method == 'POST':
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message. We will get back to you shortly.')
            return redirect('contact')  # Redirect to the contact page URL pattern name
    else:
        form = ContactSubmissionForm()

    return render(request, 'contact.html', {'form': form})





#Subscribe
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsletterUser

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        if email:
            # Check if email already exists
            if not NewsletterUser.objects.filter(email=email).exists():
                # Create a new NewsletterUser object
                new_user = NewsletterUser(email=email)
                new_user.save()
                # Add a success message
                messages.success(request, 'You have successfully subscribed!')
            else:
                # Email already exists, handle accordingly
                messages.warning(request, 'This email is already subscribed.')
        else:
            # No email provided, handle accordingly
            messages.error(request, 'Please provide an email address.')

    # Redirect back to the same page
    return redirect('index')
