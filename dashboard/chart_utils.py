
import base64
from io import BytesIO

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from django.db.models import Count

from .models import SecurityFinding


def generate_dashboard_chart():

    figure, axes = plt.subplots(1, 3, figsize=(15, 4))

    charts = [
        (
            SecurityFinding.objects.values('severity').annotate(total=Count('id')),
            SecurityFinding.Severity.choices,
            'Findings by Severity',
            ['#A62C2C', '#D65A4A', '#E5AE45', '#4B9665', '#9AA49B']
        ),
        (
            SecurityFinding.objects.values('category').annotate(total=Count('id')),
            SecurityFinding.Category.choices,
            'Findings by SDLC Area',
            ['#355E3B', '#527D57', '#719477', '#91AA92', '#B0C2AE']
        ),
        (
            SecurityFinding.objects.values('status').annotate(total=Count('id')),
            SecurityFinding.Status.choices,
            'Findings by Status',
            ['#D9A441', '#5681B2', '#368458', '#929B93']
        ),
    ]

    for axis, (queryset, choices, title, colors) in zip(axes, charts):

        totals = {
            item['severity' if title == 'Findings by Severity'
                 else 'category' if title == 'Findings by SDLC Area'
                 else 'status']: item['total']
            for item in queryset
        }

        labels = [label for value, label in choices]
        values = [totals.get(value, 0) for value, label in choices]

        bars = axis.bar(labels, values, color=colors)

        axis.set_title(title, fontsize=11, fontweight='bold')
        axis.tick_params(axis='x', rotation=25, labelsize=8)
        axis.set_ylim(0, max(values + [1]) * 1.25)
        axis.bar_label(bars, padding=3, fontsize=9)

        axis.spines['top'].set_visible(False)
        axis.spines['right'].set_visible(False)

    figure.tight_layout()

    buffer = BytesIO()
    figure.savefig(buffer, format='png', dpi=120, bbox_inches='tight')
    plt.close(figure)

    buffer.seek(0)

    return base64.b64encode(buffer.getvalue()).decode('utf-8')
