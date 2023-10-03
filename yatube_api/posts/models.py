from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

ROW_LIMIT_TO = 20


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Отслеживаемый человек'
    )

    class Meta:
        constraints = (
            models.UniqueConstraint(fields=('user', 'following', ),
                                    name='unique_follow'),
        )

    def __str__(self):
        return '{followers} подписан на {following}'.format(
            followers=self.user.username,
            following=self.following.username,
        )


class Group(models.Model):

    title = models.CharField('Заголовок текста', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title[:ROW_LIMIT_TO]


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор публикации'
    )
    image = models.ImageField(
        'Фото',
        upload_to='posts/',
        null=True,
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        verbose_name='Группа'
    )

    class Meta:
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:ROW_LIMIT_TO]


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор публикации'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Пост'
    )
    text = models.TextField('Текст')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    def __str__(self):
        return '"{post} {author}" {text}'.format(
            post=self.post,
            author=self.author.username,
            text=self.text[:ROW_LIMIT_TO]
        )
