---
description: "Passe n'importe quelle question, id├®e ou d├®cision ├á travers un conseil de 5 conseillers IA qui l'analysent ind├®pendamment, s'├®valuent mutuellement de fa├ºon anonyme, et synth├®tisent un verdict final. Bas├® sur la m├®thodologie LLM Council de Karpathy. D├ëCLENCHEURS OBLIGATOIRES : 'passe ├ºa au conseil', 'lance le conseil', 'convoque le conseil', 'war room ├ºa', 'teste sous pression', 'stress-teste ├ºa', 'd├®battons ├ºa'. D├ëCLENCHEURS FORTS (quand l'utilisateur pr├®sente une vraie d├®cision avec des enjeux) : 'est-ce que je devrais X ou Y', 'quelle option', 'qu'est-ce que tu ferais', 'est-ce le bon choix', 'valide ├ºa', 'donne-moi plusieurs perspectives', 'je n'arrive pas ├á d├®cider', 'j'h├®site entre'. NE PAS d├®clencher sur des questions triviales, des recherches factuelles, ou un simple 'je devrais' sans vrai arbitrage. D├ëCLENCHER quand l'utilisateur pr├®sente une d├®cision r├®elle avec des enjeux et plusieurs options."
---

# LLM Council

You ask one AI a question, you get one answer. That answer might be great. It might be mid. You have no way to tell because you only saw one perspective.

The council fixes this. It runs your question through 5 independent advisors, each thinking from a fundamentally different angle. Then they review each other's work. Then a chairman synthesizes everything into a final recommendation that tells you where the advisors agree, where they clash, and what you should actually do.

This is adapted from Andrej Karpathy's LLM Council. He dispatches queries to multiple models, has them peer-review each other anonymously, then a chairman produces the final answer. We do the same thing inside Claude using sub-agents with different thinking lenses instead of different models.

## when to run the council

The council is for questions where being wrong is expensive.

Good council questions:
- "Should I launch a $97 workshop or a $497 course?"
- "Which of these 3 positioning angles is strongest?"
- "I'm thinking of pivoting from X to Y. Am I crazy?"
- "Here's my landing page copy. What's weak?"
- "Should I hire a VA or build an automation first?"

Bad council questions:
- "What's the capital of France?" (one right answer, no need for perspectives)
- "Write me a tweet" (creation task, not a decision)
- "Summarize this article" (processing task, not judgment)

The council shines when there's genuine uncertainty and the cost of a bad call is high.

## the five advisors

Each advisor thinks from a different angle. They're not job titles or personas. They're thinking styles that naturally create tension with each other.

### 1. The Contrarian

Actively looks for what's wrong, what's missing, what will fail. Assumes the idea has a fatal flaw and tries to find it. If everything looks solid, digs deeper. The Contrarian is not a pessimist. They're the friend who saves you from a bad deal by asking the questions you're avoiding.

### 2. The First Principles Thinker

Ignores the surface-level question and asks "what are we actually trying to solve here?" Strips away assumptions. Rebuilds the problem from the ground up. Sometimes the most valuable council output is the First Principles Thinker saying "you're asking the wrong question entirely."

### 3. The Expansionist

Looks for upside everyone else is missing. What could be bigger? What adjacent opportunity is hiding? What's being undervalued? The Expansionist doesn't care about risk (that's the Contrarian's job). They care about what happens if this works even better than expected.

### 4. The Outsider

Has zero context about you, your field, or your history. Responds purely to what's in front of them. This is the most underrated advisor. Experts develop blind spots. The Outsider catches the curse of knowledge: things that are obvious to you but confusing to everyone else.

### 5. The Executor

Only cares about one thing: can this actually be done, and what's the fastest path to doing it? Ignores theory, strategy, and big-picture thinking. The Executor looks at every idea through the lens of "OK but what do you do Monday morning?" If an idea sounds brilliant but has no clear first step, the Executor will say so.

Why these five: They create three natural tensions. Contrarian vs Expansionist (downside vs upside). First Principles vs Executor (rethink everything vs just do it). The Outsider sits in the middle keeping everyone honest by seeing what fresh eyes see.

## how a council session works

### step 1: frame the question (with context enrichment)

When the user says "council this" (or any trigger phrase), do two things before framing:

**A. Scan the workspace for context.** Before framing, quickly scan for and read any relevant context files:
- CLAUDE.md or claude.md in the project root or workspace (business context, preferences, constraints)
- Any memory/ folder (audience profiles, voice docs, business details, past decisions)
- Any files the user explicitly referenced or attached
- Recent council transcripts in this folder (to avoid re-counciling the same ground)
- Any other context files relevant to the specific question

Use Glob and quick Read calls to find these. Don't spend more than 30 seconds on this. You're looking for the 2-3 files that would give advisors context for specific, grounded advice instead of generic takes.

**B. Frame the question.** Take the user's raw question AND the enriched context and reframe it as a clear, neutral prompt that all five advisors will receive. The framed question should include:
- The core decision or question
- Key context from the user's message
- Key context from workspace files (business stage, audience, constraints, past results, relevant numbers)
- What's at stake (why this decision matters)

Don't add your own opinion. Don't steer it. If the question is too vague, ask one clarifying question. Just one. Then proceed.

Save the framed question for the transcript.

### step 2: convene the council (5 sub-agents in parallel)

Spawn all 5 advisors simultaneously as sub-agents using the Agent tool. Each gets their advisor identity, the framed question, and this instruction: respond independently, do not hedge, lean fully into your assigned perspective.

**Sub-agent prompt template:**

```
You are [Advisor Name] on an LLM Council.

Your thinking style: [advisor description from above]

A user has brought this question to the council:

[framed question]

Respond from your perspective. Be direct and specific. Don't hedge or try to be balanced. Lean fully into your assigned angle. The other advisors will cover the angles you're not covering.

Keep your response between 150-300 words. No preamble. Go straight into your analysis.
```

### step 3: peer review (5 sub-agents in parallel)

Collect all 5 advisor responses. Anonymize them as Response A through E (randomize which advisor maps to which letter to avoid positional bias).

Spawn 5 new sub-agents simultaneously. Each reviewer sees all 5 anonymized responses and answers three questions:

1. Which response is the strongest and why? (pick one)
2. Which response has the biggest blind spot and what is it?
3. What did ALL responses miss that the council should consider?

**Reviewer prompt template:**

```
You are reviewing the outputs of an LLM Council. Five advisors independently answered this question:

[framed question]

Here are their anonymized responses:

Response A: [response]
Response B: [response]
Response C: [response]
Response D: [response]
Response E: [response]

Answer these three questions. Be specific. Reference responses by letter.

1. Which response is the strongest? Why?
2. Which response has the biggest blind spot? What is it missing?
3. What did ALL five responses miss that the council should consider?

Keep your review under 200 words. Be direct.
```

### step 4: chairman synthesis

One agent gets everything: the original question, all 5 advisor responses (de-anonymized), and all 5 peer reviews.

**Chairman prompt template:**

```
You are the Chairman of an LLM Council. Your job is to synthesize the work of 5 advisors and their peer reviews into a final verdict.

The question brought to the council:

[framed question]

ADVISOR RESPONSES:

The Contrarian: [response]
The First Principles Thinker: [response]
The Expansionist: [response]
The Outsider: [response]
The Executor: [response]

PEER REVIEWS: [all 5 peer reviews]

Produce the council verdict using this exact structure:

## Where the Council Agrees
[Points multiple advisors converged on independently. These are high-confidence signals.]

## Where the Council Clashes
[Genuine disagreements. Present both sides. Explain why reasonable advisors disagree.]

## Blind Spots the Council Caught
[Things that only emerged through peer review. Things individual advisors missed that others flagged.]

## The Recommendation
[A clear, direct recommendation. Not "it depends." A real answer with reasoning.]

## The One Thing to Do First
[A single concrete next step. Not a list. One thing.]

Be direct. Don't hedge. The whole point of the council is to give the user clarity they couldn't get from a single perspective.
```

The chairman can disagree with the majority. If 4 out of 5 advisors say "do it" but the reasoning of the 1 dissenter is strongest, the chairman should side with the dissenter and explain why.

### step 5: generate the council report

After the chairman synthesis, generate a visual HTML report and save it to the workspace.

File: `council-report-[timestamp].html`

The report is a single self-contained HTML file with inline CSS. Clean design, easy to scan. It contains:
- The question at the top
- The chairman's verdict prominently displayed
- An agreement/disagreement visual showing which advisors aligned and which diverged
- Collapsible sections for each advisor's full response (collapsed by default)
- Collapsible section for the peer review highlights
- A footer with timestamp and question counciled

Use clean styling: white background, subtle borders, readable sans-serif font (system font stack), soft accent colors to distinguish advisor sections. Nothing flashy. Professional briefing document feel.

Open the HTML file after generating it so the user can see it immediately.

### step 6: save the full transcript

Save the complete council transcript as `council-transcript-[timestamp].md` in the same location. This includes:
- The original question
- The framed question
- All 5 advisor responses
- All 5 peer reviews (with anonymization mapping revealed)
- The chairman's full synthesis

## output format

Every council session produces two files:

```
council-report-[timestamp].html    # visual report for scanning
council-transcript-[timestamp].md  # full transcript for reference
```

The user sees the HTML report. The transcript is there if they want to dig deeper or reference specific advisor arguments later.

## important notes

- Always spawn all 5 advisors in parallel. Sequential spawning wastes time and lets earlier responses bleed into later ones.
- Always anonymize for peer review. If reviewers know which advisor said what, they'll defer to certain thinking styles instead of evaluating on merit.
- The chairman can disagree with the majority. The best reasoning wins, not the most popular position.
- Don't council trivial questions. If the user asks something with one right answer, just answer it.
- The visual report matters. Most users will scan the report, not read the full transcript. Make the HTML output clean and scannable.
