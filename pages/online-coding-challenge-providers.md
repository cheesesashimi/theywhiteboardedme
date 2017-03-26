---
layout: page
title: "Automated Coding Challenge Providers"
permalink: online-coding-challenge-providers.html
---

This is a list of companies that provide [automated coding
challenges](/interview_types/online_coding_challenges.html) for job interview
candidates.

{% assign sites = (site.data.online_coding_challenges | sort: 'name') %}
{% for site in sites %}
- [{{site.name}}]({{site.url}})
{% endfor %}
