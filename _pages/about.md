---
layout: about
title: About
permalink: /
subtitle: CFD Engineer | PhD in Aerospace Engineering

profile:
  align: right
  image: prof_pic.jpg
  image_circular: false # crops the image to make it circular
  more_info: >
    <p>PhD in Aerospace Engineering</p>
    <p>CFD & Thermal Optimization</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false # includes a list of news items
  scrollable: true # adds a vertical scroll bar if there are more than 3 news items
  limit: 5 # leave blank to include all the news in the `_news` folder

latest_posts:
  enabled: false
  scrollable: true # adds a vertical scroll bar if there are more than 3 new posts items
  limit: 3 # leave blank to include all the blog posts
---

<section id="about" class="page-section">

I am a Mechanical Engineer with a PhD in Aerospace Engineering from Cranfield University. With over 10 years of experience in CFD, I specialize in delivering efficient solutions through advanced computational modeling.<br><br>

I work with industry-leading CFD tools to solve challenging fluid dynamics problems and deliver innovative solutions.<br><br>

I am open to CFD consulting projects and research collaborations in thermal optimization, HVAC systems, and multiphysics simulations.<br><br>

<strong>Areas of Expertise:</strong> Computational Fluid Dynamics | Software Development | Rotor Aerodynamics | Data Center Thermal Optimization | HVAC Systems Analysis | Multiphysics Simulations | Thermal Management | Aerodynamic Optimization 

</section>

---

<section id="projects" class="page-section" style="margin-top: 3rem;">

## <a href="/projects/" style="text-decoration: none; color: inherit;">Projects</a>

<div class="projects">
  {% assign sorted_projects = site.projects | sort: "importance" | limit: 6 %}
  <div class="row row-cols-1 row-cols-md-3">
    {% for project in sorted_projects %}
      {% include projects.liquid %}
    {% endfor %}
  </div>
</div>

<p style="text-align: center; margin-top: 2rem;">
  <a href="/projects/" class="btn btn-sm btn-primary">View All Projects →</a>
</p>

</section>

---

<section id="videos" class="page-section" style="margin-top: 3rem;">

## <a href="/videos/" style="text-decoration: none; color: inherit;">Videos</a>

<div class="videos">
  <div class="video-container" style="margin-bottom: 2rem;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
      <iframe
        src="https://www.youtube.com/embed/OG7r4naGCDA"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  </div>

  <div class="video-container" style="margin-bottom: 2rem;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
      <iframe
        src="https://www.youtube.com/embed/iveLvvddVOw"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  </div>

  <div class="video-container" style="margin-bottom: 2rem;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
      <iframe
        src="https://www.youtube.com/embed/nDr7F6_Cw-o"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  </div>

  <div class="video-container" style="margin-bottom: 2rem;">
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
      <iframe
        src="https://www.youtube.com/embed/q3In_bPAPbM"
        style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen>
      </iframe>
    </div>
  </div>
</div>

</section>

---

<section id="publications" class="page-section" style="margin-top: 3rem;">

## <a href="/publications/" style="text-decoration: none; color: inherit;">Publications</a>

{% include bib_search.liquid %}

<div class="publications">
{% bibliography %}
</div>

<p style="text-align: center; margin-top: 2rem;">
  <a href="/publications/" class="btn btn-sm btn-primary">View All Publications →</a>
</p>

</section>

---

<section id="cv" class="page-section" style="margin-top: 3rem;">

## <a href="/cv/" style="text-decoration: none; color: inherit;">CV</a>

<p>View my complete curriculum vitae including education, experience, skills, and achievements.</p>

<p style="text-align: center; margin-top: 2rem;">
  <a href="/cv/" class="btn btn-sm btn-primary">View Full CV →</a>
</p>

</section>

---

<section id="repositories" class="page-section" style="margin-top: 3rem;">

## <a href="/repositories/" style="text-decoration: none; color: inherit;">Repositories</a>

{% if site.data.repositories.github_repos %}

<ul class="repo-list">
  {% for repo in site.data.repositories.github_repos limit:6 %}
    {% include repository/repo_list.liquid repository=repo %}
  {% endfor %}
</ul>
{% endif %}

<p style="text-align: center; margin-top: 2rem;">
  <a href="/repositories/" class="btn btn-sm btn-primary">View All Repositories →</a>
</p>

</section>

---

<section id="hobbies" class="page-section" style="margin-top: 3rem;">

## <a href="/hobbies/" style="text-decoration: none; color: inherit;">Hobbies</a>

### Birdhouse Nesting Videos

A collection of videos documenting the nesting behavior of birds in my backyard birdhouse.

<div class="video-container" style="margin: 2rem 0;">
  <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
    <iframe
      src="https://www.youtube.com/embed/videoseries?list=PLBL_mK5a7wzBTb_kVSYGNeioI1oT9g4l7"
      style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen>
    </iframe>
  </div>
</div>

<p style="text-align: center; margin-top: 2rem;">
  <a href="/hobbies/" class="btn btn-sm btn-primary">View More Hobbies →</a>
</p>

</section>
