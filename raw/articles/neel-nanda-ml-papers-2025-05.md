---
title: "Highly Opinionated Advice on How to Write ML Papers"
author: Neel Nanda
source: https://www.alignmentforum.org/posts/eJGptPbbFPZGLpjsp/highly-opinionated-advice-on-how-to-write-ml-papers
mirror: https://www.lesswrong.com/posts/highly-opinionated-advice-on-how-to-write-ml-papers
date: 2025-05-12
fetched: 2026-06-24
tags: [ml-research, paper-writing, mechanistic-interpretability, neel-nanda, narrative, scientific-communication]
---

# Highly Opinionated Advice on How to Write ML Papers

**Author:** Neel Nanda (Alignment Forum / LessWrong, 12 May 2025)
**Length:** ~39 min read, 492 karma, 33 comments
**Flavour:** Mechanistic interpretability papers — author notes generalises to ML broadly.

## TL;DR

The essence of an ideal paper is the narrative: a short, rigorous and evidence-based technical story you tell, with a takeaway the readers care about.

- **What?** A narrative is fundamentally about a contribution to our body of knowledge: one to three specific novel claims that fit within a cohesive theme
- **Why?** You need rigorous empirical evidence that convincingly supports your claims
- **So what?** Why should the reader care? Motivation, problem, bigger picture. What is the impact? Why does your takeaway matter?

The north star of a paper is ensuring the reader understands and remembers the narrative, and believes the paper's evidence supports it. The first step is to compress your research into these claims. The paper must clearly motivate, explain on intuitive + technical level, and contextualise novelty vs. prior literature. This is the role of the abstract & introduction.

**Experimental Evidence:** Absolutely crucial to get right and aggressively red-team — it's how you resist the temptation of elegant but false narratives.

**Quality > Quantity:** Find compelling experiments, not a ton of vaguely relevant ones. Experiments must be explained in full technical detail: high-level in intro/abstract, results in figures, increasingly detailed in main body and appendix. Ensure researchers can check your work — sufficient detail to be replicated.

**Define key terms and techniques** — readers have less context than you think.

**Write iteratively:** abstract → bullet outline → introduction → first full draft → repeat. Get feedback and reflect after each stage.

**Spend comparable time** on abstract, intro, figures, and everything else — they have about the same `number_of_readers * time_to_read`.

**Inform, not persuade:** Avoid the trap of overclaiming or ignoring limitations. Scientific integrity may get you less hype, but gains respect from researchers who matter.

**Precision, not obfuscation:** Use jargon where needed to precisely state your point, but not for sounding smart. Use simple language wherever possible.

## Core Thesis

Case study: The abstract of refusal is mediated by a single direction, broken down into the purpose of each sentence

Your research only matters if people read, understand, and build upon it. This means that writing a good paper is a critical part of the research process. Further, the process of writing forces you to clarify your own thinking in ways that often reveal gaps or new insights - I’ve often only properly understood an idea after writing it up. Yet, to many, writing feels less fun than research and is treated as an after thought - a common but critical mistake.

In my experience supervising 20+ papers and reading/appreciating/being annoyed by a bunch more, I've developed my own opinionated framework for what I think makes a paper good and how to approach the writing process. I try to lay this out in this post, along with a bunch of concrete advice.[1] This post assumes you’ve already done a bunch of technical research, and focuses on how to effectively share it with the world, see my other posts for advice on the research part.

Caveat: I mostly have experience with writing mechanistic interpretability papers and this advice is written with that flavour. I expect much of it to generalise to the rest of ML and some to generalise to other fields but it's hard for me to say. Further, this is very much my personal opinionated, and optimised more for truth-seeking than getting into conferences[2]. See other great advice here and here.

Caveat 2: There are many reasonable objections to the academic paper as the format for communicating research. Alas, engaging with those is outside the scope of this post, it’s long enough as it is.

At its core, a paper should present a narrative of one to three specific concrete claims that you believe to be true, that build to some useful takeaway(s). Everything else in the paper exists to support this narrative. The second pillar of the paper is rigorous evidence for why they are true - obviously there will always be some chance you’re wrong, but they should be compelling and believable, without obvious glaring flaws.

One of the critical steps that can make or break a paper is crafting a narrative. What does this actually mean? And how can you do it?

Research is about discovering new things and pushing forward our frontier of existing knowledge. I view a paper as something that finds insight and provides compelling evidence behind it. The way to tell when you could start writing a paper is when you have learned something insightful, in a way that could be made legible to someone else.

This is far easier said than done. A research project is often a mess of fun results, confusions, insights, and remaining mysteries. Even when you’ve made enough progress to write it up, you will likely have a great deal of tacit knowledge, interesting rabbit holes, dangling threads, etc - projects rarely feel done.

I find that converting a project into a great narrative is a subtle and difficult skill, one of the many facets of research taste. It’s something I’ve gotten much, much better at over time, and it’s hard to say what the best way to get better at it is, beyond experience. One exercise I’d recommend is taking papers you know, and trying to write down what their narrative is, and ask yourself what its strengths and weaknesses are. If at all possible, consult mentors/more experienced researchers for advice. But if you need to come up with one yourself, the right questions to ask look like:

A good, compelling narrative comes with motivation and impact. The key points to be sure to cover:

Why do you need this kind of compressed narrative? Often there’s far more insight in a research project than can be contained in this structure. But it is impossible to convey this level of nuance in a paper. Readers will rarely take away more than a few sentences of content. Choose those sentences carefully. These are the insights shared by your paper, your contribution to the literature. These are the specific, concrete claims that you want to communicate - you cannot reliably communicate much more. You will need to compress your research findings down into a handful of claims, prioritise those, and accept that you may need to drop a bunch of other detail, or move it to appendices. If you don’t deliberately de-prioritise some details, then something else will get dropped, which may have been far more important.

One important claim, with sufficiently strong evidence, can be enough for a great paper! If you want multiple claims, I strongly recommend choosing claims that fit together in a cohesive theme - papers are far easier to understand, praise, share, etc if there is a coherent narrative, not just a grab-bag of unconnected ideas.

Depending on the strength of the evidence, you can adjust the confidence of a claim:

Generally, stronger statements make for more interesting papers, but require higher standards of evidence - resist the temptation to overclaim for clicks!

Another thorny question is: When should you stop doing research and start writing up your research? This is a hard and subtle question that is, in many ways, a matter of research taste, but here is my general guide:

But generally, this is unfortunately just a hard thing to tell when starting out, and gets far easier with time and experience. If you can consult a more experienced researcher, definitely do.

A more meta piece of advice when starting out is to try to choose projects where the narrative will be pretty obvious, e.g. method X beats SOTA method Y in domain Z on metric W

Warning: Before moving into paper-writing mode, it's crucial to verify that your evidence is actually correct. An unfortunate fact is that many published papers are basically false or wildly misleading. Don't let this happen to you! Carefully check your critical experiments and, if possible, re-implement them through alternate pathways. Ideally, verify all experiments worth mentioning in the paper, or at least 75% of them.

A common and confusing requirement for papers is that the results be novel, something that is not covered before. What exactly does this mean? Science is fundamentally about building a large body of knowledge. This means that your work exists in the context of what has come before. Novelty means it expands our knowledge.

The conventional definition of novelty can be annoying and, in my opinion, focuses too much on shininess and doesn't capture the more important aspect of whether our knowledge has expanded. Another way to put this is: Should I assign different probabilities to propositions I care about after observing the results of this paper?

Rigorous, at-scale replications of shaky results, negative results of seemingly promising hypotheses, and high-quality failed replications of popular papers are all very valuable contributions. I would personally consider these novel because they expand our knowledge. However, the revealed preferences of many reviewers and researchers suggest they do not feel the same way. Such is life.

I don’t want to go too far re criticising novelty: there are many cases where I am uninterested in a paper due to lack of novelty. This primarily occurs with methods that I expect to work when applied in standard settings, and I assign a high probability of success, so the project provides few bits of information. While knowing that such a method failed could be interesting, projects can also fail due to researcher incompetence or bad luck. Therefore, it is difficult to draw meaningful conclusions without evidence of researcher competence.

Leaving that aside, novelty can be hard to communicate. Given a paper on its own, it's difficult to tell what is and is not supposed to be novel:

The main way to address this is to be extremely clear about what is and is not novel, especially in the introduction and related work, and to liberally cite the most relevant papers and explain why your work is and is not different.

How to find out what came before? Use a large language model. If you’re not already familiar with a relevant literature, LLMs are pretty great at doing quick literature reviews, e.g. Gemini Deep Research[4]. Reading the literature yourself is much better of course, but takes way, way longer and should have been done at the start project.

One reason this is very important is that, depending on what’s claimed as novel, the same paper could be perceived as either inappropriately arrogant or making a modest incremental contribution, depending on how the claims are presented.

Contextualizing your work within existing literature is particularly crucial for experienced researchers who are familiar with the field. Clear explanation in the introduction helps them quickly engage with your work and see what’s interesting, else it blurs into all other superficially similar papers they’ve read and doesn’t seem worth the effort.

I personally prefer to just do work that is optimised for scientific value, and shoe-horn it into a peer review friendly lens at the end, if applicable. But I’m in a fortunate position here, and there are real career incentives around getting published.

A paper is worth little unless it can convince[5] the reader of its key claims. To do this, you need evidence. In machine learning, this typically means experiments. Below, I discuss how I think about what good experimental evidence looks like - see my research process sequence for more advice.

With claims the priority is being able to communicate the intuitions to everyone, but with experiments the priority is being able to justify it in full technical detail to an engaged, skeptical reader. You also want to explain what’s going on intuitively, to support your claims, but this is less key than actually having good, legitimate evidence.

A particularly important thing to get right is extensive red-teaming: you should spend a good amount of your time, both during the original research and now, red teaming your narrative. One of the main traps introduced by the framing of “find a great narrative” is the temptation to ignore inconvenient contradictory results - don’t let this happen to you. Tips:

Statistical rigour: If you're doing some type of frequentist test[6], you probably shouldn't use p < .05 as a threshold. In stats heavy fields, like the social sciences, papers that report their central finding at .01 < p < .05, usually fail to replicate. If you're doing an exploratory approach, you should be skeptical of any result that isn't p < .001, as the number of possible hypotheses is vast.

Prior work discussing replicability is very strict on this point: "One prior study of 103 replication attempts [in psychology] indeed found a 74% replication rate for findings reported at p ≤ .005 and a 28% replication rate for findings at .005 < p < .05 (Gordon et al., 2021)". There are also various statistical reasons why true findings usually won't produce .01 < p < .05.[7]

Tragically, the world is complicated, and there is often no single clear recipe to deal with all edge cases in research. These considerations are guidelines to help navigate that complexity

This is all pretty abstract. To concretise this, let’s look at my grokking paper through this lens. I’ve broken it down into claims, evidence, context and motivation, with commentary thrown in. This is somewhat stylised for pedagogical reasons, but hopefully useful!

Note: Check out my paper writing checklist for a concrete to-do list of what I recommend doing here

So, you have a list of claims and key experiments. Now, all you need to do is write the paper! I recommend an iterative process - start with a bullet point narrative, then a full bullet point outline, then flesh it out into prose, taking time to reflect at each stage. See above or the next section for more details on the actual structure of a paper, here I just try to convey the high-level strategy

A key challenge in paper writing is the illusion of transparency - you have spent months steeped in the context of this research project. You have tons of context, your reader does not. You’ll need to help them understand exactly what you are doing, in the large space of all possible ML papers, and address all the misconceptions and possible misunderstandings, even though to you it all feels obvious. This is a difficult skill - wherever possible, get extensive feedback from others to address

Spend far more time on early sections: Realistically, tons of people read the title of your paper, many read the abstract, some read the introduction/skim the figures, and occasionally they read the whole thing. This means you should spend about the same amount of time on each of: the abstract, the intro, the figures, and everything else[8]. (I’m only half joking)

As part of this process, write down common misconceptions, limitations, or ways someone might over-update on your work.

Once you have a compressed list of bullet points that you are satisfied with, you should start iteratively expanding and developing them. After each step, stop, reflect, read through, and edit - rushing a step can lead to a lot of wasted time at the next step.

If you have a research supervisor/mentor, it is very valuable to get feedback at each stage - I find it way faster and easier to give feedback on a narrative or bullet point outline than being sent 8 pages of dense prose! Even if you don’t have a mentor, try to get feedback from someone[9].

OK, so what actually goes into a paper? What are the key components you’ll need to write, and what is the point of each?

An abstract should give a cold-start reader a sense of what the paper is about - what sub-field, what type of paper, what key motivating questions, etc. This is a key manifestation of the illusion of transparency: you know exactly what your project is about but to your reader there is a large space of possibilities, and without any context may have completely incorrect priors and wildly misinterpret.

People will often leave your abstract then move on, unless strongly compelled - it’s a big deal to get right, and deserves high polish

Now the reader is situated, you need to concisely communicate your claims. Again, illusion of transparency - they often won’t know your techniques, the work you’re building on, key ideas, etc. Abstracts should be as accessible as possible - use simple language as much as you can

The introduction is broadly similar to the abstract but more extended and in-depth. I proceed in roughly this order:

Paragraph 3.5[10]: Our case - summarise the most critical evidence we provide that our main claim is true

Note: Citing here isn't about performatively covering all the relevant papers[11]. It's about providing the context a reader needs to understand why your work is interesting and how it's limited. I try to have at least one citation for each step in an important argument, eg why

The introduction is where you have room to define key terms and concepts required to understand your claims, especially if they're somewhat technical.

It's often good to explicitly end with a bullet-point list of your contributions, which are basically just the concise claims you believe to be true, potentially with brief references to the supporting evidence.

Figures are incredibly important. Having clear graphs can be the difference between a very clear and easy-to-read paper and an incomprehensible mess.

It can work well to combine several key graphs into one figure and make it your figure 1. E.g.:

Another kind of figure is an explanatory diagram rather than a graph. This can be a high-effort but very effective figure one, that gives people a sense of roughly what is happening in the paper. This should be something that would catch people's eye if you put it as the first image in a tweet thread about your paper. Some diagrams I liked (intentionally at several different levels of effortful):

Most of the actual paper, by word count, should be about communicating your experiments and results in precise technical detail. To do good science, it is important that researchers can understand exactly what you did and what you observed, so they can draw their own conclusions rather than needing to take things on faith. For example, in interpretability, there are ways that a method can give completely useless answers if misapplied, so it’s crucial that I know if a paper did that, even though the detail might seem totally unimportant to the authors!

Ideally, you want to communicate the information at several different layers of abstraction. It's your job to ensure that readers understand:

The key background context required to disambiguate and understand your work - key terms, techniques, etc[12][13]

If the experiments for each claim are more boutique, or if there are several claims with different styles of evidence, then I try to give each type of evidence its own section while explaining how it ties back to the overarching theme, rather than a methods -> results section. People will forget about the first method before they see its results.

Explaining the limitations of your work is a crucial part of scientific good practice. The goal of a paper is to contribute to our body of knowledge. Readers must understand the limitations of the evidence you provide to have a calibrated sense of what knowledge they have learned. And it's important that you put a good faith effort into documenting limitations because you know far more about your work than the readers, so they may miss things.

There is a common mistake of trying to make your work sound maximally exciting. Generally, the people whose opinions you most care about are competent researchers who can see through this kind of thing. And I generally have a much higher opinion of a piece of work if it clearly acknowledges its limitations up front. I’m not sure if this makes it easier or harder to get published.

This is also the place to discuss broader implications and general takeaways, future work you’d be excited about, reflections, etc.

Some people have conclusions too. Personally, I think conclusions are often kind of useless; the introduction should have explained this well. You can skip it

Generally, related work is often treated like a bit of an annoyance and afterthought. The feeling that you need to cite lots of things that aren't actually relevant can be annoying, but sometimes there is very important work that has done similar things to you, and a reader might have seen that and wonder why your paper is interesting.

It's very important to clearly explain why what you did is different or, if what you did is not very different, either acknowledge this ("that was parallel work") or explain why your work is still slightly interesting in this context, or how you fixed a mistake in prior work (stated politely).

But that said, there’s a lot of annoying norms here and related works often add little value IMO - needing to cite a lot so you look like you’ve put in enough effort, covering minor or obscure things that aren’t particularly relevant, citing low quality works to be polite, making sure to cite the first instance of each thing, etc. Contextualising in the literature is important, but ideally I’ve already covered it in the introduction.

Related work is often put as the second section of the paper. Personally, I generally prefer it to be the penultimate section. I think related work should only be upfront if it plays an important role in motivating the paper - if your paper is very heavily tied to the surrounding literature, plugging a gap, correcting a mistake, or unlocking a new capability that would enhance various bits of prior work.

Appendices are weird. They're basically the place you put everything that doesn't fit into the main paper. One way to think about it is that you're actually writing a much longer than nine-page paper - the main body and the appendices - but you've chosen a highlights reel for the first nine pages where you put all the absolutely key information. You place all the less crucial information in the appendices for readers to pick and choose from as they see fit.

In general, the crucial scarce resource you must manage is the reader's time and attention. The main body should be aggressively prioritized to make the most of this, be engaging, and communicate the most important pieces of information. But if you have a lot more to say than you can fit in there, then that's what appendices are for. A truly interested reader can go and take a look, though most won't.

Generally, appendices are held to a notably lower standard than the main body and will be read far less, so you should not feel obliged to put in meaningful effort polishing them. This is the standard solution to the dilemma when you want to include full technical detail but have done some fairly complex and convoluted work that just won't realistically fit.

Peer review is notoriously terrible for seeking truth. Reviewers often have biases, like favoring work that feels novel and shiny and exciting, or that doesn't feel weird or too new, or that doesn’t seriously challenge their existing beliefs. This has been shown in rigorous RCTs, where NeurIPS 2021 gave some papers two sets of reviewers and compared their decisions. The results… aren’t great:

I personally think that, at least in safety, doing good work that people respect matters more than getting into conferences, though both are nice. I’ve generally had fairly good results with just trying to write high-integrity work that explains why I believe it is interesting, and just trying to do good science and the work that I think is highest impact, even if it doesn't fit the academic mold.

But it’s pretty plausible to me that many of the people reading this are not in such a fortunate position, and that getting first author papers into top conferences would be a meaningful career boost, especially your first 1-2 papers. The strategy I generally recommend for my mentees is to spend most of the project doing the best scientific work they can. Then, as we approach the end of the project, we figure out how to wrap it up in a maximally conference-friendly package while writing and submitting it. If we did anything that made the work noticeably worse, we can undo it before uploading to Arxiv.

Papers are seen as prestigious, formal, and highly intellectual artifacts. As a result, there's a tendency towards verbosity or trying to make things sound more complex and fancy than they actually are, so they feel impressive. I think this is a highly ineffective strategy. If I don’t understand a paper, I generally ignore it and move on, or assume it’s BS in the absence of strong evidence to the contrary. Often, the best papers just take some very simple techniques and apply them carefully and well. There’s a real elegance to being simple and effective.

People need to understand a paper in order to appreciate it and build on it and think it is interesting (except for superficial Twitter clickbait). Generally, you want to be precise, but within the constraint of being precise, be as simple and accessible as possible. Try to use plain language and minimize jargon except where the jargon is needed to precisely convey your meaning. You get points for quality technical insights, not for sounding fancy. Verbosity and overly complex language and jargon is actively detrimental to your paper’s prospects, IMO.

People often do not prioritize writing. They treat it like an annoying afterthought and do all the fun bits like running experiments, and leave it to the last minute. This is a mistake. Again, your work only matters if people read and understand it. Writing quality majorly affects clarity and engagement. Writing is absolutely crucial and is a major multiplier on the impact of your work.

I typically recommend that people switch from understanding mode to distillation and paper writing a month before a conference deadline, if at all possible. You should want to spend a lot of your time iterating on a write-up, getting feedback, trying to make it clearer, thinking about weaknesses, etc.

One irritation I have about the standard paper structure is that it heavily incentivizes being rigorous and maximally objective and defensible. Obviously, there are significant advantages to this, but I think that often a lot of the most valuable insights from a research project come in the form of tacit knowledge.

I think this is really important, and I find it a real shame that this is often just discarded. I am personally a big fan of putting this kind of stuff as appendix A or as an accompanying blog post, where you can take as many liberties as you like.

Your research will only matter if people read it, understand it, engage with it, and ideally believe it. This means that good paper writing is a crucial skill, but often neglected.

The core process should be to find the concise claims you believe to be true, the strongest experimental evidence that you believe builds a robust case for these claims, and use this to craft a coherent narrative. Then flesh this out into a bullet point outline of the overall post, reflect on it, and ideally get feedback, and iteratively expand.

Again, this is a highly opinionated post about how I personally think about the process and philosophy of paper writing. I'm sure many researchers will strongly disagree with me on many important points, and the correct approach will vary significantly by field and norms.

Note: I am in no way claiming that I follow this advice, especially in blog posts - this is my attempt to paint a platonic ideal, and advise on how to be a better person than I. Personally, I find actually writing academic papers pretty frustrating and much prefer blog posts

I think writing great papers certainly helps, and if you’re new I recommend just trying to write the best paper you can, but there’s still a lot of depressingly perverse incentives from ML peer review

I mention this purely for completeness. I have never seen a convincing guarantee in deep learning, neural networks are far too squishy

Well, at least “provide enough evidence to somewhat update their beliefs”, convince is a fairly high bar

Also the title, though I haven’t figured out how to productively spend 20% of my time on that yet…

Paper swaps are a great way to get feedback - find someone else also working on a paper and offer to give each other feedback. Even if you have less time before the paper deadline, this tends to be a mutually beneficial trade.

If something is super widespread knowledge, no need to cover it, but err towards defining things. E.g. I wouldn’t bother defining the transformer architecture or an LLM, but I would define a sparse autoencoder or steering vector

4Comments4$RS=function(a,b){a=document.getElementById(a);b=document.getElementById(b);for(a.parentNode.removeChild(a);a.firstChild;)b.parentNode.insertBefore(a.firstChild,b);b.parentNode.removeChild(b)};$RS("S:5","P:5")$RC("B:3","S:3")AIPracticalFrontpage92Ω 33Previous:My Research Process: Understanding and Cultivating Research Taste3 comments36 karma$RC("B:7","S:7")New Comment Submit 4 comments, sorted by top scoringClick to highlight new comments since: Today at 6:24 AM[-]StefanHex1y20Thanks for posting this!

We also showed that we could now jailbreak the model by removing this direction from the weights - the novelty was less

[-]Gurkenglas1y20Often, the best papers just take some very simple techniques and apply them carefully and well.

[-]Sheikh Abdur Raheem Ali1y10Why isn't this part of the sequence on your research process?

[-]Neel Nanda1y30I may add it in there later. I pushed it out early bc NeurIPS, and I think it stands alone as a useful post, so don't want to imply people need to read the sequence first

---

## Key Concepts Extracted
- Paper narrative = 1–3 specific claims + cohesive theme + impact
- Two pillars: claims + rigorous evidence
- TL;DR table = single-glance framework for the whole paper
- Iterative writing loop: abstract → outline → intro → draft
- Equal-time allocation across abstract / intro / figures / body
- "Inform, don't persuade" stance
- Aggressive red-teaming of own experimental evidence
