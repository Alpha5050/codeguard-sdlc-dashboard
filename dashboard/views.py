
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import SecurityFinding
from .forms import SecurityFindingForm
from .chart_utils import generate_dashboard_chart


@login_required(login_url='/admin/login/')
def finding_list(request):
    all_findings = SecurityFinding.objects.all()
    findings = all_findings

    search = request.GET.get('search', '')
    category = request.GET.get('category', '')
    severity = request.GET.get('severity', '')
    status = request.GET.get('status', '')

    if search:
        findings = findings.filter(
            models.Q(title__icontains=search) |
            models.Q(description__icontains=search)
        )

    if category:
        findings = findings.filter(category=category)

    if severity:
        findings = findings.filter(severity=severity)

    if status:
        findings = findings.filter(status=status)

    context = {
        'findings': findings,
        'total_findings': all_findings.count(),
        'open_findings': all_findings.filter(status='open').count(),
        'critical_findings': all_findings.filter(severity='critical').count(),
        'resolved_findings': all_findings.filter(status='resolved').count(),
        'search': search,
        'selected_category': category,
        'selected_severity': severity,
        'selected_status': status,
        'categories': SecurityFinding.Category.choices,
        'severities': SecurityFinding.Severity.choices,
        'statuses': SecurityFinding.Status.choices,
        'chart': generate_dashboard_chart(),
    }

    return render(request, 'dashboard/finding_list.html', context)


@login_required(login_url='/admin/login/')
def finding_create(request):
    if request.method == 'POST':
        form = SecurityFindingForm(request.POST)

        if form.is_valid():
            finding = form.save(commit=False)
            finding.created_by = request.user
            finding.save()
            return redirect('finding_list')
    else:
        form = SecurityFindingForm()

    return render(request, 'dashboard/finding_form.html', {
        'form': form
    })

@login_required(login_url='/admin/login/')
def finding_edit(request, finding_id):
    finding = get_object_or_404(SecurityFinding, id=finding_id)

    if request.method == 'POST':
        form = SecurityFindingForm(request.POST, instance=finding)

        if form.is_valid():
            form.save()
            return redirect('finding_list')
    else:
        form = SecurityFindingForm(instance=finding)

    return render(request, 'dashboard/finding_form.html', {
        'form': form,
        'editing': True
    })

@login_required(login_url='/admin/login/')
def finding_delete(request, finding_id):
    finding = get_object_or_404(SecurityFinding, id=finding_id)

    if request.method == 'POST':
        finding.delete()
        return redirect('finding_list')

    return render(request, 'dashboard/finding_confirm_delete.html', {
        'finding': finding
    })