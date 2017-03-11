<table class="companies">
{% assign sorted_companies = (include.companies | sort: 'name') %}
{% for company in sorted_companies %}
    <tr>
        <td class="company-name">
            <a href="{{ company.url }}">{{ company.name }}</a>
        </td>

        <td class="info-icons">
            <ul class="info-icons">
                {% if company.profile %}
                <li>
                    <a title="they.whiteboarded.me profile for {{ company.name }}" href="{{ company.profile }}">&#9432;</a>
                </li>
                {% endif %}

                {% if company.glassdoor %}
                <li>
                    <a title="Glassdoor profile for {{ company.name }}" href="{{ company.glassdoor }}">
                        <img src="/images/glassdoor.svg">
                    </a>
                </li>
                {% endif %}
            </ul>
        </td>

        <td class="info-icons">
            <ul class="info-icons">
            {% assign sorted_interview_types = (company.interview_types | sort) %}
            {% for interview_type in sorted_interview_types %}
                <li>
                {% if interview_type == "online_coding_challenge" %}
                    <img title="Online Coding Challenge" alt="Online Coding Challenge" src="images/puzzle.svg">
                {% endif %}
                {% if interview_type == "whiteboarding" %}
                    <img title="Whiteboarding" alt="Whiteboarding" src="images/whiteboarding.svg">
                {% endif %}
                {% if interview_type == "live_coding" %}
                    <img title="Live Coding" alt="Live Coding" src="images/coding.svg">
                {% endif %}
                {% if interview_type == "homework" %}
                    <img title="Homework" alt="Homework" src="images/homework.svg">
                {% endif %}
                {% if interview_type == "code_review" %}
                    <img title="Code Review" alt="Code Review" src="images/codereview.svg">
                {% endif %}
                </li>
            {% endfor %}
            </ul>
        </td>
    </tr>
{% endfor %}
</table>
