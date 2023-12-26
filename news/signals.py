from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Post


@receiver(m2m_changed, sender=Post.category.through)
def news_created(sender, action, pk_set, instance, **kwargs):
    if action != 'post_add':
        return None

    emails = User.objects.filter(subscriptions__category__in=pk_set).values_list('email', flat=True)

    subject = f'Новый товар в категории {instance.category}'

    text_content = (
        f'Заголовок новости: {instance.title}\n'
        f'Ссылка на товар: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Заголовок новости: {instance.title}<br>'
        f'<a href="http://127.0.0.1{instance.get_absolute_url()}">'
        f'Ссылка на товар</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
