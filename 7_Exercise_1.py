### Make a project to make a Dictionary of 10 words , and call them and get value. ###
yourlang = str(input("inter any Language : "))
lang = {
    "javascript" : "JavaScript is light weighed, interpreted and plays a major role in front-end development.",
    "python" : "Python is one of the general purpose, user-friendly programming language",
    "java" : "Java is highly cross-platform compatible or platform independent.",
    "php" : "PHP stands for Hypertext Preprocessor, is a general-purpose programming language. Clearly, PHP is a scripting language,",
    "swift" : "Swift is a general-purpose, open-source, compiled programming language developed by Apple Inc",
    "c-sharp"or"C sharp" : "C-sharp is a powerful, object-oriented programming language developed by Microsoft in 2000",
    "ruby" : "An open source, dynamic programming language, focused on simplicity and productivity, developed in mid-1990 in Japan.",
    "sql" : "SQL (es-que-el) stands for Structured Query Language, is a programming language to operate databases.",
    "c" : "C was the dominant high-level language",
    "c++" : "C++ extends C with object-oriented features."
    }

ylang = yourlang.lower()
print(lang.get(yourlang))

