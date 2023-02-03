
def generate_response_summary(text):
    return 'summarize the following text based on the financial condition  also provide him recommendations based on the dates,country,income to stabilize his financial condition and return the summary in email format. Use n-grams that match the text  as much as possible to produce the summary,avoid using repetitive phrases from the text,emphasize key financial metrics, such as earnings per share, revenue,dates and profit margins while producing the summary,Use a thesaurus to ensure that synonymous terms are used consistently throughout the summary.Find bleu and rouge score for the summary and use this new metric to evaluate the summary,f1=2*bleu*rouge/(bleu+rouge) .Iteratively generate new summaries until blue>0.9, rouge>0.9  also ensure that blue>0.9 and rouge>0.9,and the return the corresponding summary,bleu score and rouge score:\n\n'+text



from flask import Flask, request,render_template
import openai

app = Flask(__name__)

# Set up OpenAI API client with your API key
openai.api_key = "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"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        new_input=generate_response_summary(user_input)
        response=openai.Completion.create(
            model="text-davinci-003",
            prompt=new_input,
            temperature=0.7,
            max_tokens=3000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        generated_text = response["choices"][0]["text"]
        return  render_template("output.html", output=generated_text)
    return  render_template("index.html")

if __name__ == "__main__":
    app.run()
