import random

# Sample paragraph
text = "Python is a high-level programming language. It is widely used for web development, data analysis, and AI."

# Split sentences
sentences = text.split(". ")

# Simple MCQ generator
questions = []
for sentence in sentences:
    words = sentence.split()
    if len(words) > 5:
        answer = random.choice(words)  # Pick a random word as answer
        question = sentence.replace(answer, "____")
        options = [answer]  # correct answer
        # Generate 3 random options
        for _ in range(3):
            fake_word = random.choice(words)
            while fake_word in options:
                fake_word = random.choice(words)
            options.append(fake_word)
        random.shuffle(options)
        questions.append({"question": question, "options": options, "answer": answer})

# Display MCQs
for q in questions:
    print("Q:", q["question"])
    for i, opt in enumerate(q["options"], 1):
        print(f"{i}. {opt}")
    print(f"Answer: {q['answer']}\n")
