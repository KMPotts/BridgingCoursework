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
    acadQuery = AcademicObject.objects.order_by('-gradYear')
    academics = list(acadQuery)
    achiQuery = AchievementModel.objects.all()
    achievements = list(achiQuery)
    achievementSorted = sortAchievements(achievements)
    codeQuery = CodingSkill.objects.all()
    codings = list(codeQuery)
    codingsSorted = sortCodings(codings)
    intrQuery = InterestModel.objects.all()
    interests = list(intrQuery)
    return render(request, 'blog/cv.html', {'academics': academics, 'achievements': achievementSorted, 'codings': codingsSorted, 'interests': interests})

def sortAchievements(achievements):
    months = [("January", 0), ("February", 1), ("March", 2), ("April", 3), ("May", 4), ("June", 5), ("July", 6), ("August", 7), ("September", 8), ("October", 9), ("November", 10), ("December", 11) ]
    sortableList = []
    for achievement in achievements:
        sortingValue = (achievement.year*100) + next(item for item in months if item[0] == achievement.month)[1]
        sortableList.append((achievement, sortingValue))
    sortableList.sort(key=lambda tup: tup[1])
    sortableList.reverse()
    finalList = []
    for tuple in sortableList:
        finalList.append(tuple[0])
    return finalList

def sortCodings(codings):
    highList = []
    midList = []
    lowList = []
    finalList = []
    for skill in codings:
        if skill.proficiency == 'Fluent':
            highList.append(skill)
        elif skill.proficiency == 'Working Knowledge':
            lowList.append(skill)
        else:
            midList.append(skill)
    finalList = highList + midList + lowList
    return finalList

def coding_new(request):
    form = CodingForm()
    if request.method == "POST":
        form = CodingForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.save()
            return redirect('cv')
    else:
        form = CodingForm()
    return render(request, 'blog/coding_edit.html', {'form':form})

def academic_new(request):
    form = AcademicForm()
    if request.method == "POST":
        form = AcademicForm(request.POST)
        if form.is_valid():
            academic = form.save(commit=False)
            academic.save()
            return redirect('cv')
    else:
        form = AcademicForm()
    return render(request, 'blog/academic_edit.html', {'form':form})

def achievement_new(request):
    form = AchievementForm()
    if request.method == "POST":
        form = AchievementForm(request.POST)
        if form.is_valid:
            achievement = form.save(commit = False)
            achievement.save()
            return redirect('cv')
    else:
        form = AchievementForm()
    return render(request, 'blog/achievement_edit.html', {'form': form})

def interest_new(request):
    form = InterestForm()
    if request.method == "POST":
        form = InterestForm(request.POST)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.save()
            return redirect('cv')
    else:
        form = InterestForm()
    return render(request, 'blog/interest_edit.html', {'form': form})

def coding_edit(request, pk):
    coding = get_object_or_404(CodingSkill, pk=pk)
    if request.method == "POST":
        form = CodingForm(request.POST, instance=coding)
        if form.is_valid():
            coding = form.save(commit=False)
            coding.save()
            return redirect('cv')
    else:
        form = CodingForm(instance=coding)
    return render(request, 'blog/coding_edit.html', {'form': form})

def academic_edit(request, pk):
    academic = get_object_or_404(AcademicObject, pk=pk)
    if request.method == "POST":
        form = AcademicForm(request.POST, instance=academic)
        if form.is_valid():
            academic = form.save(commit=False)
            academic.save()
            return redirect('cv')
    else:
        form = AcademicForm(instance=academic)
    return render(request, 'blog/academic_edit.html', {'form': form})

def achievement_edit(request, pk):
    achievement = get_object_or_404(AchievementModel, pk=pk)
    if request.method == "POST":
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.save()
            return redirect('cv')
    else:
        form = AchievementForm(instance=achievement)
    return render(request, 'blog/achievement_edit.html', {'form': form})

def interest_edit(request, pk):
    interest = get_object_or_404(InterestModel, pk=pk)
    if request.method == "POST":
        form = InterestForm(request.POST, instance=interest)
        if form.is_valid():
            interest = form.save(commit=False)
            interest.save()
            return redirect('cv')
    else:
        form = InterestForm(instance=interest)
    return render(request, 'blog/interest_edit.html', {'form': form})
