#!/usr/bin/env python

from collections import OrderedDict

import string
import yaml


def load_yaml():
    with open("companies_that_whiteboard.yml") as yaml_file:
        return yaml.safe_load(yaml_file)


def represent_ordereddict(dumper, data):
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode(u'tag:yaml.org,2002:map', value)


def get_ordered_company(unordered_company):
    order = ['name', 'url', 'glassdoor', 'interview_types']
    ordered_company = OrderedDict()
    for item in order:
        if unordered_company.get(item):
            ordered_company[item] = unordered_company[item]
    return ordered_company


def group_companies_by_name(loaded_yaml):
    grouped_companies = {letter: []
                         for letter in string.ascii_lowercase + string.digits}

    for company in loaded_yaml:
        company_letter = company['name'][0].lower()
        ordered_company = get_ordered_company(company)
        grouped_companies[company_letter].append(ordered_company)

    return grouped_companies


def get_formatted_yaml(group_label, group):
    header = '\n'.join([
        "# %s Companies" % group_label.upper(),
        "# %s.yml" % group_label,
        "\n"
    ])

    if group == []:
        output = '\n'.join([
            "# %s.yml is purposely empty." % group_label,
            "# Feel free to send a PR to populate!",
            "\n",
            "#- name: Company",
            "#  url: http://www.company.com",
            "#  glassdoor: http://www.glassdoor.com/path/to/interview/reviews",
            "#  interview_types:",
            "#  - online_coding_challenge",
            "#  - live_coding",
            "\n",
            "[]"
        ])
        return header + output

    yaml_output = yaml.dump(group, default_flow_style=False)
    yaml_output = yaml_output.replace("- name:", "\n- name:")
    header = '\n'.join([
        "# %s Companies" % group_label.upper(),
        "# %s.yml" % group_label,
        "\n"
    ])
    return header + yaml_output[1:]


def write_grouped_companies(grouped_companies):
    yaml.add_representer(OrderedDict, represent_ordereddict)

    for group_label, group in grouped_companies.items():
        filename = "companies_that_whiteboard/%s.yml" % group_label
        group.sort(key=lambda x: x['name'])
        with open(filename, 'w') as output_file:
            output_file.write(get_formatted_yaml(group_label, group))


def main():
    loaded_yaml = load_yaml()
    grouped_companies = group_companies_by_name(loaded_yaml)
    write_grouped_companies(grouped_companies)


if __name__ == "__main__":
    main()
