from django.contrib import admin
from .models import Skill, Experience, Education, PersonalInfo, SocialLink, Language, Testimonial, Message


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["company_name", "job_possition","starte_date", "end_date"]
    list_filter = ["company_name"]
    search_fields = ["name"]


class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value"]
    list_filter = ["value"]
    search_fields = ["name"]


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "grade", "start_date", "end_date"]
    list_filter = ["university_name"]
    

class PersonalInfoAdmin(admin.ModelAdmin):
    pass




class SocialLinkAdmin(admin.ModelAdmin):
    
    pass



class LanguageAdmin(admin.ModelAdmin):

    list_display = ["name"]


class TestimonialsAdmin(admin.ModelAdmin):

    list_display =["testimonial_name", "testimonial_job_possition"]
    search_fields = ["testimonial_name", "testimonial_job_possition"]

class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience,ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(PersonalInfo, PersonalInfoAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Testimonial, TestimonialsAdmin)
admin.site.register(Message, MessageAdmin)



