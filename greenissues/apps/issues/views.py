from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
import datetime
from apps.issues.models import Issues
from apps.issues.models import Solutions


def index(request):
    latest_issue_list = Issues.objects.order_by('-created_date')[:5]
    paginator = Paginator(latest_issue_list, 2)

    try:
        page = int(request.GET.get('page', 1))
        latest_issue_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        latest_issue_list = paginator.page(1)

    return render_to_response("issues/list.html", locals())


def detail(request, issue_id):
    issue = get_object_or_404(Issues, pk=issue_id)
    solutions = issue.solutions_set.all()

    return render_to_response("issues/detail.html", locals())


def add_solution(request, issue_id):
    issue = get_object_or_404(Issues, pk=issue_id)
    content = request.POST['new_solution']
    solution = Solutions(issue=issue,
                         content=content,
                         rate=2,
                         resolved_by='donny',
                         resolved_date=datetime.datetime.now())

    solution.save()

    return HttpResponseRedirect(reverse('detail', args=(issue.id,)))
