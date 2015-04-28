from random import randrange
from forum.models import QuestionAsked, Thread
from django.contrib.auth.models import User

sample = "ABCDEFGHIJKLMNabcdefgzxnmlkpoi123456789"
try:
    thread = Thread.objects.get(type='modern')
except:
    thread = Thread.objects.create(type='modern', description="modern hunt")
try:
    user = User.objects.get(username='user4')
except:
    user = User.objects.create_user(username='user4', password='user')

def make_title(size, sample):
    title = ""
    for i in range(size):
        title += sample[randrange(0,len(sample))]
    return title

def make_description(size, sample):
    description = ""
    for i in range(size):
        description += sample[randrange(0, len(sample))]

    return description

text1 = "Vis ne nonumy aliquid sapientem. Ut has consul ceteros, et pri sonet dolor. Nullam noster veritus in nam. Id mei docendi noluisse voluptua. Ad possit scripta accumsan nec, vim ad volutpat consulatu. Sit graeco hendrerit te, ut gubergren pertinacia ius. Omnes graecis ocurreret et vel. Vis cu modo justo feugait, nostro incorrupte vix no. Eu nec percipit evertitur, ea omnes decore vidisse per, per elit malorum cu. Usu in eros duis. Et nam mandamus disputando. Est id feugiat patrioque, eu has ornatus phaedrum salutandi. Ad ius probo graeco meliore, mei ut solum minimum vivendum."

text2 = "Ea mei vocibus mediocritatem, laoreet commune intellegebat te vel, no zril prompta numquam pri. Qui odio iriure vocibus an, an feugiat deseruisse eos. At nam veri causae, latine equidem ex sed. Et veri voluptua corrumpit duo. Amet bonorum similique ea duo, dolor dictas cu has. Quo vocibus argumentum scriptorem ei, qui ex vocent labores."

text3 = "An eripuit propriae eam, dignissim mediocritatem per ex. Pri cu inermis legendos, id vero nemore nam. Te mea saperet eleifend, no sit noster iisque scripta, ancillae atomorum salutandi ad vim. Pertinacia democritum constituam mel ex, ea prima facilisi forensibus nec, pro epicuri accusamus id. Est ea tota albucius ocurreret."

title = 'This is sample post with some random latin text. It will make our posts look good.'

text = [text1, text2, text3]
for i in range(5):
    # title = make_title(randrange(8,20), sample)
    # description = make_description(randrange(15,30), sample)
    description = text[randrange(0,3)]
    post = QuestionAsked(title = title, description = description, user = user, thread = thread)
    post.save()