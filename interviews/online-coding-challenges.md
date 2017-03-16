---
layout: page
title: "Online Coding Challenges"
permalink: "interview_types/online_coding_challenges.html"
---

## What are online coding challenges?
An online coding challenge is a coding assignment typically given to a candidate
using an automated platform such as Leetcode, Hackerrank, Codility, et. al.

These require a candidate to complete a given coding problem using their web
browser. Candidate solutions are ran and verified against problem constraints
using a series of visible and invisible (to the candidate) tests.

## What benefits do online coding challenges have?
They allow companies to inexpensively screen candidates as a precursor to
a phone screen / onsite interview.

## Why are online coding challenges bad?
Online coding challenges limit your ability to ask questions about the problem
to determine scope / approach / etc. This is crucial because some of these
problems are very poorly worded. You also gain a countdown timer ticking away
next to your code as well as hidden test cases that aren't run until after you
press "Submit". Testing your solution forces you to use a web form or some
foreign syntax to specify your test cases.

Experienced engineers often tailor their dev environments and editors to their
specific tastes and preferences. Asking a candidate to code in something other
than their preferred editor with their preferred config / plugins will cause
them to slow down dramatically. When you're being timed to complete something,
this feels like an unnecessary handicap.

These can also introduce ableist bias. For example, if you require a screen
reader, the interview platform you're using may not work well with screen
readers. If you require an alternative input device, you might not be able to
enter code as quickly as someone who can use a standard keyboard / mouse.

Lastly, these can introduce participation bias. For example, if you have
out-of-work obligations such as caring for a family, you may not necessarily
have the availability of uninterrupted time necessary to complete a coding
challenge. Some can take up to several hours.

## Who provides online coding challenges?
Some companies such as Google and Uber provide their own. Others use an
off-the-shelf coding evaluation site such as:

{% assign sites = (site.data.online_coding_challenges | sort: 'name') %}
{% for site in sites limit:3 %}
- [{{site.name}}]({{site.url}})
{% endfor %}

Complete list available [here](/online-coding-challenge-providers.html).

## I'd like more information.
Check out these [additional resources](/additional-resources.html) for more information.
