---
layout: page
title: "Frequently Asked Questions"
permalink: faq.html
---

## Overview

Others are able to articulate this thought better, so I will provide a few links to sites which describe why
whiteboarding and live-coding in general is a bad practice:

<ul>
{% assign sorted_links = (site.data.links | sort: 'author') %}
{% for link in sorted_links %}
    <li><a href="{{ link.url }}">{{ link.name }}</a> ({{ link.author }})</li>
{% endfor %}
</ul>
