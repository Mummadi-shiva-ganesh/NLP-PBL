from transformers import BertTokenizer, BertForSequenceClassification
import torch

def main():
    # 1. Load Pre-trained Tokenizer
    print("Loading BERT Tokenizer (bert-base-uncased)...")
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

    # 2. Sample Text for Tokenization
    sample_text = "The movie was absolutely fantastic, I loved the acting and the plot!"
    print(f"\nSample Text: {sample_text}")

    # 3. Tokenization Process
    # - adds [CLS] and [SEP] tokens automatically
    # - truncates or pads to max_length
    inputs = tokenizer(
        sample_text, 
        padding=True, 
        truncation=True, 
        max_length=64, 
        return_tensors="pt" # Return PyTorch tensors
    )

    print("\nTokenization Output:")
    print(f"Input IDs: {inputs['input_ids']}")
    print(f"Attention Mask: {inputs['attention_mask']}")

    # 4. Load Pre-trained BERT Model for Sequence Classification
    # num_labels=2 for binary classification (Positive/Negative)
    print("\nLoading Pre-trained BERT Model (bert-base-uncased)...")
    model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

    # 5. Model Inference (Single Review)
    print("\nRunning Model Inference...")
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
        
    print(f"Model Output (Logits): {logits}")
    
    # Converting logits to probabilities (Softmax)
    probabilities = torch.nn.functional.softmax(logits, dim=1)
    print(f"Probabilities: {probabilities}")

    predicted_class = torch.argmax(probabilities, dim=1).item()
    sentiment = "Positive" if predicted_class == 1 else "Negative"
    print(f"\nPredicted Sentiment: {sentiment}")

if __name__ == "__main__":
    main()
