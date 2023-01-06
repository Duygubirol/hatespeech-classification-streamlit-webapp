import os

import numpy as np
import tensorflow as tf
from transformers import (BertTokenizerFast, TFBertForSequenceClassification,
                          TFTrainer, TFTrainingArguments)


def load_model():
    filepath = './model/hatespeech_multiclass_BERT_100pctdataset'

    model_reloaded = TFBertForSequenceClassification.from_pretrained(
        filepath, local_files_only=True)

    training_args = TFTrainingArguments(output_dir='./results',
                                        num_train_epochs=1,
                                        per_device_train_batch_size=8,
                                        per_device_eval_batch_size=8,
                                        warmup_steps=100,
                                        weight_decay=0.01,
                                        logging_steps=10,
                                        eval_steps=5)

    trainer = TFTrainer(model=model_reloaded, args=training_args)

    return trainer


def translate_prediction(prediction):
    if prediction == 0:
        return 'not_hate'
    if prediction == 1:
        return 'offensive'
    if prediction == 2:
        return 'implicit_hate'
    if prediction == 3:
        return 'explicit_hate'


def make_prediction(input_text='hi bitch'):
    trainer = load_model()

    X_test_one_sentence = [input_text]
    y_test = [0]

    tokenizer = BertTokenizerFast.from_pretrained('bert-base-uncased')
    test_input = tokenizer(X_test_one_sentence,
                           truncation=True,
                           padding=True,
                           return_tensors='tf')

    test_dataset = tf.data.Dataset.from_tensor_slices(
        (dict(test_input), y_test))

    y_prediction = trainer.predict(test_dataset)[0]
    y_prediction = np.argmax(y_prediction, axis=-1)

    return translate_prediction(y_prediction)


if __name__ == "__main__":
    print(make_prediction())