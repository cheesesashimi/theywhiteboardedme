---
layout: page
title: "Frequently Asked Questions"
permalink: faq.html
---

## What is whiteboarding?
Whiteboarding is the practice of asking a technical job interview applicant to
write code to a pet problem, typically on a dry-erase whiteboard. While
originally promoted as a way to inspire conversation about a candidates’
approach to a problem, the use and meaning of whiteboarding has morphed into
“Implement Foo algorithm,” on the whiteboard. This is wrong because it assumes
rote memorization of a given algorithm or the steps needed to solve a particular
problem.

## What is live-coding?
Live-coding is a practice very similar to whiteboarding. The difference is,
a candidate may be able to use a computer. Whether or not they can compile / run
their code depends heavily upon the environment provided to the candidate. Some
companies just use a Google Doc. Others use purpose-built tooling such as
Coderpad, Stypi, etc.

## What are online coding challenges?
An online coding challenge is a coding assignment typically given to a candidate
using an automated platform such as Leetcode, Hackerrank, Codility, et. al.
These require a candidate to complete a given coding problem using their web
browser. Candidate solutions will be ran and verified against the constraints of
the problem using a series of both visible and invisible (to the candidate)
tests.

## Why is whiteboarding / live-coding bad?
Whiteboarding / live-coding is a bad practice because these skills are discrete
from those required for most software engineering positions. These skills
include things like presentation skills, communication skills, etc. This is not
to suggest that those skills are unimportant. However, most whiteboarding
/ live-coding measures those skills as opposed to a candidate’s ability to write
clean, clear and efficient code. As a result, interviewers believe that
a candidate's inability to produce code on a whiteboard correlates with their
ability to produce code on the job.

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

## How do we fix this?
Some companies are beginning to do away with whiteboard interviews. Others are
have developed apprenticeship programs that enable interested people to gain
experience with writing code.

Here is a list of articles that discuss alternative strategies:

<ul>
{% assign sorted_links = (site.data.links | sort: 'author') %}
{% for link in sorted_links %}
    <li><a href="{{ link.url }}">{{ link.name }}</a> ({{ link.author }})</li>
{% endfor %}
</ul>

## What is the mission of they.whiteboarded.me?
To even the field for all tech practitioners, regardless of educational
background, race or ethnicity.

It is no secret that the tech sector is growing at an unprecedented rate,
accelerating every day. With this growth, companies cannot hire candidates fast
enough.

However, many companies will not stop these practices until they have a good
reason for doing so. We, as tech practitioners, must provide them with that
reason. If we slow down the process by refusing to submit to demoralizing
interviews, we have the capability to effect change in our industry. To that
end, this site exists to provide everyone with a list of companies that engage
in these questionable practices.
