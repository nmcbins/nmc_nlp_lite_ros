Copyright (c) 2020 NMC Corp
This code is licensed under MIT license (see LICENSE.md for details)

nmc_nlp_lite (nmc_nlp stands for: Neuronmap Computing Natural Language Processing) is ROS package that offers direct access on ROS platform to a cloud based service: BINS (Bot Input Normalization Service), hosted at: http://www.nmcomputing.com/ln_home/bins_home.html

What does BINS do: it enables a robot developer to easily develop and deploy light weight natural language processing capabilities.

Robot developers can use it to do things as simple as defining a few hard-coded mappings of natural language commands to robot instructions, or as complex as a small-scale NLP engine, or anything in between.

BINS supports definitions of synonyms, phrases (i.e. ngram), and RegEx word patterns. It further supports nesting of those patterns, hence enabling robot developers to build hierarchical patterns.

Upon matching of a pre-defined pattern, BINS lets a developer specify what to produce as output -- which could be plain text, or robot executable instructions, or even intents, entities, etc. in json format.

nmc_nlp_lite, as a wrapper of BINS, can be launched as a ROS node that supports both publish/subscribe mode (for asynchronous access) or service mode (for synchronous access).