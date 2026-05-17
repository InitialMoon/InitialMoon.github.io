---
title: 简历
date: 2026-05-17
type: landing

design:
  spacing: '5rem'

sections:
  - block: resume-experience
    content:
      username: me
    design:
      date_format: '2006 年 1 月'
      is_education_first: true

  - block: resume-skills
    content:
      title: 技能
      username: me

  - block: collection
    content:
      title: 论文
      filters:
        folders:
          - publications
    design:
      view: citation

  - block: resume-languages
    content:
      title: 语言
      username: me
---
