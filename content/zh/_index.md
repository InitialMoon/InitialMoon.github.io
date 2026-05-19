---
title: ''
summary: '关注系统研究与研究工程工具的计算机科学博士生。'
date: 2026-05-17
type: landing

sections:
  - block: resume-biography-3
    content:
      username: me
      text: ''
      button:
        text: 查看简历
        url: /zh/experience/
      headings:
        about: ''
        education: 教育经历
        interests: 研究兴趣
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
      title: 研究方向
      subtitle: 以系统研究为当前主线，同时保留图形学与 AI 方向的研究积累。
      text: |-
        我目前关注 **Linux 内核内存管理** 与 **系统性能分析**，尤其是分层内存、NUMA 感知页面迁移，以及基于证据的内核行为分析。

        在当前研究主线之前，我曾在高年级操作系统项目中探索过 **微内核相关系统架构**。本科期间，我也做过 **计算机图形学与 AI** 交叉方向的研究，包括物理感知的图像动画生成和渲染相关实现。
    design:
      columns: '1'

  - block: markdown
    content:
      title: 重点内容
      subtitle: 这个网站希望让访问者快速理解我的研究和工程背景。
      text: |-
        ### 系统研究
        Linux 内核内存管理实验、NUMA 感知页面迁移、性能工具，以及可复现实验所需的系统研究基础设施。

        ### 图形学 + AI
        ANFluid 以及本科阶段围绕物理感知视觉生成和图形学研究原型的工作。

        ### 工程工具
        用于远程实验、自动化、Claude Code 和开发工作流的实用工具，支撑研究迭代。
    design:
      columns: '1'

  - block: collection
    id: papers
    content:
      title: 论文
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: citation

  - block: collection
    content:
      title: 代表项目
      text: 围绕系统、图形学 + AI 和工程工具整理的项目。
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
      title: 联系方式
      text: |-
        可以通过 [邮件](mailto:jieyingqi814@qq.com) 联系我。也可以在 [GitHub](https://github.com/InitialMoon)、[Google Scholar](https://scholar.google.com/citations?user=oszvkqEAAAAJ&hl=en) 和 [ORCID](https://orcid.org/0009-0004-1674-4984) 找到我的更多信息。
    design:
      columns: '1'
---
