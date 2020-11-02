---
layout: single
permalink: /research/
---
 
I'm still very new to the PhD, so ideas are still forming. Below are some initial ideas.


## Uncertain and Situated Knowledges for NLP


This direction builds off of previous work in NaCTeM on uncertainty detection and connects it
with the recent realization in ML that datasets embody a perspective, rather than encoding an
objective state of the world. 


### Knowledge Fusion
Knowledge fusion refers to the process of collecting multiple diverse instances of a knowledge statement (say in different databases),
normalizing them, and collecting them together into a single statement. How can we perform knowledge fusion in the presence of
uncertainty? For example, one scientific paper might be very confident about their finding that drug A interacts with drug B,
but another that attempted to reproduce this experiment achieved only borderline significant results. In this case, a knowledge base
that contains the statement "A interacts with B" should somehow encode the differences in certainty expressed.

### Incorporating Background Knowledge into NLP Models
There has been a variety of research efforts in this direction in the last few years, in both the general and scientific domain,
but we have yet to arrive a consensus of the best way to inject models with structured knowledge. This question becomes even
trickier when we consider individual knowledge statements that are situated and to some extent uncertain. For example, how can
a question answering system reason over multiple sources of corroborating (or contradictory!) evidence and provide an appropriate,
measured answer?
