from django.utils import timezone

import os
from django.utils.timezone import localtime
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    visitors = Visit.objects.filter(leaved_at=None).all()
    for visitor in visitors:
        time_in = localtime(visitor.entered_at)
        time_now = timezone.now().replace(microsecond=0)
        delta = time_now - time_in

        print(f'Зашёл в хранилище, время по Москве:\n{time_in}')
        print(f'Находится в хранилище:\n{delta}')
