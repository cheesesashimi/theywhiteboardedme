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
                        {% include glassdoor.html company_name = company.name %}
                    </a>
                </li>
                {% endif %}
            </ul>
        </td>

        {% if company.interview_types %}
        <td class="info-icons">
            <ul class="info-icons">
            {% assign sorted_interview_types = (company.interview_types | sort) %}
            {% for interview_type in sorted_interview_types %}
                <li>
                {% if interview_type == "online_coding_challenge" %}
                    {% include online_coding_challenge.html %}
                {% endif %}
                {% if interview_type == "whiteboarding" %}
                    {% include whiteboarding.html %}
                {% endif %}
                {% if interview_type == "live_coding" %}
                    {% include live_coding.html %}
                {% endif %}
                {% if interview_type == "homework" %}
                    {% include homework.html %}
                {% endif %}
                {% if interview_type == "code_review" %}
                    {% include code_review.html %}
                {% endif %}
                </li>
            {% endfor %}
            </ul>
        </td>
        {% endif %}
    </tr>
{% endfor %}
</table>
