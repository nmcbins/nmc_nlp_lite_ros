nmc_nlp_lite is ROS Node that provide access to a cloud based service: BINS (Bot Input Naturalization Service).

What does BINS do:  it is a cloud-based service that allows client to easily develop and deploy a light weight natural language processing capabilities.  

Robot developers can use it to do things as simple as defining a few hard-coded mapping of natural language commands to robot executable instructions,  or as complex as a small-scale NLP engine, 
or anything in between.

BINS supports synonym, phrase (i.e. ngram), and RegEx word patterns. It further supports nesting of those patterns.  

Upon matching of a defined pattern, BINS lets a developer specify what to output -- which could be plain text, or robot executable instructions, or even entity/slot in json format.

nmc_nlp_lite,  as a wrapper of BINS, can be launched as a ROS node that supports both publish/subscribe mode (for asynchronous access) or service mode (for synchronous access).


