# flash-card
## This is a repository for development of flash cards using django

Flashcards are a great tool when you want to memorize a new topic or learn a new language. You write a question on the front of the card and the answer on the back of the card. Then you can test your memory by going through the flashcards. The more often you show a card to yourself, the better your chances of memorizing its content. With Django, you can build your own flashcards app.

This Django flashcards app replicates a spaced repetition system, which can boost your learning potential.

### Project Overview
Your work in this tutorial is divided into multiple steps. That way, you can take breaks and continue at your own pace. You’ll build a full-stack web app with a database connection that replicates the Leitner system:

In [the Leitner system], flashcards are sorted into groups according to how well the learner knows each one in Leitner’s learning box. The learners try to recall the solution written on a flashcard. If they succeed, they send the card to the next group. If they fail, they send it back to the first group. (Source)

By using spaced repetition, you’ll test your knowledge of the new or challenging topics in the first box more frequently, while you’ll check the cards from the other boxes in larger time intervals:

You have five boxes that can contain flashcards.
When you create a flashcard, you put it into the first box.
To test your knowledge, you choose a box, pick a random flashcard, and check if you know the answer to the card’s question.
If you know the answer, then you move the card to the next higher box.
If you don’t know the answer, then you move the card back to the first box.
The higher the box number, the less frequently you check the flashcards in that box to test your knowledge.

```
Note: Flashcards are an excellent tool for learning a new language. In the examples throughout this tutorial, you’ll find translations of English and Spanish words. But the examples are kept minimal on purpose. That way, you can conveniently customize the questions and answers on your cards.
```


```
$ python manage.py runserver
```
Learning using [Spaced Repetition](https://e-student.org/spaced-repetition/)

> this is a quote

- [x] This is a list
