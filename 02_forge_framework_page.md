# edikan.ai v2 — The FORGE Framework (New Page: /framework)

> This page is the program's public design document. It should read like a curriculum
> architecture published by its designer: confident, specific, and dated. It is the single
> most important page on the site for demonstrating that a workforce-development model has
> been designed and is in execution.

---

## META

**Title tag:** The FORGE Framework — Curriculum Architecture | Project FORGE

**Meta description:** The pedagogical architecture behind Project FORGE: a competency-based,
18-month pathway from programming fundamentals to industrial optimization, designed to scale
from open access to institutional partnership.

---

## PAGE HEADER

**Title:** The FORGE Framework

**Standfirst:** How an 18-month open curriculum is engineered to turn industrial practitioners
into optimization-capable engineers — and how the model scales beyond one website.

**Published:** [insert real publish date] · **Last revised:** [auto]

---

## 1. DESIGN PRINCIPLES

**Start where the workforce is.** FORGE assumes no prior programming, no calculus, and no
statistics. This is not a simplification; it is the design constraint that makes the program
useful. The people American industry most needs to upskill — technicians, operators, plant
engineers — are systematically excluded by programs that assume a computer science degree on
day one.

**Foundations before frameworks.** Every method is implemented from first principles before
any library or AI tool is introduced. A practitioner who has built gradient descent by hand
can debug a model that misbehaves in production. A practitioner who has only called an API
cannot.

**Theory travels to the plant, every time.** No module ends at the whiteboard. Linear algebra
is taught through sensor-network data recovery. Regression is taught through roll-force
prediction. Scheduling theory is taught through steel mill and smelter operations. The
industrial application is the pedagogy, not the appendix.

**Competency, not completion.** Each phase defines what a learner can *do* on exit, stated as
capabilities an employer can verify — not certificates of attendance.

**Open by default.** All core materials are free and public. Scarcity of training is the
problem FORGE exists to solve; it cannot also be the business model.

---

## 2. THE 18-MONTH ARCHITECTURE

*(Render as the curriculum map — table or timeline. Live phases marked LIVE, others marked
IN DEVELOPMENT with target windows. Use real, achievable target windows only.)*

| Phase | Focus | Exit competencies (abridged) | Status |
|---|---|---|---|
| 1. Foundations | Programming from first principles: memory, control flow, functions, data structures, debugging | Read, write, and debug non-trivial programs unassisted; explain what code does at the memory level | LIVE |
| 2. Core Competence | Production-quality programming across the language set; algorithms and complexity; Git; SQL fundamentals | Ship maintainable code; query and manage industrial databases; reason about performance | IN DEVELOPMENT |
| 3. Mathematical Foundations | Linear algebra, calculus, statistics, probability, optimization theory | Formulate industrial questions mathematically; apply SVD/PCA, estimation, and basic optimization to plant data | PARTIAL — first modules live |
| 4. ML for Manufacturing | Regression, classification, neural networks, time series, anomaly detection — from scratch, then frameworks | Build, validate, and stress-test predictive models on manufacturing data | IN DEVELOPMENT |
| 5. Industrial Optimization | Linear, integer, and network programming; scheduling; capacity and supply chain models | Formulate and solve production scheduling and supply chain problems; interpret duals and sensitivity | IN DEVELOPMENT |
| 6. Deployment & Capstones | Data pipelines, monitoring, model maintenance, capstone projects | Take a model from notebook to monitored production use; complete an end-to-end industrial capstone | IN DEVELOPMENT |

---

## 3. THE LANGUAGE SET, JUSTIFIED

Seven languages is a deliberate curriculum decision, not breadth for its own sake. Industrial
environments are heterogeneous, and each language maps to a layer of the real stack:

- **Python** — analytics, machine learning, and the lingua franca of industrial data science.
- **SQL** — plant historians, MES databases, and production records; the most-used and
  least-taught skill in industry.
- **MATLAB** — the installed base of control engineering; fluency here is how FORGE graduates
  collaborate with existing plant engineering teams.
- **C++** — real-time systems and performance-critical processing at the edge.
- **Rust** — memory-safe systems programming for the next generation of edge and IIoT
  deployments.
- **Julia** — scientific computing and optimization, where model formulation and speed meet.
- **R** — statistical quality control and the SPC tradition manufacturing already trusts.

Learners achieve working fluency across the set and depth in the layers their role demands.

---

## 4. APPLIED PROBLEM DOMAINS

FORGE's worked examples are drawn from operations of strategic significance to American
industry, so that training capacity and national industrial priorities compound rather than
compete:

- **Aluminum smelter optimization** — energy-intensive continuous production under price and
  power constraints.
- **Steel mill scheduling** — sequencing, roll-force prediction, and predictive maintenance in
  continuous casting and hot rolling.
- **Supply chain coordination** — multi-echelon networks, including critical mineral supply
  chains where processing chokepoints, not geology, bind capacity.

**On the roadmap — Optimization for Critical Supply Chains & Defense Industrial Capacity:** a
dedicated advanced track applying the full FORGE toolkit to publicly documented problems in
industrial surge capacity: munitions production scheduling, strategic material inventory
modeling, and processing bottleneck analysis, built exclusively on open data and published
sources. Module outline to be published on this page.

---

## 5. THE SCALING MODEL

FORGE is engineered to grow through three deliberate stages:

**Stage 1 — Open access (now).** Self-paced curriculum, public repository, open problem sets.
Success measure: complete, coherent coverage of Phases 1–4.

**Stage 2 — Cohorts.** Facilitated cohorts with fixed timelines, peer review, and instructor
office hours — the structure most adult learners need to finish what open courseware starts.

**Stage 3 — Institutional partnership.** The curriculum packaged for manufacturers (in-house
upskilling tracks mapped to their own systems) and for community colleges and training
programs (technician-level pathways feeding the same progression). This is where a website
becomes workforce infrastructure.

Manufacturers interested in Stage 2–3 pilots: contact@edikan.ai.

---

## 6. GOVERNANCE OF QUALITY

- All curriculum code is public on GitHub and issues are open; errors found by learners are
  fixed in public.
- Figures, datasets, and industrial claims used in teaching materials are cited to primary
  public sources.
- The Framework itself is versioned; substantive changes are dated on this page.

---

## FOOTER LINE FOR THIS PAGE

The FORGE Framework was designed by Edikan Udofia, operations researcher, Colorado School of
Mines.
