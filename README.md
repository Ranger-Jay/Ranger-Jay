<div align="center">

<img src="https://github.com/Ranger-Jay/Ranger-Jay/raw/main/jay-gh-bg.jpg" alt="Jay — Full Stack Developer & Film Director" />

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?logo=linkedin&logoColor=white&style=for-the-badge)](https://www.linkedin.com/in/WebDevJayR)
[![Twitter](https://img.shields.io/badge/@WebDev__Jay__R-000000?logo=x&logoColor=white&style=for-the-badge)](https://twitter.com/WebDev_Jay_R)

</div>

# 📖 About Me

**Full Stack Developer · Film Director · Building AI production tooling**

I direct film, I write code, and lately those two things have collapsed into one job.
I'm currently directing a thriller/horror feature using a multi-agent AI production
pipeline — and building the tooling I kept wishing existed while making it.

Dedicated learner on a mission to have no untapped potential. **All-in** and committed to
the craft. I enjoy exploring new technologies and using them to solve problems. Aside from
that, I'm fond of mentoring new teammates, camping, traveling, and seeing people achieve
goals. It just...does something for me.

Like my stuff? Let's collab — fork and star ⭐

---

# 🚧 Currently Building

### Guided prompt builder for AI image & video generation

A structured prompt tool for AI generation platforms. Two ideas the existing tools don't have:

**Blocks.** Prompts are assembled from structured components — Subject, Camera, Lighting,
Style, Setting, Action, Sound, Negative, and Anchor — instead of typed freehand. Every
option maps to tested prompt language, so the label you click is never the text sent to
the model.

**Prompt Check.** Before you spend a credit, it tells you which parts of your prompt are
likely to fail, how badly, and what to do instead. Twenty detection rules graded against
published benchmark data and my own platform testing.

| Severity | Meaning |
|---|---|
| Expect failure | under 15% measured success |
| Unreliable | 15–50% |
| Worth knowing | 50–75% |

Built as a single dependency-free HTML file — no framework, no build step. Currently at v8.
Supports 44 image and video platforms.

### WAD — thriller/horror feature

Directing, running an AI-assisted production pipeline across image generation, video
generation, and voice.

---

# 🔬 What I've been learning the hard way

Findings from live generation testing that shaped the tool:

- **Attribute binding is the wall.** Assigning different properties to different parts of
  one subject — brown front legs, white hind legs — fails consistently. Models scatter the
  attributes instead of binding them. No prompt structure fixes it.
- **Conflicting styles don't get rejected, they bleed.** Photorealistic + Synthwave doesn't
  drop one. It applies the stylized treatment to whatever emits light — firelight, neon,
  screens.
- **Held objects float.** "In its mouth" renders as hovering-near-the-face unless you
  describe the grip itself.
- **Camera moves are reliable.** A 180° orbit executes accurately and lands where you asked.

---

# 🛠️ Stack

**Core**

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" title="HTML5" alt="HTML5" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-plain-wordmark.svg" title="CSS3" alt="CSS3" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" title="JavaScript" alt="JavaScript" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg" title="Python" alt="Python" width="40" height="40"/>&nbsp;
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" title="React" alt="React" width="40" height="40"/>&nbsp;

**Tools**

![Node.js](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Firebase](https://img.shields.io/badge/firebase-%23039BE5.svg?style=for-the-badge&logo=firebase&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![NPM](https://img.shields.io/badge/NPM-%23CB3837.svg?style=for-the-badge&logo=npm&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![VS Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

**AI production pipeline**

![Claude](https://img.shields.io/badge/Claude-D97757?style=for-the-badge&logo=anthropic&logoColor=white)
![Leonardo AI](https://img.shields.io/badge/Leonardo%20AI-8F7DE0?style=for-the-badge&logoColor=white)
![Google Flow](https://img.shields.io/badge/Google%20Flow-5B8DEF?style=for-the-badge&logo=google&logoColor=white)
![Veo](https://img.shields.io/badge/Veo-4285F4?style=for-the-badge&logo=google&logoColor=white)
![ElevenLabs](https://img.shields.io/badge/ElevenLabs-000000?style=for-the-badge&logoColor=white)

**Learning next:** TypeScript · Vite · testing (Vitest/Playwright) · Postgres

---

# 📊 Stats

<div align="center">

<img src="https://streak-stats.demolab.com?user=Ranger-Jay&theme=tokyonight&hide_border=true" alt="Jay's contribution streak" />

</div>
