from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver

from .models import Post, Subscription
from .tasks import get_notification_new_news


@receiver(m2m_changed, sender=Post.category.through)
def news_created(sender, action, pk_set, instance, **kwargs):
    if action != 'post_add':
        return None

    emails = User.objects.filter(subscriptions__category__in=pk_set).values_list('email', flat=True)

    subject = f'Новый пост в одной из категорий, на которые Вы подписаны: {instance.category.all()}'

    text_content = (
        f'Заголовок новости: {instance.title}\n'
        f'Текст новости: {instance.preview()}\n'
        f'Ссылка на новость: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Заголовок новости: {instance.title}\n<br>\n'
        f'Текст новости: {instance.preview()}\n'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на новость</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()


@receiver(post_save, sender=Post)
def send_news_notification(sender, instance, **kwargs):
    if kwargs["created"]:
        instance_id = instance.pk
        subscribers = Subscription.objects.all()
        to_email = [subscriber.user.email for subscriber in subscribers]
        get_notification_new_news.delay(instance_id, to_email)
