---
layout: page
permalink: /repositories/
title: Repositories
description: A collection of my public GitHub repositories covering CFD, machine learning, OpenFOAM, and more.
nav: true
nav_order: 4
---

{% if site.data.repositories.github_repos %}

## GitHub Repositories

<ul class="repo-list">
  {% for repo in site.data.repositories.github_repos %}
    {% include repository/repo_list.liquid repository=repo %}
  {% endfor %}
</ul>
{% endif %}
