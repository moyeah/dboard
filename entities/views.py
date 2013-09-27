from django.views.generic.list import ListView
from django.utils import timezone

from dboard.entites import Entity

class EntityListView(ListView):
  model = Entity

  def get_context_data(self, **kwargs):
    context = super(EntityListView, self).get_context_data(**kwargs)
    context['now'] = timezone.now()
    return context
