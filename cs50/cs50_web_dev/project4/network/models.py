from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm, Textarea

class User(AbstractUser):
    pass
 
class Post(models.Model):
    post = models.CharField(max_length=5000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(User, related_name='users_liked')

    def serialize(self):
        return {
            "post": self.post,
            "users_like": self.users_like.count(),
            "like_button":self.users_like.exists(),
            "input_like":[user.id for user in self.users_like.all()],
        }

class Follows(models.Model):
    user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    user_follows = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)

    # be sure that user follow another user only once
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'user_follows'], name='unique_follow')
        ]

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields= ["post"]
        widgets = {
            "post": Textarea(attrs={"cols": 80, "rows": 2}),
        }