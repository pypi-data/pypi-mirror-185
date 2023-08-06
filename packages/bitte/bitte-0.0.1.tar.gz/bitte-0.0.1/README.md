# Bitte
Please, somebody get me a beer instead of another 4 hours preprocessing NLP!

This module speeds you up so you can get to the exciting tasks.

It is a quirky collection of the makeshift-tasks most NLP tools run into, but are either too recently relevant,
too small, or too monolingual to have made it to the common NLP modules like spacy, nltk, huggingface transformers, spark etc.


# You hit walls processing data with NLP
This module helps you overcome annoying wastes of time. Now you can glue together the jagged OCR output from some strange .epub file
that once had a life as a .pdf file exported frrom .pptx, into your pristine and beautiful BERT acronym
recognition model which ONLY WORKS WITH FULL SENTENCES AND NORMAL GRAMMAR[*1]


# Quick starts
## Repunctuate
```
repunctuated = bitte.repunctuate([list])
```
- Combined functionality of modules like rpunct, NNSplitter(sentence splitting) and transformer models performing CoLA
task. Runs quickly, you don't have to deal with the hassle of rpunct difficulties on windows or fast execution of a quantized DistilBERT model: It'll just work.

This tool has 0 reliance on external APIs. It does not use a large language model API under the hood. That's why it's fast and cheap.

## Semantic Chunk Text
```
chunks: List[List[str]] = bitte.chunk_semantically(input_string)
```
Semantic search is amazing. There's so much. But the second or third time you run it, you'll get some weird disappointing half sentence returned as a result.
Oh no, you realise. The real world isn't like Wikipedia. We aren't in Kansas. The OCR parser is in Kan sa5.

You're going to need the big guns. Semantic Chunk Text can deal with any string of text and make it reasonably semantically chunked together,
ideal for retrieval tasks for semantic search and for embedding tasks.

This API functions similarly to the Autochapter API of Audacity, but it works for text and does not use transcript timing information.

This API isn't super fast as it runs transformer models often multiple times. It is cheap and quality.

## Wholesome
```
sentence_classifications = bitte.are_full_sentences(sentences)
# Filter for full sentenecs only:
full_sentences = [sentence for ind, sentence in enumerate(sentences) if sentence_classifications[ind]]
```
Have you ever felt your sentence was incompl

Now, you can check if an english sentence is complete. This is useful for grammar merging decisions, detecting conversational interupts,
and deciding whether to display questionable quality content to users or not.

This API isn't super fast, as it needs a transformer model too. It is cheap and quality.

# Why now?
It's a fact that lots of NLP right now works better for english. Large language models; medium ones like BERT;
OCR trained on english datasets... you get the point. If you speak english, you'll be tempted to take advantage
of this somewhere in your pipeline. These tools are for you.