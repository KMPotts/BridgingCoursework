from django.shortcuts import render
from django.utils import timezone
from .models import Post, CodingSkill, AcademicObject, AchievementModel, InterestModel
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CodingForm, AcademicForm, AchievementForm, InterestForm
from django.shortcuts import redirect


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def cv(request):
    return render(request, 'blog/cv.html')

def coding_edit(request):
    form = CodingForm()
    if request.method == "POST":
        form = CodingForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.skill = request.skill
            skill.proficiency = request.proficiency
            skill.save()
            return redirect('cv', pk=skill.pk)
    else:
        form = CodingForm()
    return render(request, 'blog/coding_edit.html', {'form':form})

def academic_edit(request):
    form = AcademicForm()
    if request.method == "POST":
        form = AcademicForm(request.POST)
        if form.is_valid():
            academic = form.save(commit=False)
            academic.institution = request.institution
            skill.details = request.details
            skill.save()
            return redirect('cv', pk=academic.pk)
    else:
        form = AcademicForm()
    return render(request, 'blog/academic_edit.html', {'form':form})

def achievement_edit(request):
    form = AchievementForm()
    if request.method == "POST":
        form = AchievementForm(request.POST)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.label = request.label
            achievement.year = request.year
            achievement.month = request.month
            achievement.save()
            return redirect('cv', pk=achievement.pk)
    else:
        form = AchievementForm()
    return render(request, 'blog/achievement_edit.html', {'form': form})

def interest_edit(request):
    form = InterestForm()
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.title = request.title
            interest.details = request.details
            interest.save()
            return redirect('cv', pk=achievement.pk)
    else:
        form = InterestForm()
    return render(request, 'blog/interest_edit.html', {'form': form})
