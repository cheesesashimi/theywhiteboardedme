---
layout: page
title: "Frequently Asked Questions"
permalink: faq.html
---

## What is whiteboarding?
Whiteboarding is the process of asking a candidate to write code on a whiteboard during
a job interview.

## What about live-coding?
Live coding is still considered whiteboarding since a candidate is being asked to produce
code on-the-fly.

## What about online coding challenges?
Online coding challenges are like a virtual whiteboard and have many problems of their own.

## Why is this bad?
Others are able to articulate this thought better, so here are a few links to sites which
describe why whiteboarding and live-coding in general is a bad practice:

<ul>
{% assign sorted_links = (site.data.links | sort: 'author') %}
{% for link in sorted_links %}
    <li><a href="{{ link.url }}">{{ link.name }}</a> ({{ link.author }})</li>
{% endfor %}
</ul>
