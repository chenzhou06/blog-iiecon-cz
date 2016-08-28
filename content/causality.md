Title: Note on Causality
Author: Chen Zhou
Category: Economics
Tags: econometrics
Date: 2016-08-28 20:30:59

Applied econometrists nowadays pay a lot attention on causal inference. In the book
*Causal Inference* by Imbens and Rubin (2015), the authors successfully introduce
to us the framework to make causal inference.

Causality is defined against potential outcomes. Unlike other econometrists,
Imbens and Rubin do not frequently mention "counterfactual" in their book. The
reason I come up with is that "potential outcome" is more convenient to express
the two states of a unit in two contradict settings. With potential outcome, we
need not to specify which state is imaginary and which state is realized. A unit
has two potential outcomes, one is the treated outcome, another is the
controlled outcome. The treatment effect is defined as their difference. We need
not to point out the unit is actually treated or not. If the unit is in the treated
group, the treated potential outcome is observable, the controlled potential
outcome is counterfactual. If the unit is controlled in reality, the
counterfactual outcome becomes the treated one. However, the expression of
causal effect do not differ in the two cases.

If we use "counterfactual" in our definition, the expression would be
unnecessarily complicated. We must introduce more math symbols to distinguish
states of a unit, whether it is in control group or not. Otherwise we could not
know which outcome is realized, which is counterfactual.

I wrote a note about this book, summarizing the deviation of causality and two
approaches to conduct inference for causal estimand:

* Regression methods
* Model-based approach (Bayesian)

Because this note is technical, I uploaded it [here](pdfs/causality.pdf) in PDF format.
