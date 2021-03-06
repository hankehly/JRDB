from celery import shared_task

from .templates.template import template_factory


@shared_task
def import_file(path: str) -> str:
    template = template_factory(path)
    template.extract().load()
    return template.path
