---
title: ''
summary: 'Systems PhD student building research-grade engineering tools.'
date: 2026-05-17
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      text: ''
      button:
        text: View CV
        url: experience/
      headings:
        about: ''
        education: Education
        interests: Research Interests
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  - block: markdown
    id: research
    content:
      title: Research Focus
      subtitle: Systems research as the current main line, with graphics and AI as prior research depth.
      text: |-
        I work on **microkernel-based system architectures**, especially designs that separate kernel components into user space and make system behavior easier to experiment with, measure, and evolve.

        My current interests include operating-system structure, performance experimentation, and research-grade engineering tools for systems work. During my undergraduate studies, I also worked at the intersection of **computer graphics and AI**, including physics-aware animation and rendering-related implementation.
    design:
      columns: '1'

  - block: markdown
    content:
      title: Selected Highlights
      subtitle: A compact view of the areas I want this site to make legible.
      text: |-
        ### Systems Research
        Microkernel and operating-system experiments, performance tooling, and infrastructure for repeatable systems research.

        ### Graphics + AI
        ANFluid and related undergraduate work on physics-aware visual generation, CUDA/OpenGL implementation, and graphics research prototypes.

        ### Engineering Tools
        Practical tools for remote experiments, automation, and developer workflows that support research iteration.
    design:
      columns: '1'

  - block: collection
    id: papers
    content:
      title: Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: citation

  - block: collection
    content:
      title: Selected Projects
      text: Systems, graphics + AI, and engineering tools selected for research and implementation signal.
      filters:
        folders:
          - projects
      count: 6
    design:
      view: article-grid
      columns: 3
      show_date: false
      show_read_time: false
      show_read_more: false

  - block: markdown
    content:
      title: Contact
      text: |-
        I am reachable by [email](mailto:jieyingqi814@qq.com). You can also find my work on [GitHub](https://github.com/InitialMoon), [Google Scholar](https://scholar.google.com/citations?user=oszvkqEAAAAJ&hl=en), and [ORCID](https://orcid.org/0009-0004-1674-4984).
    design:
      columns: '1'
---
