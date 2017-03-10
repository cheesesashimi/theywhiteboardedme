---
layout: page
title: "Companies that whiteboard"
permalink: companies-that-whiteboard.html
---

<div>
{% assign sorted_companies = (site.data.companies_who_whiteboard | sort: 'name') %}
{% for company in sorted_companies %}
    <h3>{{ company.name }}</h3>
    <ul>
    {% assign sorted_interview_types = (company.interview_types | sort) %}
    {% for interview_type in sorted_interview_types %}
        <li>{{ interview_type }}</li>
    {% endfor %}
    </ul>
{% endfor %}
</div>
