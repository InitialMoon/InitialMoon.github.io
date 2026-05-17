# HugoBlox Bilingual Site Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Enable HugoBlox's built-in multilingual support so the existing English site remains the default and a Chinese core site is available at `/zh/` with a visible language switcher.

**Architecture:** Use Hugo/HugoBlox native multilingual content directories, not a custom JavaScript toggle. Keep current English content at `content/`, add Chinese equivalents under `content/zh/`, and enable language switcher UI through HugoBlox configuration. Chinese content covers the homepage, CV/experience page, publications index + ANFluid page, and projects index + project pages.

**Tech Stack:** Hugo v0.161.1 extended, HugoBlox Academic CV, YAML config, Markdown content, pnpm/Pagefind build.

---

## File structure

- Modify `config/_default/languages.yaml`: add Chinese language `zh` with `contentDir: content/zh`, localized title/description, and Chinese navigation menu.
- Modify `config/_default/params.yaml`: set `hugoblox.header.language_switcher: true` and `hugoblox.footer.language_switcher: true` so HugoBlox shows built-in language switching.
- Create `content/zh/_index.md`: Chinese homepage using the same HugoBlox landing blocks as the English homepage.
- Create `content/zh/experience.md`: Chinese CV page with the same resume blocks as English.
- Create `content/zh/publications/_index.md`: Chinese publications index.
- Create `content/zh/publications/anfluid/index.md`: Chinese ANFluid publication page.
- Create `content/zh/publications/anfluid/cite.bib`: copy of the English ANFluid BibTeX so cite metadata stays available in Chinese.
- Create `content/zh/projects/_index.md`: Chinese projects index.
- Create one Chinese project file for each existing project under `content/zh/projects/<slug>/index.md`.
- Verify generated pages: `/`, `/zh/`, `/publications/anfluid/`, `/zh/publications/anfluid/`, `/projects/`, `/zh/projects/`, `/experience/`, `/zh/experience/`.

## Task 1: Add multilingual configuration

**Files:**
- Modify: `config/_default/languages.yaml`
- Modify: `config/_default/params.yaml`

- [ ] **Step 1: Run expected-failing language output check**

Run:

```bash
test -f public/zh/index.html
```

Expected: command exits non-zero because Chinese output has not been generated yet.

- [ ] **Step 2: Replace `config/_default/languages.yaml` with bilingual config**

Write this exact file:

```yaml
# Languages
# Documentation: https://docs.hugoblox.com/reference/language/

en:
  locale: en-us

zh:
  locale: zh-Hans
  contentDir: content/zh
  title: Yingqi Jie | 介应奇
  params:
    description: 介应奇的个人主页，展示系统研究、微内核相关实验、研究工程工具，以及图形学与 AI 方向的过往研究。
  menu:
    main:
      - name: 首页
        url: /zh/
        weight: 10
      - name: 研究
        url: /zh/#research
        weight: 20
      - name: 论文
        url: /zh/publications/
        weight: 30
      - name: 项目
        url: /zh/projects/
        weight: 40
      - name: 简历
        url: /zh/experience/
        weight: 50
```

- [ ] **Step 3: Enable HugoBlox built-in language switchers**

In `config/_default/params.yaml`, change the header language switcher block from:

```yaml
    language_switcher: false
```

under `hugoblox.header` to:

```yaml
    language_switcher: true
```

Also change the footer language switcher block from:

```yaml
    language_switcher: false
```

under `hugoblox.footer` to:

```yaml
    language_switcher: true
```

- [ ] **Step 4: Run build to verify config is syntactically valid**

Run:

```bash
HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890 ALL_PROXY=socks5://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 GOPROXY=https://proxy.golang.org,direct HUGO_CACHEDIR=/Users/initialmoon/websites/template-previews/.hugo_cache hugo --minify
```

Expected: Hugo build succeeds. It may not generate meaningful Chinese pages until Task 2 adds `content/zh`.

## Task 2: Add Chinese homepage and CV

**Files:**
- Create: `content/zh/_index.md`
- Create: `content/zh/experience.md`

- [ ] **Step 1: Create Chinese content directory**

Run:

```bash
mkdir -p content/zh
```

Expected: directory exists.

- [ ] **Step 2: Create `content/zh/_index.md`**

Write this exact file:

```markdown
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
        我目前关注 **微内核相关的系统架构**，尤其是如何将传统内核组件拆分到用户态，并让系统行为更容易被实验、测量和演化。

        现在的兴趣包括操作系统结构、性能实验，以及支撑系统研究的工程工具。 本科期间，我也做过 **计算机图形学与 AI** 交叉方向的研究，包括物理感知的图像动画生成和渲染相关实现。
    design:
      columns: '1'

  - block: markdown
    content:
      title: 重点内容
      subtitle: 这个网站希望让访问者快速理解我的研究和工程背景。
      text: |-
        ### 系统研究
        微内核、操作系统实验、性能工具，以及可复现实验所需的系统研究基础设施。

        ### 图形学 + AI
        ANFluid 以及本科阶段围绕物理感知视觉生成、CUDA/OpenGL 实现和图形学研究原型的工作。

        ### 工程工具
        用于远程实验、自动化和开发工作流的实用工具，支撑研究迭代。
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
```

- [ ] **Step 3: Create `content/zh/experience.md`**

Write this exact file:

```markdown
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
```

- [ ] **Step 4: Build and verify Chinese homepage/CV outputs**

Run:

```bash
HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890 ALL_PROXY=socks5://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 GOPROXY=https://proxy.golang.org,direct HUGO_CACHEDIR=/Users/initialmoon/websites/template-previews/.hugo_cache hugo --minify
```

Expected: build succeeds.

Run:

```bash
test -f public/zh/index.html && test -f public/zh/experience/index.html
```

Expected: command exits 0.

## Task 3: Add Chinese publications

**Files:**
- Create: `content/zh/publications/_index.md`
- Create: `content/zh/publications/anfluid/index.md`
- Create: `content/zh/publications/anfluid/cite.bib`

- [ ] **Step 1: Create Chinese publication directory**

Run:

```bash
mkdir -p content/zh/publications/anfluid
```

Expected: directory exists.

- [ ] **Step 2: Create `content/zh/publications/_index.md`**

Write this exact file:

```markdown
---
title: 论文
cms_exclude: true
view: citation
banner:
  caption: ''
  image: ''
---
```

- [ ] **Step 3: Create `content/zh/publications/anfluid/index.md`**

Write this exact file:

```markdown
---
title: 'ANFluid: 基于物理感知模拟与双流纹理学习的自然流体照片动画生成'

authors:
  - Xiangcheng Zhai
  - me
  - Xueguang Xie
  - Aimin Hao
  - Na Jiang
  - Yang Gao

date: '2024-10-28T00:00:00Z'
publishDate: '2024-10-28T00:00:00Z'
publication_types: ['paper-conference']
publication: 发表在 *Proceedings of the 32nd ACM International Conference on Multimedia (MM '24)*
publication_short: *ACM MM 2024*

abstract: ANFluid 提出了一种从单张静态图像生成自然流体动画的框架，结合物理感知模拟和双流纹理学习。物理感知模拟用于增强运动的物理一致性，双流纹理学习则通过自监督训练提升纹理预测和内容对齐效果。该方法在不增加模型参数的情况下提升了动画质量，并支持面向动态内容创作的交互式编辑。
summary: ACM MM 2024 论文，研究如何通过物理感知模拟和双流纹理学习从自然流体照片生成动画。

tags:
  - 计算机图形学
  - AI
  - 流体动画
  - 物理感知模拟

featured: true

hugoblox:
  ids:
    doi: 10.1145/3664647.3680950

links:
  - type: pdf
    url: /uploads/ANFluid.pdf
  - type: source
    url: https://doi.org/10.1145/3664647.3680950

image:
  caption: ''
  focal_point: ''
  preview_only: true

projects: []
slides: ''
---

ANFluid 关注如何从单张静态自然流体图片生成动态动画。方法结合了用于物理合理运动建模的 physics-aware simulation，以及用于提升纹理预测和内容对齐的 dual-flow texture learning。

Citation: Xiangcheng Zhai, Yingqi Jie, Xueguang Xie, Aimin Hao, Na Jiang, and Yang Gao. 2024. ANFluid: Animate Natural Fluid Photos base on Physics-Aware Simulation and Dual-Flow Texture Learning. In Proceedings of the 32nd ACM International Conference on Multimedia (MM '24). Association for Computing Machinery, New York, NY, USA, 3323–3331.
```

- [ ] **Step 4: Copy citation file**

Run:

```bash
cp content/publications/anfluid/cite.bib content/zh/publications/anfluid/cite.bib
```

Expected: `content/zh/publications/anfluid/cite.bib` exists.

- [ ] **Step 5: Build and verify Chinese publication output**

Run:

```bash
HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890 ALL_PROXY=socks5://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 GOPROXY=https://proxy.golang.org,direct HUGO_CACHEDIR=/Users/initialmoon/websites/template-previews/.hugo_cache hugo --minify
```

Expected: build succeeds.

Run:

```bash
test -f public/zh/publications/index.html && test -f public/zh/publications/anfluid/index.html
```

Expected: command exits 0.

## Task 4: Add Chinese projects

**Files:**
- Create: `content/zh/projects/_index.md`
- Create: `content/zh/projects/sys-research-toolkit/index.md`
- Create: `content/zh/projects/microkernel-experiments/index.md`
- Create: `content/zh/projects/anfluid/index.md`
- Create: `content/zh/projects/graphics-cuda/index.md`
- Create: `content/zh/projects/remote-server-toolkit/index.md`
- Create: `content/zh/projects/audio-output-guard/index.md`

- [ ] **Step 1: Create Chinese project directories**

Run:

```bash
mkdir -p content/zh/projects/sys-research-toolkit content/zh/projects/microkernel-experiments content/zh/projects/anfluid content/zh/projects/graphics-cuda content/zh/projects/remote-server-toolkit content/zh/projects/audio-output-guard
```

Expected: directories exist.

- [ ] **Step 2: Create `content/zh/projects/_index.md`**

Write this exact file:

```markdown
---
title: 项目
date: 2026-05-17
type: landing

sections:
  - block: collection
    content:
      title: 代表项目
      text: 按系统研究、图形学 + AI 和工程工具整理的项目。对于 fork 或参考实现，只作为研究和实验上下文呈现，不作为原创项目表述。
      filters:
        folders:
          - projects
    design:
      view: article-grid
      fill_image: false
      columns: 3
      show_date: false
      show_read_time: false
      show_read_more: false
---
```

- [ ] **Step 3: Create Chinese project entries**

Write these exact files.

`content/zh/projects/sys-research-toolkit/index.md`:

```markdown
---
title: sys-research-toolkit
date: 2026-04-08
links:
  - type: code
    url: https://github.com/InitialMoon/sys-research-toolkit
tags:
  - 系统
  - 性能
  - 工具
---

面向 Linux 系统研究、内核实验和性能分析的一组 shell 脚本与实用工具。

<!--more-->

这个项目用于支持可复现的系统实验，将 Linux、内核工作流和性能测量中常用的命令行工具整理到一起。
```

`content/zh/projects/microkernel-experiments/index.md`:

```markdown
---
title: 微内核与操作系统实验
date: 2025-09-17
links:
  - type: code
    url: https://github.com/InitialMoon/CXLOS
tags:
  - 系统
  - 操作系统
  - 微内核
---

围绕微内核操作系统、用户态系统组件和性能导向 OS 研究基础设施的实验与学习。

<!--more-->

这一方向包括原创系统工具，也包括对 CXLOS、Amkos、lionsos、seL4、pmbench 和 lkp-tests 等 fork 或参考项目的研究与实验。fork 仓库在这里作为研究上下文呈现，不写作原创项目。
```

`content/zh/projects/anfluid/index.md`:

```markdown
---
title: ANFluid
date: 2024-10-28
links:
  - type: site
    url: /zh/publications/anfluid/
  - type: pdf
    url: /uploads/ANFluid.pdf
tags:
  - 图形学
  - AI
  - 论文
---

ACM MM 2024 工作，研究如何通过物理感知模拟和双流纹理学习生成自然流体照片动画。

<!--more-->

ANFluid 是这个网站上主要的图形学 + AI 论文项目，体现了我本科阶段在图形学研究和研究实现方面的积累。
```

`content/zh/projects/graphics-cuda/index.md`:

```markdown
---
title: 图形学与 CUDA 实验
date: 2024-08-08
links:
  - type: code
    url: https://github.com/InitialMoon/gauss_density_cuda
tags:
  - 图形学
  - CUDA
  - 渲染
---

与图形管线、Gaussian Splatting 和渲染加速相关的 CUDA/OpenGL 实验。

<!--more-->

这一组包括 gauss_density_cuda、graphics_basic_OpenGL 等原创实现，也包括围绕 Gaussian Splatting 参考实现的学习和实验。fork 仓库只作为相关研究上下文呈现。
```

`content/zh/projects/remote-server-toolkit/index.md`:

```markdown
---
title: remote-server-toolkit
date: 2026-05-10
links:
  - type: code
    url: https://github.com/InitialMoon/remote-server-toolkit
tags:
  - 工具
  - 实验
  - 自动化
---

一个基于 tmux 的远程实验管理工具，面向 AI 友好的非交互式任务管理。

<!--more-->

这个工具用于支持远程实验工作流，让任务可以在不依赖交互式终端状态的情况下被启动、查看和控制。
```

`content/zh/projects/audio-output-guard/index.md`:

```markdown
---
title: audio-output-guard
date: 2026-05-16
links:
  - type: code
    url: https://github.com/InitialMoon/audio-output-guard
tags:
  - 工具
  - macOS
  - Swift
---

一个用于监控和控制音频输出行为的 macOS Swift 小工具。

<!--more-->

这个项目作为小型工程工具展示，体现研究主线之外的实用工具开发能力。
```

- [ ] **Step 4: Build and verify Chinese project output**

Run:

```bash
HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890 ALL_PROXY=socks5://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 GOPROXY=https://proxy.golang.org,direct HUGO_CACHEDIR=/Users/initialmoon/websites/template-previews/.hugo_cache hugo --minify
```

Expected: build succeeds.

Run:

```bash
test -f public/zh/projects/index.html && test -f public/zh/projects/sys-research-toolkit/index.html && test -f public/zh/projects/anfluid/index.html
```

Expected: command exits 0.

## Task 5: Final verification and local preview

**Files:**
- All changed files from Tasks 1-4.

- [ ] **Step 1: Run final full build with search indexing**

Run:

```bash
HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890 ALL_PROXY=socks5://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 GOPROXY=https://proxy.golang.org,direct HUGO_CACHEDIR=/Users/initialmoon/websites/template-previews/.hugo_cache pnpm run build
```

Expected: Hugo build succeeds and Pagefind indexes pages.

- [ ] **Step 2: Check expected bilingual output files**

Run:

```bash
test -f public/index.html && test -f public/zh/index.html && test -f public/publications/anfluid/index.html && test -f public/zh/publications/anfluid/index.html && test -f public/projects/index.html && test -f public/zh/projects/index.html && test -f public/experience/index.html && test -f public/zh/experience/index.html
```

Expected: command exits 0.

- [ ] **Step 3: Check expected Chinese content appears**

Run:

```bash
grep -R "研究方向\|代表项目\|ANFluid\|简历" -n public/zh/index.html public/zh/projects/index.html public/zh/publications/anfluid/index.html public/zh/experience/index.html | head -80
```

Expected: output includes Chinese homepage, project, publication, and CV text.

- [ ] **Step 4: Check no obvious template leftovers or job-seeking framing**

Run:

```bash
grep -R "Dr. Alex Johnson\|Meta AI\|Pandas\|PyTorch\|scikit-learn\|Build your own academic website\|Moonshot team\|GoOwnable\|Your Name\|internship\|job seeking\|hired\|offers" -n content data config README.md public 2>/dev/null | head -80
```

Expected: no output.

- [ ] **Step 5: Start local preview server**

Run:

```bash
HTTPS_PROXY=http://127.0.0.1:7890 HTTP_PROXY=http://127.0.0.1:7890 ALL_PROXY=socks5://127.0.0.1:7890 https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890 GOPROXY=https://proxy.golang.org,direct HUGO_CACHEDIR=/Users/initialmoon/websites/template-previews/.hugo_cache hugo server --disableFastRender --bind 127.0.0.1 --port 1316 --baseURL http://127.0.0.1:1316/
```

Expected: server starts and prints a local URL.

- [ ] **Step 6: Verify key preview URLs respond**

Run:

```bash
curl -I --max-time 10 http://127.0.0.1:1316/ && curl -I --max-time 10 http://127.0.0.1:1316/zh/ && curl -I --max-time 10 http://127.0.0.1:1316/zh/projects/ && curl -I --max-time 10 http://127.0.0.1:1316/zh/publications/anfluid/ && curl -I --max-time 10 http://127.0.0.1:1316/zh/experience/
```

Expected: every response is HTTP 200.

## Self-review

- Spec coverage: The plan enables HugoBlox multilingual config, creates Chinese homepage/CV/publication/project pages, enables built-in language switching, and verifies build/preview.
- Placeholder scan: No TBD/TODO/fill-in placeholders remain; every content file has exact content.
- Scope check: This is a focused bilingual-site change, not a broader redesign.
- TDD/verification: Each task starts or ends with a concrete failing/passing check. For static content, build and generated-file checks serve as the automated tests.
