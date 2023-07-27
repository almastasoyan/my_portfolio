from django.shortcuts import render, redirect, get_object_or_404
from .models import Skill, Experience, Education,  SocialLink, Language, Testimonial, PersonalInfo, PortfolioProject
from .forms import MessageForm

def home(request):

    if request.method == "POST":
        print("POSTED DATA")
        print(request.POST)
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/#contact")
        
    

    my_skills = Skill.objects.all()
    my_experience = Experience.objects.all()
    my_education = Education.objects.all()
    my_social_link = SocialLink.objects.all()
    my_language = Language.objects.all()
    my_testimonials = Testimonial.objects.all()
    my_personal_info = PersonalInfo.objects.get(user__username = "almastasoyan")
    my_messageForm = MessageForm()
    my_portfolio_projects = PortfolioProject.objects.all()

    my_data = { "personal_info":my_personal_info,
                "skills": my_skills,
                "experiences": my_experience,
                "educations": my_education,
                "social_links":my_social_link,
                "languages": my_language,
                "testimonials": my_testimonials,
                "messageForm":my_messageForm,
                "portfolio_projects": my_portfolio_projects
            }
    return render(request, "index.html", context= my_data)


def portfolio_project(request, id):
    project =  get_object_or_404(PortfolioProject, id =id)
    print(project)
    return render(request, "portfolio-details.html",context= {"project": project})


