from transformers import pipeline

stories = []
def generate_story(prompt):
    result = generator(prompt, max_length=200, truncation=True, num_return_sequences=1, do_sample=True, temperature=0.7)
    story = result[0]["generated_text"]
    stories.append({"prompt":prompt, "story":story})
    return story

generator = pipeline("text-generation", model="gpt2")


for _ in range(3):
    prompt = input("Enter the beginning of a story to generate one: ")
    print(generate_story(prompt))

#! The code below was used to save the stories along with their prompts to a txt file (generated_stories.txt)
with open("generated_stories.txt", "w") as file:
    for i, story in enumerate(stories):
        file.write(f"Prompt {i+1}: {story["prompt"]}\n")
        file.write(f"Story  {i+1}:\n{story["story"]}\n\n")
        file.write('='*50 + '\n')