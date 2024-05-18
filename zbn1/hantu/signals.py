from django.dispatch import Signal

page_viewed_signal = Signal(providing_args=['request'])
