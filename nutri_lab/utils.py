from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
# from xhtml2pdf import pisa


class GeraPDF:

    def render_pdf(self, url_template, contexto={}):
        template = get_template(url_template)
        html = template.render(contexto)
        result = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type="application/pdf")
        return None
