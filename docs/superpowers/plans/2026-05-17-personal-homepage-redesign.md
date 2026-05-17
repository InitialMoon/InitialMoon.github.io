# Personal Homepage Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rebuild InitialMoon.github.io into a more distinctive personal homepage centered on research + engineering, with systems research as the current main line, graphics/AI as important prior expertise, and academic CV/publication credibility preserved.

**Architecture:** Do not assume the current Academic Pages template should be kept. First compare replacement templates locally, then either migrate to the selected template or intentionally retain and restyle the current Jekyll site. The likely direction is HugoBlox Academic CV or a minimalist Hugo academic site, because the current Academic Pages design feels too official and stiff.

**Tech Stack:** Current site is Academic Pages / Jekyll / GitHub Pages. Candidate replacement stacks are HugoBlox Academic CV (Hugo), pmichaillat/hugo-website (Hugo), or a React/Next.js research template if the user chooses maximum visual freedom.

---

## Context captured from the planning conversation

- Repository to work in: `/Users/initialmoon/websites/InitialMoon.github.io`
- Public site: `https://initialmoon.github.io/`
- GitHub repository: `InitialMoon/InitialMoon.github.io`
- Current branch at clone time: `master`
- Current repository state at clone time: Academic Pages template, with a newly added `CLAUDE.md` and this handoff plan.
- User wants to preserve current conversation context before switching Claude Code cwd into this repository.

## User-approved positioning

Use this as the content strategy unless the user explicitly changes it.

1. Primary positioning: research + engineering hybrid.
2. Academic identity remains important: the user is a PhD student, so PhD affiliation, advisors, research direction, publications, and CV should stay visible and credible.
3. Portfolio signals also matter: make skills, project outcomes, code links, and contact paths prominent.
4. Do not explicitly say the site is for internships or job seeking.
5. Current main line: systems research, microkernel/OS, performance experimentation, research-grade engineering tools.
6. Important secondary capability: undergraduate graphics/AI background. Present it as meaningful prior expertise, not as a marginal side interest.
7. Engineering/tooling projects should support the impression that the user can build and maintain useful systems.

## Current content audit

The repository currently looks like an Academic Pages template with some real content inserted.

Real or likely real content:

- `_pages/about.md`: short homepage paragraph about being a first-year PhD at Shanghai Jiao Tong University, advised by Prof. Linpeng Huang and Prof. Shengan Zheng, with B.S. from Beijing Institute of Technology in 2025.
- `_pages/cv.md`: education section and generated publications list.
- `_publications/2024-10-28-ANFluid.md`: ANFluid ACM MM 2024 publication entry.
- `files/ANFluid.pdf`: publication PDF.
- `images/profile.jpg`: current sidebar/avatar image.

Known cleanup targets if staying in Jekyll or migrating content:

- `README.md` is still upstream Academic Pages text.
- `_config.yml` has placeholder metadata: title `Profile`, description `personal description`, and likely incorrect `twitter: UniofOxford`.
- `_data/navigation.yml` only enables Publications and CV.
- `_publications/2024-10-28-ANFluid.md` still includes template explanatory text in its body.
- `_pages/cv.md` contains commented Academic Pages example work/skills/service content.
- Template leftovers include example posts, talks, teaching entries, portfolio examples, markdown guide pages, terms page, and many example images.

## Candidate templates and current recommendation

The user disliked the current Academic Pages look: too official, stiff, and generic. Astro/as-folio was suggested but the user was not especially satisfied after a quick search. The user said HugoBlox Academic CV looked acceptable and asked to find more.

Shortlist:

1. **HugoBlox Academic CV** — strongest current candidate. Balanced academic credibility, modular homepage blocks, publications/projects/CV support, and less stiff than Academic Pages.
2. **pmichaillat/hugo-website** — minimalist Hugo academic template. Better if the user wants cleaner typography and less framework/template feel, but it has fewer ready-made academic/project blocks.
3. **tovacinni/research-website-template** — React + Next.js research website. More visual freedom and engineering feel, but higher maintenance/deployment cost and more academic features to build manually.
4. **minimal-light / al-folio** — stable academic alternatives, but likely still too academic-template-like for the user's taste.
5. **GitProfile** — useful as inspiration for GitHub project cards, but not a good main site because academic/research narrative is too weak.

Recommended next decision: clone or otherwise preview HugoBlox Academic CV and pmichaillat/hugo-website locally, then ask the user to pick the base before migrating.

## Proposed site structure

Use this structure conceptually even if the final template names pages differently.

- Home: distinctive hero, research + engineering positioning, selected highlights, quick links.
- Research: current systems/microkernel direction first; graphics/AI prior research as a secondary track.
- Projects: grouped project cards for Systems / Graphics + AI / Engineering Tools.
- Publications: ANFluid, Google Scholar link, and future publication-ready structure.
- CV: education, selected research/project experience, skills, publications, selected projects.
- Contact: email, GitHub, Google Scholar, ORCID, and other confirmed links.

Suggested homepage hero direction:

```text
Yingqi Jie · Systems PhD student building research-grade engineering tools.

I work on microkernel-based systems and performance experimentation, with prior research experience in computer graphics and AI.
```

This text is a starting point, not final copy. Keep the tone confident and specific, not inflated.

## Candidate project/material buckets

Use GitHub/profile data and repository content to validate details before publishing copy.

Systems / OS / performance:

- `CXLOS` — Experimental WASM Microkernel Operating System.
- `Amkos` — OS design for microkernel; fork/background reference.
- `lionsos` — seL4-based OS; fork/background reference.
- `sys-research-toolkit` — shell utilities for Linux system research, kernel experimentation, and performance analysis.
- `pmbench`, `lkp-tests`, `seL4` — performance/kernel experimentation context; be careful distinguishing forks from original work.

Graphics + AI:

- `ANFluid` — ACM MM 2024 publication, Physics-Aware Simulation and Dual-Flow Texture Learning.
- `gauss_density_cuda` — CUDA sampling acceleration module.
- `my_sad_gs`, `gaussian-splatting`, `diff-gaussian-rasterization`, `simple-knn` — graphics/Gaussian Splatting related work; verify authorship/fork status before wording.
- `graphics_basic_OpenGL` — traditional OpenGL pipeline, vector/quaternion implementation, universe animation simulator.

Engineering tools / portfolio signal:

- `remote-server-toolkit` — tmux-based remote experiment management, AI-friendly non-interactive task management.
- `audio-output-guard` — recent Swift utility.
- `RepoAudit` — autonomous LLM-agent for repository-level code auditing; fork status must be checked before wording.
- `remotelab` — self-hosted remote access to agent tools; fork status must be checked.
- `my_linux_config` — Linux config tooling.

## File structure to create or modify after template selection

Do not implement before the template choice is confirmed.

If choosing HugoBlox Academic CV:

- Create/replace Hugo site files in repository root according to HugoBlox structure.
- Preserve old Jekyll content on a migration branch or in git history; do not manually delete without a clear task and status check.
- Create content blocks/pages for home, research, projects, publications, and CV using HugoBlox conventions.
- Move publication data/PDF into the HugoBlox-compatible location.
- Configure GitHub Pages build workflow for Hugo if required.

If choosing pmichaillat/hugo-website:

- Create Hugo config and content pages following that template's structure.
- Build project cards manually because the template is more minimal.
- Configure GitHub Pages build workflow for Hugo if required.

If staying with Academic Pages:

- Modify `_config.yml`, `_data/navigation.yml`, `_pages/about.md`, `_pages/cv.md`, `_pages/publications.md`, `_publications/2024-10-28-ANFluid.md`, and relevant `_sass/` partials.
- Remove or hide template example content only after confirming it is not needed.
- Update `README.md` to describe the personal site rather than Academic Pages upstream instructions.

## Implementation tasks

### Task 1: Preview candidate templates locally

**Files:**
- Create temporary preview directories outside this repository or under a clearly ignored path.
- Do not modify published site content in this task.

- [ ] **Step 1: Check available tooling**

Run:

```bash
hugo version
ruby --version
bundle --version
node --version
npm --version
```

Expected: commands either print versions or clearly identify missing tooling. If Hugo is missing, ask the user before installing anything.

- [ ] **Step 2: Clone candidate templates for preview**

Run from a scratch location such as `/Users/initialmoon/websites/template-previews`:

```bash
git clone https://github.com/HugoBlox/hugo-theme-academic-cv.git hugoblox-academic-cv
git clone https://github.com/pmichaillat/hugo-website.git pmichaillat-hugo-website
```

Expected: both repositories clone successfully.

- [ ] **Step 3: Read each template's README and build instructions**

Read each template's README and any deployment docs. Do not guess commands.

Expected: identify the local preview command for each template.

- [ ] **Step 4: Start local previews one at a time**

Run the documented preview command for HugoBlox first, then for pmichaillat after stopping the first server.

Expected: each preview is accessible locally in the browser.

- [ ] **Step 5: Ask the user to choose the base**

Show the user the preview URLs and summarize the tradeoff:

```text
HugoBlox: more complete academic/project modules, more framework feel.
pmichaillat: cleaner and more personal/minimal, fewer built-in modules.
```

Expected: user chooses one base or asks for more candidates.

### Task 2: Create a migration branch after template choice

**Files:**
- Git branch only.

- [ ] **Step 1: Check working tree status**

Run:

```bash
git -C /Users/initialmoon/websites/InitialMoon.github.io status --short
```

Expected: only intentional planning files are uncommitted, or user-approved changes are present.

- [ ] **Step 2: Ask before branch/destructive changes if needed**

If the tree has user changes that are not part of this planning handoff, ask how to proceed.

Expected: no unapproved work is overwritten.

- [ ] **Step 3: Create a migration branch**

Run:

```bash
git -C /Users/initialmoon/websites/InitialMoon.github.io switch -c redesign-homepage
```

Expected: new branch `redesign-homepage` is active.

### Task 3: Migrate or scaffold the chosen template

**Files:**
- Depends on chosen template.
- Preserve `CLAUDE.md` and this plan.

- [ ] **Step 1: Copy/scaffold chosen template files into this repository**

Use the chosen template's documented setup path. Do not blindly copy `.git` from template previews.

Expected: repository root has the chosen static site structure and keeps `CLAUDE.md` plus `docs/superpowers/plans/2026-05-17-personal-homepage-redesign.md`.

- [ ] **Step 2: Configure site metadata**

Set site title, author name, public URL, and core links using verified information:

```text
Name: Yingqi Jie (介应奇)
Affiliation: Shanghai Jiao Tong University, DDST Lab
Public URL: https://initialmoon.github.io/
GitHub: InitialMoon
Google Scholar: https://scholar.google.com/citations?user=oszvkqEAAAAJ&hl=en
ORCID: https://orcid.org/0009-0004-1674-4984
Email: jieyingqi814@qq.com
```

Expected: no placeholder site metadata remains.

- [ ] **Step 3: Build once before content migration**

Run the selected template's documented build command.

Expected: build succeeds before custom content is added.

### Task 4: Add homepage and narrative content

**Files:**
- Chosen template homepage/content files.

- [ ] **Step 1: Add hero content**

Use this starting copy, adjusted to the selected template's frontmatter/block format:

```markdown
# Yingqi Jie (介应奇)

Systems PhD student building research-grade engineering tools.

I work on microkernel-based systems and performance experimentation at Shanghai Jiao Tong University, with prior research experience in computer graphics and AI.
```

Expected: homepage immediately communicates research + engineering identity.

- [ ] **Step 2: Add research focus section**

Use this structure:

```markdown
## Research Focus

- Microkernel-based system architectures and user-space kernel component design.
- Performance experimentation and tooling for systems research.
- Prior work in computer graphics and AI, including physics-aware animation and Gaussian Splatting/CUDA-related projects.
```

Expected: systems comes first; graphics/AI is meaningful but secondary.

- [ ] **Step 3: Add selected highlights section**

Create three highlight groups:

```markdown
## Selected Highlights

### Systems Research
Microkernel/OS experiments, performance tooling, and system research infrastructure.

### Graphics + AI
ANFluid and undergraduate graphics/AI work, including CUDA and OpenGL projects.

### Engineering Tools
Tools for remote experiments, automation, and developer workflows.
```

Expected: the homepage has balanced but clearly weighted content.

### Task 5: Add projects with careful attribution

**Files:**
- Chosen template project/content/data files.

- [ ] **Step 1: Verify fork/original status before wording**

Run:

```bash
gh repo list InitialMoon --limit 100 --json name,description,primaryLanguage,pushedAt,url,isFork
```

Expected: project wording distinguishes original projects, forks, and derived research experiments.

- [ ] **Step 2: Create Systems project entries**

Include 2-3 systems entries first. Use cautious wording where authorship needs verification:

```markdown
### sys-research-toolkit
A collection of shell utilities for Linux systems research, kernel experimentation, and performance analysis.

### CXLOS
Experimental WASM microkernel operating system work.

### Performance / kernel experimentation
Experiments and tooling around Linux performance tests and microkernel research infrastructure.
```

Expected: no fork is presented as original authorship unless verified.

- [ ] **Step 3: Create Graphics + AI project entries**

Use:

```markdown
### ANFluid
ACM MM 2024 work on animating natural fluid photos using physics-aware simulation and dual-flow texture learning.

### Graphics and Gaussian Splatting experiments
CUDA/OpenGL experiments related to graphics pipelines, Gaussian Splatting, and rendering acceleration.
```

Expected: graphics/AI background is visible and credible.

- [ ] **Step 4: Create Engineering Tools entries**

Use:

```markdown
### remote-server-toolkit
A tmux-based remote experiment management toolkit designed for AI-friendly, non-interactive task management.

### audio-output-guard
A macOS utility for monitoring or controlling audio output behavior.
```

Expected: tool entries support engineering competence without overpowering research identity.

### Task 6: Migrate publication and CV content

**Files:**
- Chosen template publication and CV content files.
- Preserve `files/ANFluid.pdf` or move it according to the template convention.

- [ ] **Step 1: Migrate ANFluid publication**

Use publication metadata from `_publications/2024-10-28-ANFluid.md`:

```text
Title: ANFluid: Animate Natural Fluid Photos base on Physics-Aware Simulation and Dual-Flow Texture Learning
Venue: MM' 24
Date: 2024-10-28
DOI: https://doi.org/10.1145/3664647.3680950
PDF: files/ANFluid.pdf
Citation: Xiangcheng Zhai, Yingqi Jie, Xueguang Xie, Aimin Hao, Na Jiang, and Yang Gao. 2024. ANFluid: Animate Natural Fluid Photos base on Physics-Aware Simulation and Dual-Flow Texture Learning. In Proceedings of the 32nd ACM International Conference on Multimedia (MM '24). Association for Computing Machinery, New York, NY, USA, 3323–3331.
```

Expected: publication page/list renders without template explanatory text.

- [ ] **Step 2: Migrate CV education**

Use:

```markdown
## Education

- Ph.D. Candidate in Computer Science, Shanghai Jiao Tong University, expected 2030.
- B.S. in Software Engineering, Beijing Institute of Technology, 2025.
```

Expected: CV includes education and publications.

- [ ] **Step 3: Add selected skills section**

Use categories rather than a long keyword dump:

```markdown
## Selected Skills

- Systems: microkernel architecture, Linux/kernel experimentation, performance analysis.
- Programming: C/C++, Rust, Python, Shell, CUDA, JavaScript/TypeScript.
- Graphics/AI: OpenGL, Gaussian Splatting-related tooling, research implementation.
- Tooling: tmux-based experiment management, automation, Git/GitHub workflows.
```

Expected: CV supports both academic and portfolio use.

### Task 7: Configure deployment and verify builds

**Files:**
- GitHub Actions workflow if required by chosen template.
- Static site config.

- [ ] **Step 1: Add or update GitHub Pages deployment workflow**

Use the chosen template's documented GitHub Pages workflow. If it requires GitHub Actions rather than default Jekyll, ensure the workflow builds the static output and deploys to Pages.

Expected: workflow matches the selected static generator.

- [ ] **Step 2: Run local build**

Run the selected template's documented build command.

Expected: build exits successfully and emits a static site output directory.

- [ ] **Step 3: Run local preview**

Run the selected template's documented preview command.

Expected: homepage, projects, publications, CV, and contact links are visible locally.

- [ ] **Step 4: Manually inspect UI in browser**

Check:

```text
- Homepage hero reads well.
- Navigation works.
- Project cards have no broken links.
- ANFluid publication links to DOI and PDF.
- CV has no template leftovers.
- The site does not say or imply internship/job seeking.
```

Expected: user-visible pages match the agreed positioning.

### Task 8: Clean old template leftovers after successful migration

**Files:**
- Old Jekyll files if they remain after migration.
- `README.md`.

- [ ] **Step 1: Confirm build passes before cleanup**

Run the selected build command.

Expected: build succeeds before deleting old content.

- [ ] **Step 2: Remove or archive old Academic Pages-only files**

Only remove files that are no longer used by the selected template. Do not remove `files/ANFluid.pdf`, `images/profile.jpg`, `CLAUDE.md`, or `docs/superpowers/plans/2026-05-17-personal-homepage-redesign.md` unless the new template explicitly replaces them and the replacement is verified.

Expected: repository no longer carries unused Academic Pages example pages/assets.

- [ ] **Step 3: Rewrite README**

Replace upstream Academic Pages README with a short repository README explaining:

```markdown
# InitialMoon.github.io

Personal homepage for Yingqi Jie (介应奇), hosted at https://initialmoon.github.io/.

## Development

[Use the selected template's install, build, and preview commands.]
```

Expected: README describes this site, not the upstream template.

### Task 9: Final verification and handoff

**Files:**
- All changed files.

- [ ] **Step 1: Check git status**

Run:

```bash
git -C /Users/initialmoon/websites/InitialMoon.github.io status --short
```

Expected: changed files are intentional.

- [ ] **Step 2: Run final build**

Run the selected final build command.

Expected: build succeeds.

- [ ] **Step 3: Ask user before commit/push**

Do not commit or push unless the user explicitly asks.

Expected: user chooses whether to commit, push, or keep local changes.

## Self-review

- Spec coverage: This plan covers template choice, migration, content strategy, project grouping, publication/CV migration, deployment, cleanup, and verification.
- Placeholder scan: No `TBD`/`TODO` placeholders are used as instructions. Template-specific commands are intentionally deferred until the selected template README is read, because guessing commands would be unsafe.
- Scope check: This is a full homepage migration/redesign. If the chosen template requires extensive customization, split implementation into separate plans for template migration, content migration, and visual polish.
