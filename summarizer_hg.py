from transformers import pipeline

summarizer = pipeline("summarization")

article = " UN spokesperson Stéphane Dujarric has said that the organisations secretary-general condemns an attack on the Iranian consulate in Damascus, calling for “utmost restraint”. The attack, which killed at least 11 people, including a senior commander in the al-Quds force of the Iranian Revolutionary Guards Corps (IRGC), has been widely attributed to Israel.In the statement, Dujarric said António Guterres cautions that any miscalculation could lead to broader conflict in an already volatile region, with devastating consequences for civilians who are already seeing unprecedented suffering in Syria, Lebanon, the occupied Palestinian Territory, and the broader Middle East.Reuters reports that in the statement Guterres called on all concerned to exercise utmost restraint and avoid further escalation. "

summary = summarizer(article, max_length=100, min_length = 10)



