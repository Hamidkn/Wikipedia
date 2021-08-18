Create a CLI application for fetching an article summary (for example the first paragraph) from Wikipedia based on given article name.
List the names of articles which mentions the inputted text in the case that no article of given name exists.
The application ought to have a simple cache to not fetch article names which were already fetched.
You can choose Wikipedia's language mutation by yourself (for example EN) but use only one throughout the whole application.

Existing article:
```
input_text = python
```
```
Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation. Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming.
```

Non-existent article:
```
input_text = rum
```
```
No article with the name rum was found. Inputted text is mentioned in the following articles: rim
```