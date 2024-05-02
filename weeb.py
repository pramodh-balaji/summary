from flask import Flask, request, jsonify
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import TokenizerIsparta
from sumy.summarizers.lex_rank import LexRankSummarizer
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def summarize():
  if request.method == 'POST':
    transcript = request.form['transcript']
    # Call your summarization function here (explained in point 3)
    summary = summarize_transcript(transcript)
    return jsonify({'summary': summary})
  return render_template('index.html')

# Summarization function (replace with your actual implementation)
def summarize_transcript(transcript):
  # Logic to process and summarize the transcript (e.g., using libraries)
  # ... (implementation details)
  # ...
  parser = PlaintextParser.from_string(transcript, TokenizerIsparta())
  summarizer = LexRankSummarizer()
  summary_sentences = summarizer(source=parser.document, sentences=3) # Change number of sentences for summary length
  summary = ' '.join([str(sentence) for sentence in summary_sentences])
  return "Summary of your transcript"

if __name__ == '__main__':
  app.run(debug=True)
