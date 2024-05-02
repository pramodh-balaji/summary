import nltk
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
nltk.download('punkt')

def summarize_transcript(transcript_file, output_file, sentences_count=3):
    with open(transcript_file, 'r') as file:
        transcript_text = file.read()

    parser = PlaintextParser.from_string(transcript_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    summary_text = " ".join(str(sentence) for sentence in summary)

    with open(output_file, 'w') as out_file:
        out_file.write(summary_text)

transcript_file = "part1.txt"  # Change this to the path of your transcript file
output_file = "summary1.txt"  # Path to save the summary
summarize_transcript(transcript_file, output_file)