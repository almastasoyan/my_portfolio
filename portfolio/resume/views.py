from django.shortcuts import render
from .models import Skill, Experience, Education,  SocialLink, Language, Testimonial, PersonalInfo
from .forms import MessageForm

def home(request):
    my_skills = Skill.objects.all()
    my_experience = Experience.objects.all()
    my_education = Education.objects.all()
    my_social_link = SocialLink.objects.all()
    my_language = Language.objects.all()
    my_testimonials = Testimonial.objects.all()
    my_personal_info = PersonalInfo.objects.get(user__username = "almastasoyan")
    messageForm = MessageForm()

    my_data = { "personal_info":my_personal_info,
                "skills": my_skills,
                "experiences": my_experience,
                "educations": my_education,
                "social_links":my_social_link,
                "languages": my_language,
                "testimonials": my_testimonials,
                "messageForm":messageForm

            }
    

    return render(request, "index.html", context= my_data)


