import openai

def copy_writer(api_key, article, platform, optimization, style, language, length):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",

        messages=[
            {"role": "user", "content": f"我需要撰寫廣告文案發布在社交平台上，請根據以下資訊: \
                                        1. 請以{language}撰寫\
                                        2. 文案會發佈在{platform}平台\
                                        3. 以{style}的語氣描述\
                                        4. 將文案{optimization}\
                                        5. 文字長度約{length}個字\
                                        優化以下內容為一篇完整的文案: {article}"}],
        temperature=0.4,  # regulate the diversity of the output from the model. A value of 0.0 enforces deterministic output, while a value of 1.0 introduces maximum randomness.
        max_tokens=1024,  # limit the length of the output
        top_p=1,  # used to control the probability distribution of text generation in a language model
        frequency_penalty=0.6,  # regulate the extent to which the model generates similar or duplicated content
        presence_penalty=0.6,  # encourage the generation of novel and unique content.
    )

    return (response["choices"][0]["message"]["content"])
