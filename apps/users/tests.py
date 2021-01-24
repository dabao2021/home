from django.test import TestCase
# Create your tests here.
new_comment_art = ['1','2','3','2','3','4']
new_art = []
for i in new_comment_art:
      new_art = new_art.append(i)
      if i in new_art:  # new_art_obj = models.Article.objects.filter(id=i.id)#.values('title','id','image','add_time','click_num')
            continue
      else:
            new_art = new_art.append(i)
print(11111111, new_art)