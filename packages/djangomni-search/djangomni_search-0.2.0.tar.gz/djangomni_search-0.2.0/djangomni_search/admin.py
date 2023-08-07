import json
from functools import update_wrapper

from django.urls import reverse

from .views import OmniSearchModelView


class OmniSearchAdminSite:
    def get_omnisearch_model(self, app, model):
        cls = model['model']
        return {
            'app': {
                'name': str(app['name']),
                'label': str(app['app_label']),
                'url': str(app['app_url']),
            },
            'addUrl': str(model['add_url']),
            'adminUrl': str(model['admin_url']),
            'ident': str(cls._meta.model_name),
            'name': str(cls._meta.verbose_name_plural),
            'objectName': str(cls._meta.verbose_name),
        }

    def get_admin_model(self, model):
        return self._registry[model]

    def get_omnisearch_context(self, ctx):
        items = []
        for app in ctx['available_apps']:
            for model in app['models']:
                model_admin = self.get_admin_model(model['model'])
                if model_admin.search_fields:
                    items.append(self.get_omnisearch_model(app, model))
        if len(items) == 0:
            return None
        return {
            'homeUrl': str(ctx['site_url']),
            'models': items,
            'placeholder': str(ctx['site_header']),
            'searchUrl': reverse("admin:omnisearch"),
        }

    def omnisearch_view(self, request):
        return OmniSearchModelView.as_view(admin_site=self)(request)

    def each_context(self, request):
        ctx = super().each_context(request)
        ctx['omni_search'] = json.dumps(self.get_omnisearch_context(ctx))
        return ctx

    def get_urls(self):
        from django.urls import path

        def wrap(view, cacheable=False):
            def wrapper(*args, **kwargs):
                return self.admin_view(view, cacheable)(*args, **kwargs)
            wrapper.admin_site = self
            return update_wrapper(wrapper, view)
        return [
            path("omnisearch/", self.omnisearch_view, name="omnisearch"),
        ] + super().get_urls()
