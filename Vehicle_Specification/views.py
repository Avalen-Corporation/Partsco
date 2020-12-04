from django.shortcuts import render

# Create your views here.

class ShopView(TemplateView):
    template_name = "product-grid-left-sidebar.html"

    def categories_l1(self):
        return models.CategoryL1.objects.all()

    def vehicle_makes(self):
        return models.VehicleMake.objects.all()

    def parts(self):
        category1 = self.request.GET.get('category1')
        category2 = self.request.GET.get('category2')
        category3 = self.request.GET.get('category3')
        vehicle_make = self.request.GET.get('make')
        vehicle_model = self.request.GET.get('model')
        vehicle_year = self.request.GET.get('year')
        page = self.request.GET.get('page')

        objects = models.Part.objects.all()
        if vehicle_make:
            objects = objects.filter(compatibility__model__make__id=vehicle_make).distinct()
        if vehicle_model:
            objects = objects.filter(compatibility__model__id=vehicle_model).distinct()
        #if vehicle_year:
            #objects = objects.filter(compatibility__model__id=vehicle_model).distinct()

        if category3:
            objects = objects.filter(category_l3__slug=category3).distinct()
        elif category2:
            objects = objects.filter(category_l2__slug=category2).distinct()
        elif category1:
            objects = objects.filter(category_l1__slug=category1).distinct()

        paginator = Paginator(objects, 12)
        try:
            objects = paginator.page(page)
        except InvalidPage:
            objects = paginator.page(1)

        return objects


class ShopDetailView(TemplateView):
    template_name = "single-product.html"

    def part(self):
        return get_object_or_404(models.Part, slug=self.kwargs['slug'])


