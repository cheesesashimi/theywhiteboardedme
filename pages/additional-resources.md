---
layout: page
title: "Additional Resources"
---

It can sound very hyperbolic to hear that technical interviews are broken. With
that in mind, here are some articles and videos which support the stance that
current technical interview patterns are broken:

{% assign sorted_links = (site.data.links | sort: 'author') %}
{% for link in sorted_links %}
- [{{ link.name }}]({{ link.url }}){% if link.author %} ({{ link.author }}){% endif %}
{% endfor %}
